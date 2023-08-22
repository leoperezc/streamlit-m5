import streamlit as st

st.title('Mi Segundo Sidebar')

st.header('Hecho con Streamlit')

sidebar = st.sidebar

sidebar.title('Bienvenido al uso de Sidebar')
sidebar.header('El encabezado dentro de un sidebar')
sidebar.write('Aquí puedes colocar los elementos del sidebar')
edad = sidebar.text_input("Captura tu edad: ")
sidebar.write(f'Tu edad es {edad:,d}')