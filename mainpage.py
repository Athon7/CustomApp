import streamlit as st
import asyncio

h1, h2, h3 = st.columns([0.1,0.8,0.2], gap="small", vertical_alignment="center")

with h2:
    container2_1 = st.container(border=False, height=180)
    container2_2 = st.container(border=False, height=250)
 
    with container2_1:
        st.html("<h3><span style='color: #C70039;margin=1px;'>Here is what the app can do for you!</span></h3>")
        st.html("<h2>Check these out..</h2>")
    with container2_2:
        option = [":red[Help you with ordering food you like the most from your favourite restaurant.]",
        ":red[Help you with ordering grocery items of your choice from multiple providers across different apps]",
        ":red[Get you details you require to travel to your destination in a click]",
        ":red[Pay for all recurring bills in one go without a hassle!]"]
        selection = st.pills("", option, selection_mode="single", key=1)
        if selection==":red[Help you with ordering food you like the most from your favourite restaurant.]":
            st.switch_page(st.Page("./pages/foodDelivery.py"))
        if selection==":red[Help you with ordering grocery items of your choice from multiple providers across different apps]":
            st.switch_page(st.Page("./pages/groceryDelivery.py"))
        if selection==":red[Get you details you require to travel to your destination in a click]":
            st.switch_page(st.Page("./pages/travelBooking.py"))
        if selection==":red[Pay for all recurring bills in one go without a hassle!]":
            st.switch_page(st.Page("./pages/recurringBills.py"))


with st.sidebar:
    container1 = st.container(border=False, height=320)
    container2 = st.container(border=False, height=200)
    with container1:
        st.html("<h3><span style='color: #C70039;'>What's on your Mind?</span></h3>")
        selection_url = {
            ":blue-background[:violet[Food Orders]]": "./pages/foodDelivery.py",
            ":blue-background[:violet[Grocery Shop]]": "./pages/groceryDelivery.py",
            ":blue-background[:violet[Book A Bus]]" : "./pages/travelBooking.py",
            ":blue-background[:violet[Recurring Bills]]": "./pages/recurringBills.py"
        }
        selection = st.radio(
            "",
            [":blue-background[:violet[Recurring Bills]]", 
            ":blue-background[:violet[Book A Bus]]", 
            ":blue-background[:violet[Food Orders]]", 
            ":blue-background[:violet[Grocery Shop]]"],
            index=None,
            captions=[
                "\n\n",
                "\n\n",
                "\n\n",
                " ",
                " "
            ],
        )
        if selection:
            st.switch_page(st.Page(selection_url[selection]))
    with container2:
        st.image("./assets/all2_1.jpg")

with h3:
    container5 = st.container(border=False, height=350)
    container6 = st.container(border=False, height=200)
    with container5:
        st.html("<h3><span style='color: #C70039;'>Suggestions</span></h3>")
        options = [":violet[Book me a flight to Goa]", ":violet[Order White Sauce Pasta]", ":violet[Show me my balance]", ":violet[Order some vegetables]"]
        selection = st.pills("", options, selection_mode="single")
        if selection==":violet[Book me a flight to Goa]":
            st.switch_page(st.Page("./pages/travelBooking.py"))
        elif selection==":violet[Order White Sauce Pasta]":
            st.switch_page(st.Page("./pages/foodDelivery.py"))
        elif selection==":violet[Pay my mobile bills]":
            st.switch_page(st.Page("./pages/recurringBills.py"))
        elif selection==":violet[Order some vegetables]":
            st.switch_page(st.Page("./pages/groceryDelivery.py"))
    with container6:
        st.image("./assets/all3_1.jpg")