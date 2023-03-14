import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Measurement",
    page_icon="📊"
)

st.markdown("# Measurement Ocean Flow Power 🌊")
with st.sidebar:
    header = st.success("Fitur Measurement")
    info = st.info("Pada Fitur ini silakan masukkan parameter inputan untuk menghitung daya arus laut")

# Title
st.text('By Student of Pertamina University\n')
side_title = st.success("Input the Parameters")
pilih = st.selectbox("Pilih Parameter yang ingin dicari?",('Daya Arus Laut','Luas Penampang Turbin'))
if pilih == 'Daya Arus Laut':
    v_arus_laut = st.number_input("Kecepatan Arus laut (m/s) 🌊")
    kerapatan_massa = st.number_input("Kerapatan Massa Air (kg/m^3) 💧", 1000, 1100 )
    A_luas_penampang = st.number_input("Luas Penampang(m^2) 🛑")
    Efisiensi_turbin = st.number_input("Efisiensi(%) ⚙️", 0.0, 100.0)  
    daya_listrik_arus = 0.5 * kerapatan_massa * A_luas_penampang * abs(v_arus_laut ** 3) * (Efisiensi_turbin / 100)
    hitung1 = st.button('Hitung')

elif pilih == 'Luas Penampang Turbin':
    daya = st.number_input("Daya Arus Listrik (Watt) ⚡")
    v_arus_laut = st.number_input("Kecepatan Arus laut (m/s) 🌊")
    kerapatan_massa = st.number_input("Kerapatan Massa Air (kg/m^3) 💧", 1000, 1100 )
    Efisiensi_turbin = st.number_input("Efisiensi(%) ⚙️", 0.0, 100.0)
    Luas_penampang = 2 * daya /((abs(v_arus_laut)**3) * kerapatan_massa*(Efisiensi_turbin / 100) )
    hitung2 = st.button('Hitung')

if pilih == 'Daya Arus Laut'and hitung1:
    mtr1, mtr2, mtr3 = st.columns(3)
    mtr1.metric("Daya (watt) ⚡", daya_listrik_arus)   
    mtr2.metric("Efisiensi(%) ⚙️", Efisiensi_turbin )
    mtr3.metric("Kecapatan Arus(m/s) 🌊", v_arus_laut )
    st.success(f"Potensi daya arus laut yang dihasilkan adalah {daya_listrik_arus} Watt")

elif pilih == 'Luas Penampang Turbin' and hitung2:
    mtr1, mtr2, mtr3 = st.columns(3)
    mtr1.metric("Luas Penampang(m^2) 🛑", Luas_penampang)   
    mtr2.metric("Daya (Watt) ⚡", daya )
    mtr3.metric("Kecapatan Arus(m/s) 🌊", v_arus_laut )
    st.success(f"Luas Penampang yang diperlukan adalah {Luas_penampang} m^2")
    st.exception(0)




    





    





# if daya_listrik_arus <= 1000:
#         st.error("Daya listrik yang dihasilkan kurang dari standar dari sebuah pembangkit listrik.")
#         with st.expander("Berikut beberapa saran") :
#          st.text("""
#             1. Optimalkan konfigurasi turbin: Desain dan konfigurasi yang tepat dapat 
#                membantu meningkatkan efisiensi turbin dan meningkatkan daya listrik yang dihasilkan.
#             2. Pemeliharaan rutin: Memastikan bahwa semua bagian turbin berfungsi dengan 
#                baik dan bebas dari kerusakan dapat membantu meningkatkan daya listrik yang dihasilkan.
#             3. Penggunaan material berkualitas tinggi: Menggunakan material berkualitas tinggi untuk
#                membuat bagian-bagian turbin dapat membantu memastikan bahwa turbin berfungsi dengan 
#                baik selama jangka waktu yang lama dan menghasilkan daya listrik yang optimal.
#             4. Monitoring kondisi lingkungan: Memantau kondisi lingkungan seperti arus air, 
#                gelombang, dan kondisi cuaca dapat membantu menentukan waktu yang tepat untuk 
#                mengoperasikan turbin dan memaksimalkan daya listrik yang dihasilkan.
#             5. Penggunaan teknologi baru: Penggunaan teknologi terbaru seperti teknologi
#                optimasi turbin arus laut dapat membantu meningkatkan daya listrik yang dihasilkan
#                dan memastikan bahwa turbin berfungsi dengan baik selama jangka waktu yang lama""")
#     elif daya_listrik_arus > 1000 and daya_listrik_arus < 10000:
#         st.warning(""" Daya listrik yang dihasilkan cukup dari standar, berikut beberapa saran """)
#     elif daya_listrik_arus >= 10000:
#         st.success(""" Daya listrik yang dihasilkan melebihi standar, pertahankan segala aspek dan lakukanlah perawatan berkala terhadap segala perangkat """)




