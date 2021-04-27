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

import b.c.z

print(f2x())
