#!/usr/bin/env python3
"""
Final script to restore slides 5-9 from commit b456bf3
"""

import re
import subprocess

# Get the file from the commit that has slides 5-9
result = subprocess.run(
    ['git', 'show', 'b456bf3:index.html'],
    capture_output=True,
    text=True,
    check=True,
    cwd='/Users/libreloco/Desktop/PROGRAMA SER NWL'
)
git_content = result.stdout

# Read current index.html
with open('/Users/libreloco/Desktop/PROGRAMA SER NWL/index.html', 'r', encoding='utf-8') as f:
    current_content = f.read()

updated_content = current_content
restored_count = 0

# Extract slides 5-9
for i in range(5, 10):
    slide_name = f'slide{i}_HTML'
    print(f"\nProcessing {slide_name}...")
    
    # Extract the slide definition
    pattern = rf'(const {slide_name} = `[\s\S]*?`;)'
    match = re.search(pattern, git_content)
    
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

# Write updated content
with open('/Users/libreloco/Desktop/PROGRAMA SER NWL/index.html', 'w', encoding='utf-8') as f:
    f.write(updated_content)

print(f"\n✅ Final restoration complete!")
print(f"Slides 5-9 restored: {restored_count}/5")
print(f"\nTotal slides with data: 4 (from old_index.html) + {restored_count} (from Git) = {4 + restored_count}/9")
