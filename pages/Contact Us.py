import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_form"):                         # создаём форму (зону) для взаимодействия с посетителями
    user_email = st.text_input("Your email address")    # можно ввести только одну строку кода
    raw_message = st.text_area("Your message")             # можно вводить многострочный код
    # message = message + '\n' + user_email

    # 1) \ -> обратная косая - обязательный атрибут для сепарации ТЕМЫ письма (после косой НЕ должно быть пробелов):
    # 2) также обязательно нужно оставить одну пустую строку между Темой (Subject) и От кого письмо (From):
    # 3) После \ обратной косой последующий текст сообщения должен быть без отступов совсем! Это важно!
    # т.е. текст начиная с Subject и до """ должен быть загнан в самый край левого поля.
    message = f"""\
Subject: New letter from {user_email}

From: {user_email}
{raw_message}
"""
    button = st.form_submit_button("Submit")  # спец.кнопка отправки, привязанная к нашей форме. (True|False)

    if button:
        send_email(message)
        st.info("Your email was sent successfully.")