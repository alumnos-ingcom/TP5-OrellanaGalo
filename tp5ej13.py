################
# Galo Orellana - @OrellanaGalo
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

class SinUbicacion(Exception):
    """Esta es la excepcion para las palabras que no pudieron ser ubicadas"""
    pass

def ubicacion_palabra(texto, palabra):
    
    ubicacion = 0
    letra = 0
    misma_letra = 0
    for i in range(len(texto)):
        if letra < len(palabra) and texto[i] == palabra[letra]:
            if letra == 0:
                ubicacion = i
                letra = letra + 1
                misma_letra = misma_letra + 1
            else:
                misma_letra = misma_letra + 1
                letra = letra + 1
        elif misma_letra == len(palabra) and texto[i] == ' ':
            return ubicacion
        else:
            ubicacion = 0
            letra = 0
            misma_letra = 0
    if misma_letra == len(palabra):
        return ubicacion
    raise SinUbicacion('La palabra que desea encontrar no existe o no pudo ser ubicada.')
    
def prueba():
    
    print('Bienvenido a mi codigo!')
    texto = str(input('\nIngrese el texto que desea comparar: '))
    palabra = str(input('\nPalabra que desee saber su ubicacion y si esta dentro del texto: '))
    ubicacion = ubicacion_palabra(texto, palabra)
    print(f'\nLa palabra esta ubicada en la posicion nro: {ubicacion}.')

if __name__ == "__main__":
    prueba()

