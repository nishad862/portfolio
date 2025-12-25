import streamlit as st
from pathlib import Path
import base64
import mimetypes

st.set_page_config(
    page_title="Nishad N. Kotkar",
    layout="centered"
)

# Hide Streamlit UI
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Utility: convert file → base64 data URL
def to_data_url(path):
    mime, _ = mimetypes.guess_type(path)
    if mime is None:
        mime = "application/octet-stream"
    data = Path(path).read_bytes()
    encoded = base64.b64encode(data).decode()
    return f"data:{mime};base64,{encoded}"

# Load HTML & CSS
html = Path("index.html").read_text(encoding="utf-8")
css = Path("screen.css").read_text(encoding="utf-8")

# Inject CSS
html = html.replace("</head>", f"<style>{css}</style></head>")

# Replace image src
html = html.replace(
    'src="photo.png"',
    f'src="{to_data_url("photo.png")}"'
)

# Replace resume PDF link
# html = html.replace(
#     'href="ezyang-resume.pdf"',
#     f'href="{to_data_url("ezyang-resume.pdf")}"'
# )

# Render
st.components.v1.html(
    html,
    height=2300,
    scrolling=True
)
