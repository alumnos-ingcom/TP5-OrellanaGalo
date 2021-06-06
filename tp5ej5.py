################
# Galo Orellana - @OrellanaGalo
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

def inversion_mayusculas(texto):
    
    cambio = texto.swapcase()
    
    return cambio

def prueba():
    
    print('Bienvenido a mi codigo')
    texto = input('\nIngrese un texto para modificar sus mayusculas por minusculas y visceversa: #')
    inversion = inversion_mayusculas(texto)
    print('\nEste es el texto ingresado: ', texto)
    print('\nEste es el texto convertido: ', inversion)

if __name__ == "__main__":
    prueba()

