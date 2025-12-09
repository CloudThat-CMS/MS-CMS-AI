#!/usr/bin/env python3
"""
Link Validation Script

Validates all links and references in markdown content files.
"""

import re
import os
import sys
from pathlib import Path
from urllib.parse import urlparse


def find_markdown_links(file_path):
    """Extract all links from a markdown file."""
    links = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find markdown links: [text](url)
        markdown_pattern = r'\[([^\]]+)\]\(([^\)]+)\)'
        matches = re.finditer(markdown_pattern, content)
        
        for match in matches:
            text, url = match.groups()
            links.append({
                'text': text,
                'url': url,
                'file': str(file_path),
                'type': 'markdown'
            })
        
        # Find HTML links: <a href="url">
        html_pattern = r'<a\s+href=["\']([^"\']+)["\']'
        matches = re.finditer(html_pattern, content)
        
        for match in matches:
            url = match.group(1)
            links.append({
                'text': url,
                'url': url,
                'file': str(file_path),
                'type': 'html'
            })
    
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    
    return links


def validate_link(link):
    """Validate a single link."""
    url = link['url']
    
    # Check for internal references
    if url.startswith('#'):
        return True, "anchor link"
    
    # Check for internal files
    if not url.startswith(('http://', 'https://', 'ftp://')):
        # It's a relative path
        base_path = Path(link['file']).parent
        target_path = base_path / url
        
        if target_path.exists():
            return True, "local file exists"
        else:
            return False, f"local file not found: {url}"
    
    # External links are assumed to be valid (would need network call to verify)
    return True, "external link (not validated)"


def main():
    """Run link validation for all markdown files."""
    errors = []
    warnings = []
    valid_count = 0

    # Find all markdown files
    content_dir = Path("content")
    if not content_dir.exists():
        print("❌ Content directory not found")
        return 1

    markdown_files = list(content_dir.rglob("*.md"))
    
    if not markdown_files:
        print("⚠️  No markdown files found in content directory")
        return 0

    print(f"Validating {len(markdown_files)} markdown files...\n")

    for file_path in markdown_files:
        links = find_markdown_links(file_path)
        
        for link in links:
            valid, message = validate_link(link)
            
            if valid:
                valid_count += 1
            else:
                errors.append(
                    f"In {file_path.relative_to('.')}:\n"
                    f"  ❌ Invalid link: [{link['text']}]({link['url']})\n"
                    f"     {message}"
                )

    # Report results
    print("\n" + "="*50)
    print(f"Link Validation Summary: {valid_count} valid links")
    
    if errors:
        print(f"\nErrors found ({len(errors)}):")
        for error in errors:
            print(error)
        return 1
    
    print("\n✅ All link validation passed!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
