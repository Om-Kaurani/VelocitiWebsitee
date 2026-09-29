import os
import re

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix the media query for tablet
css = css.replace('@media (max-width: 1024px) {\n    .bento-values { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; position: relative; z-index: 2; }',
                  '@media (max-width: 1024px) {\n    .bento-values { grid-template-columns: repeat(2, 1fr); }')

# Fix the media query for mobile (add it if missing)
if '.bento-values { grid-template-columns: 1fr; }' not in css:
    css = css.replace('@media (max-width: 768px) {\n    .hero-grid { grid-template-columns: 1fr; gap: 48px; }',
                      '@media (max-width: 768px) {\n    .bento-values { grid-template-columns: 1fr; }\n    .hero-grid { grid-template-columns: 1fr; gap: 48px; }')

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print('Fixed bento grid media queries')
