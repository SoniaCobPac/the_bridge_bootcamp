# En vez de utilizar argparse utilizamos sys
# La unica diferencia con la otra opcion es que no tenemos que \
# especificarle las variables en la terminal, ya podemos meter los valores directamente, \
# pero estos valores que le damos SIEMPRE son string

import sys

print("All arguments:\n", sys.argv)
print("First argument:", sys.argv[0], "type:", type(sys.argv[0]))
print("Second argument:", sys.argv[1], "type:", type(sys.argv[1]))
print("Third argument:", sys.argv[2], "type:", type(sys.argv[2]))
print("Third argument:", sys.argv[3], "type:", type(sys.argv[3]))

