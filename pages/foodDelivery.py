import streamlit as st
from chat import chat
from subpageLayout import subpageLayout
import asyncio

h1, h2, h3, h4 = subpageLayout("./assets/foodDelivery.jpg", "Order Your Favourite Food!")
with h2:
    st.session_state.clearcache = True
    container1, container2 = asyncio.run(chat("What do you want to eat?", "food_delivery"))

with h4:
    container5 = st.container(border=False, height=30)
    container6 = st.container(border=False, height=500)
    with container6:
        st.html("<h3><span style='color: #C70039;'>Suggestions</span></h3>")
        options = [":violet[I want to eat some pasta]", ":violet[Can you show me some indian food?]", ":violet[Show previous orders]", ":violet[Order meals]"]
        selection = st.pills("", options, selection_mode="single")
