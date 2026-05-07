import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Multi_Company Analytics",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
    <style>
        .block-container {
            padding: 1rem 1rem 0rem 1rem !important;
            max-width: 100% !important;
        }
        section[data-testid="stMain"] {
            overflow-x: hidden;
        }
    </style>
""", unsafe_allow_html=True)

st.title("📊 Dashboard Multi_Company Analytics")
st.markdown("---")

EMBED_URL = "https://app.powerbi.com/reportEmbed?reportId=efaf934a-f411-4ac5-b0fc-7db259900b50&autoAuth=true&ctid=a62ee7c4-ed2d-4991-b4b8-3120e8333e11"

components.iframe(
    src=EMBED_URL,
    width=1400,
    height=820,
    scrolling=False
)

st.markdown("---")
st.caption("Données provenant de Power BI Service")
