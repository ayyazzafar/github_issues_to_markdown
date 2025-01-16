import os
import asyncio
import requests
from xml.etree import ElementTree
from typing import List
from urllib.parse import urlparse

from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode

def get_sitemap_urls(sitemap_url: str) -> List[str]:
    """Get URLs from sitemap."""
    try:
        response = requests.get(sitemap_url)
        response.raise_for_status()
        
        # Parse the XML
        root = ElementTree.fromstring(response.content)
        
        # Extract all URLs from the sitemap
        namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        urls = [loc.text for loc in root.findall('.//ns:loc', namespace)]
        
        return urls
    except Exception as e:
        print(f"Error fetching sitemap: {e}")
        return []

async def save_document(url: str, markdown: str):
    """Save markdown content to file."""
    # Create 'crawled_docs' directory if it doesn't exist
    os.makedirs('crawled_docs', exist_ok=True)
    
    # Create filename from URL path
    filename = urlparse(url).path.replace('/', '_')
    if not filename:
        filename = 'index'
    filename = f"crawled_docs/{filename}.md"
    
    # Save content
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(markdown)
    print(f"Saved: {filename}")

async def crawl_parallel(urls: List[str], max_concurrent: int = 5):
    """Crawl multiple URLs in parallel with a concurrency limit."""
    browser_config = BrowserConfig(
        headless=True,
        verbose=False,
        extra_args=["--disable-gpu", "--disable-dev-shm-usage", "--no-sandbox"],
    )
    crawl_config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS)

    # Create crawler instance
    crawler = AsyncWebCrawler(config=browser_config)
    await crawler.start()

    try:
        # Create semaphore to limit concurrency
        semaphore = asyncio.Semaphore(max_concurrent)
        
        async def process_url(url: str):
            async with semaphore:
                result = await crawler.arun(
                    url=url,
                    config=crawl_config,
                    session_id="session1"
                )
                if result.success:
                    print(f"Successfully crawled: {url}")
                    await save_document(url, result.markdown_v2.raw_markdown)
                else:
                    print(f"Failed: {url} - Error: {result.error_message}")
        
        # Process all URLs in parallel
        await asyncio.gather(*[process_url(url) for url in urls])
    finally:
        await crawler.close()

async def main():
    # Specify the sitemap URL you want to crawl
    sitemap_url = "http://192.168.0.217:5500/sitemap.xml"  # Replace with your sitemap URL
    
    # Get URLs from sitemap
    urls = get_sitemap_urls(sitemap_url)
    if not urls:
        print("No URLs found to crawl")
        return
    
    print(f"Found {len(urls)} URLs to crawl")
    await crawl_parallel(urls)

if __name__ == "__main__":
    asyncio.run(main())
