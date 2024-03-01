import pandas as pd
import streamlit as st

st.title('Análisis de datos de Producción')
uploaded_file = st.file_uploader('Choose a file')
if uploaded_file is not None:
   df1=pd.read_csv(uploaded_file)
   st.write(df1)
   #Asegúrate de que la columna de fechas es de tipo datetime
   df['fecha'] = pd.to_datetime(df['fecha Inicio'])

   # Define tu rango de tiempo
   inicio = pd.to_datetime('2024-02-29')
   fin = pd.to_datetime('2024-03-29')

   # Filtra el DataFrame
   df_filtrado = df[df['fecha Inicio'].between(inicio, fin)]

   # Muestra el DataFrame filtrado
   print(df_filtrado)
else:
 st.warning('you need to upload a csv or excel file.')
