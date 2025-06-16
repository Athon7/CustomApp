import streamlit as st
from chat import chat
from subpageLayout import subpageLayout
import asyncio

h1, h2, h3, h4 = subpageLayout("./assets/groceryDelivery.png", "Order your grocery!")
with h2:
    st.session_state.clearcache = True
    container1, container2 = asyncio.run(chat("What do you need to order?", "grocery_delivery"))

with h4:
    container5 = st.container(border=False, height=30)
    container6 = st.container(border=False, height=500)
    with container6:
        st.html("<h3><span style='color: #C70039;'>Suggestions</span></h3>")
        options = [":violet[Order some rice and wheat]", ":violet[I would like to buy milk]", ":violet[Show previous orders]", ":violet[Order some vegetables]"]
        selection = st.pills("", options, selection_mode="single")