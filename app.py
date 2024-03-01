import pandas as pd
import streamlit as st

st.title('Análisis de datos de Producción')
uploaded_file = st.file_uploader('Choose a file')
if uploaded_file is not None:
   df1=pd.read_csv(uploaded_file)
   st.write(df1)
else:
 st.warning('you need to upload a csv or excel file.')
