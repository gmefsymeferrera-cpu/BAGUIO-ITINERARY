import streamlit as st
import streamlit.components.v1 as components

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
    .stop-card {{
        background-color: {card_bg};
        border: 1.5px solid {border_color} !important;
        border-radius: 20px;
        padding: 18px;
        margin-bottom: 16px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.06);
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
        <h1 style="font-family: 'Pacifico', cursive !important; color: #FFFFFF !important; font-size: 3.8rem !important; font-weight: 400 !important; text-shadow: 0 4px 20px rgba(0,0,0,0.9); margin: 0px 0px 2px 0px; line-height: 1.1;">Baguio Itinerary</h1>
        <p style="color: #FFFFFF !important; font-size: 0.95rem !important; font-weight: 600; letter-spacing: 2px; margin: 5px 0 10px 0; text-shadow: 0 2px 6px rgba(0,0,0,0.7); text-transform: uppercase;">🌲 3 Days & 2 Nights Highland Escape 🌲</p>
        <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 8px;">
            <span style="background: rgba(0, 0, 0, 0.45); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.6); padding: 5px 14px; border-radius: 20px; font-size: 0.8rem; font-weight: 600; color: #FFFFFF !important;">🚌 Arrival: 5:55 AM</span>
            <span style="background: rgba(0, 0, 0, 0.45); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.6); padding: 5px 14px; border-radius: 20px; font-size: 0.8rem; font-weight: 600; color: #FFFFFF !important;">🏨 Benguet Prime Hotel</span>
        </div>
    </div>
</div>
"""
components.html(banner_html, height=banner_height + 30)

# Weather Widget
st.markdown("🌡️ **Baguio Live Weather Forecast:** `18°C` • 🌫️ **Misty Pine & Cool**")
st.divider()

# --- ITINERARY DATA ---
itinerary_days = [
    {
        "tab_label": "DAY 1",
        "header": "DAY 1 — Downtown Core, Art & Night Market",
        "stops": [
            {
                "time": "5:55 AM - 6:15 AM",
                "title": "1. Arrival - Baguio City Terminal",
                "desc": "Touch Down! Welcome to Baguio.",
                "img": "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?w=600",
                "transit": "🚶‍♂️ Walk ~5 mins (400m) to Benguet Prime Hotel",
            },
            {
                "time": "6:15 AM – 6:30 AM",
                "title": "2. Luggage Drop-Off at Benguet Prime Hotel",
                "desc": "Secure our belongings at the front desk on F. Calderon St. to explore hands-free.",
                "img": "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=600",
                "transit": "🚶‍♂️ Walk ~4 mins (300m) to Carantes St.",
            },
            {
                "time": "6:30 AM – 8:30 AM",
                "title": "3. Breakfast at Good Taste Restaurant",
                "desc": "Enjoy local breakfast served by their signature robotic staff.",
                "img": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=600",
                "transit": "🚶‍♂️ Walk ~3 mins (200m) across to Burnham Lagoon",
            },
            {
                "time": "8:30 AM – 9:30 AM",
                "title": "4. Burnham Park",
                "desc": "Breathe in the crisp morning pine air and enjoy a peaceful stroll by the lagoon.",
                "img": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=600",
                "transit": "🚶‍♂️ Walk ~8 mins (600m uphill via Session Rd/Assumption Rd)",
            },
            {
                "time": "10:00 AM – 1:00 PM",
                "title": "5. Ili-Likha Artists Village",
                "desc": "Discover an architectural masterpiece filled with artisan cafes and sculptures.",
                "img": "https://images.unsplash.com/photo-1513694203232-719a280e022f?w=600",
                "transit": "🚶‍♂️ Walk ~6 mins (500m) back down to Calderon St.",
            },
            {
                "time": "1:30 PM – 2:00 PM",
                "title": "6. Hotel Check-In & Rest",
                "desc": "Return to Benguet Prime Hotel to claim our room and refresh for the evening.",
                "img": "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?w=600",
                "transit": "🚶‍♂️ / 🚕 Walk ~12 mins uphill (900m) or 4-min taxi to SM City",
            },
            {
                "time": "6:00 PM – 8:30 PM",
                "title": "7. SM City Baguio & Dinner",
                "desc": "Savor dinner overlooking panoramic city lights from the open-air terraces.",
                "img": "https://images.unsplash.com/photo-1519501025264-65ba15a82390?w=600",
                "transit": "🚶‍♂️ Walk ~8 mins downhill (700m) back to Harrison Road",
            },
            {
                "time": "9:00 PM – 10:00 PM",
                "title": "8. Baguio Night Market (Harrison Road)",
                "desc": "Experience the bustling ukay-ukay thrift stalls and local street food culture.",
                "img": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=600",
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
                "img": "https://images.unsplash.com/photo-1554118811-1e0d58224f24?w=600",
                "transit": "🚕 Taxi (~12 mins) or Mines View Jeepney from Gov. Pack Rd",
            },
            {
                "time": "9:00 AM – 10:30 AM",
                "title": "2. Baguio Botanical Garden",
                "desc": "Wander through towering pine avenues, orchid houses, and cultural heritage huts.",
                "img": "https://images.unsplash.com/photo-1513836279014-a89f7a76ae86?w=600",
                "transit": "🚶‍♂️ Walk ~10 mins (750m) along Leonard Wood Rd to Wright Park",
            },
            {
                "time": "10:30 AM – 12:00 PM",
                "title": "3. Wright Park & The Mansion",
                "desc": "Marvel at the iconic Pool of Pines and the historic presidential summer residence.",
                "img": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=600",
                "transit": "🚕 Short taxi or jeepney ride (~6 mins) uphill to Mines View",
            },
            {
                "time": "12:15 PM – 2:30 PM",
                "title": "4. Mines View Park & Good Shepherd Convent",
                "desc": "Take in sweeping mountain vistas and purchase world-famous Good Shepherd Ube Jam.",
                "img": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=600",
                "transit": "🚕 Taxi (~10 mins) to Camp John Hay",
            },
            {
                "time": "3:00 PM – 6:30 PM",
                "title": "5. Camp John Hay (Bell House & Eco-Trail)",
                "desc": "Unwind amidst American-era heritage architecture and pine forest walking trails.",
                "img": "https://images.unsplash.com/photo-1542224566-6e85f2e6772f?w=600",
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
                "img": "https://images.unsplash.com/photo-1464965911861-746a04b4bca6?w=600",
                "transit": "🚕 Taxi (~15 mins) to Tam-awan Village",
            },
            {
                "time": "10:15 AM – 12:00 PM",
                "title": "2. Tam-awan Village",
                "desc": "Immerse yourself in authentic Ifugao indigenous art and mountainside galleries.",
                "img": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=600",
                "transit": "🚕 Taxi (~15 mins) back to downtown / Benguet Prime Hotel",
            },
            {
                "time": "12:00 PM – 1:30 PM",
                "title": "3. Hotel Check-Out & Baguio Public Market",
                "desc": "Check out, retrieve luggage, and acquire local Benguet coffee beans and fresh produce.",
                "img": "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=600",
                "transit": "🚶‍♂️ Walk ~5 mins (400m) back to Benguet Prime Hotel",
            },
            {
                "time": "2:00 PM – 3:30 PM",
                "title": "4. Farewell Lunch on Session Road & Departure",
                "desc": "Relish a final meal on Session Road before heading to the bus terminal for departure.",
                "img": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=600",
                "transit": "🚌 Safe travels back home!",
            },
        ],
    },
]

# Initialize session state
if "selected_day_idx" not in st.session_state:
    st.session_state.selected_day_idx = 0
if "is_expanded" not in st.session_state:
    st.session_state.is_expanded = True

st.markdown("### ⏰ 3 Days Itinerary")
st.markdown("<p style='font-size: 0.95rem; margin-top: -10px;'>Select a day below to reveal its schedule:</p>", unsafe_allow_html=True)

# --- HORIZONTAL NAVIGATION BUTTONS ---
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

# --- CONTENT DISPLAY CONTAINER ---
if st.session_state.is_expanded:
    active_day = itinerary_days[st.session_state.selected_day_idx]
    st.markdown(f"<h4 style='margin-top: 25px; margin-bottom: 15px;'>{active_day['header']}</h4>", unsafe_allow_html=True)

    for stop in active_day["stops"]:
        # Naayos gamit ang custom div wrapper imbes na st.container(border=True) para maiwasan ang UI crashes
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

st.divider()

# --- BUDGET & EXPENSE CALCULATOR ---
st.subheader("💰 Expense Calculator")
st.markdown("Calculate our Travel expenses:")

col_b1, col_b2, col_b3 = st.columns(3)
with col_b1:
    transpo_cost = st.number_input("Taxi / Transpo (PHP)", min_value=0, value=1200, step=100)
with col_b2:
    food_cost = st.number_input("Food & Dining (PHP)", min_value=0, value=3500, step=200)
with col_b3:
    pasalubong_cost = st.number_input("Souvenirs (PHP)", min_value=0, value=2000, step=200)

total_est_budget = transpo_cost + food_cost + pasalubong_cost
st.info(f"💡 **Estimated Out-of-Pocket Expenses:** ₱{total_est_budget:,} (Not including hotel accommodation)")

st.divider()

# --- MAP SECTION ---
st.subheader("🗺️ Neighborhood Reference Map")
st.markdown("Interactive cartography centered around Benguet Prime Hotel:")

map_html = """
<iframe 
    src="https://maps.google.com/maps?q=Benguet+Prime+Hotel,+F.+Calderon+St,+Baguio+City&t=m&z=15&output=embed" 
    width="100%" 
    height="380" 
    style="border:0; border-radius: 16px; box-shadow: 0 8px 24px rgba(0,0,0,0.06);" 
    allowfullscreen="" 
    loading="lazy">
</iframe>
"""
components.html(map_html, height=400)

st.divider()

# --- INTERACTIVE PACKING CHECKLIST ---
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

st.divider()
st.markdown("<p style='text-align: center; font-size: 0.9rem;'>Enjoy! 🍓 </p>", unsafe_allow_html=True)
