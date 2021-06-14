################
# Galo Orellana - @OrellanaGalo
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

from tp4ej1 import ingreso_entero

def es_capicua(numero):
    
    if numero >= 0:
        return str(numero) == str(numero)[::-1]
    else:
        return False

def prueba():
    
    print('Bienvenido a mi codigo!')
    numero = ingreso_entero('\n Ingrese numero/s para saber si son capicua o no: ')
    capicua = es_capicua(numero)
    print(f'\n Condicion: ', capicua)

if __name__ == "__main__":
    prueba()

