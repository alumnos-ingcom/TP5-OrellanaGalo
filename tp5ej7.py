################
# Galo Orellana - @OrellanaGalo
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

from tp4ej1 import ingreso_entero

def distancia_numeros(n1, n2):
    
    if n1 > n2:
        resultado = n1 - n2
    else:
        resultado = n2 - n1
    
    return resultado

def prueba():
    
    print('Bienvenido a mi codigo!')
    print('\nIngrese dos valores para saber la distancia estre ellos.')
    ingreso_uno = ingreso_entero('\n   Ingrese el primer valor: ')
    ingreso_dos = ingreso_entero('\n   Ingrese el segundo valor: ')
    distancia = distancia_numeros(ingreso_uno, ingreso_dos)
    print('\nLa distancia entre las dos variables es: ', distancia)

if __name__ == "__main__":
    prueba()

