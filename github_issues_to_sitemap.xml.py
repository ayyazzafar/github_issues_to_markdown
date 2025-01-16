from github import Github
from datetime import datetime
import xml.etree.ElementTree as ET
from xml.dom import minidom

def get_all_issues_urls(repo_name, token):
    # Initialize Github instance with token
    g = Github(token)
    
    try:
        # Get repository
        repo = g.get_repo(repo_name)
        
        # Get all issues
        issues = repo.get_issues(state='all')
        
        # Create the root element for sitemap
        urlset = ET.Element('urlset')
        urlset.set('xmlns', 'http://www.sitemaps.org/schemas/sitemap/0.9')
        
        # Add each issue URL to the sitemap
        count = 0
        for issue in issues:
            url = ET.SubElement(urlset, 'url')
            loc = ET.SubElement(url, 'loc')
            loc.text = issue.html_url
            lastmod = ET.SubElement(url, 'lastmod')
            lastmod.text = issue.updated_at.strftime('%Y-%m-%d')
            count += 1
            if count % 10 == 0:
                print(f"Processed {count} issues...")
        
        # Create the XML string with proper formatting
        xml_str = minidom.parseString(ET.tostring(urlset)).toprettyxml(indent="  ")
        
        # Save to sitemap.xml
        with open('sitemap.xml', 'w', encoding='utf-8') as f:
            f.write(xml_str)
            
        print(f"Sitemap generated successfully with {count} issues from {repo_name}")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    repo_name = "REPO_OWNER_USERNAME/REPO_NAME"
    token = "YOUR_GITHUB_PERSONAL_ACCESS_TOKEN"  # Your GitHub token
    get_all_issues_urls(repo_name, token)
