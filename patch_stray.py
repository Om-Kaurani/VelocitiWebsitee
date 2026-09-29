import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

stray_card = """                <div class="bento-card">
                        <span class="bento-num">06</span>
                        <h3>Complete IP Ownership</h3>
                        <p>Once your project is delivered, all source code, design assets, and intellectual property belong entirely to you — no licensing restrictions, no vendor lock-in.</p>
                    </div>"""

# Remove the one inside hero-actions
# We find hero-actions
idx1 = html.find('<div class="hero-actions">')
idx2 = html.find('</div>', idx1)
# Actually the bento card is inside hero-actions? No, the bento card starts with `                <div class="bento-card">`.
# Let's just regex replace the specific block after Explore Our Work
hero_actions_start = html.find('Explore Our Work</a>')
if hero_actions_start != -1:
    end_of_hero = html.find('<div class="hero-visual"', hero_actions_start)
    hero_chunk = html[hero_actions_start:end_of_hero]
    
    # Remove the bento-card from hero_chunk
    new_hero_chunk = re.sub(r'<div class="bento-card">.*?</div>', '', hero_chunk, flags=re.DOTALL)
    
    html = html[:hero_actions_start] + new_hero_chunk + html[end_of_hero:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Done removing stray card')
