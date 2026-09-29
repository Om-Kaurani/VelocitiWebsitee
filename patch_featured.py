import re

with open('js/script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Replace Featured Projects Array
featured_projects = """const projects = [
            {
                title: "Restaurant Owner Portfolio",
                category: "Web Application",
                description: "Dynamic portfolio and menu management system for multi-location restaurant owners.",
                link: "projects.html",
                images: ["assets/images/projects/restaurant-owner-portfolio/img1.jpeg", "assets/images/projects/restaurant-owner-portfolio/img2.jpeg"]
            },
            {
                title: "Nexus Financial Dashboard",
                category: "Fintech Platform",
                description: "A secure, performant web application handling real-time transaction processing for enterprise clients.",
                link: "projects.html",
                images: ["assets/images/projects/ai-spend-audit/img1.png", "assets/images/projects/ai-spend-audit/img2.png"]
            },
            {
                title: "Sentinel AI",
                category: "Security Infrastructure",
                description: "Predictive threat modeling dashboard built on top of proprietary threat intelligence feeds.",
                link: "projects.html",
                images: ["assets/images/projects/sentinel-ai/img1.jpeg", "assets/images/projects/sentinel-ai/img2.jpeg"]
            }
        ];"""

# We need to replace the featured projects array in the script
# We can find it by finding the start of it and the end of it
start = js.find('const projects = [', js.find('featured-projects-container'))
end = js.find('];', start) + 2

if start != -1:
    js = js[:start] + featured_projects + js[end:]
    
with open('js/script.js', 'w', encoding='utf-8') as f:
    f.write(js)
print("Updated featured projects.")
