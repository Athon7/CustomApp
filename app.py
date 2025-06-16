import streamlit as st
import os

## Page Layout
st.set_page_config(layout="wide")
st.markdown("""
        <style>
               .block-container {
                    padding-top: 18px;
                    padding-bottom: 1rem;
                    padding-left: 50px;
                    padding-right: 50px;
                }
        </style>
        """, unsafe_allow_html=True)

## Session State
if "clearcache" not in st.session_state:
        st.session_state.clearcache = False
        st.session_state.userflag = False
try:
    if os.environ["OPENAI_API_KEY"]:
        st.session_state.apikey = True
except:
    st.session_state.apikey = False

## Navigation
pg = st.navigation([
        st.Page("frontpage.py"),
        st.Page("mainpage.py"),
        st.Page("./pages/foodDelivery.py"),
        st.Page("./pages/groceryDelivery.py"),
        st.Page("./pages/travelBooking.py"),
        st.Page("./pages/recurringBills.py"),
        st.Page("./pages/checkout.py")], position = "hidden")
pg.run()