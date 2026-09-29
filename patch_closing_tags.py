with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Instead of exact whitespace matching, use regex to just find the Explore Our Work button and fix the closing tags after it.
import re
# We want to replace whatever comes after Explore Our Work</a> up to <div class="hero-visual"
hero_actions_start = html.find('Explore Our Work</a>')
if hero_actions_start != -1:
    end_of_btn = hero_actions_start + len('Explore Our Work</a>')
    start_of_visual = html.find('<div class="hero-visual"', end_of_btn)
    
    html = html[:end_of_btn] + '\n                      </div>\n                  </div>\n\n                  ' + html[start_of_visual:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Fixed closing tags')
