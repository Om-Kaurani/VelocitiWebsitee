import os
import re

with open('js/script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace calendar logic
old_logic_start = js.find('// Functional Calendar')
old_logic_end = js.find('// Archive Projects')
if old_logic_end == -1:
    old_logic_end = js.find('const allProjectsContainer')

new_logic = """// Functional Calendar
    const calGrid = document.getElementById('cal-grid');
    const monthDisplay = document.getElementById('cal-month-display');
    const prevBtn = document.getElementById('cal-prev');
    const nextBtn = document.getElementById('cal-next');
    const dateTitle = document.getElementById('cal-date-title');
    const timeSlots = document.getElementById('cal-time-slots');
    const confirmBtn = document.getElementById('cal-confirm');
    
    const bookingUi = document.getElementById('booking-ui');
    const successToast = document.getElementById('booking-success');
    const resetBtn = document.getElementById('cal-reset');
    
    const calEmail = document.getElementById('cal-email');
    const calPhone = document.getElementById('cal-phone');
    const calCompany = document.getElementById('cal-company');
    const calError = document.getElementById('cal-error');

    if (calGrid && monthDisplay) {
        let currentDate = new Date();
        let selectedDate = null;
        let selectedTime = null;

        const validateForm = () => {
            if (!selectedDate || !selectedTime) return false;
            
            const email = calEmail.value.trim();
            const phone = calPhone.value.trim();
            
            const emailRegex = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/;
            const isEmailValid = emailRegex.test(email);
            const isPhoneValid = phone.length >= 7; // basic validation
            
            if (email && !isEmailValid) {
                calError.textContent = "Please enter a valid email.";
                calError.style.display = "block";
                return false;
            }
            if (phone && !isPhoneValid) {
                calError.textContent = "Please enter a valid phone number.";
                calError.style.display = "block";
                return false;
            }
            
            calError.style.display = "none";
            return email && isEmailValid && phone && isPhoneValid;
        };

        const updateConfirmButton = () => {
            confirmBtn.disabled = !validateForm();
        };

        if (calEmail) calEmail.addEventListener('input', updateConfirmButton);
        if (calPhone) calPhone.addEventListener('input', updateConfirmButton);
        if (calCompany) calCompany.addEventListener('input', updateConfirmButton);

        const renderCalendar = () => {
            calGrid.innerHTML = '';
            
            const year = currentDate.getFullYear();
            const month = currentDate.getMonth();
            
            const monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
            monthDisplay.textContent = `${monthNames[month]} ${year}`;
            
            const firstDay = new Date(year, month, 1).getDay();
            const daysInMonth = new Date(year, month + 1, 0).getDate();
            
            for (let i = 0; i < firstDay; i++) {
                const empty = document.createElement('div');
                empty.className = 'day empty';
                empty.style.border = 'none';
                calGrid.appendChild(empty);
            }
            
            const today = new Date();
            today.setHours(0,0,0,0);
            
            for (let i = 1; i <= daysInMonth; i++) {
                const dayEl = document.createElement('div');
                dayEl.className = 'cal-day day';
                dayEl.textContent = i;
                
                const thisDate = new Date(year, month, i);
                
                if (thisDate.getDay() === 0 || thisDate.getDay() === 6 || thisDate < today) {
                    dayEl.classList.add('disabled');
                } else {
                    dayEl.addEventListener('click', () => {
                        document.querySelectorAll('.cal-grid .cal-day, .booking-calendar .cal-day').forEach(el => {
                            el.classList.remove('active');
                            el.style.background = 'transparent';
                            el.style.color = 'inherit';
                        });
                        dayEl.classList.add('active');
                        dayEl.style.background = 'var(--accent, #ff6b35)';
                        dayEl.style.color = '#fff';
                        
                        selectedDate = thisDate;
                        selectedTime = null;
                        updateSidebar();
                        updateConfirmButton();
                    });
                }
                
                calGrid.appendChild(dayEl);
            }
        };

        const updateSidebar = () => {
            timeSlots.innerHTML = '';
            
            if (!selectedDate) {
                dateTitle.textContent = "Select a date";
                return;
            }

            const options = { weekday: 'long', month: 'short', day: 'numeric' };
            dateTitle.textContent = `Selected: ${selectedDate.toLocaleDateString('en-US', options)}`;

            const baseTimes = ['09:00 AM', '10:00 AM', '11:00 AM', '12:00 PM', '02:00 PM', '03:00 PM', '04:00 PM', '05:00 PM'];
            // Filter some out just to make it look realistic, or show all
            const availableTimes = baseTimes.filter((_, idx) => (selectedDate.getDate() + idx) % 3 !== 0 || idx === 1);

            if (availableTimes.length === 0) {
                timeSlots.innerHTML = '<p style="color:#94a3b8; font-size: 0.9rem;">No times available.</p>';
                return;
            }

            availableTimes.forEach(time => {
                const btn = document.createElement('button');
                btn.className = 'time-btn cal-slot-btn';
                btn.textContent = time;
                btn.addEventListener('click', () => {
                    document.querySelectorAll('.time-btn').forEach(el => {
                        el.classList.remove('active');
                    });
                    btn.classList.add('active');
                    selectedTime = time;
                    updateConfirmButton();
                });
                timeSlots.appendChild(btn);
            });
        };

        prevBtn.addEventListener('click', () => {
            currentDate.setMonth(currentDate.getMonth() - 1);
            renderCalendar();
        });

        nextBtn.addEventListener('click', () => {
            currentDate.setMonth(currentDate.getMonth() + 1);
            renderCalendar();
        });

        confirmBtn.addEventListener('click', async () => {
            if (validateForm()) {
                const originalText = confirmBtn.textContent;
                confirmBtn.textContent = "Sending...";
                confirmBtn.disabled = true;

                try {
                    const payload = {
                        formType: "meeting",
                        date: selectedDate.toLocaleDateString('en-US'),
                        time: selectedTime,
                        email: calEmail.value.trim(),
                        phone: calPhone.value.trim(),
                        company: calCompany.value.trim() || ""
                    };

                    const response = await fetch("https://script.google.com/macros/s/AKfycbyOt5v0qyuAhy47ujLmihIOlgmNU5iFSF7gjtlJm2ux8yGl-VsRgmLhdwmYF9PEVonu/exec", {
                        method: "POST",
                        headers: { "Content-Type": "text/plain;charset=utf-8" },
                        body: JSON.stringify(payload)
                    });

                    if (response.ok) {
                        bookingUi.style.display = 'none';
                        successToast.style.display = 'block';
                        
                        // Clear form
                        calEmail.value = '';
                        calPhone.value = '';
                        calCompany.value = '';
                    } else {
                        throw new Error("Network response was not ok.");
                    }
                } catch (error) {
                    console.error("Error:", error);
                    calError.textContent = "Failed to send request. Please try again later.";
                    calError.style.display = "block";
                } finally {
                    confirmBtn.textContent = originalText;
                    updateConfirmButton();
                }
            }
        });

        if(resetBtn) {
            resetBtn.addEventListener('click', () => {
                successToast.style.display = 'none';
                bookingUi.style.display = 'flex';
                selectedDate = null;
                selectedTime = null;
                renderCalendar();
                updateSidebar();
                updateConfirmButton();
            });
        }

        renderCalendar();
        updateSidebar();
        updateConfirmButton();
    }

    """

js = js[:old_logic_start] + new_logic + js[old_logic_end:]

with open('js/script.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("JS updated")
