################
# Galo Orellana - @OrellanaGalo
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

def parentesis_balanceado(ingreso_cadena):
    
    apertura = 0
    
    balanceado = True
    
    for cadena in ingreso_cadena:
        if apertura >= 0:
            if cadena == '[' or cadena == '{' or cadena == '(':
                apertura = apertura + 1
            elif cadena == ']' or cadena == '}' or cadena == ')':
                apertura = apertura - 1
        elif apertura < 0:
            balanceado = False
    if apertura > 0:
        balanceado = False
    return balanceado
    
def prueba():
    
    print('Bienvenido a mi codigo!')
    ingreso = input('\nIngrese su cadena de parentesis # ')
    condicion = parentesis_balanceado(ingreso)
    if condicion == True:
        print(f'{ingreso} - OK')
    else:
        print(f'{ingreso} - NO OK')
    
if __name__ == "__main__":
    prueba()

