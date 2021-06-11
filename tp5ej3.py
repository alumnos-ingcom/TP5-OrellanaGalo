################
# Galo Orellana - @OrellanaGalo
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

from tp4ej1 import ingreso_entero

def tribonacci(n):
    
    if n > 3:
        
        num1 = 1
        num2 = 1
        num3 = 1
        sucesion = []
        
        for i in range(n):
            total = num1 + num2 + num3
            num1 = num2
            num2 = num3
            num3 = total         
            sucesion.append(total - num1 - num2) 
        return sucesion
    else:
        return 1
def prueba():
    
    print('Bienvenido a mi codigo')
    numero = ingreso_entero('\nIngrese un numero entero para establecer su posicion en la tabla de tribonacci:')
    sucesion_tribonacci = tribonacci(numero)
    print('\nTermino:', sucesion_tribonacci)

if __name__ == "__main__":
    prueba()

