import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Multi_Company Analytics",
    page_icon="📊",
    layout="wide"
)

# Cache la barre Streamlit et les marges
st.markdown("""
    <style>
        .block-container {
            padding: 0 !important;
            margin: 0 !important;
        }
        header {display: none !important;}
        footer {display: none !important;}
    </style>
""", unsafe_allow_html=True)

EMBED_URL = "https://app.powerbi.com/reportEmbed?reportId=efaf934a-f411-4ac5-b0fc-7db259900b50&autoAuth=true&ctid=a62ee7c4-ed2d-4991-b4b8-3120e8333e11"

components.iframe(
    src=EMBED_URL,
    width=1600,
    height=900,
    scrolling=True
)
