import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
url = "dataset_filtered_0_131.csv"
data = pd.read_csv(url)

st.title('Calidad del aire en la ciudad de Zaragoza')
st.write('Esta aplicación muestra información sobre la calidad del aire en la ciudad de Zaragoza.')

# Filtros
contaminantes = data['contaminante'].unique()
contaminante_seleccionado = st.selectbox('Contaminante', contaminantes)

anios = data['year'].unique()
anio_selecionado = st.selectbox('Año', sorted(anios))

grafica_seleccionada = st.selectbox('Graficas', ("Barras", "Puntos", "Radio"))

tabla = ["Si", "No"]
mostrar_tabla = st.radio("Seleccione una opción", tabla)

# Datos filtrados
data_filtrada = data[(data['contaminante'] == contaminante_seleccionado) & (data['year'] == anio_selecionado)]

# Linea para no mostrar texto de funcionción que proximamente se deprecara
st.set_option('deprecation.showPyplotGlobalUse', False)

# Mostramos la grafica seleccionada con los datos filtrados
if grafica_seleccionada == "Barras":
    plt.bar(data_filtrada['title'], data_filtrada['value'])
    plt.xticks(rotation=90)
    plt.xlabel('Estación de medición')
    plt.ylabel('Nivel')
    st.pyplot()
elif grafica_seleccionada == "Puntos":
    plt.scatter(data_filtrada['title'], data_filtrada['value'])
    plt.xticks(rotation=90)
    plt.xlabel('Estación de medición')
    plt.ylabel('Nivel')
    st.pyplot()
elif grafica_seleccionada == "Radio":
    fig, ax = plt.subplots(subplot_kw=dict(polar=True))
    ax.plot(data_filtrada['title'], data_filtrada['value'])
    ax.fill(data_filtrada['title'], data_filtrada['value'], alpha=0.3)
    plt.xticks(rotation=90)
    plt.xlabel('Estación de medición')
    plt.ylabel('Nivel')
    st.pyplot()

if mostrar_tabla == "Si":
    st.write(data_filtrada)