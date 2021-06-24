import streamlit as st
from PIL import Image
import os
import sys
import json
import pandas as pd 
from sqlalchemy import create_engine
import pandas as pd
from sklearn.decomposition import PCA

# Haz que se pueda importar correctamente estas funciones que están en la carpeta utils/

sep = os.sep
def route (steps):
    """
    This function appends the route of the file to the sys path
    to be able to import files from/to other foders within the EDA project folder.
    """
    route = os.path.abspath(__file__)
    for i in range(steps):
        route = os.path.dirname(route)
    sys.path.append(route)
    return route

route(2)

from utils.stream_config import draw_map
from utils.dataframes import load_csv_for_map

menu = st.sidebar.selectbox('Menu:',
            options=["No selected", "Load Image", "Map", "API", "MySQL", "Machine Learning"])

if menu == "No selected": 
    """2"""
    with open(route(3) + sep + "config" + sep + "config.json", "r+", encoding="latin-1") as outfile:
        json_readed = json.load(outfile)
    
    # Pon el título del proyecto que está en el archivo "config.json" en /config   
    st.title(json_readed["Title"])
    # Pon la descripción del proyecto que está en el archivo "config.json" en /config
    st.write(json_readed["Description"])
    
if menu == "Load Image": 
    """3"""
    # Carga la imagen que está en data/img/happy.jpg
    
    image = Image.open(route(3) + sep + "data" + sep + "img" + sep + "happy.jpg")  
    st.image (image,use_column_width=True)

if menu == "Map":
    """4"""
    # El archivo que está en data/ con nombre 'red_recarga_acceso_publico_2021.csv'
    csv_map_path = (route(3) + sep + "data" + sep + "red_recarga_acceso_publico_2021.csv")
    df_map = load_csv_for_map(csv_map_path)
    draw_map(df_map)

if menu == "API":
    """5"""
    # Accede al único endpoint de tu API flask y lo muestra por pantalla como tabla/dataframe
    route(2)
    url = "http://127.0.0.1:6060/"
    output = pd.read_json(url)
    st.write(output)

    
if menu == "MySQL":
    """6"""
    route(2)
    import utils.sql_functions as s
    
    with open(route(3) + sep + "config" + sep + "bd_info.json", "r+", encoding="latin-1") as outfile:
        json_readed = json.load(outfile)
    
    IP_DNS = json_readed["IP_DNS"]
    USER = json_readed["USER"]
    PASSWORD = json_readed["PASSWORD"]
    BD_NAME = json_readed["BD_NAME"]
    PORT = json_readed["PORT"]
    # 1. Conecta a la BBDD
    mysql_db = s.MySQL(IP_DNS=IP_DNS, USER=USER, PASSWORD=PASSWORD, BD_NAME=BD_NAME, PORT=PORT)
    mysql_db.connect()
        
    # 2. Obtén, a partir de sentencias SQL (no pandas), 
    # la información de las tablas que empiezan por 'fire_archive*' (join)
    #query = """SELECT * FROM fire_archive_M6_96619
    #        UNION 
    #        SELECT * FROM fire_archive_V1_96617  
    #"""

    #result = mysql_db.execute_get_sql(query)
    #st.write(result.head())

    select_sql = """SELECT * FROM fire_nrt_M6_96619"""
    result = mysql_db.execute_get_sql(select_sql)
    df = pd.DataFrame(result)
    st.write(df.head())
    print(df)


    # 3. Entrena tres modelos de ML diferentes siendo el target la columna 'fire_type'. 
    # Utiliza un pipeline que preprocese los datos con PCA. Usa Gridsearch.  
    
if menu == "Machine Learning": 
    from utils.ml import machine_functions
# 3. Entrena tres modelos de ML diferentes siendo el target la columna 'fire_type'. Utiliza un pipeline que preprocese los datos con PCA. Usa Gridsearch.  
    machine_functions(df=df) 


    # 4. Añade una entrada en la tabla 'student_findings' por cada uno de los tres modelos. 
    # 'student_id' es EL-ID-DE-TU-GRUPO.
    
    # 5. Obtén la información de la tabla 'fire_nrt_M6_96619' y utiliza el mejor modelo 
    # para predecir la columna target de esos datos. 
    

    # 6. Usando SQL (no pandas) añade una columna nueva en la tabla 'fire_nrt_M6_96619' 
    # con el nombre 'fire_type_EL-ID-DE-TU-GRUPO'
   

    # 7. Muestra por pantalla en Streamlit la tabla completa (X e y)
    
  



