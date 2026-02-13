#!/usr/bin/env python3
"""
Script to restore complete slide data from old_index.html to index.html
Extracts slides 1-9 with complete data and replaces placeholder content
"""

import re

# Read the old file with complete data
with open('old_index.html', 'r', encoding='utf-8') as f:
    old_content = f.read()

# Read the current file
with open('index.html', 'r', encoding='utf-8') as f:
    current_content = f.read()

# Extract each slide definition from old_index.html
slides_to_extract = {}

for i in range(1, 10):  # slides 1-9
    slide_name = f'slide{i}_HTML'
    
    # Pattern to match: const slideX_HTML = `...`;
    pattern = rf'(const {slide_name} = `[\s\S]*?`;)'
    match = re.search(pattern, old_content)
    
    if match:
        slides_to_extract[slide_name] = match.group(1)
        print(f"✓ Extracted {slide_name} ({len(match.group(1))} chars)")
    else:
        print(f"✗ Could not find {slide_name}")

# Now replace the placeholder slides in current index.html
updated_content = current_content

for slide_name, slide_content in slides_to_extract.items():
    # Find and replace the placeholder version
    pattern = rf'const {slide_name} = `[\s\S]*?`;'
    
    if re.search(pattern, updated_content):
        updated_content = re.sub(pattern, slide_content, updated_content, count=1)
        print(f"✓ Replaced {slide_name} in index.html")
    else:
        print(f"✗ Could not find {slide_name} in index.html to replace")

# Write the updated content
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(updated_content)

print("\n✅ Slide restoration complete!")
print(f"Total slides restored: {len(slides_to_extract)}")
