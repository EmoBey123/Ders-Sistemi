import streamlit as st
import sqlitecloud
import time
import requests

#Bağlantı
conn = sqlitecloud.connect("your_api")
c = conn.cursor()

st.title("Duyurular")
st.write("Ders Sistemine Hoş Geldin!")
st.image('https://timasokul.com/files/content/shutterstock_688093252-171220211059.png')


