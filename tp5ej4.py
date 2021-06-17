################
# Galo Orellana - @OrellanaGalo
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

from tp4ej1 import ingreso_entero

def numero_perfecto(numero_perfecto):
    
    condicion = False
    
    for n in range(numero_perfecto):
        if 2**(n-1)*((2**n) - 1) == numero_perfecto:
            condicion = True
    return condicion

def prueba():
    
    print('Bienvenido a mi codigo!')
    numero = ingreso_entero('\nIngrese un numero entero para saber si es un numero perfecto:')
    es_perfecto = numero_perfecto(numero)
    print('\n True = Es perfecto\n False = No es perfecto')
    print('\nCondicion: ', es_perfecto)

if __name__ == "__main__":
    prueba()

