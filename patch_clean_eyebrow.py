with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re

# We will just regex remove the extra duplicate properties from .eyebrow
# Specifically: font-size: 0.75rem; font-weight: 700; letter-spacing: 0.1em;
# that come right after `gap: 12px;`

pattern = r'(gap:\s*12px;)\s*font-size:\s*0\.75rem;\s*font-weight:\s*700;\s*letter-spacing:\s*0\.1em;'
css = re.sub(pattern, r'\1', css)

# Also there might be a global color for eyebrow that is missing or something?
# Let's ensure it has color: var(--accent);
# I don't see color: var(--accent); in the block we just looked at.
# I will add it just in case.
css = css.replace('.eyebrow {\n    font-family', '.eyebrow {\n    color: var(--accent);\n    font-family')

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print('Fixed eyebrow block duplicates')
