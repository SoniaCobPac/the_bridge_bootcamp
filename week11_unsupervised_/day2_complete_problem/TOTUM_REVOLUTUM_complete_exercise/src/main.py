"""
Siempre que veas 'pass' es un TO-DO (por hacer)

"""

"""1"""

import os
import sys

# Llama a la función 'mi_funcion' que está en /flask/api.py. No puede dar error.
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

route(1)

path = route(1) + sep + "flask"
sys.path.append(path)

import api

print(api.mi_funcion())
