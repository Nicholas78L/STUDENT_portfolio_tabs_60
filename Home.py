import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.header("The Best Company")
txt_content = """
Our development company specializes in creating websites and web applications that are accessed through web browsers. 
This includes the development of the front-end (user interface) and back-end (server-side logic) of web-based solutions
"""
st.write(txt_content)
st.subheader("Our Team")

df = pandas.read_csv('data.csv')

col1, gap1, col2, gap2, col3 = st.columns([1.5, 0.2, 1.5, 0.2, 1.5])

# col1, gaps1, col2, gaps2, col3 = st.columns(5)
# Задача состоит в том, чтобы пройти по всем строкам этого DataFrame (df)
# и иметь возможность обращаться к значениям в каждой ячейке по имени столбца.

# метод .iterrows() возвращает итератор, который генерирует индекс каждой строки и данные этой строки
# в виде row - объекта Series. Обращение к значениям ячеек осуществляется по имени столбца.

with col1:
    for index, row in df[0:4].iterrows():
        st.subheader(row['first name'].capitalize() + ' ' + row['last name'].capitalize())
        st.text(row['role'])
        st.image(f'images/{row['image']}')

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(row['first name'].capitalize() + ' ' + row['last name'].capitalize())
        st.text(row['role'])
        st.image(f'images/{row['image']}')

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(row['first name'].capitalize() + ' ' + row['last name'].capitalize())
        st.text(row['role'])
        st.image(f'images/{row['image']}')