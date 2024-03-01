import pandas as pd
import streamlit as st
uploaded_file = st.file_uploader('Choose a file')
if uploaded_file is not None:
   df1=pd.read_excel(uploaded_file)
else:
st.warning(“you need to upload a csv or excel file.”)
