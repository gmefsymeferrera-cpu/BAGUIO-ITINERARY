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

# REVISED DEFAULT IMAGE: Tunay na Pine Trees / Baguio Vibe sa Camp John Hay
header_img_url = st.sidebar.text_input(
    "Title Banner Image URL",
    value="https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=1600&q=80",  # Pine forest vibe
)

banner_height = st.sidebar.slider(
    "Banner Elegance Height (px)", min_value=250, max_value=550, value=380, step=10
)

banner_vertical_pos = st.sidebar.slider(
    "Banner Focus Framing (%)", min_value=0, max_value=100, value=50, step=5
)

banner_tint = st.sidebar.slider(
    "Banner Dark Luxury Gradient (%)", min_value=20, max_value=90, value=60, step=5
)
banner_alpha = round(banner_tint / 100, 2)

# Luxury Color Tokens
bg_css_rule = "background-color: #f4f6f4;"
text_color = "#2c3830"
card_bg = "#ffffff"
border_color = "#e2e8e4"
accent_color = "#829c8e"
gold_accent = "#d4af37"

if page_theme == "Warm Cashmere & Sand (Luxury Neutral)":
  bg_css_rule = "background-color: #f7f5f0;"
  text_color = "#3d3832"
  card_bg = "#ffffff"
  border_color = "#eae4db"
  accent_color = "#a38b6d"
  gold_accent = "#c5a880"
elif page_theme == "Midnight Pine & Emerald":
  bg_css_rule = "background-color: #edf2ef;"
  text_color = "#1e3026"
  card_bg = "#ffffff"
  border_color = "#d1dfd6"
  accent_color = "#3d6b52"
  gold_accent = "#dfc159"
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

# Mas realistic at malalim na gradient para litaw na litaw ang mga letra
if header_img_url:
  header_bg_rule = (
      f"linear-gradient(135deg, rgba(20, 30, 25, {banner_alpha}) 0%, rgba(10, 15, 12, {banner_alpha + 0.15}) 100%), "
      f"url('{header_img_url}'); background-size: cover; background-position: center {banner_vertical_pos}%;"
  )
else:
  header_bg_rule = "background: linear-gradient(135deg, #2c3830, #1e3026);"

# Custom CSS with Enhanced Luxury Layout & Calligraphy Art
custom_css = f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Playfair+Display:ital,wght@0,500;0,700;1,400&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');

    .stApp {{
        {bg_css_rule}
        color: {text_color};
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }}
    
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
        padding: 18px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.04);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }}
    [data-testid="stVerticalBlockBorderWrapper"]:hover {{
        transform: translateY(-3px);
        box-shadow: 0 16px 40px rgba(0,0,0,0.08);
    }}

    @keyframes slideDown {{
        0% {{ opacity: 0; transform: translateY(-10px); }}
        100% {{ opacity: 1; transform: translateY(0); }}
    }}

    .curtain-container {{
        animation: slideDown 0.4s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }}

    /* Horizontal Toggle Buttons */
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
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }}
    div.stButton > button[kind="primary"] p {{
        color: #ffffff !important;
        text-shadow: 0 1px 3px rgba(0,0,0,0.3);
    }}

    /* CENTERED LUXURY MAGAZINE BANNER */
    .header-box {{
        {header_bg_rule}
        padding: 50px 30px;
        border-radius: 24px;
        color: white !important;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        min-height: {banner_height}px;
        margin-bottom: 30px;
        box-shadow: 0 15px 40px rgba(0,0,0,0.25);
        border: 1px solid rgba(255, 255, 255, 0.15);
    }}
    
    .header-content {{
        max-width: 85%;
        display: flex;
        flex-direction: column;
        align-items: center;
    }}
    
    /* ULTRA-REALISTIC CALLIGRAPHY ARTISTIC TITLE */
    .header-box h1 {{
        font-family: 'Great Vibes', cursive !important;
        color: {gold_accent} !important;
        font-size: 5.5rem !important;
        font-weight: 400 !important;
        text-shadow: 0 5px 25px rgba(0, 0, 0, 0.8), 0 0 40px rgba(212, 175, 55, 0.5);
        margin: 0px 0px 5px 0px;
        line-height: 1.0;
        letter-spacing: 3px;
    }}
    
    .subtitle-tag {{
        font-family: 'Playfair Display', serif !important;
        font-size: 1.4rem;
        letter-spacing: 4px;
        color: #f0f0f0;
        text-transform: uppercase;
        margin-bottom: 15px;
        text-shadow: 0 2px 8px rgba(0,0,0,0.6);
    }}

    .badge-row {{
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 10px;
        margin-top: 15px;
    }}
    
    .badge {{
        display: inline-block;
        background: rgba(20, 20, 20, 0.45);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.3);
        padding: 8px 16px;
        border-radius: 30px;
        font-size: 0.9rem;
        font-weight: 500;
        color: #ffffff;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }}

    @media (max-width: 640px) {{
        .header-box h1 {{
            font-size: 4rem !important;
        }}
        .subtitle-tag {{
            font-size: 1.1rem;
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
        background-color: rgba(212, 175, 55, 0.08);
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

# Header Section with Centered Calligraphy Art Banner
st.markdown(
    """
    <div class="header-box">
        <div class="header-content">
            <h1>Baguio Itinerary</h1>
            <div class="subtitle-tag">🌲 Luxury Highland Escape 🌲</div>
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
                "img": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=600&q=80",
                "transit": "🚶‍♂️ Walk ~5 mins (400m) to Benguet Prime Hotel",
            },
            {
                "time": "6:15 AM – 6:30 AM",
                "title": "2. Luggage Drop-Off at Benguet Prime Hotel",
                "desc": (
                    "Secure your belongings at the front desk on F. Calderon St."
                    " to explore hands-free."
                ),
                "img": "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=600&q=80",
                "transit": "🚶‍♂️ Walk ~4 mins (300m) to Carantes St.",
            },
            {
                "time": "6:30 AM – 8:30 AM",
                "title": "3. Breakfast at Good Taste Restaurant",
                "desc": (
                    "Indulge in a hearty local breakfast served by their"
                    " signature robotic staff."
                ),
                "img": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=600&q=80",
                "transit": "🚶‍♂️ Walk ~3 mins (200m) across to Burnham Lagoon",
            },
            {
                "time": "8:30 AM – 9:30 AM",
                "title": "4. Burnham Park",
                "desc": (
                    "Breathe in the crisp morning pine air and enjoy a peaceful"
                    " stroll by the lagoon."
                ),
                "img": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=600&q=80",
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
                "img": "https://images.unsplash.com/photo-1513519245088-0e12902e5a38?auto=format&fit=crop&w=600&q=80",
                "transit": "🚶‍♂️ Walk ~6 mins (500m) back down to Calderon St.",
            },
            {
                "time": "1:30 PM – 2:00 PM",
                "title": "6. Hotel Check-In & Rest",
                "desc": (
                    "Return to Benguet Prime Hotel to claim your room and refresh"
                    " for the evening."
                ),
                "img": "https://images.unsplash.com/photo-1582719508461-905c673771fd?auto=format&fit=crop&w=600&q=80",
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
                "img": "https://images.unsplash.com/photo-1519501025264-65ba15a82390?auto=format&fit=crop&w=600&q=80",
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
                "img": "https://images.unsplash.com/photo-1555939594-58d7cb561ad1?auto=format&fit=crop&w=600&q=80",
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
                "img": "https://images.unsplash.com/photo-1533777857889-4be7c70b33f7?auto=format&fit=crop&w=600&q=80",
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
                "img": "https://images.unsplash.com/photo-1448375240586-882707db888b?auto=format&fit=crop&w=600&q=80",
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
                "img": "https://images.unsplash.com/photo-1511497584788-876761192569?auto=format&fit=crop&w=600&q=80",
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
                "img": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=600&q=80",
                "transit": "🚕 Taxi (~10 mins) to Camp John Hay",
            },
            {
                "time": "3:00 PM – 6:30 PM",
                "title": "5. Camp John Hay (Bell House & Eco-Trail)",
                "desc": (
                    "Unwind amidst American-era heritage architecture and pine"
                    " forest walking trails."
                ),
                "img": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=600&q=80",
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
                "img": "https://images.unsplash.com/photo-1464965911861-746a04b4bca6?auto=format&fit=crop&w=600&q=80",
                "transit": "🚕 Taxi (~15 mins) to Tam-awan Village",
            },
            {
                "time": "10:15 AM – 12:00 PM",
                "title": "2. Tam-awan Village",
                "desc": (
                    "Immerse yourself in authentic Ifugao indigenous art and"
                    " mountainside galleries."
                ),
                "img": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=600&q=80",
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
                "img": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=600&q=80",
                "transit": "🚶‍♂️ Walk ~5 mins (400m) back to Benguet Prime Hotel",
            },
            {
                "time": "2:00 PM – 3:30 PM",
                "title": "4. Farewell Lunch on Session Road & Departure",
                "desc": (
                    "Relish a final meal on Session Road before heading to the"
                    " bus terminal for departure."
                ),
                "img": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=600&q=80",
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
