################
# Galo Orellana - @OrellanaGalo
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

from tp4ej1 import ingreso_entero

def fibonacci(n):
    
    if n > 2:
        
        num1 = 0
        num2 = 1
        
        sucesion = []
        
        for i in range(n):
            
            total = num1 + num2
            num1 = num2
            num2 = total
            sucesion.append(total - num1)
            
        return sucesion
    else:
        return 1 

def prueba():
    
    print('Bienvenido a mi codigo!')
    numero = ingreso_entero('\nIngrese un numero n para determinar su posicion en la sucesion de Fibonacci:')
    sucesion_fibonacci = fibonacci(numero)
    print('\nTermino: ', sucesion_fibonacci)


if __name__ == "__main__":
    prueba()

