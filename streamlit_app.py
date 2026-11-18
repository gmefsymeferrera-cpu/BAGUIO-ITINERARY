import streamlit as st

# Page setup
st.set_page_config(
    page_title="Baguio Itinerary | Benguet Prime Hotel",
    page_icon="🌲",
    layout="centered"
)

# Custom CSS para magmukhang modern web dashboard
st.markdown("""
    <style>
    .header-box {
        background: linear-gradient(135deg, #0f3d2e, #256149);
        padding: 30px 20px;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
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
        color: #d97706;
        font-weight: bold;
        font-size: 0.9rem;
        text-transform: uppercase;
    }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("""
    <div class="header-box">
        <h1>🌲 Baguio Adventure Itinerary</h1>
        <p>Pre-Check-In & Day 1 Visual Guide</p>
        <div>
            <span class="badge">🚌 Arrival: 5:55 AM</span>
            <span class="badge">🏨 Benguet Prime Hotel</span>
            <span class="badge">🔑 Check-in: 2:00 PM</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# Itinerary Data
stops = [
    {
        "time": "5:55 AM – 6:30 AM",
        "title": "1. Luggage Drop-Off at Benguet Prime Hotel",
        "desc": "Head directly to Benguet Prime Hotel on F. Calderon St. Leave your bags at the front desk so you can explore hands-free.",
        "img": "https://images.unsplash.com/photo-1590490360182-c33d57733427?q=80&w=800&auto=format&fit=crop"
    },
    {
        "time": "6:30 AM – 8:30 AM",
        "title": "2. Breakfast at Good Taste Restaurant",
        "desc": "Fuel up with a hearty breakfast and experience getting your food served by their robot crew.",
        "img": "https://i0.wp.com/shellwanders.com/wp-content/uploads/2023/11/Good-taste-cafe-and-restaurant-baguio-Food.png?resize=720%2C730&ssl=1"
    },
    {
        "time": "8:30 AM – 9:30 AM",
        "title": "3. Morning Stroll at Burnham Park",
        "desc": "Enjoy the crisp morning air around Burnham Lagoon before the daytime crowds arrive.",
        "img": "https://encrypted-tbn1.gstatic.com/licensed-image?q=tbn:ANd9GcRlPzvf2Z6akTze8mMI6vWj0c21cNJKZ7xpk7PzN9jC_oyJhUNmuc76oe3i5cu6MoqfbigGFGGeiK1I0K0"
    },
    {
        "time": "10:00 AM – 1:00 PM",
        "title": "4. Ili-Likha Artists Village",
        "desc": "Explore this hidden food and art park filled with woodwork, sculptures, stained glass art, and cozy cafes.",
        "img": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEifmuhRfMXPsmp3WQ_-2q4jqvcgwpRCYHzG3U6Mei9MYlfRsKpv31w8gRxfLEwf-iKO-M9mFZA0dspOC_tjbz123_65sPB0yZNViNNzDH_OLQd7D8aGRcnkXcyieNNdj-2ozuUOTdQulP7dkXHnNRv74eTRBzJV7YtOmkKqEeJ5-I9fE6Z3e67ZTkn-6g/s1600/Ili%20Likhaan-7.jpg"
    },
    {
        "time": "1:30 PM – 2:00 PM",
        "title": "5. Hotel Check-In & Rest",
        "desc": "Return to Benguet Prime Hotel to claim your luggage, check into your room, and rest up.",
        "img": "https://images.unsplash.com/photo-1566073771259-6a8506099945?q=80&w=800&auto=format&fit=crop"
    },
    {
        "time": "6:00 PM – 8:30 PM",
        "title": "6. SM City Baguio & Dinner",
        "desc": "Enjoy the cool evening breeze and panoramic city views from the open-air terraces of SM Baguio.",
        "img": "https://encrypted-tbn2.gstatic.com/licensed-image?q=tbn:ANd9GcTHAT_2Dib-tY8AXEX61isbo6_YqdLN-3pk3_1tMiwQMwH_8oeJ3cgaIR5D31iCxD2ZRA9-tz3N2vHkUA0"
    },
    {
        "time": "9:00 PM – 10:00 PM",
        "title": "7. Baguio Night Market (Harrison Road)",
        "desc": "Browse through ukay-ukay thrift stalls and sample hot street food just a short walk from the hotel.",
        "img": "https://encrypted-tbn2.gstatic.com/licensed-image?q=tbn:ANd9GcSSUGdp2eXAtiPGjyYagOPVs7op5MoZMiUqvKkINowAZBdCg9k9qE42XMqgiHi0ETMwEF93ND-hx9geU8I"
    }
]

st.subheader("⏰ Day 1 Schedule")

# Display each stop with image and text side-by-side
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

# Interactive Packing Checklist
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
