import streamlit as st
from send_email import send_email   # импортируем созданную нами ф-цию из бэк-энда
import pandas

df_topics = pandas.read_csv("topics.csv")
st.header("Contact Me")

with st.form(key="email_form"):                         # создаём форму (зону) для взаимодействия с посетителями
    user_email = st.text_input("Your Email Address")    # можно ввести только одну строку кода
    option = st.selectbox("What topic do you want to discuss?", df_topics['topic'], # topic - name of column topics.csv
                          index=None, placeholder="Press an arrow to select topics...")
    # st.selectbox("What topic do you want to discuss?", ("Job inquiries", "Project proposals", "Other"),
    #              index=None, placeholder="Select topic...")
    raw_message = st.text_area("Text", on_change=None)             # можно вводить многострочный код
    # message = message + '\n' + user_email

    # 1) \ -> обратная косая - обязательный атрибут для сепарации ТЕМЫ письма (после косой НЕ должно быть пробелов):
    # 2) также обязательно нужно оставить одну пустую строку между Темой (Subject) и От кого письмо (From):
    # 3) После \ обратной косой последующий текст сообщения должен быть без отступов совсем! Это важно!
    # т.е. текст начиная с Subject и до """ должен быть загнан в самый край левого поля.
    message = f"""\
Subject: New letter from {user_email}

From: {user_email}
Topic: {option}
{raw_message}
"""
    button = st.form_submit_button("Submit")  # спец.кнопка отправки, привязанная к нашей форме. (True|False)

    if button:
        send_email(message)
        st.info("Your email was sent successfully.")