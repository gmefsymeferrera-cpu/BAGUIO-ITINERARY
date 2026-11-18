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
        "Morning Fog (Soft Gray)",
        "Crisp White",
        "Warm Cabin (Cream)",
        "Misty Pine (Dark Forest)",
        "Midnight Baguio (Dark Slate)",
        "Custom Solid Color",
        "Custom Image URL"
    ]
)

# Default theme tokens
bg_css = "background-color: #f4f7f5;"
text_color = "#1f2937"
card_bg = "#ffffff"
border_color = "#e5e7eb"

if bg_mode == "Crisp White":
    bg_css = "background-color: #ffffff;"
elif bg_mode == "Warm Cabin (Cream)":
    bg_css = "background-color: #fdf8f0;"
elif bg_mode == "Misty Pine (Dark Forest)":
    bg_css = "background-color: #0b291e;"
    text_color = "#f3f4f6"
    card_bg = "#133a2c"
    border_color = "#256149"
elif bg_mode == "Midnight Baguio (Dark Slate)":
    bg_css = "background-color: #0f172a;"
    text_color = "#f8fafc"
    card_bg = "#1e293b"
    border_color = "#334155"
elif bg_mode == "Custom Solid Color":
    custom_hex = st.sidebar.color_picker("Pick a background color", "#e8f3ee")
    bg_css = f"background-color: {custom_hex};"
    r, g, b = int(custom_hex[1:3], 16), int(custom_hex[3:5], 16), int(custom_hex[5:7], 16)
    luminance = (0.299 * r + 0.587 * g + 0.114 * b)
    if luminance < 130:
        text_color = "#f8fafc"
        card_bg = "rgba(30, 41, 59, 0.9)"
        border_color = "#475569"
elif bg_mode == "Custom Image URL":
    img_url = st.sidebar.text_input(
        "Paste Image URL",
        value="https://images.unsplash.com/photo-1542273917363-3b1817f69a2d?q=80&w=1600&auto=format&fit=crop"
    )
    if img_url:
        bg_css = f"background-image: linear-gradient(rgba(15, 23, 42, 0.55), rgba(15, 23, 42, 0.55)), url('{img_url}'); background-size: cover; background-position: center; background-attachment: fixed;"
        text_color = "#f8fafc"
        card_bg = "rgba(15, 23, 42, 0.85)"
        border_color = "rgba(255, 255, 255, 0.2)"

# Custom CSS injecting theme rules
st.markdown(
    f"""
    <style>
    .stApp {{
        {bg_css}
        color: {text_color};
