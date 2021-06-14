################
# Galo Orellana - @OrellanaGalo
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

from tp4ej1 import ingreso_entero

class MenorACero (Exception):
    """Esta es la excepcion para los enteros menores a cero"""
    pass

def calculadora_factorial(numero):
    
    if numero < 0:
        raise MenorACero('No existen enteros exponenciables menores a cero')
    elif numero == 0:
        return 1
    else:
        factorial = 1
        while (numero > 1):
            factorial *= numero
            numero -= 1
        return factorial

def lista_factoriales():
    
    contador = 1
    lista_factoriales = []
    lista_factoriales.append(1)
    
    for i in range(1, 10):
        contador = contador * i
        lista_factoriales.append(contador)
    return lista_factoriales

def factoriones():
    pass

def prueba():
    
    numero = ingreso_entero('*')
    resultado = calculadora_factorial(numero)
    print(f'{resultado}')

if __name__ == "__main__":
    prueba()

