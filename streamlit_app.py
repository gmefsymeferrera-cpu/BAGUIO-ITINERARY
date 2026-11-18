import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

# Page setup
st.set_page_config(
    page_title="Baguio Itinerary | December 20-22",
    page_icon="🍓",
    layout="centered",
)

# --- CONFIG & BANNER CONTROLS ---
page_theme = "Earthy Sage & Gold (Botanical)"
header_img_url = "https://cdn.corner.inc/place-photo/Ab43m-t7jaJzsCTchqAeA-yawcbwHPOITbjj2Mz0uiBiR90VfW5yaFfzVDYvGQXXxEVOnMoFrtBpqoixwUg2SY0oOYFdfhtdJkvgfrjzcHfKTnED0afxFsLEpdne9X-XuyoN3gFpmnf6TUcBl9vogDTjmJZkkZdGCFVSPnF7LunVVaroHAD5KELaHf6Q5QKBXyZxXo0fLGOLKRXrF8khWj7XqD1V_oKA0HdrWomHZqL_mwn39ZXNwSuVFiRBrhqnMNmg9Koxkhn92irpi_h-ETlQ919Srksyc1Q9nfZYpsA2rKf6WQIBZpbQo7FS9pS7fe_BwmRu3iqDi0vb3WuLn3KunmHU51pkcscEDpyZC-51EoSpmcTpZ_BsiuDnTSo72HbSA_FiB0MNu7CrkHguJO0J1UyOGY0irSBNqeVdNvams-ciYzpFZdBPlegCKE_tl1bf.jpeg"
banner_height = 210
banner_vertical_pos = 35
banner_alpha = 0.15

# Color Tokens (Light Mode Only)
bg_css_rule = "background-color: #ffffff;"
text_color = "#23332a"
card_bg = "#ffffff"
border_color = "#d6e0d8"
accent_color = "#507a64"
gold_accent = "#b8860b"

# Custom CSS
custom_css = f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Montserrat:wght@400;500;600;700&display=swap');
    .stApp {{
        {bg_css_rule}
        color: {text_color} !important;
        font-family: 'Montserrat', sans-serif !important;
    }}
    h2, h3, h4, h5, h6 {{
        font-family: 'Montserrat', sans-serif !important;
        font-weight: 700;
        letter-spacing: 0.3px;
        color: {text_color} !important;
    }}
    p, span, label, div, markdown, .stMarkdown, [data-testid="stMarkdownContainer"] p {{
        font-family: 'Montserrat', sans-serif !important;
        color: {text_color} !important;
    }}
    .stop-card, .contact-card {{
        background-color: {card_bg};
        border: 1.5px solid {border_color} !important;
        border-radius: 20px;
        padding: 18px;
        margin-bottom: 16px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.06);
        text-align: center;
    }}
    div.stButton > button {{
        width: 100%;
        border-radius: 16px !important;
        padding: 18px 14px !important;
        border: 2px solid {border_color} !important;
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        background-color: {card_bg} !important;
    }}
    div.stButton > button p {{
        font-family: 'Montserrat', sans-serif !important;
        font-size: 1.25rem !important;
        font-weight: 700 !important;
        letter-spacing: 1px !important;
        margin: 0 !important;
        color: {text_color} !important;
    }}
    div.stButton > button[kind="primary"] {{
        background: linear-gradient(135deg, {accent_color}, {gold_accent}) !important;
        border-color: transparent !important;
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }}
    div.stButton > button[kind="primary"] p {{
        color: #ffffff !important;
        text-shadow: 0 1px 3px rgba(0,0,0,0.3);
    }}
    .time-tag {{
        color: {gold_accent} !important;
        font-weight: 700;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }}
    .transit-badge {{
        background-color: rgba(184, 134, 11, 0.1);
        color: {gold_accent};
        padding: 6px 14px;
        border-radius: 10px;
        font-size: 0.85rem;
        font-weight: 600;
        display: inline-block;
        margin: 10px 0px;
        border-left: 3px solid {gold_accent};
    }}
    .collage-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
        gap: 12px;
        padding: 10px 0;
    }}
    .collage-item {{
        position: relative;
        overflow: hidden;
        border-radius: 16px;
        box-shadow: 0 6px 15px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
        border: 2px solid {border_color};
        background: #fff;
        padding: 8px;
    }}
    .collage-item:hover {{
        transform: scale(1.03);
    }}
    </style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Compact Banner HTML
banner_html = f"""
<div style="
    background-image: linear-gradient(135deg, rgba(10, 25, 18, {banner_alpha}) 0%, rgba(20, 15, 5, {banner_alpha}) 100%), url('{header_img_url}');
    background-size: cover;
    background-position: center {banner_vertical_pos}%;
    padding: 20px;
    border-radius: 24px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    min-height: {banner_height}px;
    margin-bottom: 25px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.15);
    border: 2px solid rgba(255, 255, 255, 0.4);
">
    <div style="width: 100%; display: flex; flex-direction: column; align-items: center;">
        <h1 style="font-family: 'Ziglets', cursive !important; color: #FFFFFF !important; font-size: 4.2rem !important; font-weight: 400 !important; text-shadow: 0 4px 20px rgba(0,0,0,0.9); margin: 0px 0px 2px 0px; line-height: 1.5;">Baguio Itinerary</h1>
        <p style="color: #FFFFFF !important; font-size: 1rem !important; font-weight: 600; letter-spacing: 2px; margin: 5px 0 10px 0; text-shadow: 0 2px 6px rgba(0,0,0,0.7); text-transform: uppercase;"> 🍓3 Days & 2 Nights Escape 🍓</p>
        <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 8px;">
            <span style="background: rgba(0, 0, 0, 0.45); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.6); padding: 5px 14px; border-radius: 20px; font-size: 0.85rem; font-weight: 600; color: #FFFFFF !important;">🚌 Arrival: December 20, 5:55 AM</span>
            <span style="background: rgba(0, 0, 0, 0.45); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.6); padding: 5px 14px; border-radius: 20px; font-size: 0.85rem; font-weight: 600; color: #FFFFFF !important;">🏨 Benguet Prime Hotel</span>
        </div>
    </div>
</div>
"""
components.html(banner_html, height=banner_height + 60)

# --- REDESIGNED STYLISH WEATHER WIDGET ---
weather_widget_html = f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600;700&display=swap');
    .weather-card {{
        background: linear-gradient(135deg, rgba(80, 122, 100, 0.08) 0%, rgba(184, 134, 11, 0.08) 100%);
        border: 2px solid {border_color};
        border-radius: 20px;
        padding: 16px 20px;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-wrap: wrap;
        gap: 15px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.04);
        font-family: 'Montserrat', sans-serif;
    }}
    .weather-left {{
        display: flex;
        align-items: center;
        gap: 14px;
    }}
    .weather-icon {{
        font-size: 2.5rem;
        background: #ffffff;
        border: 1.5px solid {border_color};
        border-radius: 16px;
        padding: 8px 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }}
    .weather-title {{
        font-size: 0.8rem;
        font-weight: 700;
        color: {accent_color};
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-bottom: 2px;
    }}
    .weather-main {{
        font-size: 1.35rem;
        font-weight: 700;
        color: {text_color};
    }}
    .weather-right {{
        display: flex;
        gap: 15px;
    }}
    .weather-badge {{
        background-color: #ffffff;
        border: 1.5px solid {border_color};
        border-radius: 12px;
        padding: 8px 12px;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.03);
    }}
    .badge-label {{
        font-size: 0.65rem;
        font-weight: 600;
        color: {text_color};
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }}
    .badge-val {{
        font-size: 0.9rem;
        font-weight: 700;
        color: {gold_accent};
        margin-top: 2px;
    }}
</style>

<div class="weather-card">
    <div class="weather-left">
        <div class="weather-icon">🌫️</div>
        <div>
            <div class="weather-title">Baguio City Live Weather</div>
            <div class="weather-main">18°C &nbsp;•&nbsp; <span style="font-size: 1rem; font-weight: 600; color: {accent_color};">Misty Pine & Cool</span></div>
        </div>
    </div>
    <div class="weather-right">
        <div class="weather-badge">
            <div class="badge-label">Humidity</div>
            <div class="badge-val">88%</div>
        </div>
        <div class="weather-badge">
            <div class="badge-label">Wind</div>
            <div class="badge-val">12 km/h</div>
        </div>
    </div>
</div>
"""
components.html(weather_widget_html, height=105)

# --- LIVE COUNTDOWN ---
countdown_html = f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700&display=swap');
    .countdown-card {{
        background: linear-gradient(135deg, rgba(80, 122, 100, 0.08) 0%, rgba(184, 134, 11, 0.08) 100%);
        border: 2px solid {border_color};
        border-radius: 20px;
        padding: 22px 18px;
        margin-top: 15px;
        margin-bottom: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        text-align: center;
        font-family: 'Montserrat', sans-serif;
    }}
    .countdown-title {{
        font-size: 0.95rem;
        font-weight: 700;
        color: {accent_color};
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-bottom: 12px;
    }}
    .countdown-grid {{
        display: flex;
        justify-content: center;
        gap: 12px;
        flex-wrap: wrap;
    }}
    .countdown-box {{
        background-color: #ffffff;
        border: 1.5px solid {border_color};
        border-radius: 14px;
        padding: 10px 12px;
        min-width: 65px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.04);
    }}
    .countdown-num {{
        font-size: 1.4rem;
        font-weight: 700;
        color: {gold_accent};
        line-height: 1.2;
    }}
    .countdown-label {{
        font-size: 0.7rem;
        font-weight: 600;
        color: {text_color};
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-top: 2px;
    }}
</style>

<div class="countdown-card">
    <div class="countdown-title">⏳ Countdown Until This Baguio Trip! 🍓🌲</div>
    <div class="countdown-grid" id="countdown">
        <div class="countdown-box"><div class="countdown-num" id="days">--</div><div class="countdown-label">Day</div></div>
        <div class="countdown-box"><div class="countdown-num" id="hours">--</div><div class="countdown-label">Hour</div></div>
        <div class="countdown-box"><div class="countdown-num" id="minutes">--</div><div class="countdown-label">Minute</div></div>
        <div class="countdown-box"><div class="countdown-num" id="seconds">--</div><div class="countdown-label">Second</div></div>
    </div>
</div>

<script>
    const targetDate = new Date("December 20, 2026 05:55:00").getTime();

    function updateCountdown() {{
        const now = new Date().getTime();
        const distance = targetDate - now;

        if (distance < 0) {{
            document.getElementById("countdown").innerHTML = "<h3 style='color: #507a64; margin: 0;'>🎉 Nandito na tayo o nakalipas na ang petsa ng ating Baguio trip! Enjoy!</h3>";
            return;
        }}

        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        document.getElementById("days").innerText = days;
        document.getElementById("hours").innerText = hours;
        document.getElementById("minutes").innerText = minutes;
        document.getElementById("seconds").innerText = seconds;
    }}

    setInterval(updateCountdown, 1000);
    updateCountdown();
</script>
"""

components.html(countdown_html, height=170)
st.divider()

# --- NAVIGATION TABS (MAIN SECTIONS) ---
selected_tab = st.selectbox(
    "Choices:",
    [
        "📅 3-Day Itinerary", 
        "💰 Expense Calculator", 
        "🎒 Packing Checklist", 
        "📝 Travel Journal & Notes", 
        "📸 Photo Gallery",
        "🗺️ Map & 🚨 Emergency Contacts"
    ]
)

st.divider()

# ==========================================
# 1. ITINERARY SECTION
# ==========================================
if selected_tab == "📅 3-Day Itinerary":
    itinerary_days = [
        {
            "tab_label": "DAY 1",
            "header": "DAY 1 — Downtown Core, Art & Night Market",
            "stops": [
                {
                    "time": "5:55 AM - 6:15 AM",
                    "title": "1. Arrival - Baguio City Terminal",
                    "desc": "Touch Down! Welcome to Baguio.",
                    "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQBz7rtObyyo6ISt9Wc8fjp_Y6tISdxKiqjP86i1hFOoftnfQy_u1ds2-zL&s=10",
                    "transit": "🚶‍♂️ Walk ~5 mins (400m) to Benguet Prime Hotel",
                },
                {
                    "time": "6:15 AM – 6:30 AM",
                    "title": "2. Luggage Drop-Off at Benguet Prime Hotel",
                    "desc": "Secure our belongings at the front desk on F. Calderon St. to explore hands-free.",
                    "img": "https://pix10.agoda.net/hotelImages/30155249/0/1ee5b88cd5ae9c397d4baf3e53da783f.jpeg?ce=2&s=414x232",
                    "transit": "🚶‍♂️ Walk ~4 mins (300m) to Carantes St.",
                },
                {
                    "time": "6:30 AM – 8:30 AM",
                    "title": "3. Breakfast at Good Taste Restaurant",
                    "desc": "Enjoy local breakfast served by their signature robotic staff.",
                    "img": "https://i0.wp.com/shellwanders.com/wp-content/uploads/2023/11/Good-taste-cafe-and-restaurant-baguio-Food.png?resize=720%2C730&ssl=1",
                    "transit": "🚶‍♂️ Walk ~3 mins (200m) across to Burnham Lagoon",
                },
                {
                    "time": "8:30 AM – 9:30 AM",
                    "title": "4. Burnham Park",
                    "desc": "Breathe in the crisp morning pine air and enjoy a peaceful stroll by the lagoon.",
                    "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSmOEbzDrhZOWyTvF9DPkwsNph6mg3A8zsMJSITie6WM_TQODGtHNOjALc&s=10",
                    "transit": "🚶‍♂️ Walk ~8 mins (600m uphill via Session Rd/Assumption Rd)",
                },
                {
                    "time": "10:00 AM – 1:00 PM",
                    "title": "5. Ili-Likha Artists Village",
                    "desc": "Discover an architectural masterpiece filled with artisan cafes and sculptures.",
                    "img": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEifmuhRfMXPsmp3WQ_-2q4jqvcgwpRCYHzG3U6Mei9MYlfRsKpv31w8gRxfLEwf-iKO-M9mFZA0dspOC_tjbz123_65sPB0yZNViNNzDH_OLQd7D8aGRcnkXcyieNNdj-2ozuUOTdQulP7dkXHnNRv74eTRBzJV7YtOmkKqEeJ5-I9fE6Z3e67ZTkn-6g/s1600/Ili%20Likhaan-7.jpg",
                    "transit": "🚶‍♂️ Walk ~6 mins (500m) back down to Calderon St.",
                },
                {
                    "time": "1:30 PM – 2:00 PM",
                    "title": "6. Hotel Check-In & Rest",
                    "desc": "Return to Benguet Prime Hotel to claim our room and refresh for the evening.",
                    "img": "https://cf.bstatic.com/xdata/images/hotel/max1024x768/172377839.jpg?k=1d4760bf2cdfd7abf95af2fa677c4fd253e7977b98eb19b3832bfccc6f37be96&o=",
                    "transit": "🚶‍♂️ / 🚕 Walk ~12 mins uphill (900m) or 4-min taxi to SM City",
                },
                {
                    "time": "6:00 PM – 8:30 PM",
                    "title": "7. SM City Baguio & Dinner",
                    "desc": "Savor dinner overlooking panoramic city lights from the open-air terraces.",
                    "img": "https://encrypted-tbn2.gstatic.com/licensed-image?q=tbn:ANd9GcTHAT_2Dib-tY8AXEX61isbo6_YqdLN-3pk3_1tMiwQMwH_8oeJ3cgaIR5D31iCxD2ZRA9-tz3N2vHkUA0",
                    "transit": "🚶‍♂️ Walk ~8 mins downhill (700m) back to Harrison Road",
                },
                {
                    "time": "9:00 PM – 10:00 PM",
                    "title": "8. Baguio Night Market (Harrison Road)",
                    "desc": "Experience the bustling ukay-ukay thrift stalls and local street food culture.",
                    "img": "https://encrypted-tbn2.gstatic.com/licensed-image?q=tbn:ANd9GcSSUGdp2eXAtiPGjyYagOPVs7op5MoZMiUqvKkINowAZBdCg9k9qE42XMqgiHi0ETMwEF93ND-hx9geU8I",
                    "transit": "🏨 Short walk back to Benguet Prime Hotel for a restful night.",
                },
            ],
        },
        {
            "tab_label": "DAY 2",
            "header": "DAY 2 — Pine Forests, Parks & Mountain Views",
            "stops": [
                {
                    "time": "7:30 AM – 8:30 AM",
                    "title": "1. Breakfast at Café by the Ruins",
                    "desc": "Enjoy artisan hot chocolate-eh and traditional Cordillera breakfast specialties.",
                    "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSmOEbzDrhZOWyTvF9DPkwsNph6mg3A8zsMJSITie6WM_TQODGtHNOjALc&s=10",
                    "transit": "🚕 Taxi (~12 mins) or Mines View Jeepney from Gov. Pack Rd",
                },
                {
                    "time": "9:00 AM – 10:30 AM",
                    "title": "2. Baguio Botanical Garden",
                    "desc": "Wander through towering pine avenues, orchid houses, and cultural heritage huts.",
                    "img": "https://shoestringdiary.wordpress.com/wp-content/uploads/2023/05/miradorhill08-cover-ssdiaries.jpg?w=1140",
                    "transit": "🚶‍♂️ Walk ~10 mins (750m) along Leonard Wood Rd to Wright Park",
                },
                {
                    "time": "10:30 AM – 12:00 PM",
                    "title": "3. Wright Park & The Mansion",
                    "desc": "Marvel at the iconic Pool of Pines and the historic presidential summer residence.",
                    "img": "https://encrypted-tbn2.gstatic.com/licensed-image?q=tbn:ANd9GcTHAT_2Dib-tY8AXEX61isbo6_YqdLN-3pk3_1tMiwQMwH_8oeJ3cgaIR5D31iCxD2ZRA9-tz3N2vHkUA0",
                    "transit": "🚕 Short taxi or jeepney ride (~6 mins) uphill to Mines View",
                },
                {
                    "time": "12:15 PM – 2:30 PM",
                    "title": "4. Mines View Park & Good Shepherd Convent",
                    "desc": "Take in sweeping mountain vistas and purchase world-famous Good Shepherd Ube Jam.",
                    "img": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEifmuhRfMXPsmp3WQ_-2q4jqvcgwpRCYHzG3U6Mei9MYlfRsKpv31w8gRxfLEwf-iKO-M9mFZA0dspOC_tjbz123_65sPB0yZNViNNzDH_OLQd7D8aGRcnkXcyieNNdj-2ozuUOTdQulP7dkXHnNRv74eTRBzJV7YtOmkKqEeJ5-I9fE6Z3e67ZTkn-6g/s1600/Ili%20Likhaan-7.jpg",
                    "transit": "🚕 Taxi (~10 mins) to Camp John Hay",
                },
                {
                    "time": "3:00 PM – 6:30 PM",
                    "title": "5. Camp John Hay (Bell House & Eco-Trail)",
                    "desc": "Unwind amidst American-era heritage architecture and pine forest walking trails.",
                    "img": "https://shoestringdiary.wordpress.com/wp-content/uploads/2023/05/miradorhill08-cover-ssdiaries.jpg?w=1140",
                    "transit": "🚕 Taxi (~10 mins) back to Benguet Prime Hotel / Session Road",
                },
            ],
        },
        {
            "tab_label": "DAY 3",
            "header": "DAY 3 — Strawberry Farms, Culture & Pasalubong",
            "stops": [
                {
                    "time": "7:30 AM – 10:00 AM",
                    "title": "1. La Trinidad Strawberry Farm & StoBoSa",
                    "desc": "Pick fresh strawberries, enjoy strawberry taho, and admire the vibrant hillside mural art.",
                    "img": "https://i0.wp.com/shellwanders.com/wp-content/uploads/2023/11/Good-taste-cafe-and-restaurant-baguio-Food.png?resize=720%2C730&ssl=1",
                    "transit": "🚕 Taxi (~15 mins) to Tam-awan Village",
                },
                {
                    "time": "10:15 AM – 12:00 PM",
                    "title": "2. Tam-awan Village",
                    "desc": "Immerse yourself in authentic Ifugao indigenous art and mountainside galleries.",
                    "img": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEifmuhRfMXPsmp3WQ_-2q4jqvcgwpRCYHzG3U6Mei9MYlfRsKpv31w8gRxfLEwf-iKO-M9mFZA0dspOC_tjbz123_65sPB0yZNViNNzDH_OLQd7D8aGRcnkXcyieNNdj-2ozuUOTdQulP7dkXHnNRv74eTRBzJV7YtOmkKqEeJ5-I9fE6Z3e67ZTkn-6g/s1600/Ili%20Likhaan-7.jpg",
                    "transit": "🚕 Taxi (~15 mins) back to downtown / Benguet Prime Hotel",
                },
                {
                    "time": "12:00 PM – 1:30 PM",
                    "title": "3. Hotel Check-Out & Baguio Public Market",
                    "desc": "Check out, retrieve luggage, and acquire local Benguet coffee beans and fresh produce.",
                    "img": "https://cf.bstatic.com/xdata/images/hotel/max1024x768/172377839.jpg?k=1d4760bf2cdfd7abf95af2fa677c4fd253e7977b98eb19b3832bfccc6f37be96&o=",
                    "transit": "🚶‍♂️ Walk ~5 mins (400m) back to Benguet Prime Hotel",
                },
                {
                    "time": "2:00 PM – 3:30 PM",
                    "title": "4. Farewell Lunch on Session Road & Departure",
                    "desc": "Relish a final meal on Session Road before heading to the bus terminal for departure.",
                    "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQBz7rtObyyo6ISt9Wc8fjp_Y6tISdxKiqjP86i1hFOoftnfQy_u1ds2-zL&s=10",
                    "transit": "🚌 Safe travels back home!",
                },
            ],
        },
    ]

    if "selected_day_idx" not in st.session_state:
        st.session_state.selected_day_idx = 0
    if "is_expanded" not in st.session_state:
        st.session_state.is_expanded = True

    st.markdown("### ⏰ Select Day")
    day_cols = st.columns(3, gap="small")
    for idx, day in enumerate(itinerary_days):
        is_selected = st.session_state.selected_day_idx == idx
        arrow = "▴" if (is_selected and st.session_state.is_expanded) else "▾"
        btn_type = "primary" if (is_selected and st.session_state.is_expanded) else "secondary"

        with day_cols[idx]:
            if st.button(f"{day['tab_label']} {arrow}", key=f"day_nav_{idx}", type=btn_type, use_container_width=True):
                if is_selected:
                    st.session_state.is_expanded = not st.session_state.is_expanded
                else:
                    st.session_state.selected_day_idx = idx
                    st.session_state.is_expanded = True
                st.rerun()

    if st.session_state.is_expanded:
        active_day = itinerary_days[st.session_state.selected_day_idx]
        st.markdown(f"<h4 style='margin-top: 25px; margin-bottom: 15px;'>{active_day['header']}</h4>", unsafe_allow_html=True)

        for stop in active_day["stops"]:
            st.markdown(f"""
            <div class="stop-card">
                <div style="display: flex; gap: 15px; flex-wrap: wrap;">
                    <div style="flex: 1; min-width: 200px;">
                        <img src="{stop['img']}" style="width: 100%; height: 140px; object-fit: cover; border-radius: 12px;" />
                    </div>
                    <div style="flex: 2; min-width: 250px;">
                        <span class="time-tag">{stop['time']}</span>
                        <h3 style="margin: 5px 0 8px 0; font-size: 1.1rem;">{stop['title']}</h3>
                        <p style="margin: 0; font-size: 0.95rem;">{stop['desc']}</p>
                        <div class="transit-badge">{stop['transit']}</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown("<div style='text-align: center; padding: 25px; font-style: italic;'>✨ Itinerary curtain is closed. Click any DAY above to reveal.</div>", unsafe_allow_html=True)

# ==========================================
# 2. EXPENSE CALCULATOR & SPLITTER SECTION
# ==========================================
elif selected_tab == "💰 Expense Calculator & Splitter":
    st.subheader("💰 Trip Budget & Expense Splitter")
    st.markdown("Kalkulahin ang pangkalahatang gastos at hatiin ito kung kayo ay magkakasama:")

    col_b1, col_b2, col_b3 = st.columns(3)
    with col_b1:
        transpo_cost = st.number_input("Taxi / Transpo & Fees (PHP)", min_value=0, value=1200, step=100)
    with col_b2:
        food_cost = st.number_input("Food & Dining (PHP)", min_value=0, value=3500, step=200)
    with col_b3:
        pasalubong_cost = st.number_input("Pasalubong & Souvenirs (PHP)", min_value=0, value=2000, step=200)

    total_est_budget = transpo_cost + food_cost + pasalubong_cost
    st.info(f"💡 **Total Estimated Expenses:** ₱{total_est_budget:,} (Hindi kasama ang hotel)")

    st.markdown("---")
    st.subheader("👥 Group Expense Splitter")
    num_persons = st.slider("Ilan kayong maghahati sa gastusin?", min_value=1, max_value=10, value=2)
    
    if num_persons > 0:
        share_per_person = total_est_budget / num_persons
        st.success(f"✨ Bawat isa ay mag-aambag ng: **₱{share_per_person:,.2f}** (para sa {num_persons} katao)")

# ==========================================
# 3. PACKING CHECKLIST SECTION
# ==========================================
elif selected_tab == "🎒 Packing Checklist":
    st.subheader("🎒 Curated Packing Checklist")
    st.markdown("Check off essentials for your highland escape:")

    checklist_items = [
        "Warm wool jacket or cashmere sweater (Baguio evenings drop significantly)",
        "Comfortable walking shoes or boots (For heritage walks and pine trails)",
        "Insulated or reusable tumbler for hot chocolate and mountain tea",
        "Compact umbrella / lightweight weather shell",
        "Power bank and high-speed charging cables",
        "Philippine Peso cash & small bills (Essential for local taxis & night markets)",
    ]

    checked_states = []
    for i, item in enumerate(checklist_items):
        is_checked = st.checkbox(item, key=f"check_{i}")
        checked_states.append(is_checked)

    total_items = len(checklist_items)
    completed_items = sum(checked_states)
    progress_pct = completed_items / total_items

    st.progress(progress_pct)
    st.caption(f"✨ Packed Essentials: **{completed_items} / {total_items}** ready")

    if completed_items == total_items:
        st.success("🌟 All set! You are fully prepared for our Baguio Escape.")

# ==========================================
# 4. TRAVEL JOURNAL & NOTES SECTION
# ==========================================
elif selected_tab == "📝 Travel Journal & Notes":
    st.subheader("📝 Interactive Travel Journal & Notes")
    st.markdown("Isulat dito ang iyong mga alaala, mga biniling pasalubong, resibo, o mga susunod na pupuntahan habang naglalakbay:")

    if "travel_journal" not in st.session_state:
        st.session_state.travel_journal = "Day 1 Notes:\n- Natikman namin ang strawberry taho sa Burnham Park.\n- Masarap ang kape sa Ili-Likha!\n\nMga Resibo / Gastos:\n- Taxi going to hotel: ₱150"

    journal_text = st.text_area("I-edit ang iyong Journal:", value=st.session_state.travel_journal, height=250)
    
    if st.button("I-save ang Notes"):
        st.session_state.travel_journal = journal_text
        st.success("✅ Matagumpay na nai-save ang iyong journal notes!")

    st.markdown("---")
    st.download_button(
        label="📥 I-download ang Journal bilang Text File (.txt)",
        data=st.session_state.travel_journal,
        file_name="baguio_trip_journal.txt",
        mime="text/plain"
    )

# ==========================================
# 5. PHOTO COLLAGE GALLERY SECTION
# ==========================================
elif selected_tab == "📸 Photo Collage Gallery":
    st.subheader("📸 Baguio Memories Photo Collage")
    st.markdown("Mag-upload ng mga litrato para awtomatikong mabuo ang iyong **Photo Collage Album**:")

    if "uploaded_photos" not in st.session_state:
        st.session_state.uploaded_photos = []

    uploaded_files = st.file_uploader(
        "Mag-upload ng mga larawan para sa Collage:", 
        type=["png", "jpg", "jpeg"], 
        accept_multiple_files=True
    )

    if uploaded_files:
        for file in uploaded_files:
            if file not in st.session_state.uploaded_photos:
                st.session_state.uploaded_photos.append(file)

    if st.session_state.uploaded_photos:
        st.markdown("### 🖼️ Na-upload na Collage:")
        
        collage_html = '<div class="collage-grid">'
        for idx, photo in enumerate(st.session_state.uploaded_photos):
            import base64
            bytes_data = photo.getvalue()
            b64_str = base64.b64encode(bytes_data).decode()
            img_format = photo.type.split('/')[-1]
            
            collage_html += f'''
            <div class="collage-item">
                <img src="data:image/{img_format};base64,{b64_str}" style="width: 100%; height: 160px; object-fit: cover; border-radius: 10px;" />
                <p style="text-align: center; font-size: 0.75rem; margin: 5px 0 0 0; font-weight: 600;">Memories #{idx+1}</p>
            </div>
            '''
        collage_html += '</div>'
        
        st.markdown(collage_html, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🗑️ Linisin / Alisin lahat ng Larawan"):
            st.session_state.uploaded_photos = []
            st.rerun()
    else:
        st.info("Wala pang na-upload na larawan para sa collage. Mag-upload sa itaas para makita ang epekto!")

# ==========================================
# 6. MAP & EMERGENCY CONTACTS SECTION
# ==========================================
elif selected_tab == "🗺️ Map & 🚨 Emergency Contacts":
    st.subheader("🗺️ Neighborhood Reference Map")
    st.markdown("Interactive cartography centered around Benguet Prime Hotel:")

    map_html = """
    <iframe 
        src="https://maps.google.com/maps?q=Benguet+Prime+Hotel,+F.+Calderon+St,+Baguio+City&t=m&z=15&output=embed" 
        width="100%" 
        height="350" 
        style="border:0; border-radius: 16px; box-shadow: 0 8px 24px rgba(0,0,0,0.06);" 
        allowfullscreen="" 
        loading="lazy">
    </iframe>
    """
    components.html(map_html, height=370)

    st.divider()
    st.subheader("🚨 Emergency & Important Contacts (Baguio)")
    st.markdown("Mga importanteng numero sakaling kailanganin habang naglalakbay:")

    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.markdown("""
        <div class="contact-card">
            <h4>👮‍♂️ Public Safety</h4>
            <p><b>Baguio City Police Office:
            </b> (074) 442-1211</p>
            <p><b>Emergency Hotline:</b> 911</p>
        </div>
        """, unsafe_allow_html=True)
    with col_c2:
        st.markdown("""
        <div class="contact-card">
            <h4>🏥 Medical & Health</h4>
            <p><b>SLU Hospital of the Sacred Heart:
            </b> (074) 444-5720</p>
            <p><b>Baguio General Hospital (BGH):
            </b> (074) 442-4216</p>
        </div>
        """, unsafe_allow_html=True)

st.divider()
st.markdown("<p style='text-align: center; font-size: 0.9rem;'>Enjoy your Baguio Trip! 🍓 </p>", unsafe_allow_html=True)
