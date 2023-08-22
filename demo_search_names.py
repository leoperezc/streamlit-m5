import streamlit as st
import pandas as pd

st.title('Streamlit con Cache')
data_url = 'dataset.csv'

@st.cache_data
def load_data_byname(name):
    data = pd.read_csv(data_url)
    filtered_data_byname = data[data['name'].str.contains(name)]
    return filtered_data_byname

data_load_state = st.text('Loading data...')

name = (st.text_input('Qué nombre quieres buscar: '))
if st.button('Buscar'):
    if (name):
        filterbyname = load_data_byname(name)    
        data = load_data_byname(name)
        data_load_state = st.text('Done !')
        st.write(f'La cantidad de nombres econtrados es de: {data.shape[0]}')
        st.dataframe(data)
    