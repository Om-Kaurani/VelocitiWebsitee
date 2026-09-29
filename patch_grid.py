import os

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('<div class="booking-calendar" style="grid-template-columns: repeat(7, 1fr);">',
                    '<div class="booking-calendar" style="display: grid; grid-template-columns: repeat(7, 1fr); gap: 4px; text-align: center;">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Grid alignment fixed')
