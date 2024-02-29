import streamlit as st
import pandas as pd

def main():
    # Título de la aplicación
    st.title("Análisis de Datos de Energía")

    # Carga del archivo de Excel
    df = pd.read_excel('referencia.xlsx')
    

    if archivo_excel is not None:
        # Lectura del archivo Excel
        df = pd.read_excel(archivo_excel)

        # Despliegue del DataFrame
        st.subheader("Datos del archivo Excel")
        st.write(df)

        

if __name__ == "__main__":
    main()
