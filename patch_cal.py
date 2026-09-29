import re

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix disabled days visibility
css = css.replace('.cal-day.disabled { color: rgba(255,255,255,0.2); cursor: not-allowed; opacity: 0.4; }',
                  '.cal-day.disabled { color: rgba(255,255,255,0.5); cursor: not-allowed; opacity: 1; }')

# Make sure day borders/backgrounds are nice
# Ensure .day { ... } is nicely appended if we didn't add it fully
# I added it in patch_ui.py at the end of the file.

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('Calendar disabled visibility improved')
