import os
import re

for filename in ['index.html', 'projects.html', 'inquiry.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Remove Social Icons
    html = re.sub(r'<div class="footer-social".*?</div>', '', html, flags=re.DOTALL)
    
    # 2. Add Get Estimate button to Navbar
    if '<a class="button button-primary nav-estimate"' not in html:
        nav_end_idx = html.find('</nav>')
        if nav_end_idx != -1:
            btn = '\n                <a class="button button-primary nav-estimate" href="index.html#contact" style="margin-left: 24px; padding: 10px 20px; font-size: 0.9rem;">Get Estimate</a>\n            '
            html = html[:nav_end_idx] + btn + html[nav_end_idx:]

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
        
print("Global HTML updates applied.")
