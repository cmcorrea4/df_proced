import streamlit as st
import pandas as pd

def main():
    # Título de la aplicación
    st.title("Análisis de Datos de Energía")

    # Carga del archivo de Excel
    archivo_excel = st.file_uploader("Cargar archivo Excel", type=["xlsx"])

    if archivo_excel is not None:
        # Lectura del archivo Excel
        df = pd.read_excel(archivo_excel)

        # Despliegue del DataFrame
        st.subheader("Datos del archivo Excel")
        st.write(df)

        # Estadísticas descriptivas
        st.subheader("Estadísticas descriptivas")
        st.write(df.describe())

        # Consulta por código
        st.subheader("Consulta por código")
        codigo = st.text_input("Introduce el código a consultar:")
        consulta = df[df['Código'] == codigo]
        st.write(consulta)

if __name__ == "__main__":
    main()
