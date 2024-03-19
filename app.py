import pandas as pd
import streamlit as st
import datetime as dt
import datetime as datetime
import pytz
from datetime import datetime, timedelta

st.title('Análisis de datos de Producción')
uploaded_file = st.file_uploader('Choose a file')
if uploaded_file is not None:
   df1=pd.read_csv(uploaded_file)
   st.write(df1)
   #Asegúrate de que la columna de fechas es de tipo datetime
   df1['Fecha Inicio'] = pd.to_datetime(df1['Fecha Inicio'])

   

   # Define tu rango de tiempo
   inicio = pd.to_datetime('2023-05-05')
   fin = pd.to_datetime('2023-05-29')


   # Filtra el DataFrame
   #df1_filtrado = df1[df1['Fecha Inicio'].between(inicio, fin)]

   # Muestra el DataFrame filtrado
   #st.write(df1_filtrado)

else:
 st.warning('you need to upload a csv or excel file.')

now=datetime.now()
    #with st.sidebar:
    #   opcion_c = st.selectbox('Como quieres hacer la consulta?',('Calendario','Tiempo atrás'))
with st.sidebar:
       st.subheader("Parámetros de consulta")
       sd = st.date_input("Fecha de inicio de Consulta" , max_value=datetime.today())
       sd=sd-timedelta(hours=0)

with st.sidebar:

       th_start = st.time_input('Hora inicio de Consulta', datetime.now(pytz.timezone('America/Bogota')),10,step=3600)


       ed = st.date_input( "Fecha de Fin de Consulta" , max_value=datetime.today())
       ed=ed-timedelta(hours=0)

with st.sidebar:
       th_end = st.time_input('Hora fin de Consulta', datetime.now(pytz.timezone('America/Bogota')),step=3600)

if st.button('Consulta '):
   ic = str(sd)+" "+str(th_start)
   fc=  str(ed)+" "+str(th_end)
   st.write(ic)
   st.write(fc)
   st.write(inicio)
   st.write(fin)
   df1_filtrado = df1[df1['Fecha Inicio'].between(ic, fc)]
   #df2_filtrado = df1[df1['Fecha Inicio'].between(inicio, fin)]
   st.write(df1_filtrado)
   #st.write(df2_filtrado)
