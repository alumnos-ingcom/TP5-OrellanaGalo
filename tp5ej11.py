################
# Galo Orellana - @OrellanaGalo
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

def promedio_movil(lista, cantidad_valores):
    
    promedio_movil = []
    valor = round(len(lista)/cantidad_valores)
    ubicacion_valor = 1
    suma = 0
    contador = 0
    
    for i in lista:
        if contador < cantidad_valores:
            suma = suma + i
            contador = contador + 1
        else:
            promedio_movil.append(suma/cantidad_valores)
            contador = 1
            suma = i
        if contador == cantidad_valores:
            ubicacion_valor = ubicacion_valor + 1
    if ubicacion_valor == valor:
        promedio_movil.append(suma/cantidad_valores)
    return promedio_movil

def prueba():
    
    print('Bienvenido a mi codigo!')
    print('\nEl programa calcula el promedio movil de una lista previamente ingresada.')
    resultado = promedio_movil([1, 2, 4, 5, 8, 9, 10, 12], 3)
    print('\nEl promedio movil de la lista ingresada es: ', resultado)

if __name__ == "__main__":
    prueba()

