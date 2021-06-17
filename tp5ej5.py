################
# Galo Orellana - @OrellanaGalo
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

def inversion_mayusculas(texto):
    
    lista = []
    for i in texto:
        if i.isupper():
            mayuscula_unicode = ord(i)
            inversion = mayuscula_unicode + 32
            letra_nueva = chr(inversion)
            lista.append(letra_nueva)
        elif i.islower():
            minuscula_unicode = ord(i)
            inversion = minuscula_unicode - 32
            letra_nueva = chr(inversion)
            lista.append(letra_nueva)
    str1 = " "
    return (str1.join(lista))

def prueba():
    
    print('Bienvenido a mi codigo')
    texto = input('\nIngrese un texto para modificar sus mayusculas por minusculas y visceversa: #')
    inversion = inversion_mayusculas(texto)
    print('\nEste es el texto ingresado: ', texto)
    print('\nEste es el texto convertido: ', inversion)

if __name__ == "__main__":
    prueba()

