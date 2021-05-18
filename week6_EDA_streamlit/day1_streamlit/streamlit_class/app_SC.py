# -*- coding: utf-8 -*-
import streamlit as st
import os
from utils.stream_config import draw_map
from utils.dataframes import load_normal_csv, load_csv_for_map,load_csv_df

path = os.path.dirname(__file__)
df = None
    
menu = st.sidebar.selectbox('Menu:',
            options=["Bienvenida", "Analizador", "Mapa con Globos"])

if menu == 'Bienvenida':
    st.title('¡Bienvenidos al Bootcamp de the Bridge!')
    st.write('Es un placer tenerte por aquí.')

if menu == 'Analizador':
    slider_csv = st.sidebar.file_uploader("Selecciona un CSV", type=['csv', "png"]) # aqui podemos darle la opción de \
    #subir diferentes tipos de archivos
    # cargar el dataframe
    if type(slider_csv) != type(None): # se cumple cuando subamos un archivo
        filtro_edades = st.sidebar.checkbox("Filtrar edades") # tengo el boton de filtrar edades pero no estoy \
        #recogiendo ninguna informacion
        df_slider = load_csv_df(slider_csv)
        # Cada vez que clico en filtrar edades todo el código se lee para cargar la página. Para ser un poco mas eficiente\
        #podemos decir que df_slider solo se carge si no se había ejecutado antes:
        if type(df_slider) == None:
            df_slider = load_normal_csv(slider_csv)
        if filtro_edades:
            df_slider = df_slider[df_slider["age"] < 10] # máscara quedarnos con los menores de 10 años
        # cuando clico en filtrar edades se actualiza la gráfica, por eso lo saco del if porque irrespectivamente si lo clico\
        # o no la gráfica se va a actualizar correctamente:
        st.bar_chart(df_slider) # mostrar grafico de todo el dataframe
        st.table(df_slider) # mostrar el dataframe

if menu == 'Mapa con Globos':
    csv_map_path = path + os.sep + "data" + os.sep + 'red_recarga_acceso_publico_2021.csv'
    df_map = load_csv_for_map(csv_map_path)
    draw_map(df_map)
