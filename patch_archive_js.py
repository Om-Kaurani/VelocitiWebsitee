import os

with open('js/script.js', 'r', encoding='utf-8') as f:
    js = f.read()

archive_js = """
    const allProjectsContainer = document.querySelector('[data-project-list="all"]');
    if (allProjectsContainer) {
        const projects = [
            {
                title: "Nexus Financial Dashboard",
                category: "Fintech Platform",
                description: "A secure, performant web application handling real-time transaction processing for enterprise clients.",
                images: ["assets/images/projects/ai-spend-audit/img1.png", "assets/images/projects/ai-spend-audit/img2.png"]
            },
            {
                title: "CargoStream AI",
                category: "Logistics Engine",
                description: "Machine learning powered route optimization system that reduced global delivery delays by 34%.",
                images: ["assets/images/projects/ma-cargo-services/img1.png", "assets/images/projects/ma-cargo-services/img2.png"]
            },
            {
                title: "Vitality HealthTrack",
                category: "Mobile Application",
                description: "Cross-platform mobile experience for remote patient monitoring, integrated directly with Apple HealthKit.",
                images: ["assets/images/projects/deep-sight/img1.jpeg", "assets/images/projects/deep-sight/img2.jpeg"]
            },
            {
                title: "Gesture UI",
                category: "Computer Vision",
                description: "Advanced model integration for real-time video analytics and pattern recognition.",
                images: ["assets/images/projects/gesture-controller/img1.jpeg", "assets/images/projects/gesture-controller/img2.jpeg"]
            },
            {
                title: "Restaurant Owner Portfolio",
                category: "Web Application",
                description: "Dynamic portfolio and menu management system for multi-location restaurant owners.",
                images: ["assets/images/projects/restaurant-owner-portfolio/img1.jpeg", "assets/images/projects/restaurant-owner-portfolio/img2.jpeg"]
            },
            {
                title: "Sentinel AI",
                category: "Security Infrastructure",
                description: "Predictive threat modeling dashboard built on top of proprietary threat intelligence feeds.",
                images: ["assets/images/projects/sentinel-ai/img1.jpeg", "assets/images/projects/sentinel-ai/img2.jpeg"]
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
                </div>
            `;
            allProjectsContainer.appendChild(article);
        });

        const visuals = allProjectsContainer.querySelectorAll('.cs-visual');
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
"""

# Replace the LAST occurrence of `});` to inject it before the DOMContentLoaded closes.
idx = js.rfind('});')
if idx != -1:
    js = js[:idx] + archive_js + '\n});'
    with open('js/script.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print('JS updated with archive projects')
else:
    print('Could not find DOMContentLoaded closure')
