# GitHub Issues to Markdown

This repository contains Python scripts to convert GitHub issues to markdown files. The process involves generating an XML sitemap from all issues in a specified GitHub repository and then crawling the URLs from the sitemap to save the content as markdown files.

## github_issues_to_sitemap.xml.py

This script generates an XML sitemap from all issues in a specified GitHub repository.

### Usage

1. **Install Dependencies**:
   Ensure you have the `PyGithub` library installed. You can install it using pip:
   ```sh
   pip install PyGithub
   ```

2. **Set Up**:
   - Replace `REPO_OWNER_USERNAME/REPO_NAME` with the actual repository name.
   - Replace `YOUR_GITHUB_PERSONAL_ACCESS_TOKEN` with your GitHub personal access token.

3. **Run the Script**:
   ```sh
   python github_issues_to_sitemap.xml.py
   ```

### Functionality

- **get_all_issues_urls(repo_name, token)**: This function initializes a GitHub instance with the provided token, retrieves all issues from the specified repository, and generates an XML sitemap with the URLs of these issues.

## github_issues_sitemap_to_markdown.py

This script crawls URLs from a sitemap and saves the content as markdown files.

### Usage

1. **Install Dependencies**:
   Ensure you have the `crawl4ai` library installed. You can install it using pip:
   ```sh
   pip install crawl4ai
   ```

2. **Set Up**:
   - Replace `http://192.168.0.217:5500/sitemap.xml` with the actual sitemap URL.

3. **Run the Script**:
   ```sh
   python github_issues_sitemap_to_markdown.py
   ```

### Functionality

- **get_sitemap_urls(sitemap_url)**: This function fetches URLs from the specified sitemap.
- **save_document(url, markdown)**: This function saves the markdown content to a file.
- **crawl_parallel(urls, max_concurrent)**: This function crawls multiple URLs in parallel with a concurrency limit.
- **main()**: This function orchestrates the process of fetching URLs from the sitemap and crawling them.

## Guide to Use

1. **Generate Sitemap**:
   - Run `github_issues_to_sitemap.xml.py` to generate an XML sitemap from all issues in the specified GitHub repository.
   - This will create a file named `sitemap.xml` in the current directory.

2. **Convert to Markdown**:
   - Run `github_issues_sitemap_to_markdown.py` to crawl the URLs from the sitemap and save the content as markdown files.
   - The markdown files will be saved in the `crawled_docs` directory.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
