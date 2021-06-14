################
# Galo Orellana - @OrellanaGalo
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

from tp4ej1 import ingreso_entero

def construccion_lista():
    lista=[]
    for i in range(5):
        numero = ingreso_entero("Ingrese un valor para sumarlo a la lista")
        lista.append(numero)
    return lista

def comparacion(primera_lista, segunda_lista):
    
    mismo_elemento = 0
    for i in primera_lista:
        for i in segunda_lista:
            mismo_elemento = mismo_elemento + 1
    return mismo_elemento >= len(primera_lista)

def prueba():
    
    print('Bienvenido a mi codigo!')
    
    print('\nIngrese 2 listas para comparar sus similitudes')
    print('\nPrimer lista: ')
    primera_lista = construccion_lista()
    print('\nSegunda lista: ')
    segunda_lista = construccion_lista()
    busqueda = comparacion(primera_lista, segunda_lista)
    print(f'\n Similitudes encontradas: {busqueda}')

if __name__ == "__main__":
    prueba()

