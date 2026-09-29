import os

# Files to process
files = ['index.html', 'projects.html', 'inquiry.html']

for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Add Favicon
    if 'favicon_icon.png' not in html:
        html = html.replace('</head>', '    <link rel="icon" type="image/png" href="assets/images/logo/favicon_icon.png">\n</head>')
    
    # 2. Fix the "Get Estimate" button to be brighter white and bolder
    html = html.replace('class="button button-primary nav-estimate" href="index.html#contact" style="margin-left: 24px; padding: 10px 20px; font-size: 0.9rem;"',
                        'class="button button-primary nav-estimate" href="index.html#contact" style="margin-left: 24px; padding: 10px 20px; font-size: 0.9rem; color: #ffffff !important; font-weight: 800;"')

    if filename == 'index.html':
        # Remove "small" from the vision section
        html = html.replace('We are a small team of software engineers,', 'We are a team of software engineers,')
        
        # Remove bento-wide from cards
        html = html.replace('bento-card bento-wide', 'bento-card')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

# Now, update CSS for the 3x2 grid
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace repeat(auto-fit, minmax(280px, 1fr)) with exactly repeat(3, 1fr)
import re
css = re.sub(r'\.bento-values \{ display: grid; grid-template-columns: repeat\(auto-fit, minmax\(280px, 1fr\)\);',
             '.bento-values { display: grid; grid-template-columns: repeat(3, 1fr);', css)

# Make sure we replace any other occurrences in media queries, or define proper media queries
# For tablets: repeat(2, 1fr). For mobile: repeat(1, 1fr).
# The user wants exactly 3 on top, 3 on bottom for desktop.
# The `bento-wide` CSS rule might still be there, but we removed it from HTML, so it won't affect it.

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('All patches applied')
