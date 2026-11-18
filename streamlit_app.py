import streamlit as st
import streamlit.components.v1 as components

# Page setup
st.set_page_config(
    page_title="Baguio Itinerary | Benguet Prime Hotel",
    page_icon="🌲",
    layout="centered",
)

# --- SIDEBAR: THEME & HEADER CUSTOMIZER ---
st.sidebar.header("🎨 Customize Theme")

page_theme = st.sidebar.selectbox(
    "Page Background",
    [
        "Pastel Sage (Soft Green)",
        "Pastel Cream (Warm Neutral)",
        "Pastel Sky (Soft Blue)",
        "Morning Fog (Soft Gray)",
        "Crisp White",
    ],
)

header_img_url = st.sidebar.text_input(
    "Title Banner Image URL",
    value="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQKMMW-LwHbNVZcyMwdl1P-nOVPuzhfWEVTyF8HwyjIkNugqqTJ7MsTfE&s=10",
)

banner_height = st.sidebar.slider(
    "Title Banner Height (px)", min_value=180, max_value=450, value=260, step=10
)

banner_vertical_pos = st.sidebar.slider(
    "Vertical Framing (%) — Move Lion's Head Up/Down",
    min_value=0,
    max_value=100,
    value=35,
    step=5,
)

banner_tint = st.sidebar.slider(
    "Title Banner Dark Overlay (%)", min_value=20, max_value=80, value=45, step=5
)
banner_alpha = round(banner_tint / 100, 2)

# Pastel theme tokens
bg_css_rule = "background-color: #f0f4f1;"
text_color = "#2c3e35"
card_bg = "#ffffff"
border_color = "#d6e2d9"

if page_theme == "Pastel Cream (Warm Neutral)":
  bg_css_rule = "background-color: #fbf9f5;"
  text_color = "#3d3832"
  card_bg = "#ffffff"
  border_color = "#eae4db"
elif page_theme == "Pastel Sky (Soft Blue)":
  bg_css_rule = "background-color: #f0f4f8;"
  text_color = "#2b3a4a"
  card_bg = "#ffffff"
  border_color = "#d3e0ed"
elif page_theme == "Morning Fog (Soft Gray)":
  bg_css_rule = "background-color: #f5f6f8;"
  text_color = "#333d47"
  card_bg = "#ffffff"
  border_color = "#e2e6eb"
elif page_theme == "Crisp White":
  bg_css_rule = "background-color: #ffffff;"
  text_color = "#2d3748"
  card_bg = "#fcfdfd"
  border_color = "#edf2f7"

# Header box background rule: keeps left side clear for Lion's Head, tints right side for text readability
if header_img_url:
  header_bg_rule = (
      "background-image: linear-gradient(90deg, rgba(44, 62, 53, 0.05) 0%,"
      f" rgba(64, 96, 82, {round(banner_alpha * 0.75, 2)}) 45%, rgba(44, 62,"
      f" 53, {min(round(banner_alpha + 0.25, 2), 0.9)}) 100%),"
      f" url('{header_img_url}'); background-size: cover; background-position:"
      f" left {banner_vertical_pos}%;"
  )
else:
  header_bg_rule = "background: linear-gradient(135deg, #749c86, #9cb8a9);"

# Custom CSS injecting pastel theme rules + right-aligned hero header
custom_css = """
    <style>
    .stApp {
        REPLACE_BG
        color: REPLACE_TEXT;
    }
    .stApp h1, .stApp h2, .stApp h3, .stApp p, .stApp label, .stApp span {
        color: REPLACE_TEXT;
    }
    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: REPLACE_CARD;
        border-color: REPLACE_BORDER !important;
        border-radius: 14px;
        padding: 10px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.03);
    }
    /* Style the Day 1, Day 2, Day 3 dropdown headers */
    [data-testid="stExpander"] {
        background-color: REPLACE_CARD;
        border: 1.5px solid REPLACE_BORDER !important;
        border-radius: 14px !important;
        margin-bottom: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.04);
    }
    [data-testid="stExpander"] summary p {
        font-size: 1.15rem !important;
        font-weight: 700 !important;
    }
    /* Right-aligned Header Box to expose Lion's Head on the left */
    .header-box {
        REPLACE_HEADER_BG
        padding: 36px 28px;
        border-radius: 16px;
        color: white !important;
        display: flex;
        flex-direction: column;
        align-items: flex-end;
        justify-content: center;
        text-align: right;
        min-height: REPLACE_HEIGHTpx;
        margin-bottom: 25px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.08);
    }
    .header-content {
        max-width: 65%;
    }
    .header-box h1 {
        color: white !important;
        text-shadow: 0 2px 8px rgba(0,0,0,0.45);
        margin-bottom: 6px;
        line-height: 1.2;
    }
    .header-box p, .header-box span {
        color: white !important;
        text-shadow: 0 2px 6px rgba(0,0,0,0.45);
    }
    .badge-row {
        display: flex;
        flex-wrap: wrap;
        justify-content: flex-end;
        gap: 6px;
        margin-top: 10px;
    }
    .badge {
        display: inline-block;
        background: rgba(255, 255, 255, 0.22);
        backdrop-filter: blur(4px);
        border: 1px solid rgba(255, 255, 255, 0.45);
        padding: 5px 12px;
        border-radius: 20px;
        font-size: 0.85rem;
        color: #ffffff;
    }
    @media (max-width: 640px) {
        .header-content {
            max-width: 85%;
        }
    }
    .time-tag {
        color: #b87a3d !important;
        font-weight: 700;
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .transit-badge {
        background-color: rgba(184, 122, 61, 0.12);
        color: #b87a3d;
        padding: 6px 12px;
        border-radius: 8px;
        font-size: 0.85rem;
        font-weight: 600;
        display: inline-block;
        margin: 10px 0px;
        border-left: 3px solid #b87a3d;
    }
    </style>
"""

custom_css = (
    custom_css.replace("REPLACE_BG", bg_css_rule)
    .replace("REPLACE_TEXT", text_color)
    .replace("REPLACE_CARD", card_bg)
    .replace("REPLACE_BORDER", border_color)
    .replace("REPLACE_HEADER_BG", header_bg_rule)
    .replace("REPLACE_HEIGHT", str(banner_height))
)

st.markdown(custom_css, unsafe_allow_html=True)

# Header Section (Right-aligned to showcase Lion's Head on the left)
st.markdown(
    """
    <div class="header-box">
        <div class="header-content">
            <h1>🌲 Baguio 3-Day Adventure Itinerary</h1>
            <p>Complete Visual & Transit Guide from Benguet Prime Hotel</p>
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

# --- MULTI-DAY ITINERARY DATA ---
itinerary_days = [
    {
        "header": "DAY 1 — Downtown Core, Art & Night Market",
        "expanded": True,
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
                "desc": (
                    "Head directly to Benguet Prime Hotel on F. Calderon St."
                    " Leave our bags at the front desk so we can explore"
                    " hands-free."
                ),
                "img": "https://pix10.agoda.net/hotelImages/30155249/0/1ee5b88cd5ae9c397d4baf3e53da783f.jpeg?ce=2&s=414x232",
                "transit": "🚶‍♂️ Walk ~4 mins (300m) to Carantes St.",
            },
            {
                "time": "6:30 AM – 8:30 AM",
                "title": "3. Breakfast at Good Taste Restaurant",
                "desc": (
                    "Fuel up with a hearty local breakfast. Experience getting"
                    " our food served with their famous robot crew."
                ),
                "img": "https://i0.wp.com/shellwanders.com/wp-content/uploads/2023/11/Good-taste-cafe-and-restaurant-baguio-Food.png?resize=720%2C730&ssl=1",
                "transit": "🚶‍♂️ Walk ~3 mins (200m) across to Burnham Lagoon",
            },
            {
                "time": "8:30 AM – 9:30 AM",
                "title": "4. Burnham Park",
                "desc": (
                    "Experience the famous Burnham Lagoon. Rent a small"
                    " rowboat or enjoy the quiet, crisp morning air walking"
                    " around the pathways."
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
                    "Explore a hidden food and art park filled with woodwork,"
                    " sculptures, and cozy cafes."
                ),
                "img": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEifmuhRfMXPsmp3WQ_-2q4jqvcgwpRCYHzG3U6Mei9MYlfRsKpv31w8gRxfLEwf-iKO-M9mFZA0dspOC_tjbz123_65sPB0yZNViNNzDH_OLQd7D8aGRcnkXcyieNNdj-2ozuUOTdQulP7dkXHnNRv74eTRBzJV7YtOmkKqEeJ5-I9fE6Z3e67ZTkn-6g/s1600/Ili%20Likhaan-7.jpg",
                "transit": "🚶‍♂️ Walk ~6 mins (500m) back down to Calderon St.",
            },
            {
                "time": "1:30 PM – 2:00 PM",
                "title": "6. Hotel Check-In & Rest",
                "desc": (
                    "Return to Benguet Prime Hotel to claim your luggage, check"
                    " into your room, and rest up."
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
                    "Enjoy the cool evening breeze and panoramic views of the"
                    " city proper from the open-air terraces of SM Baguio."
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
                    "Browse through the vibrant ukay-ukay thrift stalls and"
                    " sample delicious street food right near Burnham Park."
                ),
                "img": "https://encrypted-tbn2.gstatic.com/licensed-image?q=tbn:ANd9GcSSUGdp2eXAtiPGjyYagOPVs7op5MoZMiUqvKkINowAZBdCg9k9qE42XMqgiHi0ETMwEF93ND-hx9geU8I",
                "transit": (
                    "🏨 Short walk back to Benguet Prime Hotel to rest for Day"
                    " 2!"
                ),
            },
        ],
    },
    {
        "header": "DAY 2 — Pine Forests, Parks & Mountain Views",
        "expanded": False,
        "stops": [
            {
                "time": "7:30 AM – 8:30 AM",
                "title": "1. Breakfast at Café by the Ruins",
                "desc": (
                    "Start Day 2 with Baguio chocolate-eh, fresh pan de sal,"
                    " and mountain-inspired Filipino breakfast dishes."
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
                    "Stroll through towering pine trees, vibrant flower"
                    " terraces, Japanese-inspired tunnels, and Cordillera"
                    " huts."
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
                    "Take photos across the iconic Pool of Pines facing The"
                    " Mansion, or try horseback riding along the pine-lined"
                    " trails."
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
                    "Take in panoramic views of the Benguet mining town and"
                    " stock up on famous Good Shepherd Ube Jam and strawberry"
                    " preserves."
                ),
                "img": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEifmuhRfMXPsmp3WQ_-2q4jqvcgwpRCYHzG3U6Mei9MYlfRsKpv31w8gRxfLEwf-iKO-M9mFZA0dspOC_tjbz123_65sPB0yZNViNNzDH_OLQd7D8aGRcnkXcyieNNdj-2ozuUOTdQulP7dkXHnNRv74eTRBzJV7YtOmkKqEeJ5-I9fE6Z3e67ZTkn-6g/s1600/Ili%20Likhaan-7.jpg",
                "transit": "🚕 Taxi (~10 mins) to Camp John Hay",
            },
            {
                "time": "3:00 PM – 6:30 PM",
                "title": "5. Camp John Hay (Bell House & Eco-Trail)",
                "desc": (
                    "Walk through the historic Bell House amphitheater, Lost"
                    " Cemetery, and Yellow Trail before grabbing hot chocolate"
                    " at Choco-late de Batirol."
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
        "header": "DAY 3 — Strawberry Farms, Culture & Pasalubong",
        "expanded": False,
        "stops": [
            {
                "time": "7:30 AM – 10:00 AM",
                "title": "1. La Trinidad Strawberry Farm & StoBoSa",
                "desc": (
                    "Head north to La Trinidad for fresh strawberry taho, farm"
                    " walks, and photos at the colorful hillside murals of"
                    " StoBoSa."
                ),
                "img": "https://i0.wp.com/shellwanders.com/wp-content/uploads/2023/11/Good-taste-cafe-and-restaurant-baguio-Food.png?resize=720%2C730&ssl=1",
                "transit": "🚕 Taxi (~15 mins) to Tam-awan Village",
            },
            {
                "time": "10:15 AM – 12:00 PM",
                "title": "2. Tam-awan Village",
                "desc": (
                    "Explore reconstructed traditional Ifugao and Kalinga huts"
                    " nestled on a forested hillside with local art galleries."
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
                    "Check out of Benguet Prime Hotel (leave bags at front"
                    " desk) and walk 5 minutes to Baguio Public Market for"
                    " fresh veggies, coffee beans, and brooms."
                ),
                "img": "https://cf.bstatic.com/xdata/images/hotel/max1024x768/172377839.jpg?k=1d4760bf2cdfd7abf95af2fa677c4fd253e7977b98eb19b3832bfccc6f37be96&o=",
                "transit": "🚶‍♂️ Walk ~5 mins (400m) back to Benguet Prime Hotel",
            },
            {
                "time": "2:00 PM – 3:30 PM",
                "title": "4. Final Lunch on Session Road & Departure",
                "desc": (
                    "Enjoy a farewell meal along Session Road, claim your"
                    " luggage at the hotel, and walk 5 minutes to the bus"
                    " terminal."
                ),
                "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQBz7rtObyyo6ISt9Wc8fjp_Y6tISdxKiqjP86i1hFOoftnfQy_u1ds2-zL&s=10",
                "transit": "🚌 Safe trip back home!",
            },
        ],
    },
]

st.subheader("⏰ 3-Day Schedule & Walking Guide")
st.caption("Click any day bar below to expand or collapse its destinations:")

# --- VISIBLE STACKED DROPDOWN ACCORDIONS (DAY 1, DAY 2, DAY 3) ---
for day in itinerary_days:
  with st.expander(day["header"], expanded=day["expanded"]):
    for stop in day["stops"]:
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

st.divider()

# --- INTERACTIVE CHECKLIST ---
st.subheader("🎒 Interactive Packing Checklist")
st.markdown("Check items off as you pack your bags:")

checklist_items = [
    (
        "Light jacket or sweater (Crucial: Baguio mornings & evenings get"
        " chilly!)"
    ),
    "Comfortable walking shoes (For parks & uphill walks)",
    "Reusable water bottle",
    "Compact umbrella or light rain gear",
    "Power bank and charging cables",
    "Cash & small bills (For taxis, jeepneys, and Night Market stalls)",
]

checked_states = []
for i, item in enumerate(checklist_items):
  is_checked = st.checkbox(item, key=f"check_{i}")
  checked_states.append(is_checked)

total_items = len(checklist_items)
completed_items = sum(checked_states)
progress_pct = completed_items / total_items

st.progress(progress_pct)
st.caption(f"✨ Packed: **{completed_items} / {total_items}** items ready")

if completed_items == total_items:
  st.success("🎉 All set! You're fully packed and ready for Baguio!")

st.divider()

# --- MAP AT THE BOTTOM ---
st.subheader("🗺️ Baguio Reference Map")
st.markdown(
    "Interactive vector map centered on your hotel and downtown starting point:"
)

map_html = """
<iframe 
    src="https://maps.google.com/maps?q=Benguet+Prime+Hotel,+F.+Calderon+St,+Baguio+City&t=m&z=15&output=embed" 
    width="100%" 
    height="420" 
    style="border:0; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.06);" 
    allowfullscreen="" 
    loading="lazy">
</iframe>
"""
components.html(map_html, height=430)

st.caption("🗺️ *Interactive map positioned at the bottom for quick neighborhood reference.*")

st.divider()
st.caption("Safe travels to the Summer Capital of the Philippines! 🌲")
