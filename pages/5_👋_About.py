import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="About",
    page_icon="👋"
)
 

def about_us():
    st.write("# About Us 👋 ")
    st.markdown(
        f"""
            <strong>Counting Ocean Flow Power Web App ini dirancang oleh Mahasiswa ilmu Komputer Universitas Pertamina
            di bawah lisensi Framework Streamlit.<br></strong>
            Streamlit v1.17.0<br>
            https://streamlit.io<br>
            Copyright 2023 Snowflake Inc. All rights reserved.<br>

        """, unsafe_allow_html=True
    )
    st.markdown("<hr style='margin-top: 10px;'>", unsafe_allow_html=True)
    st.subheader("Anggota Tanker ")

    container1 = st.container()
    with container1:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"<h2 style='text-align: center; font-size: 25px;'>Developer Web</h2>", unsafe_allow_html=True)
            image1 = Image.open('image/wabil.jpg')
            st.image(image1, caption='Ahmad Al wabil', use_column_width='auto')

        with col2:
            st.markdown(f"<h2 style='text-align: center; font-size: 25px;'>Project Leader</h2>", unsafe_allow_html=True)
            image2 = Image.open('image/ari.jpg')
            st.image(image2, caption='Ari Aprilianto Satriyo', use_column_width='auto')

        with col3:
            st.markdown(f"<h2 style='text-align: center; font-size: 25px;'>Support System</h2>", unsafe_allow_html=True)
            image3 = Image.open('image/oji.jpg')
            st.image(image3, caption='Ahmad Arroziqi', width=400, use_column_width='auto')

    st.markdown("<hr style='margin-top: 10px;'>", unsafe_allow_html=True)
    st.subheader("Dosen Pembimbing")
    container2 = st.container()
    with container2:
        col4 = st.columns(1)[0]
        with col4:
            st.markdown(f"<h2 style='text-align: left; font-size: 25px;'>Pembimbing</h2>", unsafe_allow_html=True)
            image4 = Image.open('image/drAriana.jpg')
            st.image(image4, caption='Dr. Ariana Yunita',width= 230)

if __name__ == '__main__' :
    about_us()
