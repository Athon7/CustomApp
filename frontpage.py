import streamlit as st

container1 = st.container(border=False, height=50)
container2 = st.container(border=True, height=400)
container3 = st.container(border=False, height=50)

with container3:
    h1, h2, h3 = st.columns([0.8,0.1,0.1], gap="small", vertical_alignment="bottom")
    with h2:
        if st.button("Chat!", type="primary", use_container_width=True):
            st.switch_page(st.Page("mainpage.py"))
    with h3:
        st.write("Start A Chat")


with container2:
    ## Title
    h3, h4 = st.columns([0.6,0.4])
    h3.image("C:/Users/akd77/Documents/code/ManagePays/assets/title.gif")
    with h4:
        container2_1 = st.container(border=False, height=200)
        container2_2 = st.container(border=False, height=200)
        with container2_2:
            st.write("Manage all your payments in one App!")
            st.write("A one stop app for all your transactions with multiple \
                      services like travel booking and other recurring \
                      payments like mobile recharge, home usage payments. ")