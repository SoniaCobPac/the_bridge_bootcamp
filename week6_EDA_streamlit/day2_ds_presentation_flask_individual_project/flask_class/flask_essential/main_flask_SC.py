from flask import Flask, request, render_template
from utils.functions import read_json
import os

# Mandatory
app = Flask(__name__)  # __name__ --> __main__  

# ---------- Flask functions ----------
@app.route("/")  # @ --> esto representa el decorador de la función
def home():
    """ Default path """
    return app.send_static_file('greet.html')

@app.route("/greet")    # cada una de las funciones con barrita algo son diferentes endpoints
def greet():
    username = request.args.get('name')
    return render_template('index.html', name=username)

@app.route("/info") #en el proyecto vamos a tener que crear un parametro pasando por un endpoint 
def create_json():
    return 'Tienes que acceder al endpoint "/give_me_id" pasando por parámetro "password" con la contraseña correcta' 

@app.route('/give_me_id', methods=['GET']) #hay que poner el password directamente ?password= para que funcione la página
def give_id():
    x = request.args['password']    #request.args recoge como un diccionario todos los parametros que le pasemos 
    if x == "12345":
        return request.args
    else:
        return "No es la contraseña correcta"

# ---------- Other functions ----------

def main():
    print("---------STARTING PROCESS---------")
    print(__file__)
    
    # Get the settings fullpath
    # \\ --> WINDOWS
    # / --> UNIX
    # Para ambos: os.sep
    settings_file = os.path.dirname(__file__) + os.sep + "settings.json"
    print(settings_file)
    # Load json from file
    json_readed = read_json(fullpath=settings_file)
    
    # Load variables from jsons (estoy guardando información mas delicada en un json, en vez de tenerlas en el mismo archivo)
    SERVER_RUNNING = json_readed["server_running"]
    print("SERVER_RUNNING", SERVER_RUNNING)
    if SERVER_RUNNING:
        DEBUG = json_readed["debug"]
        HOST = json_readed["host"]
        PORT_NUM = json_readed["port"]
        # HOST= "0.0.0.0" Abro mis puertos para las redes exteriores
        # HOST = "127.0.0.1" Abro mis puertos para las redes internas - es lo que tengo que elegir para mi proyecto EDA
        
        app.run(debug=DEBUG, host=HOST, port=PORT_NUM) #debug=True muestra el error en la web
    else:
        print("Server settings.json doesn't allow to start server. " + 
            "Please, allow it to run it.")


if __name__ == "__main__":
    main()