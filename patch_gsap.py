import os

files = ['index.html', 'projects.html', 'inquiry.html']

GSAP_TAGS = """    <!-- GSAP + ScrollTrigger -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js" defer></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js" defer></script>
    <script src="js/animations.js" defer></script>"""

for fname in files:
    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()

    # Don't double-inject
    if 'gsap.min.js' in html:
        print(f'{fname}: GSAP already present, skipping.')
        continue

    # Insert before </body>
    html = html.replace('</body>', f'{GSAP_TAGS}\n</body>')

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'{fname}: GSAP scripts injected.')
