import streamlit as st
import sqlitecloud
import time
import requests
from streamlit import session_state

#Bağlantı
conn = sqlitecloud.connect("your_api")
c = conn.cursor()

if "giris_yapildi" not in st.session_state:
    st.session_state.giris_yapildi = False

if session_state.giris_yapildi == False:
    isim=st.text_input("Kullanıcı İsmi")
    sifre=st.text_input("Kullanıcı Şifresi")
    if isim == "admin" and sifre == "admin123":
        st.session_state.giris_yapildi= True

if st.session_state.giris_yapildi == True:
    ders=st.selectbox("Ders Seçiniz" , ("Matematik" , "Edebiyat" , "Tarih" , "Kimya" ),)
    konu=st.text_input("Konuyu Giriniz")
    if st.button("Ekle"):
        if len(konu)>1:
            c.execute(f"""CREATE TABLE IF NOT EXISTS {ders}(
                konu TEXT
            )""")
            c.execute(f"INSERT INTO {ders} VALUES(?)",(konu,))
            conn.commit()
            st.subheader("Başarılı")
            time.sleep((2))
            st.rerun()

        else:
            st.error("Lütfen Konuyu Giriniz!!!")



