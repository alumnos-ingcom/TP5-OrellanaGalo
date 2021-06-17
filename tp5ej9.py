################
# Galo Orellana - @OrellanaGalo
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

from tp4ej1 import ingreso_entero

def lista_factoriones():
    
    lista_factoriones = []
    lim = 1499999
    for i in range(lim):
        if i == factoriones(i):
            lista_factoriones.append(i)
    return lista_factoriones

def factoriones(numero):
    
    factorial = 1
    suma = 0
    for j in str(numero):
        j = int(j)
        for i in range(j):
            factorial = factorial * (i + 1)
        suma = suma + factorial
        factorial = 1
    return suma

def prueba():
    
    print('Bienvenido a mi codigo!')
    print('\n Lista de todos los factoriones menores a 1.499.999: ')
    factoriales = lista_factoriones()
    print(f'\n {factoriales}')

if __name__ == "__main__":
    prueba()

