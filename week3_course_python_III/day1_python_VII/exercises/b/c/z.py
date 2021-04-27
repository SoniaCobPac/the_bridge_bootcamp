import sys, os

z1= 5
z2= 6

def f1z():
    print("f1z")
    b.y.f1y()

def f2z():
    print("f2z")
    a.x.f2x()

ruta = __file__

for i in range(3):
    ruta= os.path.dirname(ruta)
    print(ruta)

sys.path.append(ruta)

import a.x

print(f2z())

ruta_y = os.path.dirname(__file__)
print(ruta_y)

print(f2z())