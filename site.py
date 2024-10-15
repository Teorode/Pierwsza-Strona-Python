import streamlit as st

st.set_page_config(page_title="Moja pierwsza strona internetowa w pythonie", page_icon=":cold_face:")

with st.container():
    st.title("Witam na mojej stronie internetowej!")
    st.page_link("https://www.google.pl", label="Google", icon="🌎")
    st.write("---")
    left_column, right_column = st.columns(2)
    st.write("Hello python!")