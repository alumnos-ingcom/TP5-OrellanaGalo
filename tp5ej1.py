################
# Galo Orellana - @OrellanaGalo
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

from tp4ej1 import ingreso_entero

def par_e_impar(numero):
    
    if numero & 1:    # Busca la imparidad en los numeros binarios, ya que los impares terminan en 1 y los pares en 0
        return False
    else:
        return True

def prueba():
    
    print('Bienvenido a mi codigo!')
    numero = ingreso_entero('\nPor favor, ingrese un numero entero para saber si es par o impar: ')
    print('\n Par = True\n Impar = False')
    par_o_impar = par_e_impar(numero)
    print('\nLa condicion del numero es:', par_o_impar)

if __name__ == "__main__":
    prueba()

