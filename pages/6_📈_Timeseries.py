import streamlit as st
import pandas as pd
import firebase_admin
import plotly.express as px
from firebase_admin import credentials, db, initialize_app, get_app


# Check if the default app has been initialized
cred = credentials.Certificate("../src/pages/ocflop-esp32-iot-firebase-adminsdk-c7o6h-75edfcf280.json")

# Try to get the existing app or create a new one
try:
    app = get_app() 
except ValueError:
    app = initialize_app(cred,{"databaseURL":"https://ocflop-esp32-iot-default-rtdb.asia-southeast1.firebasedatabase.app/"})

def fetch_data_from_firebase():
    ref = db.reference('/test')  # Adjust the path to your data in Firebase
    data = ref.get()  # Get the data from Firebase
    df = pd.DataFrame.from_dict(data, orient='index')  # Convert data to DataFrame
    
   
    return df

def main():
    st.title('Visualisasi Time Line Data Real-Time dari Firebase')

    # Ambil data dari Firebase
    data = fetch_data_from_firebase()

    # Visualisasi time line dengan Plotly
    fig = px.line(data, x=data.index, y=data.columns, title='Time Series Data Visualization')
    st.plotly_chart(fig)

if __name__ == '__main__':
    main()
    
