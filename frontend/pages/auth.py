import streamlit as st

st.set_page_config(
    page_title="My Streamlit App",
    layout="wide",
    initial_sidebar_state="collapsed"
)

query_params = st.query_params

st.header("Code: ")
st.header(query_params['code'])