import os
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace any occurrence of `</div></div>` that is immediately followed by whitespace and `</div>\n          </section>`
html = re.sub(r'</div></div>\s*</div>\s*</section>', '</div>\n              </div>\n          </section>', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Fixed timeline closing tags')
