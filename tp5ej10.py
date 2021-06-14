################
# Galo Orellana - @OrellanaGalo
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

from tp4ej1 import ingreso_entero

def conversion_binaria(numero):
    
    lista = []
    while numero >= 1:
        if numero % 2 != 0:
            numero = numero - 1
            lista.append(1)
        else:
            lista.append(0)
        numero = numero / 2
    binario = reversed(lista)
    return tuple(binario)

def prueba():
    
    print('Bienvenido a mi codigo')
    numero = ingreso_entero('Ingresa un numero entero')
    resultado = conversion_binaria(numero)
    print(f'{resultado}')

if __name__ == "__main__":
    prueba()

