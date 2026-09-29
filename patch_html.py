import os

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start = html.find('<div class="booking-ui" id="booking-ui">')
end = html.find('<div class="booking-success" id="booking-success"')

new_booking = """<div class="booking-ui" id="booking-ui">
                            <div class="booking-sidebar">
                                <div class="booking-month" style="display:flex; justify-content:space-between; align-items:center;">
                                    <button id="cal-prev" style="background:transparent; border:none; color:white; cursor:pointer;">&lt;</button>
                                    <span id="cal-month-display"></span>
                                    <button id="cal-next" style="background:transparent; border:none; color:white; cursor:pointer;">&gt;</button>
                                </div>
                                <div class="booking-calendar" style="grid-template-columns: repeat(7, 1fr);">
                                    <div class="day-name">Su</div><div class="day-name">Mo</div><div class="day-name">Tu</div><div class="day-name">We</div><div class="day-name">Th</div><div class="day-name">Fr</div><div class="day-name">Sa</div>
                                    <div id="cal-grid" style="display: contents;"></div>
                                </div>
                            </div>
                            <div class="booking-main">
                                <div class="booking-date-title" id="cal-date-title">Select a date</div>
                                <div class="time-slots" id="cal-time-slots">
                                    <!-- slots injected by js -->
                                </div>
                                <button id="cal-confirm" class="button button-primary confirm-booking-btn" disabled>Confirm Time</button>
                            </div>
                        </div>
                        """

if start != -1 and end != -1:
    html = html[:start] + new_booking + html[end:]
    
    # Also fix the View Work links
    html = html.replace('href="#"', 'href="projects.html"')
    html = html.replace('href="/"', 'href="projects.html"')

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("HTML Updated")
else:
    print("Could not find start/end")
