import streamlit as st
import streamlit.components.v1 as components

# Page setup
st.set_page_config(
    page_title="Baguio Itinerary | Luxury Edition",
    page_icon="🌲",
    layout="centered",
)

# --- SIDEBAR: REFINED THEME & BANNER CONTROLS ---
st.sidebar.header("✨ Elegance & Theme Studio")

page_theme = st.sidebar.selectbox(
    "Curated Color Palette",
    [
        "Earthy Sage & Gold (Botanical)",
        "Warm Cashmere & Sand (Luxury Neutral)",
        "Midnight Pine & Emerald",
        "Soft Rose & Champagne",
        "Minimalist Pearl White",
    ],
)

header_img_url = st.sidebar.text_input(
    "Title Banner Image URL",
    value="https://upload.wikimedia.org/wikipedia/commons/2/23/The_Mirador_Heritage_Eco_park.jpg?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=original",
)

banner_height = st.sidebar.slider(
    "Banner Elegance Height (px)", min_value=200, max_value=500, value=300, step=10
)

banner_vertical_pos = st.sidebar.slider(
    "Lion's Head Framing (%)", min_value=0, max_value=100, value=35, step=5
)

banner_tint = st.sidebar.slider(
    "Banner Dark Luxury Gradient (%)", min_value=20, max_value=85, value=45, step=5
)
banner_alpha = round(banner_tint / 100, 2)

# Luxury Color Tokens
bg_css_rule = "background-color: #f4f6f4;"
text_color = "#2c3830"
card_bg = "#ffffff"
border_color = "#e2e8e4"
accent_color = "#829c8e"
gold_accent = "#c29b61"

if page_theme == "Warm Cashmere & Sand (Luxury Neutral)":
  bg_css_rule = "background-color: #f7f5f0;"
  text_color = "#3d3832"
  card_bg = "#ffffff"
  border_color = "#eae4db"
  accent_color = "#a38b6d"
  gold_accent = "#b8976b"
elif page_theme == "Midnight Pine & Emerald":
  bg_css_rule = "background-color: #edf2ef;"
  text_color = "#1e3026"
  card_bg = "#ffffff"
  border_color = "#d1dfd6"
  accent_color = "#3d6b52"
  gold_accent = "#d4af37"
elif page_theme == "Soft Rose & Champagne":
  bg_css_rule = "background-color: #f8f4f5;"
  text_color = "#4a383b"
  card_bg = "#ffffff"
  border_color = "#f0e1e4"
  accent_color = "#b5838d"
  gold_accent = "#d4af37"
elif page_theme == "Minimalist Pearl White":
  bg_css_rule = "background-color: #ffffff;"
  text_color = "#2a2a2a"
  card_bg = "#fafafa"
  border_color = "#eaeaea"
  accent_color = "#666666"
  gold_accent = "#999999"

# Header box background rule: keeps left side clear for Lion's Head, rich gradient on the right
if header_img_url:
  header_bg_rule = (
      "background-image: linear-gradient(90deg, rgba(30, 40, 35, 0.02) 0%,"
      f" rgba(44, 56, 48, {round(banner_alpha * 0.75, 2)}) 45%, rgba(30, 40,"
      f" 35, {min(round(banner_alpha + 0.25, 2), 0.9)}) 100%),"
      f" url('{header_img_url}'); background-size: cover; background-position:"
      f" left {banner_vertical_pos}%;"
  )
else:
  header_bg_rule = "background: linear-gradient(135deg, #749c86, #9cb8a9);"

# Custom CSS for Luxury Typography, Glassmorphism, and Artistic Calligraphy Title
custom_css = f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Playfair+Display:ital,wght@0,500;0,700;1,400&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');

    .stApp {{
        {bg_css_rule}
        color: {text_color};
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }}
    
    /* Elegant Serif Headings */
    h2, h3, .stApp h2, .stApp h3 {{
        font-family: 'Playfair Display', serif !important;
        letter-spacing: 0.3px;
        color: {text_color};
    }}

    p, span, label, div {{
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }}

    /* Glassmorphic Cards */
    [data-testid="stVerticalBlockBorderWrapper"] {{
        background-color: {card_bg};
        border: 1px solid {border_color} !important;
        border-radius: 20px;
        padding: 16px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.03);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }}
    [data-testid="stVerticalBlockBorderWrapper"]:hover {{
        transform: translateY(-2px);
        box-shadow: 0 14px 35px rgba(0,0,0,0.06);
    }}

    /* Curtain Slide-Down Animation for Active Day */
    @keyframes slideDown {{
        0% {{
            opacity: 0;
            transform: translateY(-12px);
        }}
        100% {{
            opacity: 1;
            transform: translateY(0);
        }}
    }}

    .curtain-container {{
        animation: slideDown 0.45s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }}

    /* Luxurious Horizontal DAY Toggle Buttons */
    div.stButton > button {{
        width: 100%;
        border-radius: 16px !important;
        padding: 18px 14px !important;
        border: 1.5px solid {border_color} !important;
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        background-color: {card_bg} !important;
    }}
    div.stButton > button p {{
        font-family: 'Playfair Display', serif !important;
        font-size: 1.35rem !important;
        font-weight: 700 !important;
        letter-spacing: 2px !important;
        margin: 0 !important;
        color: {text_color} !important;
    }}
    div.stButton > button:hover {{
        border-color: {accent_color} !important;
        box-shadow: 0 6px 20px rgba(0,0,0,0.05);
        transform: translateY(-2px);
    }}
    div.stButton > button[kind="primary"] {{
        background: linear-gradient(135deg, {accent_color}, {gold_accent}) !important;
        border-color: transparent !important;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
    }}
    div.stButton > button[kind="primary"] p {{
        color: #ffffff !important;
        text-shadow: 0 1px 3px rgba(0,0,0,0.2);
    }}

    /* Right-aligned Luxury Header Box */
    .header-box {{
        {header_bg_rule}
        padding: 45px 35px;
        border-radius: 24px;
        color: white !important;
        display: flex;
        flex-direction: column;
        align-items: flex-end;
        justify-content: center;
        text-align: right;
        min-height: {banner_height}px;
        margin-bottom: 30px;
        box-shadow: 0 12px 35px rgba(0,0,0,0.1);
    }}
    .header-content {{
        max-width: 80%;
    }}
    
    /* BIG ARTISTIC CALLIGRAPHY TITLE */
    .header-box h1 {{
        font-family: 'Great Vibes', cursive !important;
        color: {gold_accent} !important;
        font-size: 5rem !important;
        font-weight: 400 !important;
        text-shadow: 0 4px 20px rgba(0,0,0,0.7), 0 0 30px rgba(194, 155, 97, 0.4);
        margin-bottom: -5px;
        line-height: 1.0;
        letter-spacing: 2px;
    }}
    
    .header-box p, .header-box span {{
        color: rgba(255, 255, 255, 0.95) !important;
        text-shadow: 0 2px 6px rgba(0,0,0,0.4);
        font-size: 1.05rem;
    }}
    .badge-row {{
        display: flex;
        flex-wrap: wrap;
        justify-content: flex-end;
        gap: 8px;
        margin-top: 14px;
    }}
    .badge {{
        display: inline-block;
        background: rgba(255, 255, 255, 0.18);
        backdrop-filter: blur(8px);
        border: 1px solid rgba(255, 255, 255, 0.4);
        padding: 6px 14px;
        border-radius: 30px;
        font-size: 0.85rem;
        font-weight: 500;
        color: #ffffff;
    }}
    @media (max-width: 640px) {{
        .header-content {{
            max-width: 90%;
        }}
        .header-box h1 {{
            font-size: 3.5rem !important;
        }}
        div.stButton > button p {{
            font-size: 1.1rem !important;
        }}
    }}
    .time-tag {{
        color: {gold_accent} !important;
        font-weight: 700;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }}
    .transit-badge {{
        background-color: rgba(194, 155, 97, 0.1);
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

# Header Section with Large Artistic Calligraphy Title
st.markdown(
    """
    <div class="header-box">
        <div class="header-content">
            <h1>Baguio Itinerary</h1>
            <p>3 Days & 2 Nights</p>
            <div class="badge-row">
                <span class="badge">🚌 Arrival: 5:55 AM</span>
                <span class="badge">🏨 Benguet Prime Hotel</span>
                <span class="badge">📅 3 Days / 2 Nights</span>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- ITINERARY DATA ---
itinerary_days = [
    {
        "tab_label": "DAY 1",
        "header": "DAY 1 — Downtown Core, Art & Night Market",
        "stops": [
            {
                "time": "5:55 AM - 6:15 AM",
                "title": "1. Arrival - Baguio City Terminal",
                "desc": "Touch Down! Welcome to the Summer Capital.",
                "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQBz7rtObyyo6ISt9Wc8fjp_Y6tISdxKiqjP86i1hFOoftnfQy_u1ds2-zL&s=10",
                "transit": "🚶‍♂️ Walk ~5 mins (400m) to Benguet Prime Hotel",
            },
            {
                "time": "6:15 AM – 6:30 AM",
                "title": "2. Luggage Drop-Off at Benguet Prime Hotel",
                "desc": (
                    "Secure your belongings at the front desk on F. Calderon St."
                    " to explore hands-free."
                ),
                "img": "https://pix10.agoda.net/hotelImages/30155249/0/1ee5b88cd5ae9c397d4baf3e53da783f.jpeg?ce=2&s=414x232",
                "transit": "🚶‍♂️ Walk ~4 mins (300m) to Carantes St.",
            },
            {
                "time": "6:30 AM – 8:30 AM",
                "title": "3. Breakfast at Good Taste Restaurant",
                "desc": (
                    "Indulge in a hearty local breakfast served by their"
                    " signature robotic staff."
                ),
                "img": "https://i0.wp.com/shellwanders.com/wp-content/uploads/2023/11/Good-taste-cafe-and-restaurant-baguio-Food.png?resize=720%2C730&ssl=1",
                "transit": "🚶‍♂️ Walk ~3 mins (200m) across to Burnham Lagoon",
            },
            {
                "time": "8:30 AM – 9:30 AM",
                "title": "4. Burnham Park",
                "desc": (
                    "Breathe in the crisp morning pine air and enjoy a peaceful"
                    " stroll by the lagoon."
                ),
                "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSmOEbzDrhZOWyTvF9DPkwsNph6mg3A8zsMJSITie6WM_TQODGtHNOjALc&s=10",
                "transit": (
                    "🚶‍♂️ Walk ~8 mins (600m uphill via Session Rd/Assumption Rd)"
                ),
            },
            {
                "time": "10:00 AM – 1:00 PM",
                "title": "5. Ili-Likha Artists Village",
                "desc": (
                    "Discover an architectural masterpiece filled with artisan"
                    " cafes and sculptures."
                ),
                "img": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEifmuhRfMXPsmp3WQ_-2q4jqvcgwpRCYHzG3U6Mei9MYlfRsKpv31w8gRxfLEwf-iKO-M9mFZA0dspOC_tjbz123_65sPB0yZNViNNzDH_OLQd7D8aGRcnkXcyieNNdj-2ozuUOTdQulP7dkXHnNRv74eTRBzJV7YtOmkKqEeJ5-I9fE6Z3e67ZTkn-6g/s1600/Ili%20Likhaan-7.jpg",
                "transit": "🚶‍♂️ Walk ~6 mins (500m) back down to Calderon St.",
            },
            {
                "time": "1:30 PM – 2:00 PM",
                "title": "6. Hotel Check-In & Rest",
                "desc": (
                    "Return to Benguet Prime Hotel to claim your room and refresh"
                    " for the evening."
                ),
                "img": "https://cf.bstatic.com/xdata/images/hotel/max1024x768/172377839.jpg?k=1d4760bf2cdfd7abf95af2fa677c4fd253e7977b98eb19b3832bfccc6f37be96&o=",
                "transit": (
                    "🚶‍♂️ / 🚕 Walk ~12 mins uphill (900m) or 4-min taxi to SM"
                    " City"
                ),
            },
            {
                "time": "6:00 PM – 8:30 PM",
                "title": "7. SM City Baguio & Dinner",
                "desc": (
                    "Savor dinner overlooking panoramic city lights from the"
                    " open-air terraces."
                ),
                "img": "https://encrypted-tbn2.gstatic.com/licensed-image?q=tbn:ANd9GcTHAT_2Dib-tY8AXEX61isbo6_YqdLN-3pk3_1tMiwQMwH_8oeJ3cgaIR5D31iCxD2ZRA9-tz3N2vHkUA0",
                "transit": (
                    "🚶‍♂️ Walk ~8 mins downhill (700m) back to Harrison Road"
                ),
            },
            {
                "time": "9:00 PM – 10:00 PM",
                "title": "8. Baguio Night Market (Harrison Road)",
                "desc": (
                    "Experience the bustling ukay-ukay thrift stalls and local"
                    " street food culture."
                ),
                "img": "https://encrypted-tbn2.gstatic.com/licensed-image?q=tbn:ANd9GcSSUGdp2eXAtiPGjyYagOPVs7op5MoZMiUqvKkINowAZBdCg9k9qE42XMqgiHi0ETMwEF93ND-hx9geU8I",
                "transit": (
                    "🏨 Short walk back to Benguet Prime Hotel for a restful"
                    " night."
                ),
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
                "desc": (
                    "Enjoy artisan hot chocolate-eh and traditional Cordillera"
                    " breakfast specialties."
                ),
                "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSmOEbzDrhZOWyTvF9DPkwsNph6mg3A8zsMJSITie6WM_TQODGtHNOjALc&s=10",
                "transit": (
                    "🚕 Taxi (~12 mins) or Mines View Jeepney from Gov. Pack"
                    " Rd"
                ),
            },
            {
                "time": "9:00 AM – 10:30 AM",
                "title": "2. Baguio Botanical Garden",
                "desc": (
                    "Wander through towering pine avenues, orchid houses, and"
                    " cultural heritage huts."
                ),
                "img": "https://shoestringdiary.wordpress.com/wp-content/uploads/2023/05/miradorhill08-cover-ssdiaries.jpg?w=1140",
                "transit": (
                    "🚶‍♂️ Walk ~10 mins (750m) along Leonard Wood Rd to Wright"
                    " Park"
                ),
            },
            {
                "time": "10:30 AM – 12:00 PM",
                "title": "3. Wright Park & The Mansion",
                "desc": (
                    "Marvel at the iconic Pool of Pines and the historic"
                    " presidential summer residence."
                ),
                "img": "https://encrypted-tbn2.gstatic.com/licensed-image?q=tbn:ANd9GcTHAT_2Dib-tY8AXEX61isbo6_YqdLN-3pk3_1tMiwQMwH_8oeJ3cgaIR5D31iCxD2ZRA9-tz3N2vHkUA0",
                "transit": (
                    "🚕 Short taxi or jeepney ride (~6 mins) uphill to Mines"
                    " View"
                ),
            },
            {
                "time": "12:15 PM – 2:30 PM",
                "title": "4. Mines View Park & Good Shepherd Convent",
                "desc": (
                    "Take in sweeping mountain vistas and purchase world-famous"
                    " Good Shepherd Ube Jam."
                ),
                "img": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEifmuhRfMXPsmp3WQ_-2q4jqvcgwpRCYHzG3U6Mei9MYlfRsKpv31w8gRxfLEwf-iKO-M9mFZA0dspOC_tjbz123_65sPB0yZNViNNzDH_OLQd7D8aGRcnkXcyieNNdj-2ozuUOTdQulP7dkXHnNRv74eTRBzJV7YtOmkKqEeJ5-I9fE6Z3e67ZTkn-6g/s1600/Ili%20Likhaan-7.jpg",
                "transit": "🚕 Taxi (~10 mins) to Camp John Hay",
            },
            {
                "time": "3:00 PM – 6:30 PM",
                "title": "5. Camp John Hay (Bell House & Eco-Trail)",
                "desc": (
                    "Unwind amidst American-era heritage architecture and pine"
                    " forest walking trails."
                ),
                "img": "https://shoestringdiary.wordpress.com/wp-content/uploads/2023/05/miradorhill08-cover-ssdiaries.jpg?w=1140",
                "transit": (
                    "🚕 Taxi (~10 mins) back to Benguet Prime Hotel / Session"
                    " Road"
                ),
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
                "desc": (
                    "Pick fresh strawberries, enjoy strawberry taho, and admire"
                    " the vibrant hillside mural art."
                ),
                "img": "https://i0.wp.com/shellwanders.com/wp-content/uploads/2023/11/Good-taste-cafe-and-restaurant-baguio-Food.png?resize=720%2C730&ssl=1",
                "transit": "🚕 Taxi (~15 mins) to Tam-awan Village",
            },
            {
                "time": "10:15 AM – 12:00 PM",
                "title": "2. Tam-awan Village",
                "desc": (
                    "Immerse yourself in authentic Ifugao indigenous art and"
                    " mountainside galleries."
                ),
                "img": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEifmuhRfMXPsmp3WQ_-2q4jqvcgwpRCYHzG3U6Mei9MYlfRsKpv31w8gRxfLEwf-iKO-M9mFZA0dspOC_tjbz123_65sPB0yZNViNNzDH_OLQd7D8aGRcnkXcyieNNdj-2ozuUOTdQulP7dkXHnNRv74eTRBzJV7YtOmkKqEeJ5-I9fE6Z3e67ZTkn-6g/s1600/Ili%20Likhaan-7.jpg",
                "transit": (
                    "🚕 Taxi (~15 mins) back to downtown / Benguet Prime Hotel"
                ),
            },
            {
                "time": "12:00 PM – 1:30 PM",
                "title": "3. Hotel Check-Out & Baguio Public Market",
                "desc": (
                    "Check out, retrieve luggage, and acquire local Benguet"
                    " coffee beans and fresh produce."
                ),
                "img": "https://cf.bstatic.com/xdata/images/hotel/max1024x768/172377839.jpg?k=1d4760bf2cdfd7abf95af2fa677c4fd253e7977b98eb19b3832bfccc6f37be96&o=",
                "transit": "🚶‍♂️ Walk ~5 mins (400m) back to Benguet Prime Hotel",
            },
            {
                "time": "2:00 PM – 3:30 PM",
                "title": "4. Farewell Lunch on Session Road & Departure",
                "desc": (
                    "Relish a final meal on Session Road before heading to the"
                    " bus terminal for departure."
                ),
                "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQBz7rtObyyo6ISt9Wc8fjp_Y6tISdxKiqjP86i1hFOoftnfQy_u1ds2-zL&s=10",
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

st.markdown("### ⏰ Daily Itinerary Guide")
st.markdown(
    "<p style='color: #666; font-size: 0.95rem; margin-top: -10px;'>Select a"
    " day below to reveal its curated schedule with curtain-like smoothness:</p>",
    unsafe_allow_html=True,
)

# --- HORIZONTAL ELEGANT TOGGLE BAR ---
day_cols = st.columns(3, gap="small")
for idx, day in enumerate(itinerary_days):
  is_selected = st.session_state.selected_day_idx == idx
  arrow = "▴" if (is_selected and st.session_state.is_expanded) else "▾"
  btn_type = (
      "primary" if (is_selected and st.session_state.is_expanded) else "secondary"
  )

  with day_cols[idx]:
    if st.button(
        f"{day['tab_label']} {arrow}",
        key=f"day_nav_{idx}",
        type=btn_type,
        use_container_width=True,
    ):
      if is_selected:
        st.session_state.is_expanded = not st.session_state.is_expanded
      else:
        st.session_state.selected_day_idx = idx
        st.session_state.is_expanded = True
      st.rerun()

# --- CURTAIN REVEAL CONTAINER ---
if st.session_state.is_expanded:
  active_day = itinerary_days[st.session_state.selected_day_idx]
  st.markdown(
      f"<div class='curtain-container'><h4 style='margin-top: 25px;"
      f" margin-bottom: 15px;'>{active_day['header']}</h4>",
      unsafe_allow_html=True,
  )

  for stop in active_day["stops"]:
    with st.container(border=True):
      col1, col2 = st.columns([1, 2])
      with col1:
        st.image(stop["img"], use_container_width=True)
      with col2:
        st.markdown(
            f'<span class="time-tag">{stop["time"]}</span>',
            unsafe_allow_html=True,
        )
        st.markdown(f"### {stop['title']}")
        st.write(stop["desc"])
        st.markdown(
            f'<div class="transit-badge">{stop["transit"]}</div>',
            unsafe_allow_html=True,
        )
  st.markdown("</div>", unsafe_allow_html=True)
else:
  st.markdown(
      "<div style='text-align: center; padding: 25px; color: #777; font-style:"
      " italic;'>✨ Itinerary curtain is closed. Click any DAY above to"
      " reveal.</div>",
      unsafe_allow_html=True,
  )

st.divider()

# --- INTERACTIVE CHECKLIST ---
st.subheader("🎒 Curated Packing Checklist")
st.markdown("Check off essentials for your highland escape:")

checklist_items = [
    (
        "Warm wool jacket or cashmere sweater (Baguio evenings drop"
        " significantly)"
    ),
    "Comfortable walking shoes or boots (For heritage walks and pine trails)",
    "Insulated or reusable tumbler for hot chocolate and mountain tea",
    "Compact umbrella / lightweight weather shell",
    "Power bank and high-speed charging cables",
    (
        "Philippine Peso cash & small bills (Essential for local taxis & night"
        " markets)"
    ),
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
  st.success("🌟 All set! You are fully prepared for your luxury Baguio retreat.")

st.divider()

# --- MAP SECTION ---
st.subheader("🗺️ Neighborhood Reference Map")
st.markdown("Interactive cartography centered around Benguet Prime Hotel:")

map_html = """
<iframe 
    src="https://maps.google.com/maps?q=Benguet+Prime+Hotel,+F.+Calderon+St,+Baguio+City&t=m&z=15&output=embed" 
    width="100%" 
    height="420" 
    style="border:0; border-radius: 16px; box-shadow: 0 8px 24px rgba(0,0,0,0.06);" 
    allowfullscreen="" 
    loading="lazy">
</iframe>
"""
components.html(map_html, height=430)

st.divider()
st.markdown(
    "<p style='text-align: center; color: #888; font-size: 0.9rem;'>Wishing you"
    " an extraordinary journey to the Summer Capital of the Philippines! 🌲</p>",
    unsafe_allow_html=True,
)
