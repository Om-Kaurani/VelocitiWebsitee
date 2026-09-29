import os

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix timeline CSS
css = css.replace('.horizontal-timeline {\n    display: flex;\n    gap: 32px;\n    overflow-x: auto;',
                  '.horizontal-timeline {\n    display: flex;\n    gap: 16px;\n    overflow-x: visible;')

css = css.replace('.ht-step {\n    flex: 0 0 280px;',
                  '.ht-step {\n    flex: 1;')

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print('Timeline layout updated to flex: 1')
