import streamlit as st
import streamlit.components.v1 as components

# Page setup
st.set_page_config(
    page_title="Baguio Itinerary | Benguet Prime Hotel", page_icon="🌲", layout="centered"
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
    value="https://shoestringdiary.wordpress.com/wp-content/uploads/2023/05/miradorhill08-cover-ssdiaries.jpg?w=1140",
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

# Header box background rule (Image + Pastel Sage Tint)
if header_img_url:
  header_bg_rule = (
      f"background-image: linear-gradient(135deg, rgba(82, 119, 103,"
      f" {banner_alpha}), rgba(118, 150, 134, {banner_alpha})), "
      f"url('{header_img_url}'); background-size: cover; background-position:"
      " center;"
  )
else:
  header_bg_rule = "background: linear-gradient(135deg, #749c86, #9cb8a9);"

# Custom CSS injecting pastel theme rules safely
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
    .header-box {
        REPLACE_HEADER_BG
        padding: 40px 20px;
        border-radius: 16px;
        color: white !important;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.08);
    }
    .header-box h1, .header-box p, .header-box span {
        color: white !important;
        text-shadow: 0 2px 6px rgba(0,0,0,0.3);
    }
    .badge {
        display: inline-block;
        background: rgba(255, 255, 255, 0.25);
        backdrop-filter: blur(4px);
        border: 1px solid rgba(255, 255, 255, 0.4);
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 0.9rem;
        margin: 5px;
        color: #ffffff;
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
)

st.markdown(custom_css, unsafe_allow_html=True)

# Header Section
st.markdown(
    """
    <div class="header-box">
        <h1>🌲 Baguio Adventure Itinerary</h1>
        <p>Pre-Check-In & Day 1 Visual Guide</p>
        <div>
            <span class="badge">🚌 Arrival: 5:55 AM</span>
            <span class="badge">🏨 Benguet Prime Hotel</span>
            <span class="badge">🔑 Check-in: 2:00 PM</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Itinerary Data with Walking Estimates
stops = [
    {
        "time": "5:55 AM - 6:15 AM",
        "title": "1. Arrival - Baguio City Terminal",
        "desc": f"Touch Down! Welcome to Baguio. Stay at [Benguet Prime Hotel](link{{place_id:ChIJFXd6_2ehkTMRDo3Of5y4MHI}}).",
        "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQBz7rtObyyo6ISt9Wc8fjp_Y6tISdxKiqjP86i1hFOoftnfQy_u1ds2-zL&s=10",
        "transit": "🚶‍♂️ Walk ~5 mins (400m) to Benguet Prime Hotel",
    },
    {
        "time": "6:15 AM – 6:30 AM",
        "title": "2. Luggage Drop-Off at Benguet Prime Hotel",
        "desc": "Head directly to Benguet Prime Hotel on F. Calderon St. Leave your bags at the front desk so you can explore hands-free.",
        "img": "https://pix10.agoda.net/hotelImages/30155249/0/1ee5b88cd5ae9c397d4baf3e53da783f.jpeg?ce=2&s=414x232",
        "transit": "🚶‍♂️ Walk ~4 mins (300m) to Carantes St.",
    },
    {
        "time": "6:30 AM – 8:30 AM",
        "title": "3. Breakfast at Good Taste Restaurant",
        "desc": f"Fuel up with a hearty breakfast at [The Original Good Taste Cafe & Restaurant](link{{place_id:ChIJTc4JcGehkTMRF0lG3u4bhDw}}).",
        "img": "https://i0.wp.com/shellwanders.com/wp-content/uploads/2023/11/Good-taste-cafe-and-restaurant-baguio-Food.png?resize=720%2C730&ssl=1",
        "transit": "🚶‍♂️ Walk ~3 mins (200m) across to Burnham Lagoon",
    },
    {
        "time": "8:30 AM – 9:30 AM",
        "title": "4. Burnham Park",
        "desc": f"Enjoy the crisp morning air around [Burnham Park](link{{place_id:ChIJiYLvmGmhkTMR8rwh5qkzitE}}) before the daytime crowds arrive.",
        "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSmOEbzDrhZOWyTvF9DPkwsNph6mg3A8zsMJSITie6WM_TQODGtHNOjALc&s=10",
        "transit": "🚶‍♂️ Walk ~8 mins (600m uphill via Session Rd/Assumption Rd)",
    },
    {
        "time": "10:00 AM – 1:00 PM",
        "title": "5. Ili-Likha Artists Village",
        "desc": f"Explore [Ili-Likha Artists Village](link{{place_id:ChIJ2w0UZ12hkTMRpJn52VDBf_U}}), a hidden food and art park filled with woodwork, sculptures, and cozy cafes.",
        "img": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEifmuhRfMXPsmp3WQ_-2q4jqvcgwpRCYHzG3U6Mei9MYlfRsKpv31w8gRxfLEwf-iKO-M9mFZA0dspOC_tjbz123_65sPB0yZNViNNzDH_OLQd7D8aGRcnkXcyieNNdj-2ozuUOTdQulP7dkXHnNRv74eTRBzJV7YtOmkKqEeJ5-I9fE6Z3e67ZTkn-6g/s1600/Ili%20Likhaan-7.jpg",
        "transit": "🚶‍♂️ Walk ~6 mins (500m) back down to Calderon St.",
    },
    {
        "time": "1:30 PM – 2:00 PM",
        "title": "6. Hotel Check-In & Rest",
        "desc": "Return to Benguet Prime Hotel to claim your luggage, check into your room, and rest up.",
        "img": "https://cf.bstatic.com/xdata/images/hotel/max1024x768/172377839.jpg?k=1d4760bf2cdfd7abf95af2fa677c4fd253e7977b98eb19b3832bfccc6f37be96&o=",
        "transit": "🚶‍♂️ / 🚕 Walk ~12 mins uphill (900m) or 4-min taxi to SM City",
    },
    {
        "time": "6:00 PM – 8:30 PM",
        "title": "7. SM City Baguio & Dinner",
        "desc": f"Enjoy cool evening breezes and panoramic views from [SM City Baguio](link{{place_id:ChIJd5wuUEKhkTMR2M1ll8O2f1U}}).",
        "img": "https://encrypted-tbn2.gstatic.com/licensed-image?q=tbn:ANd9GcTHAT_2Dib-tY8AXEX61isbo6_YqdLN-3pk3_1tMiwQMwH_8oeJ3cgaIR5D31iCxD2ZRA9-tz3N2vHkUA0",
        "transit": "🚶‍♂️ Walk ~8 mins downhill (700m) back to Harrison Road",
    },
    {
        "time": "9:00 PM – 10:00 PM",
        "title": "8. Baguio Night Market (Harrison Road)",
        "desc": f"Browse ukay-ukay stalls at [Baguio Night Market (Food Stalls)](link{{place_id:ChIJvbe53mehkTMR8T_ioyknfYk}}).",
        "img": "https://encrypted-tbn2.gstatic.com/licensed-image?q=tbn:ANd9GcSSUGdp2eXAtiPGjyYagOPVs7op5MoZMiUqvKkINowAZBdCg9k9qE42XMqgiHi0ETMwEF93ND-hx9geU8I",
        "transit": "🏨 Short walk back to Benguet Prime Hotel to rest for Day 2!",
    },
]

st.subheader("⏰ Day 1 Schedule & Walking Guide")

for stop in stops:
  with st.container(border=True):
    col1, col2 = st.columns([1, 2])
    with col1:
      st.image(stop["img"], use_container_width=True)
    with col2:
      st.markdown(
          f'<span class="time-tag">{stop["time"]}</span>', unsafe_allow_html=True
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

# --- MAP MOVED TO THE LAST SECTION ---
st.subheader("🗺️ Baguio Downtown Reference Map")
st.markdown("Interactive vector map showing your downtown route and destinations:")

map_html = """
<iframe 
    src="https://maps.google.com/maps?q=Benguet+Prime+Hotel,+F.+Calderon+St,+Baguio+City&t=m&z=16&output=embed" 
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
