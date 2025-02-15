import streamlit as st
import sqlitecloud
import time
import requests

#Bağlantı
conn = sqlitecloud.connect("your_api")
c = conn.cursor()

odev=st.selectbox("Ders Seçiniz" , ("Matematik" , "Edebiyat" , "Tarih" , "Kimya" ),)
if st.button("Ödevleri Listele"):
    c.execute(f"SELECT * FROM {odev}")
    veriler=c.fetchall()
    if veriler:
        for veri in veriler:
            st.write("*" , veri[0])
    else:
        st.warning("Bu ders için ödev bulunamadı")