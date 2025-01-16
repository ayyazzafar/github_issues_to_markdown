# GitHub Issues to Markdown

Welcome to the **GitHub Issues to Markdown** repository! 🚀 This repository contains Python scripts to convert GitHub issues to markdown files. The process involves generating an XML sitemap from all issues in a specified GitHub repository and then crawling the URLs from the sitemap to save the content as markdown files.

## Table of Contents

- [Features](#features)
- [Usage](#usage)
  - [github_issues_to_sitemap.xml.py](#github_issues_to_sitemapxmlpy)
  - [github_issues_sitemap_to_markdown.py](#github_issues_sitemap_to_markdownpy)
- [Guide to Use](#guide-to-use)
- [Real-World Use Cases](#real-world-use-cases)
- [Contributing](#contributing)
- [License](#license)

## Features

- 🌐 Generate an XML sitemap from all issues in a specified GitHub repository.
- 🕸️ Crawl URLs from a sitemap and save the content as markdown files.
- 🔄 Easy integration with other tools and workflows.

## Usage

### github_issues_to_sitemap.xml.py

This script generates an XML sitemap from all issues in a specified GitHub repository.

#### Installation

Ensure you have the `PyGithub` library installed. You can install it using pip:
```sh
pip install PyGithub
```

#### Setup

1. Replace `REPO_OWNER_USERNAME/REPO_NAME` with the actual repository name.
2. Replace `YOUR_GITHUB_PERSONAL_ACCESS_TOKEN` with your GitHub personal access token.

#### Run the Script

```sh
python github_issues_to_sitemap.xml.py
```

### github_issues_sitemap_to_markdown.py

This script crawls URLs from a sitemap and saves the content as markdown files.

#### Installation

Ensure you have the `crawl4ai` library installed. You can install it using pip:
```sh
pip install crawl4ai
```

#### Setup

1. Replace `http://192.168.0.217:5500/sitemap.xml` with the actual sitemap URL.

#### Run the Script

```sh
python github_issues_sitemap_to_markdown.py
```

## Guide to Use

1. **Generate Sitemap**:
   - Run `github_issues_to_sitemap.xml.py` to generate an XML sitemap from all issues in the specified GitHub repository.
   - This will create a file named `sitemap.xml` in the current directory.

2. **Convert to Markdown**:
   - Run `github_issues_sitemap_to_markdown.py` to crawl the URLs from the sitemap and save the content as markdown files.
   - The markdown files will be saved in the `crawled_docs` directory.

## Real-World Use Cases

### 1. **Retrieval-Augmented Generation (RAG)**

Feed the generated markdown files into a Language Model (LLM) for RAG. This allows the model to generate responses that are augmented with relevant information from the GitHub issues.

### 2. **Documentation Generation**

Automatically generate documentation from GitHub issues. This can be particularly useful for open-source projects where issues often contain valuable information for users and contributors.

### 3. **Knowledge Base Creation**

Create a knowledge base from GitHub issues. This can be used for internal documentation, FAQs, or support articles.

### 4. **Issue Tracking and Analysis**

Analyze GitHub issues to identify trends, common problems, and areas for improvement. The markdown files can be used as a basis for more detailed analysis.

### 5. **Content Aggregation**

Aggregate content from multiple GitHub repositories into a single markdown file or directory. This can be useful for creating comprehensive documentation or reports.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

---

Feel free to explore the repository and contribute to its development! If you have any questions or need further assistance, please don't hesitate to reach out. Happy coding! 🌟