################
# Galo Orellana - @OrellanaGalo
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

from tp4ej1 import ingreso_entero

def calculadora_factorial(numero):
    
    if numero < 0:
        print('No existe')
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
    n_factorion = digito_

def prueba():
    
    numero = ingreso_entero('*')
    resultado = 
    print(f'{resultado}')

if __name__ == "__main__":
    prueba()

