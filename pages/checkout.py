import streamlit as st
import json

st.html("<h3><span style='color: #C70039;'>Your Order details are</span></h3>")
st.markdown("Thanks for shopping with us!")
h1, h2, h3 = st.columns([0.2,0.4,0.4], gap="small", border=False)

with h3:
    h31, h32, h33 = st.columns([0.3,0.4,0.3], gap="large")
    with h31:
        container1 = st.container(border=False, height=50, key=1)
        with container1:
            st.html("<strong>Item</strong>")
        st.divider()
    with h32:
        container2 = st.container(border=False, height=50, key=2)
        with container2:
            st.html("<strong>Quantity</strong>")
        st.divider()
    with h33:
        container3 = st.container(border=False, height=50, key=3)
        with container3:
            st.html("<strong>Price</strong>")
        st.divider()

orders = []
if "messages" in st.session_state:
    orders = st.session_state.messages[len(st.session_state.messages)-1].get("content")
    st.session_state.messages.pop()
    orders = orders.replace("\'",'\"')
    orders = json.loads(orders)[0]

if type(orders)==dict:

    for i, order in enumerate(orders["selected_items"]):
        with h31:
            containerx = st.container(border=False, height=50, key=str(i)+"x")
            with containerx:
                st.markdown(order[0])
        with h32: 
            containery = st.container(border=False, height=50, key=str(i)+"y")
            with containery:
                st.markdown(1)
        with h33:
            containerz = st.container(border=False, height=50, key=str(i)+"z")
            with containerz:
                st.markdown(order[1])
        with h2:
            container21 = st.container(border=False, height=50)
    with h3:
        st.divider()

    with h2:
        container21 = st.container(border=False, height=200)
        with container21:
            h21, h22 = st.columns([0.8,0.5], gap="small", border=False, vertical_alignment="top")
            with h22:
                container211 = st.container(border=False, height=100)
                st.html("<h3><span style='color: #C70039;'>Total Price: </span></h3>")
    with h33:
        st.html(f"<strong>{orders['amount']}</strong>")
else:
    st.html("<strong>You haven't added anything to the cart yet!</strong>")