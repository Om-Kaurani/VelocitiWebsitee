import os

with open('inquiry.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_form = """
                    <form id="inquiry-form">
                        <div class="form-group">
                            <label for="name">Name (Required)</label>
                            <input type="text" id="name" name="name" required placeholder="Jane Doe" class="form-input">
                        </div>
                        
                        <div class="form-group">
                            <label for="email">Email Address (Required)</label>
                            <input type="email" id="email" name="email" required placeholder="jane@example.com" class="form-input">
                        </div>

                        <div class="form-group">
                            <label for="phone">Contact Number (Required)</label>
                            <input type="tel" id="phone" name="phone" required placeholder="+1 (555) 000-0000" class="form-input">
                        </div>

                        <div class="form-group">
                            <label for="message">What are you looking to build? (Required)</label>
                            <textarea id="message" name="message" required placeholder="Describe your idea, goals, and any specific requirements..." class="form-input"></textarea>
                        </div>

                        <div class="form-group">
                            <label for="company">Company (Optional)</label>
                            <input type="text" id="company" name="company" placeholder="Your Company" class="form-input">
                        </div>

                        <div id="inq-error" style="color: #ff6b35; font-size: 0.9rem; margin-bottom: 16px; display: none;"></div>

                        <div class="form-actions" id="inq-actions">
                            <button type="submit" id="inq-submit" class="button button-primary" style="width: 100%;">Submit Inquiry</button>
                        </div>
                        
                        <div id="inq-success" style="padding: 24px; background: rgba(0,255,0,0.1); border: 1px solid #27c93f; border-radius: 8px; display: none; text-align: center; margin-top: 24px;">
                            <h4 style="color: #27c93f; margin-bottom: 8px;">Inquiry Sent Successfully!</h4>
                            <p>We've received your project details and will be in touch shortly.</p>
                        </div>
                    </form>
"""

import re
html = re.sub(r'<form action="#" method="POST" id="inquiry-form">.*?</form>', new_form, html, flags=re.DOTALL)

# Add script at the bottom
script_tag = """
    <script src="js/script.js"></script>
    <script>
        document.addEventListener("DOMContentLoaded", () => {
            const form = document.getElementById("inquiry-form");
            const nameInput = document.getElementById("name");
            const emailInput = document.getElementById("email");
            const phoneInput = document.getElementById("phone");
            const messageInput = document.getElementById("message");
            const companyInput = document.getElementById("company");
            const errorEl = document.getElementById("inq-error");
            const submitBtn = document.getElementById("inq-submit");
            const successEl = document.getElementById("inq-success");
            const actionsEl = document.getElementById("inq-actions");

            if(form) {
                form.addEventListener("submit", async (e) => {
                    e.preventDefault();
                    
                    const name = nameInput.value.trim();
                    const email = emailInput.value.trim();
                    const phone = phoneInput.value.trim();
                    const message = messageInput.value.trim();
                    const company = companyInput.value.trim();
                    
                    if (!name || !email || !phone || !message) {
                        errorEl.textContent = "Please fill in all required fields.";
                        errorEl.style.display = "block";
                        return;
                    }

                    const emailRegex = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/;
                    if (!emailRegex.test(email)) {
                        errorEl.textContent = "Please enter a valid email address.";
                        errorEl.style.display = "block";
                        return;
                    }
                    
                    if (phone.length < 7) {
                        errorEl.textContent = "Please enter a valid phone number.";
                        errorEl.style.display = "block";
                        return;
                    }

                    errorEl.style.display = "none";
                    const originalText = submitBtn.textContent;
                    submitBtn.textContent = "Sending...";
                    submitBtn.disabled = true;

                    try {
                        const payload = {
                            formType: "inquiry",
                            name: name,
                            email: email,
                            phone: phone,
                            message: message,
                            company: company || ""
                        };

                        const response = await fetch("https://script.google.com/macros/s/AKfycbyOt5v0qyuAhy47ujLmihIOlgmNU5iFSF7gjtlJm2ux8yGl-VsRgmLhdwmYF9PEVonu/exec", {
                            method: "POST",
                            headers: { "Content-Type": "text/plain;charset=utf-8" },
                            body: JSON.stringify(payload)
                        });

                        if (response.ok) {
                            form.reset();
                            actionsEl.style.display = "none";
                            successEl.style.display = "block";
                        } else {
                            throw new Error("Network response was not ok.");
                        }
                    } catch (error) {
                        console.error("Error:", error);
                        errorEl.textContent = "Failed to submit inquiry. Please try again later.";
                        errorEl.style.display = "block";
                        submitBtn.textContent = originalText;
                        submitBtn.disabled = false;
                    }
                });
            }
        });
    </script>
</body>
"""

html = html.replace('<script src="js/script.js"></script>\n</body>', script_tag)

with open('inquiry.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("inquiry.html updated")
