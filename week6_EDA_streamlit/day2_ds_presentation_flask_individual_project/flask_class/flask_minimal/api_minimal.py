# No puede ser un jupiter, tiene que ser archivo .py

from flask import Flask, flash, request, render_template, redirect, url_for
import pandas as pd
import os
import json

UPLOAD_FOLDER = os.sep + "static" + os.sep
# Flask es una clase cuyo primer atributo es un atributo obligatorio (name):
app = Flask(__name__)   # El atributo name es el nombre del archivo desde donde los estoy ejecutando 
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'hellohello'

# Estas dos funciones van a ser accesibles desde la API
@app.route("/") #esta función es la que se va a llamar por defecto
def home(): 
    return render_template("upload.html", 
                           Genre_list = options["Genre_list"],
                           Platform_list= options["Platform_list"], 
                           Publisher_list= options["Publisher_list"])
    
@app.route("/upload_form", methods = ['POST', 'GET'])
def upload_form():
    if request.method == 'POST':
        genre_res = request.form['Genre']
        platform_res= request.form['Platform']
        publisher_res = request.form['Publisher']
        all_returned = str(genre_res) + str(platform_res) + str(publisher_res)
        return json.dumps({"genre": genre_res,
                            "platform": platform_res,
                            "publisher": publisher_res,
                            "all_returned": all_returned})

if __name__ == '__main__':
    # host='127.0.0.1' --> No permite recibir llamadas desde el exterior
    # host='0.0.0.0' --> Permite recibir llamadas desde el exterior (primer paso pero no el ultimo, habria luego que \
    # cambiar el router)
    # si 0.0.0.0 no funciona externamente desde la IP privada de tu PC
    # es que tu ordenador o del dispositivo desde el que se accede 
    # tiene bloqueada la conexión (antivirus / firewall)
    app.run(host='127.0.0.1',port=os.getenv("PORT", 1991), debug=True)    
    #app es la clase de la instancia Class