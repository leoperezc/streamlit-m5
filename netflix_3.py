import streamlit as st
import pandas as pd
import numpy as np



st.title('Netflix app')

DATE_COLUMN = 'released'
DATA_URL = ('movies_2.csv')

import codecs

@st.cache_data
def load_data(nrows):
    doc = codecs.open('movies_2.csv','rU','latin1')
    data = pd.read_csv(doc, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    return data

def filter_data_by_filme(filme):
    data2 = data.copy
    data2 = data2[['budget', 'director', 'name', 'gross']]
    filtered_data_filme = data[(data['name'].str.upper().str.contains(filme))]
    return filtered_data_filme


data_load_state = st.text('Loading cicle nyc data...')
data = load_data(1000)
data_load_state.text("Done! (using st.cache)")

data2 = data.copy
data2.loc[:, ['budget', 'director', 'name', 'gross']]
print(data2)