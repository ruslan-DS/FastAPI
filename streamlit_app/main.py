import streamlit as st
import requests
import json


st.write("""
 # Приложение с моделью ruBERT и FastAPI
""")

text_users = st.text_input('Напишите свой текст, чтобы определить, какое у вас сейчас настроение:')


if st.button('Нажмите, чтобы Ваше настроение:') and (text_users is not None and text_users != ''):
    res = requests.post('http://158.160.136.168', json={'text': text_users, 'inference': 0}) # отправим json-формат данных на сервер для обработки
                                                                                                         # ключ inference сделаем 0 по-дефолту
    st.info(f'Ваш текст имеет: **{res.text}** настроение!')
