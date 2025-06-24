import streamlit as st
from chat import chat
from subpageLayout import subpageLayout
import asyncio

h1, h2, h3, h4 = subpageLayout("./assets/travelBooking.png", "Book your Tickets!")
with h2:
    st.session_state.clearcache = True
    st.session_state.messages = [{"role":"assistant", "content":"Where do you want to travel to?"}]
    container1, container2 = asyncio.run(chat("Where do you want to travel to?", "travel_booking"))

with h4:
    container5 = st.container(border=False, height=30)
    container6 = st.container(border=False, height=500)
    with container6:
        st.html("<h3><span style='color: #C70039;'>Suggestions</span></h3>")
        options = [":violet[I want to go to Bhopal]", ":violet[Can you book me a bus to Trichy?]", ":violet[Can I travel via Train]", ":violet[Show my past travels]"]
        selection = st.pills("", options, selection_mode="single")
