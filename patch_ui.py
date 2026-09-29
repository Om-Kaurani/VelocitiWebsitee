import re

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix the base .eyebrow style
css = css.replace('.eyebrow {\n    color: var(--accent);\n    font-family: var(--font-heading, "Rajdhani", sans-serif);\n    font-weight: 800;\n    font-size: 1.75rem;\n    letter-spacing: 4px;\n    text-transform: uppercase;\n\n    display: inline-flex;\n    align-items: center;\n    gap: 12px;\n    text-transform: uppercase;\n    color: var(--accent);',
                  '.eyebrow {\n    color: var(--accent);\n    font-family: var(--font-heading, "Rajdhani", sans-serif);\n    font-weight: 700;\n    font-size: 1rem;\n    letter-spacing: 2px;\n    text-transform: uppercase;\n    display: inline-flex;\n    align-items: center;\n    gap: 12px;')

# Ensure section-header eyebrows are large
css = css.replace('.section-header-center .eyebrow {',
                  '.section-header-left .eyebrow, .section-header-center .eyebrow {\n    font-size: 1.75rem;\n    font-weight: 800;\n    letter-spacing: 4px;\n}\n.section-header-center .eyebrow {')

# The calendar visuals
# Add a subtle background to all days to make the grid pop, and lighten the disabled days
css += """
.day {
    background: rgba(255, 255, 255, 0.03);
    border-radius: 8px;
    margin: 2px;
}
.day:not(.active):not(:empty) {
    opacity: 0.5; /* more visible than before */
}
"""

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('CSS fixes applied')
