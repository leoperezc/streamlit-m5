import streamlit as st

#Crear el título para la aplicación web

st.title('Mi primera App con Streamlit')

st.header("Información sobre el Conjunto de Datos")
st.header("Descripción de los datos")

sidebar = st.sidebar
sidebar.title('Esta es la barra lateral.')
sidebar.write('Aquí van los elementos de entrada')
sidebar.text_input("Capture el rango inicial")

st.write("""
Este es un simple ejemplo de una app para predecir
         
¡Esta app predice mis datos!
         """)


