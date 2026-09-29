import os
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add section-glow to text-heavy sections
html = html.replace('id="vision"', 'id="vision" class="section section-darker section-glow"')
html = html.replace('id="values"', 'id="values" class="section section-glow"')

# 2. Rewrite 1st card in "How We Do Things"
old_card1 = "<p>We speak in plain language. You will always know what we are building, why we are building it, and where the project stands.</p>"
new_card1 = "<p>We keep you updated in plain, jargon-free language, so you always know what's being built, why, and where the project stands.</p>"
html = html.replace(old_card1, new_card1)

# 3. Add 6th card to "How We Do Things"
card6 = """                    <div class="bento-card">
                        <span class="bento-num">06</span>
                        <h3>Complete IP Ownership</h3>
                        <p>Once your project is delivered, all source code, design assets, and intellectual property belong entirely to you — no licensing restrictions, no vendor lock-in.</p>
                    </div>
                </div>"""
html = html.replace('</div>\n                </div>', card6, 1)  # Only replaces the FIRST occurrence if we're careful. Wait, replacing `</div>\n                </div>` is risky.

# Let's use regex to insert the 6th card just before the closing of bento-values
html = re.sub(r'(<div class="bento-card.*?>\s*<span class="bento-num">05</span>.*?</div>)\s*</div>', r'\1\n' + card6, html, flags=re.DOTALL)


# 4. Project Timeline
# We need to add duration tags to ALL steps, and restore 5 and 6 if they are missing or just replace the timeline track completely.
old_timeline_start = html.find('<div class="horizontal-timeline">')
old_timeline_end = html.find('</div>\n            </div>\n        </section>', old_timeline_start)

if old_timeline_start != -1 and old_timeline_end != -1:
    new_timeline = """<div class="horizontal-timeline">
                    <div class="timeline-track"></div>
                    <div class="ht-step">
                        <div class="ht-node">01</div>
                        <div class="ht-content">
                            <h3>First Meeting</h3>
                            <p>Understand idea & goals.</p>
                            <span class="ht-duration">Day 1</span>
                        </div>
                    </div>
                    <div class="ht-step">
                        <div class="ht-node">02</div>
                        <div class="ht-content">
                            <h3>Ideation</h3>
                            <p>Discuss features & direction.</p>
                            <span class="ht-duration">Day 2-3</span>
                        </div>
                    </div>
                    <div class="ht-step">
                        <div class="ht-node">03</div>
                        <div class="ht-content">
                            <h3>Planning</h3>
                            <p>Define structure before dev.</p>
                            <span class="ht-duration">Day 4-5</span>
                        </div>
                    </div>
                    <div class="ht-step">
                        <div class="ht-node">04</div>
                        <div class="ht-content">
                            <h3>Development</h3>
                            <p>Build and test product.</p>
                            <span class="ht-duration">Week 2-4</span>
                        </div>
                    </div>
                    <div class="ht-step">
                        <div class="ht-node">05</div>
                        <div class="ht-content">
                            <h3>Revisions</h3>
                            <p>Review & make changes.</p>
                            <span class="ht-duration">Week 5</span>
                        </div>
                    </div>
                    <div class="ht-step">
                        <div class="ht-node">06</div>
                        <div class="ht-content">
                            <h3>Delivery</h3>
                            <p>Hand over finished project.</p>
                            <span class="ht-duration">Week 6</span>
                        </div>
                    </div>
                </div>"""
    
    html = html[:old_timeline_start] + new_timeline + html[old_timeline_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("index.html specific updates applied.")
