import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="DataVisualization",
    page_icon="📊"
)
st.sidebar.success("Data Visualization")
st.sidebar.info("Data visualization merupakan fitur untuk menampilkan penyajian data arus laut dalam bentuk chart yang dibedakan berdasarkan 8 pembagian waktu")
st.markdown("# Data Visualization 📊")
st.markdown("Hasil data lapangan")
data1 = pd.read_csv('data/KecepatanArus_Bulan12.csv')
data2 = pd.read_csv('data/KecepatanArusLaut_Bulan1.csv')
data3 = pd.read_csv('data/KecepatanArusLaut_Bulan2.csv')
st.subheader("Tambah Data")
tahun = int(st.number_input("Tahun"))
bulan = st.number_input("Bulan")
data = st.file_uploader("Unggah file CSV")

tab1, tab2, tab3, tab4 = st.tabs(
    ["Desember 2022", "Januari 2023", "Februari 2023", 'Data Compare'])
with tab1:
    st.subheader("Data Arus Laut Desember 2022")
    chart_raw_bar1 = pd.DataFrame(data1)
    st.area_chart(chart_raw_bar1, x='Tanggal', y=(
        '0', '12', '15', '18', '21', '3', '6', '9'), use_container_width=True)
    st.subheader("Average Arus laut")
    average1 = chart_raw_bar1[['0', '3', '6',
                               '9', '12', '15', '18', '21']].mean()
    st.bar_chart(average1)


with tab2:
    st.subheader("Data Arus Laut Januari 2023")
    chart_raw_bar2 = pd.DataFrame(data2)
    st.area_chart(chart_raw_bar2, x='Tanggal', y=(
        '0', '3', '6', '9', '12', '15', '18', '21'), use_container_width=True)
    st.subheader("Average Arus laut")
    average2 = chart_raw_bar2[['0', '12', '15',
                               '18', '21', '3', '6', '9']].mean()
    st.bar_chart(average2)
# def show_data():
with tab3:
    st.subheader("Data Arus Laut Februari 2023")
    chart_raw_bar3 = pd.DataFrame(data3)
    st.area_chart(chart_raw_bar3, x='Tanggal', y=(
        '0', '3', '6', '9', '12', '15', '18', '21'), use_container_width=True)
    st.subheader("Average Arus laut")
    average3 = chart_raw_bar3[['0', '3', '6',
                               '9', '12', '15', '18', '21']].mean()
    st.bar_chart(average3)

with tab4:
    st.subheader("Tambah Data")
    # data_comp=pd.DataFrame(['data1','data2','data3'], columns=['0','3','6','9','12','15','18','21'])
    # st.area_chart(data_comp,use_container_width=True)
# if __name__ == "__main__":
    # show_data()
# 'tanggal','0','3','6','9','12','15','18','21'
# columns=['tanggal','0','3','6','9','12','15','18','21']
