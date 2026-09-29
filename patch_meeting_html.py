import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Text Replacements
html = html.replace('Schedule a Call', 'Schedule a Meeting')
html = html.replace('introductory call', 'introductory meeting')
html = html.replace('Book Another Call', 'Book Another Meeting')
html = html.replace('<h4>Call Scheduled</h4>', '<h4>Request Sent</h4>')
html = html.replace("<p>We've sent a calendar invite to your email.</p>", "<p>We'll follow up with a meeting link shortly.</p>")

# 2. Add form fields to the meeting scheduler
form_fields = """
                                <div class="booking-form" style="display: flex; flex-direction: column; gap: 12px; margin-top: 24px; margin-bottom: 16px;">
                                    <input type="email" id="cal-email" placeholder="Email (required)" class="form-input" required>
                                    <input type="tel" id="cal-phone" placeholder="Contact Number (required)" class="form-input" required>
                                    <input type="text" id="cal-company" placeholder="Company (optional)" class="form-input">
                                </div>
                                <div id="cal-error" style="color: #ff6b35; font-size: 0.85rem; margin-bottom: 12px; display: none;"></div>
                                <button id="cal-confirm" class="button button-primary confirm-booking-btn" disabled>Confirm Time</button>
"""
# Replace the existing button and its container
html = re.sub(r'<button id="cal-confirm".*?</button>', form_fields, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("index.html updated")

# Also add CSS for form inputs to style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix calendar alignment and colors
css = css.replace('.cal-day { padding: 8px 0; font-size: 0.9rem; border-radius: 4px; cursor: pointer; transition: background 0.2s; border: 1px solid transparent; }',
                  '.cal-day { padding: 8px 0; font-size: 0.9rem; border-radius: 4px; cursor: pointer; transition: background 0.2s; border: 1px solid transparent; display: flex; align-items: center; justify-content: center; height: 36px; }')
css = css.replace('.cal-day.disabled { color: rgba(255,255,255,0.2); cursor: not-allowed; }',
                  '.cal-day.disabled { color: rgba(255,255,255,0.2); cursor: not-allowed; opacity: 0.4; }')
css = css.replace('.cal-day:not(.empty):not(.disabled) { color: inherit; }', '') # Just in case

# Fix time slots colors
css = css.replace('.cal-slot-btn { background: rgba(0,0,0,0.3); border: 1px solid var(--color-border); color: var(--color-text-main); padding: 8px; border-radius: 4px; font-size: 0.85rem; cursor: pointer; transition: all 0.2s; }',
                  '.cal-slot-btn { background: var(--bg-tertiary, rgba(255,255,255,0.05)); border: 1px solid var(--border, rgba(255,255,255,0.1)); color: var(--text-primary, #fff); padding: 8px; border-radius: 4px; font-size: 0.85rem; cursor: pointer; transition: all 0.2s; }')
css = css.replace('.cal-slot-btn:hover { border-color: var(--color-accent); color: var(--color-accent); }',
                  '.cal-slot-btn:hover { border-color: var(--accent); background: var(--accent); color: #fff; }')
css = css.replace('.cal-slot-btn.active { background: var(--color-accent); color: #fff; border-color: var(--color-accent); }',
                  '.cal-slot-btn.active { background: var(--accent); color: #fff; border-color: var(--accent); }')
                  
# Form input styles (reused from inquiry page)
input_css = """
.form-input {
    width: 100%;
    padding: 12px 16px;
    background: var(--bg-tertiary, rgba(255,255,255,0.05));
    border: 1px solid var(--border, rgba(255,255,255,0.1));
    border-radius: 6px;
    color: var(--text-primary, #fff);
    font-family: inherit;
    font-size: 0.95rem;
    transition: border-color 0.2s ease;
}
.form-input:focus { outline: none; border-color: var(--accent); }
"""
if '.form-input' not in css:
    css += input_css

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("style.css updated")
