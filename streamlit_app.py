import os
import webbrowser

def generate_visual_baguio_website():
    # Verified real photo URLs for each specific Baguio stop
    img_hotel = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSp7904HFSYFqJz5hViqRWDd5W_kuO2hNGxUOCn7Lg51g&s" # Hotel room/lobby vibe
    img_goodtaste = "https://i0.wp.com/shellwanders.com/wp-content/uploads/2023/11/Good-taste-cafe-and-restaurant-baguio-Food.png?resize=720%2C730&ssl=1" # Good Taste food/restaurant
    img_burnham = "https://i.pinimg.com/736x/e3/51/08/e351089c4ffedfec45835b0c088be245.jpg" # Burnham Lake, Baguio
    img_ilikha = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEifmuhRfMXPsmp3WQ_-2q4jqvcgwpRCYHzG3U6Mei9MYlfRsKpv31w8gRxfLEwf-iKO-M9mFZA0dspOC_tjbz123_65sPB0yZNViNNzDH_OLQd7D8aGRcnkXcyieNNdj-2ozuUOTdQulP7dkXHnNRv74eTRBzJV7YtOmkKqEeJ5-I9fE6Z3e67ZTkn-6g/s1600/Ili%20Likhaan-7.jpg" # Ili-Likha Artists Village
    img_sm = "https://encrypted-tbn2.gstatic.com/licensed-image?q=tbn:ANd9GcTHAT_2Dib-tY8AXEX61isbo6_YqdLN-3pk3_1tMiwQMwH_8oeJ3cgaIR5D31iCxD2ZRA9-tz3N2vHkUA0" # SM City Baguio Entrance
    img_nightmarket = "https://encrypted-tbn2.gstatic.com/licensed-image?q=tbn:ANd9GcSSUGdp2eXAtiPGjyYagOPVs7op5MoZMiUqvKkINowAZBdCg9k9qE42XMqgiHi0ETMwEF93ND-hx9geU8I" # Baguio Night Market on Harrison Road

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Baguio Real Itinerary | Benguet Prime Hotel</title>
    <style>
        :root {{
            --pine-dark: #0f3d2e;
            --pine-mid: #256149;
            --pine-light: #e6f7ef;
            --accent: #d97706;
            --bg: #f3f7f4;
            --card: #ffffff;
            --text: #111827;
            --muted: #6b7280;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', system-ui, -apple-system, sans-serif; }}
        body {{ background-color: var(--bg); color: var(--text); padding-bottom: 60px; }}
        
        header {{
            background: linear-gradient(150deg, var(--pine-dark), var(--pine-mid));
            color: white;
            padding: 50px 20px;
            text-align: center;
            box-shadow: 0 4px 15px rgba(0,0,0,0.15);
        }}
        header h1 {{ font-size: 2.5rem; font-weight: 800; letter-spacing: -1px; margin-bottom: 10px; }}
        header p {{ opacity: 0.9; font-size: 1.1rem; max-width: 600px; margin: 0 auto; }}
        .badges {{ display: flex; justify-content: center; gap: 14px; flex-wrap: wrap; margin-top: 25px; }}
        .badge {{ background: rgba(255,255,255,0.18); padding: 8px 16px; border-radius: 30px; font-size: 0.9rem; font-weight: 600; backdrop-filter: blur(5px); }}
        
        .container {{ max-width: 960px; margin: 40px auto; padding: 0 20px; display: grid; gap: 30px; }}
        .card {{ background: var(--card); border-radius: 16px; padding: 30px; box-shadow: 0 5px 20px rgba(0,0,0,0.06); }}
        .card h2 {{ color: var(--pine-dark); border-bottom: 3px solid var(--pine-light); padding-bottom: 12px; margin-bottom: 25px; font-size: 1.6rem; font-weight: 700; }}
        
        .timeline {{ position: relative; padding-left: 30px; }}
        .timeline::before {{ content: ''; position: absolute; left: 0; top: 5px; bottom: 5px; width: 4px; background: var(--pine-mid); border-radius: 2px; }}
        .stop {{ position: relative; margin-bottom: 30px; display: flex; gap: 20px; align-items: flex-start; }}
        .stop:last-child {{ margin-bottom: 0; }}
        .stop::before {{ content: ''; position: absolute; left: -37px; top: 6px; width: 18px; height: 18px; border-radius: 50%; background: var(--accent); border: 4px solid white; box-shadow: 0 0 0 3px var(--pine-mid); z-index: 1; }}
        
        .stop-content {{ flex: 1; }}
        .time {{ font-weight: 800; color: var(--accent); font-size: 0.95rem; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 4px; display: block; }}
        .title {{ font-size: 1.3rem; font-weight: 700; color: var(--pine-dark); margin-bottom: 8px; }}
        .desc {{ color: var(--muted); font-size: 1rem; line-height: 1.6; }}
        
        .stop-image {{ width: 140px; height: 140px; object-fit: cover; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.12); cursor: pointer; transition: transform 0.2s ease, box-shadow 0.2s ease; flex-shrink: 0; }}
        .stop-image:hover {{ transform: scale(1.05); box-shadow: 0 6px 18px rgba(0,0,0,0.2); }}
        
        .checklist-item {{ display: flex; align-items: center; gap: 15px; padding: 15px 0; border-bottom: 1px solid #eee; cursor: pointer; }}
        .checklist-item:last-child {{ border-bottom: none; }}
        input[type="checkbox"] {{ width: 22px; height: 22px; accent-color: var(--pine-mid); cursor: pointer; }}
        .checklist-text {{ font-size: 1.05rem; transition: color 0.2s, text-decoration 0.2s; }}
        .checked-text {{ text-decoration: line-through; color: var(--muted); opacity: 0.8; }}
        
        footer {{ text-align: center; color: var(--muted); font-size: 0.9rem; margin-top: 30px; padding: 20px; border-top: 1px solid #eee; }}
        
        #lightbox {{ display: none; position: fixed; z-index: 9999; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.9); justify-content: center; align-items: center; cursor: pointer; opacity: 0; transition: opacity 0.3s ease; }}
        #lightbox.active {{ display: flex; opacity: 1; }}
        #lightbox-img {{ max-width: 90%; max-height: 90%; border: 5px solid white; border-radius: 8px; box-shadow: 0 0 30px rgba(0,0,0,0.5); transform: scale(0.9); transition: transform 0.3s ease; }}
        #lightbox.active #lightbox-img {{ transform: scale(1); }}

        @media (max-width: 768px) {{
            .stop {{ flex-direction: column-reverse; gap: 15px; }}
            .stop-image {{ width: 100%; height: 180px; }}
            header h1 {{ font-size: 2rem; }}
        }}
    </style>
</head>
<body>

<header>
    <h1>🌲 Baguio Real-Photo Itinerary</h1>
    <p>Your interactive day guide. Click any photo to expand.</p>
    <div class="badges">
        <span class="badge">🚌 Arrival: 5:55 AM</span>
        <span class="badge">🏨 Benguet Prime Hotel</span>
        <span class="badge">🔑 Check-in: 2:00 PM</span>
    </div>
</header>

<div class="container">
    <div class="card">
        <h2>⏰ Day 1 - Schedule & Real Photography</h2>
        <div class="timeline">
            
            <div class="stop">
                <img src="{img_hotel}" alt="Benguet Prime Hotel" class="stop-image" onclick="openLightbox(this.src)">
                <div class="stop-content">
                    <span class="time">5:55 AM – 6:30 AM</span>
                    <h3 class="title">Luggage Drop-Off</h3>
                    <p class="desc">Head directly to Benguet Prime Hotel on F. Calderon St. Drop your bags at the front desk and begin your hands-free adventure.</p>
                </div>
            </div>

            <div class="stop">
                <img src="{img_goodtaste}" alt="Good Taste Restaurant" class="stop-image" onclick="openLightbox(this.src)">
                <div class="stop-content">
                    <span class="time">6:30 AM – 8:30 AM</span>
                    <h3 class="title">Breakfast at Good Taste</h3>
                    <p class="desc">Fuel up with a hearty local breakfast. Experience getting your food served with their famous robot crew.</p>
                </div>
            </div>

            <div class="stop">
                <img src="{img_burnham}" alt="Burnham Park" class="stop-image" onclick="openLightbox(this.src)">
                <div class="stop-content">
                    <span class="time">8:30 AM – 9:30 AM</span>
                    <h3 class="title">Stroll at Burnham Park</h3>
                    <p class="desc">Experience the famous Burnham Lagoon. Rent a small rowboat or enjoy the quiet, crisp morning air walking around the pathways.</p>
                </div>
            </div>

            <div class="stop">
                <img src="{img_ilikha}" alt="Ili-Likha Artists Village" class="stop-image" onclick="openLightbox(this.src)">
                <div class="stop-content">
                    <span class="time">10:00 AM – 1:00 PM</span>
                    <h3 class="title">Ili-Likha Artists Village</h3>
                    <p class="desc">Explore this hidden food and art park in Baguio City. You will be greeted by woodwork, sculptures, stained glass arts, and cozy local cafes.</p>
                </div>
            </div>

            <div class="stop">
                <img src="{img_hotel}" alt="Hotel Check-In" class="stop-image" onclick="openLightbox(this.src)">
                <div class="stop-content">
                    <span class="time">1:30 PM – 2:00 PM</span>
                    <h3 class="title">Hotel Check-In & Rest</h3>
                    <p class="desc">Return to Benguet Prime Hotel to grab your bags, check into your room, and rest up after an early morning start.</p>
                </div>
            </div>

            <div class="stop">
                <img src="{img_sm}" alt="SM City Baguio" class="stop-image" onclick="openLightbox(this.src)">
                <div class="stop-content">
                    <span class="time">6:00 PM – 8:30 PM</span>
                    <h3 class="title">SM City Baguio & Dinner</h3>
                    <p class="desc">Enjoy the cool evening breeze and panoramic views of the city proper from the open-air terraces of SM Baguio.</p>
                </div>
            </div>

            <div class="stop">
                <img src="{img_nightmarket}" alt="Baguio Night Market" class="stop-image" onclick="openLightbox(this.src)">
                <div class="stop-content">
                    <span class="time">9:00 PM – 10:00 PM</span>
                    <h3 class="title">Baguio Night Market (Harrison Road)</h3>
                    <p class="desc">Browse through the vibrant ukay-ukay thrift stalls and sample delicious street food right near Burnham Park.</p>
                </div>
            </div>

        </div>
    </div>

    <div class="card">
        <h2>🎒 Interactive Packing Checklist</h2>
        <div id="checklist">
            <label class="checklist-item"><input type="checkbox" onchange="toggleItem(this)"><span class="checklist-text">Light jacket or sweater (Crucial: Baguio evenings get chilly!)</span></label>
            <label class="checklist-item"><input type="checkbox" onchange="toggleItem(this)"><span class="checklist-text">Comfortable walking shoes (For parks & hills)</span></label>
            <label class="checklist-item"><input type="checkbox" onchange="toggleItem(this)"><span class="checklist-text">Reusable water bottle</span></label>
            <label class="checklist-item"><input type="checkbox" onchange="toggleItem(this)"><span class="checklist-text">Compact umbrella or rain gear</span></label>
            <label class="checklist-item"><input type="checkbox" onchange="toggleItem(this)"><span class="checklist-text">Power bank and charging cables</span></label>
            <label class="checklist-item"><input type="checkbox" onchange="toggleItem(this)"><span class="checklist-text">Cash / small bills (Jeepneys, taxis, night market stalls)</span></label>
        </div>
    </div>
</div>

<footer>Generated with Real Photos via Python • Have a wonderful trip to the Summer Capital!</footer>

<div id="lightbox" onclick="closeLightbox()">
    <img id="lightbox-img" src="" alt="Full size preview">
</div>

<script>
    function toggleItem(checkbox) {{
        const textSpan = checkbox.nextElementSibling;
        if (checkbox.checked) {{
            textSpan.classList.add('checked-text');
        }} else {{
            textSpan.classList.remove('checked-text');
        }}
    }}

    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightbox-img');

    function openLightbox(imgSrc) {{
        lightboxImg.src = imgSrc;
        lightbox.classList.add('active');
    }}

    function closeLightbox() {{
        lightbox.classList.remove('active');
        setTimeout(() => {{ if(!lightbox.classList.contains('active')) lightboxImg.src = ''; }}, 300);
    }}

    document.addEventListener('keydown', e => {{
        if (e.key === 'Escape' && lightbox.classList.contains('active')) {{
            closeLightbox();
        }}
    }});
</script>

</body>
</html>
"""

    filename = "visual_baguio_guide.html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_content)

    full_path = os.path.abspath(filename)
    print(f"Visual dashboard created at: {full_path}")
    webbrowser.open(f"file:///{full_path}")

if __name__ == "__main__":
    generate_visual_baguio_website()
