import pandas as pd
import plotly.express as px
import streamlit as st

# Encabezado principal de la app
st.header('Análisis interactivo de vehículos en venta')

# Cargar datos
car_data = pd.read_csv('vehicles_us.csv')

# Casilla para construir histograma
build_histogram = st.checkbox('Mostrar histograma del odómetro')

if build_histogram:
    st.write('Histograma del kilometraje (odómetro) de los vehículos')
    fig_hist = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig_hist, use_container_width=True)

# Casilla para construir gráfico de dispersión
build_scatter = st.checkbox('Mostrar gráfico de dispersión precio vs. kilometraje')

if build_scatter:
    st.write('Gráfico de dispersión: Precio vs. Kilometraje')
    fig_scatter = px.scatter(car_data, x='odometer', y='price', color='type',
                             title='Precio según el kilometraje por tipo de vehículo')
    st.plotly_chart(fig_scatter, use_container_width=True)