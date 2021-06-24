import os
import sys
import json
from flask import Flask, request

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
from utils.flask_functions import funcion_flask_1

"""

Crea una API flask con un solo endpoint que muestre por pantalla el json 'googleplaystore.json'
de la carpeta /data. En resumen, el endpoint tiene que leer el fichero 'googleplaystore.json' y retornarlo.

Además, este fichero contiene otra función que está fuera de la funcionalidad de la API flask

"""

""" 1: No es una función de flask"""
def mi_funcion():
    """
    TODO - Esta función ha de llamar a la función 'funcion_flask_1' que está en /utils/flask_functions.py y
    mostrar por pantalla lo que retorne esa función. 
    """
    return funcion_flask_1()    


app = Flask(__name__)   

@app.route("/") 
def home():
    with open(route(3) + sep + "data" + sep + "googleplaystore.json", "r+", encoding="latin-1") as outfile:
        json_readed = json.load(outfile)
    return json_readed 

def main():
    fullpath = (route(3) + sep + "config" + sep + "flask_settings.json")
    with open(fullpath, "r") as json_file_readed:
        json_readed = json.load(json_file_readed)
    # Json variables are loaded:
    SERVER_RUNNING = json_readed["server_running"]
    if SERVER_RUNNING:
        DEBUG = json_readed["debug"]
        HOST = json_readed["host"]
        PORT_NUM = json_readed["port"]
        app.run(debug=DEBUG, host=HOST, port=PORT_NUM)

""" PARTE PURA DE FLASK """
if __name__ == '__main__':
    """ Todo lo que está aquí debajo tiene que ver con la funcionalidad del flask """
    
    """2"""

    main()
