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
            Copyright 2024 Snowflake Inc. All rights reserved.<br>

        """, unsafe_allow_html=True
    )
    st.markdown("<hr style='margin-top: 10px;'>", unsafe_allow_html=True)
    st.subheader("Anggota Tanker ")

    container1 = st.container()
    with container1:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"<h2 style='text-align: center; font-size: 25px;'>Developer Web</h2>", unsafe_allow_html=True)
            image1 = Image.open('image/ahmad.jpeg')
            st.image(image1, caption='Ahmad Al wabil', use_column_width='auto')

        with col2:
            st.markdown(f"<h2 style='text-align: center; font-size: 25px;'>Project Leader</h2>", unsafe_allow_html=True)
            image2 = Image.open('image/ari2.jpeg')
            st.image(image2, caption='Ari Aprilianto Satriyo', use_column_width='auto')

        with col3:
            st.markdown(f"<h2 style='text-align: center; font-size: 25px;'>Support System</h2>", unsafe_allow_html=True)
            image3 = Image.open('image/ozi.jpeg')
            st.image(image3, caption='Ahmad Arroziqi', width=400, use_column_width='auto')


if __name__ == '__main__' :
    about_us()
