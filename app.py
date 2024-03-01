import pandas as pd
import streamlit as st

st.title('Análisis de datos de Producción')
uploaded_file = st.file_uploader('Choose a file')
if uploaded_file is not None:
   df1=pd.read_csv(uploaded_file)
   st.write(df1)
   #Asegúrate de que la columna de fechas es de tipo datetime
   df1['Fecha Inicio'] = pd.to_datetime(df1['Fecha Inicio'])

   # Define tu rango de tiempo
   inicio = pd.to_datetime('2024-02-29')
   fin = pd.to_datetime('2024-03-29')
   st.write(inicio)
   st.write(fin)

   # Filtra el DataFrame
   df1_filtrado = df1[df1['Fecha Inicio'].between(inicio, fin)]

   # Muestra el DataFrame filtrado
   st.write(df1_filtrado)
else:
 st.warning('you need to upload a csv or excel file.')
