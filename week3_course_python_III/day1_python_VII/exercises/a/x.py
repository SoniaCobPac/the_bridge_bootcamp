import sys, os

x1 = 12
x2 = 23

def f1x():
    if x1 % 2 == 0:
        print("f1x")


def f2x():
    if x2 > 4:
        print("f2x")
        b.c.z.f2z()


ruta = __file__
for i in range(2):
    ruta = os.path.dirname(ruta)
    
print(ruta)

sys.path.append(ruta)    

import b.c.z    #Solo por importar un archivo ya estaría ejecutando todo ese archivo, de la forma que sea. 
                #Da igual que use import/as o from/import. Pero si usamos el "from" solo estamos trayendo la función
                #que nombramos, todo el archivo se esta ejecutando pero no se imprime porque solo estoy llamando una función.

print(f2x())

# if __name__ == "__main__":  La variable 'name' de cualquier archivo .py será __main__ si es el archivo que se está ejecutando.
# En cualquier otro caso no será main entonces la condición no se cumple y todo lo que hay debajo de ella no se ejecuta. 
# Esta función solo se ejecuta cuando ejecuto el archivo que la contiene.
# (Tengo que escribir esta linea en los dos archivos para que funcione.) 