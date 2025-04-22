import numpy as np 
import pandas as pd
from classeMarota import classeMarota
# from wrapper import wp #n]ao vou masi precisar dessa classe de wrapper time measurement -> irei usar o benchmark

# Testes para o gRPC
# 1 - tempo para chamada de uma operação sem argumentos e sem valor de retorno (void)
def teste1():
    return

# 2 - tempo para chamada de uma operação com um argumento long e valor de retorno long
def teste2(a):
    #operacao com o parametro a (que é um long)
    return a #retorno de a modificado (ainda long)

# 3 - tempo para chamada de uma operação com oito argumentos long e valor de retorno long
def teste3(a,b,c,d,e,f,g,h):
    if(e == 0):
        return ((a+b-c)*d/(e+1))^f -g +h
    else:
        return ((a+b-c)*d/e)^f -g +h #o retorno tem que ser um long

# 4 - tempo para chamada de uma operação com um argumento String e valor de retorno String, para strings com diferentes tamanhos (segure-se testes com potencias de 2: 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, ....)
def teste4(s):
    return 'É uma string de tamanho potencia de 2' if np.size(s)%2 == 0 else 'Não é uma string de tamanho potencia de 2'

# 5 - tempo para a chamada de uma operação com um argumento e um valor de retorno de um tipo complexo (ex.: uma classe definida por vocês)
def teste5(a):
    return classeMarota

# 6 - outras métricas de desempenho de desempenho que vocês acharem pertinente
def teste6():
    return

if '__main__':
    cm = classeMarota()

else:
    print('Error: please execute the correct script.')