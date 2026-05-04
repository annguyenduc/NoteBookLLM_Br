import asyncio
import sys
import argparse
import io
from crawl4ai import AsyncWebCrawler
from pathlib import Path

# Fix Unicode issues on Windows console
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

async def main():
    parser = argparse.ArgumentParser(description="Crawl a website and save as Markdown using Crawl4AI.")
    parser.add_argument("--url", required=True, help="URL to crawl")
    parser.add_argument("--output", required=True, help="Output file path (.md)")
    args = parser.parse_args()

    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url=args.url)
        
        if result.success:
            output_path = Path(args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Extract clean markdown
            markdown_content = result.markdown
            
            # Add metadata header compatible with NoteBookLLM_Br
            title = result.metadata.get('title', args.url) if result.metadata else args.url
            header = f"---\ntitle: \"{title}\"\nsource_url: \"{args.url}\"\nscraped_at: \"{Path(args.output).name}\"\nengine: \"Crawl4AI\"\n---\n\n"
            
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(header + markdown_content)
            
            print(f"[+] Successfully crawled to: {args.output}")
        else:
            print(f"[-] Failed to crawl: {result.error_message}")
            sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
