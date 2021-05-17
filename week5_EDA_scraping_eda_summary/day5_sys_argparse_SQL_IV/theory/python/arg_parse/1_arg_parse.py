import argparse
from my_module import exponent

parser = argparse.ArgumentParser()
parser.add_argument("-x", "--x", type=int, help="the base")
parser.add_argument("-y", "--y", type=int, help="the exponent", required=True)
parser.add_argument("-v", "--v", default=0, type=int, help="the result will be multiplied by 'v'")
args = vars(parser.parse_args())

print("####################\n")
print(type(args))
print(args)
base = args["x"]
exp = args["y"]
v = args["v"]
result = exponent(x=base, y=exp, v=v)
print("\nThe operation was: (x^y)*v (if v exists)\n")
print("(" + str(base) + "^" + str(exp) + ")" + "*" + str(v) + "[if exists]" + " = " + str(result))
print("\nThe final result is:", result)
print("\n####################")


# copio la ruta absoluta del archivo y voy a la terminal del ordenador: \
# python y pego la ruta del archivo. Asi ejecuto el archivo desde la terminal
# Control C o salgo de la terminal para parar la ejecución

# TO RUN: 
#python Z:\Data_Science\TheBridge\Content\Contenido_Curso\data_science_apr_2021\
# week5_EDA_scraping_eda_summary\day5_sys_argparse\theory\python\arg_parse\1_arg_parse.py -x 2 -y 4 -v 2

# 1
# python o python3 
# 2
# ruta al fichero 
# 3
# args
# --help

# 'python' 'ruta' 'args'
 

# volver a mirar la clase 17.05.2021 para ver como escribir parametros en la terminal