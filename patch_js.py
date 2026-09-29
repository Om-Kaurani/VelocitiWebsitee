import os

js = """
document.addEventListener("DOMContentLoaded", () => {
    // Current Year
    const yearEl = document.getElementById("current-year");
    if (yearEl) {
        yearEl.textContent = new Date().getFullYear();
    }

    // Mobile Menu
    const menuToggle = document.querySelector(".menu-toggle");
    const primaryNav = document.getElementById("primary-navigation");

    if (menuToggle && primaryNav) {
        menuToggle.addEventListener("click", () => {
            const isExpanded = menuToggle.getAttribute("aria-expanded") === "true";
            menuToggle.setAttribute("aria-expanded", !isExpanded);
            
            if (!isExpanded) {
                primaryNav.style.display = "flex";
                primaryNav.style.position = "absolute";
                primaryNav.style.top = "var(--header-height)";
                primaryNav.style.left = "0";
                primaryNav.style.right = "0";
                primaryNav.style.background = "rgba(8, 11, 18, 0.98)";
                primaryNav.style.flexDirection = "column";
                primaryNav.style.padding = "32px";
                primaryNav.style.borderBottom = "1px solid var(--border)";
                primaryNav.style.alignItems = "flex-start";
            } else {
                primaryNav.style.display = "none";
                primaryNav.style.position = "";
            }
        });
        
        const navLinks = primaryNav.querySelectorAll('a');
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                if(window.innerWidth <= 768) {
                    menuToggle.setAttribute("aria-expanded", "false");
                    primaryNav.style.display = "none";
                }
            });
        });
    }

    // Copy Email
    const copyBtn = document.querySelector('.copy-email-btn');
    if (copyBtn) {
        copyBtn.addEventListener('click', async () => {
            const email = copyBtn.getAttribute('data-email');
            const feedbackEl = document.getElementById('copy-feedback');
            
            if (email) {
                try {
                    await navigator.clipboard.writeText(email);
                    if (feedbackEl) {
                        feedbackEl.textContent = 'Email copied to clipboard!';
                        setTimeout(() => { feedbackEl.textContent = ''; }, 3000);
                    }
                } catch (err) {
                    console.error('Failed to copy email:', err);
                }
            }
        });
    }

    // Featured Projects
    const projectsContainer = document.getElementById("featured-projects-container");
    if (projectsContainer) {
        const projects = [
            {
                title: "Nexus Financial Dashboard",
                category: "Fintech Platform",
                description: "A secure, performant web application handling real-time transaction processing for enterprise clients.",
                link: "projects.html",
                images: ["assets/images/projects/ai-spend-audit/img1.png", "assets/images/projects/ai-spend-audit/img2.png"]
            },
            {
                title: "CargoStream AI",
                category: "Logistics Engine",
                description: "Machine learning powered route optimization system that reduced global delivery delays by 34%.",
                link: "projects.html",
                images: ["assets/images/projects/ma-cargo-services/img1.png", "assets/images/projects/ma-cargo-services/img2.png"]
            },
            {
                title: "Vitality HealthTrack",
                category: "Mobile Application",
                description: "Cross-platform mobile experience for remote patient monitoring, integrated directly with Apple HealthKit.",
                link: "projects.html",
                images: ["assets/images/projects/deep-sight/img1.jpeg", "assets/images/projects/deep-sight/img2.jpeg"]
            },
            {
                title: "Gesture UI",
                category: "Computer Vision",
                description: "Advanced model integration for real-time video analytics and pattern recognition.",
                link: "projects.html",
                images: ["assets/images/projects/gesture-controller/img1.jpeg", "assets/images/projects/gesture-controller/img2.jpeg"]
            }
        ];

        projects.forEach(project => {
            const article = document.createElement("article");
            article.className = "case-study";

            let imagesHtml = project.images.map((img, idx) => `<img class="slide ${idx === 0 ? 'active' : ''}" src="${img}" alt="${project.title}">`).join('');

            article.innerHTML = `
                <div class="cs-visual">
                    ${imagesHtml}
                </div>
                <div class="cs-content">
                    <div class="cs-meta">
                        <span class="cs-tag">${project.category}</span>
                    </div>
                    <h3 class="cs-title">${project.title}</h3>
                    <p class="cs-desc">${project.description}</p>
                    <a href="${project.link}" class="cs-link">
                        View Work
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                    </a>
                </div>
            `;
            projectsContainer.appendChild(article);
        });

        // Slideshow Logic
        const visuals = document.querySelectorAll('.cs-visual');
        visuals.forEach(visual => {
            const slides = visual.querySelectorAll('.slide');
            if(slides.length > 1) {
                let current = 0;
                setInterval(() => {
                    slides[current].classList.remove('active');
                    current = (current + 1) % slides.length;
                    slides[current].classList.add('active');
                }, 3000);
            }
        });
    }

    // Functional Calendar
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
    const successMsg = document.getElementById('cal-success-msg');

    if (calGrid && monthDisplay) {
        let currentDate = new Date();
        let selectedDate = null;
        let selectedTime = null;

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
                dayEl.className = 'day';
                dayEl.textContent = i;
                
                const thisDate = new Date(year, month, i);
                
                if (thisDate.getDay() === 0 || thisDate.getDay() === 6 || thisDate < today) {
                    dayEl.classList.add('disabled');
                    dayEl.style.opacity = '0.3';
                    dayEl.style.cursor = 'not-allowed';
                } else {
                    dayEl.style.cursor = 'pointer';
                    dayEl.addEventListener('click', () => {
                        document.querySelectorAll('.cal-grid .day').forEach(el => {
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
                    });
                }
                
                calGrid.appendChild(dayEl);
            }
        };

        const updateSidebar = () => {
            confirmBtn.disabled = true;
            timeSlots.innerHTML = '';
            
            if (!selectedDate) {
                dateTitle.textContent = "Select a date";
                return;
            }

            const options = { weekday: 'long', month: 'short', day: 'numeric' };
            dateTitle.textContent = selectedDate.toLocaleDateString('en-US', options);

            const baseTimes = ['09:00 AM', '10:00 AM', '11:30 AM', '01:00 PM', '02:30 PM', '04:00 PM'];
            const availableTimes = baseTimes.filter((_, idx) => (selectedDate.getDate() + idx) % 2 === 0 || idx === 1);

            if (availableTimes.length === 0) {
                timeSlots.innerHTML = '<p style="color:#94a3b8; font-size: 0.9rem;">No times available.</p>';
                return;
            }

            availableTimes.forEach(time => {
                const btn = document.createElement('button');
                btn.className = 'time-btn';
                btn.textContent = time;
                btn.addEventListener('click', () => {
                    document.querySelectorAll('.time-btn').forEach(el => {
                        el.classList.remove('active');
                        el.style.background = 'rgba(255,255,255,0.05)';
                        el.style.borderColor = 'rgba(255,255,255,0.1)';
                    });
                    btn.classList.add('active');
                    btn.style.background = 'var(--accent, #ff6b35)';
                    btn.style.borderColor = 'var(--accent, #ff6b35)';
                    selectedTime = time;
                    confirmBtn.disabled = false;
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

        confirmBtn.addEventListener('click', () => {
            if (selectedDate && selectedTime) {
                const options = { weekday: 'long', month: 'short', day: 'numeric' };
                successMsg.textContent = `${selectedDate.toLocaleDateString('en-US', options)} at ${selectedTime}`;
                bookingUi.style.display = 'none';
                successToast.style.display = 'block';
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
            });
        }

        renderCalendar();
        updateSidebar();
    }
});
"""

with open('js/script.js', 'w', encoding='utf-8') as f:
    f.write(js)
