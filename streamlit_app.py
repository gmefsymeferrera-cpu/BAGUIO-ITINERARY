import streamlit as st

# Page setup
st.set_page_config(
    page_title="Baguio Itinerary | Benguet Prime Hotel",
    page_icon="🌲",
    layout="centered"
)

# --- SIDEBAR: BACKGROUND & THEME SWITCHER ---
st.sidebar.header("🎨 Customize Background")

bg_mode = st.sidebar.selectbox(
    "Background Style",
    [
        "Custom Image URL",
        "Morning Fog (Soft Gray)",
        "Crisp White",
        "Warm Cabin (Cream)",
        "Misty Pine (Dark Forest)",
        "Midnight Baguio (Dark Slate)",
        "Custom Solid Color"
    ]
)

# Default theme tokens
bg_css_rule = "background-color: #f4f7f5;"
text_color = "#1f2937"
card_bg = "#ffffff"
border_color = "#e5e7eb"

if bg_mode == "Crisp White":
    bg_css_rule = "background-color: #ffffff;"
elif bg_mode == "Warm Cabin (Cream)":
    bg_css_rule = "background-color: #fdf8f0;"
elif bg_mode == "Misty Pine (Dark Forest)":
    bg_css_rule = "background-color: #0b291e;"
    text_color = "#f3f4f6"
    card_bg = "#133a2c"
    border_color = "#256149"
elif bg_mode == "Midnight Baguio (Dark Slate)":
    bg_css_rule = "background-color: #0f172a;"
    text_color = "#f8fafc"
    card_bg = "#1e293b"
    border_color = "#334155"
elif bg_mode == "Custom Solid Color":
    custom_hex = st.sidebar.color_picker("Pick a background color", "#e8f3ee")
    bg_css_rule = f"background-color: {custom_hex};"
    r, g, b = int(custom_hex[1:3], 16), int(custom_hex[3:5], 16), int(custom_hex[5:7], 16)
    luminance = (0.299 * r + 0.587 * g + 0.114 * b)
    if luminance < 130:
        text_color = "#f8fafc"
        card_bg = "rgba(30, 41, 59, 0.9)"
        border_color = "#475569"
elif bg_mode == "Custom Image URL":
    img_url = st.sidebar.text_input(
        "Paste Image URL",
        value="https://shoestringdiary.wordpress.com/wp-content/uploads/2023/05/miradorhill08-cover-ssdiaries.jpg?w=1140"
    )
    fade_tint = st.sidebar.radio("Fade Style", ["Light Fog (Soft Wash)", "Dark Mist (Moody)"])
    fade_strength = st.sidebar.slider("Background Fade Amount (%)", min_value=50, max_value=95, value=82, step=3)
    alpha = round(fade_strength / 100, 2)

    if img_url:
        if fade_tint == "Light Fog (Soft Wash)":
            overlay = f"rgba(244, 247, 245, {alpha})"
            text_color = "#1f2937"
            card_bg = "rgba(255, 255, 255, 0.92)"
            border_color = "#d1d5db"
        else:
            overlay = f"rgba(15, 23, 42, {alpha})"
            text_color = "#f8fafc"
            card_bg = "rgba(15, 23, 42, 0.88)"
            border_color = "rgba(255, 255, 255, 0.2)"

        bg_css_rule = (
            f"background-image: linear-gradient({overlay}, {overlay}), url('{img_url}'); "
            "background-size: cover; background-position: center; background-attachment: fixed;"
        )

# Custom CSS injecting theme rules safely
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
        border-radius: 12px;
        padding: 8px;
        backdrop-filter: blur(4px);
    }
    .header-box {
        background: linear-gradient(135deg, #0f3d2e, #256149);
        padding: 30px 20px;
        border-radius: 15px;
        color: white !important;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.15);
    }
    .header-box h1, .header-box p, .header-box span {
        color: white !important;
    }
    .badge {
        display: inline-block;
        background: rgba(255,255,255,0.2);
        padding: 5px 14px;
        border-radius: 20px;
        font-size: 0.9rem;
        margin: 5px;
    }
    .time-tag {
        color: #d97706 !important;
        font-weight: bold;
        font-size: 0.9rem;
        text-transform: uppercase;
    }
    </style>
"""

custom_css = (
    custom_css.replace("REPLACE_BG", bg_css_rule)
    .replace("REPLACE_TEXT", text_color)
    .replace("REPLACE_CARD", card_bg)
    .replace("REPLACE_BORDER", border_color)
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
    unsafe_allow_html=True
)

# Itinerary Data
stops = [

     {
        "time": "5:55 AM - 6:15 AM",
        "title": "1. Arrival - Baguio City Terminal",
        "desc": "eyyyyyy",
        "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQBz7rtObyyo6ISt9Wc8fjp_Y6tISdxKiqjP86i1hFOoftnfQy_u1ds2-zL&s=10"
    },
    {
        "time": "6:15 AM – 6:30 AM",
        "title": "2. Luggage Drop-Off at Benguet Prime Hotel",
        "desc": "Head directly to Benguet Prime Hotel on F. Calderon St. Leave your bags at the front desk so you can explore hands-free.",
        "img": "https://images.unsplash.com/photo-1590490360182-c33d57733427?q=80&w=800&auto=format&fit=crop"
    },
    {
        "time": "6:30 AM – 8:30 AM",
        "title": "3. Breakfast at Good Taste Restaurant",
        "desc": "Fuel up with a hearty breakfast and experience getting your food served by their robot crew.",
        "img": "https://i0.wp.com/shellwanders.com/wp-content/uploads/2023/11/Good-taste-cafe-and-restaurant-baguio-Food.png?resize=720%2C730&ssl=1"
    },
    {
        "time": "8:30 AM – 9:30 AM",
        "title": "4. Morning Stroll at Burnham Park",
        "desc": "Enjoy the crisp morning air around Burnham Lagoon before the daytime crowds arrive.",
        "img": "https://encrypted-tbn1.gstatic.com/licensed-image?q=tbn:ANd9GcRlPzvf2Z6akTze8mMI6vWj0c21cNJKZ7xpk7PzN9jC_oyJhUNmuc76oe3i5cu6MoqfbigGFGGeiK1I0K0"
    },
    {
        "time": "10:00 AM – 1:00 PM",
        "title": "5. Ili-Likha Artists Village",
        "desc": "Explore this hidden food and art park filled with woodwork, sculptures, stained glass art, and cozy cafes.",
        "img": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEifmuhRfMXPsmp3WQ_-2q4jqvcgwpRCYHzG3U6Mei9MYlfRsKpv31w8gRxfLEwf-iKO-M9mFZA0dspOC_tjbz123_65sPB0yZNViNNzDH_OLQd7D8aGRcnkXcyieNNdj-2ozuUOTdQulP7dkXHnNRv74eTRBzJV7YtOmkKqEeJ5-I9fE6Z3e67ZTkn-6g/s1600/Ili%20Likhaan-7.jpg"
    },
    {
        "time": "1:30 PM – 2:00 PM",
        "title": "6. Hotel Check-In & Rest",
        "desc": "Return to Benguet Prime Hotel to claim your luggage, check into your room, and rest up.",
        "img": "https://images.unsplash.com/photo-1566073771259-6a8506099945?q=80&w=800&auto=format&fit=crop"
    },
    {
        "time": "6:00 PM – 8:30 PM",
        "title": "7. SM City Baguio & Dinner",
        "desc": "Enjoy the cool evening breeze and panoramic city views from the open-air terraces of SM Baguio.",
        "img": "https://encrypted-tbn2.gstatic.com/licensed-image?q=tbn:ANd9GcTHAT_2Dib-tY8AXEX61isbo6_YqdLN-3pk3_1tMiwQMwH_8oeJ3cgaIR5D31iCxD2ZRA9-tz3N2vHkUA0"
    },
    {
        "time": "9:00 PM – 10:00 PM",
        "title": "8. Baguio Night Market (Harrison Road)",
        "desc": "Browse through ukay-ukay thrift stalls and sample hot street food just a short walk from the hotel.",
        "img": "https://encrypted-tbn2.gstatic.com/licensed-image?q=tbn:ANd9GcSSUGdp2eXAtiPGjyYagOPVs7op5MoZMiUqvKkINowAZBdCg9k9qE42XMqgiHi0ETMwEF93ND-hx9geU8I"
    }
]

st.subheader("⏰ Day 1")

for stop in stops:
    with st.container(border=True):
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(stop["img"], use_container_width=True)
        with col2:
            st.markdown(f'<span class="time-tag">{stop["time"]}</span>', unsafe_allow_html=True)
            st.markdown(f"### {stop['title']}")
            st.write(stop["desc"])

st.divider()

st.subheader("🎒 Interactive Packing Checklist")
checklist_items = [
    "Light jacket or sweater (Crucial: Baguio mornings & evenings get chilly!)",
    "Comfortable walking shoes (For parks & uphill walks)",
    "Reusable water bottle",
    "Compact umbrella or light rain gear",
    "Power bank and charging cables",
    "Cash & small bills (For taxis, jeepneys, and Night Market stalls)"
]

for item in checklist_items:
    st.checkbox(item)

st.caption("Safe travels to the Summer Capital of the Philippines! 🌲")
