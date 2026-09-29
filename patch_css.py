import re

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Fonts & Typography
if '@import' not in css:
    css = "@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600&family=Rajdhani:wght@500;600;700&display=swap');\n" + css

css = re.sub(r'--font-main:\s*[^;]+;', "--font-main: 'Manrope', sans-serif;", css)
if '--font-heading:' not in css:
    css = css.replace('--font-main:', "--font-heading: 'Rajdhani', sans-serif;\n    --font-main:")

css = re.sub(r'font-family:\s*var\(--font-main\);', 'font-family: var(--font-main);', css)

# Make all headings use font-heading
heading_css = """h1, h2, h3, h4, h5, h6 {
    font-family: var(--font-heading, 'Rajdhani', sans-serif);
    font-weight: 700;
}"""
if 'font-family: var(--font-heading' not in css:
    css = css.replace('h1, h2, h3, h4, p { margin: 0; }', 'h1, h2, h3, h4, p { margin: 0; }\n' + heading_css)

# Update eyebrow spacing
css = css.replace('.eyebrow {', '.eyebrow {\n    letter-spacing: 2px;\n    font-family: var(--font-heading, "Rajdhani", sans-serif);\n    font-weight: 600;\n')

# 2. Logo Size & Navbar Sticky
css = css.replace('.brand-logo { height: 40px;', '.brand-logo { height: 56px;')
if 'position: sticky;' not in css:
    css = css.replace('.site-header {', '.site-header {\n    position: sticky;\n    top: 0;\n    z-index: 1000;\n    background: rgba(8, 11, 18, 0.95);\n    backdrop-filter: blur(12px);\n    border-bottom: 1px solid var(--border);\n')

# 3. Bento Numbers Contrast
css = css.replace('color: var(--accent-soft);', 'color: rgba(255, 107, 53, 0.4);') # or similar for higher contrast but subordinate

# 4. Timeline tags
ht_tag = """
.ht-duration {
    display: inline-block;
    padding: 4px 10px;
    font-size: 0.8rem;
    color: var(--accent);
    background: rgba(255, 100, 31, 0.1);
    border-radius: 4px;
    margin-top: 12px;
    font-weight: 600;
    letter-spacing: 0.5px;
    font-family: var(--font-main);
}
"""
if '.ht-duration' not in css:
    css += ht_tag

# 5. Section Padding & Background glow
# The original CSS had `.section { padding: 120px 0; }` (guessing). Let's check it.
css = re.sub(r'\.section\s*\{\s*padding:\s*120px\s+0;\s*\}', '.section { padding: 96px 0; position: relative; }', css)

glow_css = """
.section-glow::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 60vw;
    height: 60vh;
    background: radial-gradient(circle, rgba(255,107,53,0.03) 0%, rgba(8,11,18,0) 70%);
    z-index: 0;
    pointer-events: none;
}
.section > .container { position: relative; z-index: 1; }
"""
if '.section-glow' not in css:
    css += glow_css
    
# Adjust footer layout
css = re.sub(r'\.footer-grid\s*\{[^}]*\}', '.footer-grid { display: flex; flex-wrap: wrap; justify-content: space-between; gap: 48px; border-bottom: 1px solid var(--border); padding-bottom: 48px; }', css)

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("CSS Updated")
