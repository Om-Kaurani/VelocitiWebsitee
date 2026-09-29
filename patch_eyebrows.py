with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace block 1
css = css.replace(""".eyebrow {
    letter-spacing: 2px;
    font-family: var(--font-heading, "Rajdhani", sans-serif);
    font-weight: 600;
    font-size: 1.25rem;
    letter-spacing: 3px;
    text-transform: uppercase;""",
    """.eyebrow {
    font-family: var(--font-heading, "Rajdhani", sans-serif);
    font-weight: 800;
    font-size: 1.75rem;
    letter-spacing: 4px;
    text-transform: uppercase;""")

# Replace block 2
css = css.replace(""".section-header-center .eyebrow {
    letter-spacing: 2px;
    font-family: var(--font-heading, "Rajdhani", sans-serif);
    font-weight: 600;
    font-size: 1.25rem;
    letter-spacing: 3px;
    text-transform: uppercase;""",
    """.section-header-center .eyebrow {
    font-family: var(--font-heading, "Rajdhani", sans-serif);
    font-weight: 800;
    font-size: 1.75rem;
    letter-spacing: 4px;
    text-transform: uppercase;""")

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('Updated eyebrows specifically')
