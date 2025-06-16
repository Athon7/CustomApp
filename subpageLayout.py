import streamlit as st

def subpageLayout(img, title):
    h1, h2, h3, h4 = st.columns([0.2,0.5,0.1,0.2], gap="small", vertical_alignment="center")
    with h1:
        container1 = st.container(border=False, height=90)
        container2 = st.container(border=False, height=400)
        with container1:
            st.html("<h1>"+title+"</h1>")
        with container2:
            st.image(img)
    return h1,h2,h3,h4