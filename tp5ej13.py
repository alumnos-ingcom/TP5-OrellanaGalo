################
# Galo Orellana - @OrellanaGalo
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

def construccion_texto(mensaje):
    
    texto = []
    for i in range(1):
        palabra = str(input(mensaje + '-'))
        texto.append(palabra)
    return texto

def ubicacion_palabra(texto, palabra):
    
    contador = 0
    misma_palabra = 0
    for i in texto:
        for i in palabra:
            return misma_palabra == misma_palabra + 1
    
def prueba():
    
    print('Bienvenido a mi codigo!')
    texto = construccion_texto('\nIngrese el texto que desea comparar: ')
    palabra = str(input('\nPalabra que desee saber su ubicacion y si esta dentro del texto: '))
    ubicacion = ubicacion_palabra(texto, palabra)
    print(f'\nLa palabra esta ubicadad en la posicion nro: {ubicacion}.')

if __name__ == "__main__":
    prueba()

