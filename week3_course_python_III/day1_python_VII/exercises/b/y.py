import os, sys

y1 = 3
y2 = "4"

def f1y():
    if y1 == 3:
        print("f1y")
        a.x.f1x()

def f2y():
    if y2 == str:
        print("f2y")
        a.x.f2x()

ruta = __file__
for i in range(2):
    ruta = os.path.dirname(ruta)
    print(ruta)

sys.path.append(ruta)    

import a.x

print(f1y())
print(f2y())



