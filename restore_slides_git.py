#!/usr/bin/env python3
"""
Enhanced script to restore slides 5-9 from Git history
"""

import re
import subprocess

# Mapping of slides to their Git commits
slide_commits = {
    'slide5_HTML': '755d42d',  # Resumen 2025-26
    'slide6_HTML': '2de6718',  # Resumen CON S.E.R.
    'slide7_HTML': '94da7b3',  # Programa PIN 60%
    'slide8_HTML': '9a10d42',  # Resumen SER AL 60%
    'slide9_HTML': '9e09468',  # Resumen CON S.E.R. 60%
}

# Read current index.html
with open('index.html', 'r', encoding='utf-8') as f:
    current_content = f.read()

updated_content = current_content
restored_count = 0

for slide_name, commit_hash in slide_commits.items():
    print(f"\nProcessing {slide_name} from commit {commit_hash}...")
    
    try:
        # Get the file from Git
        result = subprocess.run(
            ['git', 'show', f'{commit_hash}:index.html'],
            capture_output=True,
            text=True,
            check=True
        )
        old_content = result.stdout
        
        # Extract the slide definition
        pattern = rf'(const {slide_name} = `[\s\S]*?`;)'
        match = re.search(pattern, old_content)
        
        if match:
            slide_content = match.group(1)
            print(f"  ✓ Extracted {slide_name} ({len(slide_content)} chars)")
            
            # Replace in current content
            replace_pattern = rf'const {slide_name} = `[\s\S]*?`;'
            if re.search(replace_pattern, updated_content):
                updated_content = re.sub(replace_pattern, slide_content, updated_content, count=1)
                print(f"  ✓ Replaced {slide_name} in index.html")
                restored_count += 1
            else:
                print(f"  ✗ Could not find {slide_name} in index.html")
        else:
            print(f"  ✗ Could not extract {slide_name} from commit")
            
    except subprocess.CalledProcessError as e:
        print(f"  ✗ Git error: {e}")

# Write updated content
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(updated_content)

print(f"\n✅ Restoration complete!")
print(f"Total slides restored from Git: {restored_count}/5")
