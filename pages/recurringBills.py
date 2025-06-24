import streamlit as st
from chat import chat
from subpageLayout import subpageLayout
import asyncio

h1, h2, h3, h4 = subpageLayout("./assets/recurringBills.png", "Pay All Your Bills!")
with h2:
    st.session_state.clearcache = True
    container1, container2 = asyncio.run(chat("What do you need to pay?", "recurring_bills"))

with h4:
    container5 = st.container(border=False, height=30)
    container6 = st.container(border=False, height=500)
    with container6:
        st.html("<h3><span style='color: #C70039;'>Suggestions</span></h3>")
        options = [":violet[Recharge my phone]", ":violet[Pay water bill]", ":violet[Can I check my previous paid bills]", ":violet[Pay for electricity bill]"]
        selection = st.pills("", options, selection_mode="single")
