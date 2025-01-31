import streamlit as st

st.header("Contact Me")

with st.form(key="email_form"):                         # создаём форму (зону) для взаимодействия с посетителями
    user_email = st.text_input("Your email address")    # можно ввести только одну строку кода
    message = st.text_area("Your message ")             # можно вводить многострочный код
    button = st.form_submit_button("Submit")            # спец.кнопка отправки, привязанная к нашей форме. (True|False)