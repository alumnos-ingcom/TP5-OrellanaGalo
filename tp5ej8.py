################
# Galo Orellana - @OrellanaGalo
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

class NoCiclo(Exception):
    """Esta es la excepcion para los errores dentro del ciclo"""
    pass

def ciclo(posicion_inicial, rotacion, minimo, maximo):
    if rotacion > rotacion or rotacion *-1 > maximo:
        rotacion = rotacion - maximo*(rotacion//maximo)
    posicion_final = posicion_inicial + rotacion
    if rotacion > 0:
        while posicion_final >= maximo:
            posicion_final = posicion_final - maximo
    elif rotacion == 0:
        raise NoCiclo('La rotacion debe ser distinta de cero.')
    else:
        while posicion_final < minimo:
            posicion_final = maximo + posicion_final
    return posicion_final

def encontrar_elemento(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    pass

def codigo_cesar(texto, rotacion):
    
    abecedario = ('aábcdeéfghiíjklmnoópqrstuúvwxyz'
                'AÁBCDEÉFGHIÍJKLMNOÓPQRSTUÚVWXYZ'
                '0123456789 ')
    codificado = list()
    for letra in texto:
        posicion_inicial = encontrar_elemento(abecedario, letra)
        codex = ciclo(posicion_inicial, rotacion, 0, len(abecedario))
        codificado.append(abecedario[codex])
    return ''.join(codificado)


def codigont_cesar(texto, rotacion):
    return codigo_cesar(texto, -rotacion)

def prueba():
    
    print('Bienvenido a mi codigo!')
    texto = input('Ingrese el texto que desea convertir al codigo cesar: ')
    rotacion = int(input('Ingrese la cantidad de rotaciones que desea que el cifrado haga: '))
    conversion = codigo_cesar(texto, rotacion)
    des_conversion = codigont_cesar(conversion, rotacion)
    print(f'El texto cifrado a Cesar es: {conversion}')
    print(f"La frase cifradan't es: {des_conversion}")

if __name__ == "__main__":
    prueba()

