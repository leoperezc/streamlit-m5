import streamlit as st
import pandas as pd

st.title('Streamlit con Cache')
data_url = 'dataset.csv'

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(data_url, nrows=nrows)
    return data

data_load_state = st.text('Loading data...')

nrows = int(st.text_input('Cuántos registros quieres cargar: '))

data = load_data(nrows)
data_load_state = st.text(f'Done ! {nrows:,d} fueron cargados')

st.dataframe(data)
