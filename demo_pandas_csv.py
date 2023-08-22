import streamlit as st
import pandas as pd

ruta_archivo = 'dataset.csv'

data = pd.read_csv(ruta_archivo)

st.title('Datos usados con Pandas')

st.dataframe(data)

