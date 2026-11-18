import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

# Page setup
st.set_page_config(
    page_title="Baguio Itinerary | December 20-22",
    page_icon="🍓",
    layout="centered",
)

# --- THEME STATE INITIALIZATION ---
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

# --- COLOR TOKENS (Dynamic batay sa Dark Mode toggle) ---
if st.session_state.dark_mode:
    bg_css_rule = "background-color: #121c17;"
    text_color = "#e2e8e4"
    card_bg = "#1b2821"
    border_color = "#2c4035"
    accent_color = "#75a38a"
    gold_accent = "#d4af37"
    banner_alpha = 0.45
else:
    bg_css_rule = "background-color: #ffffff;"
    text_color = "#23332a"
    card_bg = "#ffffff"
    border_color = "#d6e0d8"
    accent_color = "#507a64"
    gold_accent = "#b8860b"
    banner_alpha = 0.15

header_img_url = "https://cdn.corner.inc/place-photo/Ab43m-t7jaJzsCTchqAeA-yawcbwHPOITbjj2Mz0uiBiR90VfW5yaFfzVDYvGQXXxEVOnMoFrtBpqoixwUg2SY0oOYFdfhtdJkvgfrjzcHfKTnED0afxFsLEpdne9X-XuyoN3gFpmnf6TUcBl9vogDTjmJZkkZdGCFVSPnF7LunVVaroHAD5KELaHf6Q5QKBXyZxXo0fLGOLKRXrF8khWj7XqD1V_oKA0HdrWomHZqL_mwn39ZXNwSuVFiRBrhqnMNmg9Koxkhn92irpi_h-ETlQ919Srksyc1Q9nfZYpsA2rKf6WQIBZpbQo7FS9pS7fe_BwmRu3iqDi0vb3WuLn3KunmHU51pkcscEDpyZC-51EoSpmcTpZ_BsiuDnTSo72HbSA_FiB0MNu7CrkHguJO0J1UyOGY0irSBNqeVdNvams-ciYzpFZdBPlegCKE_tl1bf.jpeg"
banner_height = 210
banner_vertical_pos = 35

# Custom CSS na gumagamit ng dynamic tokens
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
        background-color: rgba(184, 134, 11, 0.15);
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
        background: {card_bg};
        padding: 8px;
    }}
    .collage-item:hover {{
        transform: scale(1.03);
    }}
    </style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# --- THEME TOGGLE SWITCH SA ITAAS ---
col_t1, col_t2 = st.columns([4, 1])
with col_t2:
    is_dark = st.toggle("🌙 Dark Mode", value=st.session_state.dark_mode)
    if is_dark != st.session_state.dark_mode:
        st.session_state.dark_mode = is_dark
        st.rerun()

# Compact Banner HTML (Gumagamit ng components.html para sa banner)
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
        <h1 style="font-family: 'Pacifico', cursive !important; color: #FFFFFF !important; font-size: 3.5rem !important; font-weight: 400 !important; text-shadow: 0 4px 20px rgba(0,0,0,0.9); margin: 0px 0px 2px 0px; line-height: 1.1;">Baguio Itinerary</h1>
        <p style="color: #FFFFFF !important; font-size: 0.95rem !important; font-weight: 600; letter-spacing: 2px; margin: 5px 0 10px 0; text-shadow: 0 2px 6px rgba(0,0,0,0.7); text-transform: uppercase;">🌲 3 Days & 2 Nights Highland Escape 🌲</p>
        <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 8px;">
            <span style="background: rgba(0, 0, 0, 0.45); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.6); padding: 5px 14px; border-radius: 20px; font-size: 0.8rem; font-weight: 600; color: #FFFFFF !important;">🚌 Arrival: Dec 20, 5:55 AM</span>
            <span style="background: rgba(0, 0, 0, 0.45); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.6); padding: 5px 14px; border-radius: 20px; font-size: 0.8rem; font-weight: 600; color: #FFFFFF !important;">🏨 Benguet Prime Hotel</span>
        </div>
    </div>
</div>
"""
components.html(banner_html, height=banner_height + 30)

# --- LIVE COUNTDOWN TIMER W/ SECONDS (Inayos gamit ang st.markdown + HTML/JS) ---
countdown_container = f"""
<div style="
    background-color: {card_bg};
    border: 1.5px solid {border_color};
    border-radius: 20px;
    padding: 16px;
    margin-bottom: 20px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.06);
    text-align: center;
">
    <h4 style="margin: 0 0 6px 0; color: {accent_color}; font-size: 1rem; font-weight: 700;">⏳ Live Countdown hanggang sa Baguio Trip!</h4>
    <div id="live-countdown" style="font-size: 1.1rem; font-weight: 700; color: {gold_accent};">
        Naglo-load ang timer...
    </div>
</div>

<script>
const countDownDate = new Date("Dec 20, 2026 05:55:00").getTime();

const timerInterval = setInterval(function() {
    const now = new Date().getTime();
    const distance = countDownDate - now;

    if (distance < 0) {
        clearInterval(timerInterval);
        document.getElementById("live-countdown").innerHTML = "🎉 Nandito na tayo o nakalipas na ang petsa ng ating Baguio trip!";
        return;
    }

    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    document.getElementById("live-countdown").innerHTML = 
        days + " Araw • " + hours + " Oras • " + minutes + " Minuto • " + seconds + " Segundo na lang! 🎒🌲";
}, 1000);
</script>
"""
st.markdown(countdown_container, unsafe_allow_html=True)

# Weather Widget
st.markdown("🌡️ **Baguio Live Weather Forecast:** `18°C` • 🌫️ **Misty Pine & Cool**")
st.divider()

# --- NAVIGATION TABS (MAIN SECTIONS) ---
selected_tab = st.selectbox(
    "Pumili ng pahina:",
    [
        "📅 3-Day Itinerary", 
        "💰 Expense Calculator & Splitter", 
        "🎒 Packing Checklist", 
        "📝 Travel Journal & Notes", 
        "📸 Photo Collage Gallery",
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
                    "img": "
