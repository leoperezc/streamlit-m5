# %%writefile employees.py 

import streamlit as st
import pandas as pd
import numpy as np
import codecs
import matplotlib.pyplot as plt

# Función para carga de datos, máximo nrows(registros) de manera predeterminada.
# Se utiliza el atributo cahe_data, ya que cache manda mensaje de que está descontinuado.

@st.cache_data
def load_data(nrows):
    doc = codecs.open('Employees.csv','rU','latin1')
    data = pd.read_csv(doc, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    return data

# Carga de datos
# La carga de datos es con un valor predeterminado de 500 registros
data = load_data(500)


# Título en la página web
st.title('M5 - Reto')

# Encabezado
st.header('Deserción Laboral')

# Explicación del proyecto
st.text('El proyecto le perimitirá obtener resultados que expliquen la deserción laboral')
st.text('a través de los diferentes filtros disponibles en la barra lateral.')

# Creación de objeto sidebar para manejar la barra lateral
sidebar = st.sidebar

sidebar.header('Apóyese de las diferentes opciones de filtrado para mostrar datos de la encuesta de diferente manera.')

# Se agrega un control Checkbox para desplegar el data frame completo

if sidebar.checkbox('Mostrar todos los empleados'):
    st.subheader('Todos los Empleados')
    st.write(data)


# Filtros para los empleados 

#  Filtro por ID de empleado, campo Employee_ID.
@st.cache_data
def filtro_data_por_empleado_id(empleado_id):
    filtro_data_employee_id = data[data['Employee_ID'].str.contains(empleado_id)]
    return filtro_data_employee_id

#  Filtro por Hometown de empleado.
@st.cache_data
def filtro_data_por_ciudad(ciudad):
    filtro_data_ciudad = data[data['Hometown'].str.contains(ciudad)]
    return filtro_data_ciudad

#  Filtro por Unit de empleado.
@st.cache_data
def filtro_data_por_unidad(unidad):
    filtro_data_unidad = data[data['Unit'].str.contains(unidad)]
    return filtro_data_unidad


# Función para el filtro por nivel educativo.
@st.cache_data
def filtro_data_nivel_educativo(nivel_educativo):
    nivel_educativo_filtrado = data[data['Education_Level'] == nivel_educativo]
    return nivel_educativo_filtrado

# Funcion para el filtro por Ciudad seleccionada
@st.cache_data
def filtro_data_ciudad_sel(ciudad_sel):
    ciudad_filtrada = data[data['Hometown'] == ciudad_sel]
    return ciudad_filtrada

#  Filtro por Unit de seleccionada.
@st.cache_data
def filtro_data_unidad_sel(unidad):
    filtro_data_unidad = data[data['Unit'].str.contains(unidad)]
    return filtro_data_unidad

# Se agrega control tex_input para obtener valores para filtrado

empleado_id = st.sidebar.text_input('Capture el ID del empleado :')
btnBuscar = st.sidebar.button('Buscar Empleado')

if (btnBuscar):
   data_empleado_id = filtro_data_por_empleado_id(empleado_id.upper())
#   count_row = data_filme.shape[0]  # Cantidad de registro
   conteo_reg = data_empleado_id.shape[0]  # Cantidad de registros
   st.write(f"Total de registros mostrados por ID del empleado: {conteo_reg}")
   st.write(data_empleado_id)


# Función para filtro por Hometown de empleado
ciudad_capturada = sidebar.text_input('Capture la ciudad del empleado:')
btnBuscar = sidebar.button('Buscar Ciudad')

if (btnBuscar):
   data_ciudad = filtro_data_por_ciudad(ciudad_capturada)
#   count_row = data_filme.shape[0]  # Cantidad de registro
#   st.write(f"Total filmes mostrados : {count_row}")
   conteo_reg = data_ciudad.shape[0]  # Cantidad de registros
   st.write(f"Total de registros mostrados por ciudad capturada: {conteo_reg}")
   st.write(data_ciudad)


# Función para filtro por Unit de empleado
unidad_capturada = sidebar.text_input('Capture la unidad:')
btnbuscarunidad = sidebar.button('Buscar Unidad')

if (btnbuscarunidad):
   data_unidad = filtro_data_por_unidad(unidad_capturada)
   conteo_reg = data_unidad.shape[0]  # Cantidad de registros
   st.write(f"Total de registros mostrados por Unidad capturada: {conteo_reg}")

   st.write(data_unidad)


#Filtro utilizando el control Select

data2 = np.sort(data['Education_Level'].unique())
nivel_educativo_seleccionado = sidebar.selectbox("Seleccionar Nivel Educativo", data2)

btnfiltroniveleducativo = sidebar.button('Filtrar Nivel Educativo')

if (btnfiltroniveleducativo):
   filtronivedu = filtro_data_nivel_educativo(nivel_educativo_seleccionado)
   conteo_reg = filtronivedu.shape[0]  # Cantidad de registros
   st.write(f"Total de registros mostrados por Nivel Educativo seleccionado: {conteo_reg}")

   st.dataframe(filtronivedu)


#Filtro utilizando el control Selectbox por ciudades

ciudad_seleccionada = sidebar.selectbox("Seleccionar Ciudad", data['Hometown'].unique())
btnfiltrociudad = sidebar.button('Filtrar Por Ciudad')

if (btnfiltrociudad):
   filtrociudad = filtro_data_ciudad_sel(ciudad_seleccionada)
   conteo_reg = filtrociudad.shape[0]  # Cantidad de registros
   st.write(f"Total de registros mostrados por Ciudad seleccionada: {conteo_reg}")

   st.dataframe(filtrociudad)

# Filtro por Unidad seleccionada con control Selecbox
unidad_seleccionada = sidebar.selectbox("Seleccionar Unidad", data['Unit'].unique())
btnfiltrounidadsel = sidebar.button('Filtrar Por Unidad')

if (btnfiltrounidadsel):
   filtrounidad = filtro_data_unidad_sel(unidad_seleccionada)
   conteo_reg = filtrounidad.shape[0]  # Cantidad de registros
   st.write(f"Total de registros mostrados por Unidad seleccionada: {conteo_reg}")
   st.dataframe(filtrounidad)


#  GRÁFICAS.

# Histograma de los empleados agrupados por edad.

fig, ax = plt.subplots()
ax.hist(data.Age)
st.subheader('Histograma de los empleados agrupados por edad')
st.pyplot(fig)


# Diagrama de frecuencias por Unidad.

fig2, ax = plt.subplots()
ax.hist(data.Unit)
st.subheader('Diagrama de frecuencias por Cantidad de Empleados por Unidad')
st.pyplot(fig2)


# Diagrama de Mayor índice de deserción por ciudad.

fig3, ax = plt.subplots()
ax.scatter(x=data.Hometown, y=data.Attrition_rate)
st.subheader('Mayor índice de Deserción por Ciudad')
st.pyplot(fig3)

# Diagrama de Mayor índice de deserción por Edad.

fig4, ax = plt.subplots()
ax.scatter(x=data.Age, y=data.Attrition_rate)
st.subheader('Mayor índice de Deserción por Edad')
st.pyplot(fig4)


# Diagrama de Mayor índice de deserción por Tiempo de servicio.

fig5, ax = plt.subplots()
ax.scatter(x=data.Time_of_service, y=data.Attrition_rate)
st.subheader('Mayor índice de Deserción por Tiempo de Servicio')
st.pyplot(fig5)
