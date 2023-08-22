# import streamlit
import streamlit as st
import pandas as pd

names_link = 'dataset.csv'

# read csv
names_data = pd.read_csv(names_link)

# Create title
st.title('Streamlit and pandas')

#print dataframe
st.dataframe(names_data)

# streamlit run demo_pandas.py --server.enableCORS false --server.enableXsrfProtection false