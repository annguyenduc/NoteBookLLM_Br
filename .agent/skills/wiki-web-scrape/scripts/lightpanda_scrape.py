import asyncio
import argparse
import os
import sys
from playwright.async_api import async_playwright

async def scrape(url, output_path):
    async with async_playwright() as p:
        try:
            # Try to connect to existing Lightpanda server
            print(f"[*] Attempting to connect to Lightpanda at http://127.0.0.1:9222...")
            browser = await p.chromium.connect_over_cdp("http://127.0.0.1:9222", timeout=2000)
            print("[+] Connected to Lightpanda.")
        except Exception as e:
            print(f"[!] Lightpanda connection failed: {str(e)}")
            print("[*] Falling back to standard Chromium launch...")
            browser = await p.chromium.launch(headless=True)
            print("[+] Launched standard Chromium.")

        try:
            context = browser.contexts[0] if browser.contexts else await browser.new_context()
            page = await context.new_page()
            
            print(f"[*] Navigating to: {url}")
            await page.goto(url, wait_until="networkidle", timeout=30000)
            
            # Get title and content
            title = await page.title()
            content = await page.evaluate("() => document.body.innerText")
            html_content = await page.content()
            
            # Simple Markdown formatting
            markdown_output = f"""---
title: "{title}"
source_url: "{url}"
scraped_at: "{asyncio.get_event_loop().time()}"
engine: "Lightpanda (via Playwright)"
---

# {title}

Source: {url}

## Content

{content}

---
## Raw Source Metadata
- URL: {url}
- Title: {title}
"""
            
            # Ensure directory exists
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(markdown_output)
                
            print(f"[+] Successfully scraped to: {output_path}")
            
            await browser.close()
        except Exception as e:
            print(f"[!] Error: {str(e)}")
            sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrape web content using Lightpanda")
    parser.add_argument("--url", required=True, help="URL to scrape")
    parser.add_argument("--output", required=True, help="Path to save the output file")
    
    args = parser.parse_args()
    asyncio.run(scrape(args.url, args.output))
