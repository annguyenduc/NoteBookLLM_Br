import asyncio
import sys
import argparse
import io
import base64
import time
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from pathlib import Path

# Fix Unicode issues on Windows console
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

async def main():
    parser = argparse.ArgumentParser(description="Advanced Crawl4AI script: Headful + Human-like Scrolling.")
    parser.add_argument("--url", required=True, help="URL to crawl")
    parser.add_argument("--output", required=True, help="Output file path (.md)")
    parser.add_argument("--screenshot", action="store_true", help="Capture a high-fidelity screenshot")
    parser.add_argument("--headless", action="store_true", default=False, help="Run in headless mode")
    args = parser.parse_args()

    # Browser Configuration
    browser_config = BrowserConfig(
        headless=args.headless, 
        verbose=True
    )

    # METHOD 3: Human-like Interaction (Cuộn trang để kích hoạt Lazy Load và chứng minh không phải bot)
    js_interaction_code = """
    await new Promise(async (resolve) => {
        let totalHeight = 0;
        let distance = 200;
        let timer = setInterval(() => {
            let scrollHeight = document.body.scrollHeight;
            window.scrollBy(0, distance);
            totalHeight += distance;
            if(totalHeight >= scrollHeight - window.innerHeight){
                clearInterval(timer);
                window.scrollTo(0, 0); // Quay lại đầu trang để chụp ảnh
                resolve();
            }
        }, 150); 
    });
    """

    # Advanced Run Configuration
    run_config = CrawlerRunConfig(
        screenshot=args.screenshot,
        js_code=js_interaction_code,    # Chạy đoạn cuộn trang
        wait_until="networkidle",
        magic=True,
        cache_mode=CacheMode.BYPASS,
        simulate_user=True,
        override_navigator=True,
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )

    async with AsyncWebCrawler(config=browser_config) as crawler:
        print(f"[*] Crawling in HEADFUL mode: {args.url}...")
        result = await crawler.arun(url=args.url, config=run_config)
        
        if result.success:
            output_path = Path(args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Save screenshot with validation
            screenshot_link = ""
            if args.screenshot and result.screenshot:
                screenshot_data = base64.b64decode(result.screenshot)
                size_kb = len(screenshot_data) / 1024
                
                screenshot_path = output_path.with_suffix(".png")
                try:
                    with open(screenshot_path, "wb") as f:
                        f.write(screenshot_data)
                    screenshot_link = f"\n\n## 📸 Visual Proof (Evidence)\n![Screenshot]({screenshot_path.name})\n"
                    print(f"[+] Screenshot saved ({size_kb:.1f} KB): {screenshot_path}")
                except Exception as e:
                    print(f"[-] Error saving screenshot: {e}")
            
            # Save Markdown
            markdown_content = result.markdown
            header = f"---\ntitle: \"{result.metadata.get('title', args.url) if result.metadata else args.url}\"\nsource_url: \"{args.url}\"\nengine: \"Crawl4AI-Headful\"\n---\n\n"
            
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(header + markdown_content + screenshot_link)
            
            print(f"[+] Successfully finished: {args.output}")
        else:
            print(f"[-] Crawl failed: {result.error_message}")
            sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
