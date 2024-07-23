'''
nombre:
apellido:
---
TP: Bucles 08
---
Enunciado:

Ingresar 10 números enteros. Determinar el máximo y el mínimo.

'''

contador = 0
cantidad_numeros = 4
numero_max_ingresado = None
numero_min_ingresado = None

    # contador = contador + 1
while contador < cantidad_numeros :
    contador += 1
    numero_ingresado = int(input("Ingrese un numero: "))
    
    if(numero_max_ingresado == None or  numero_ingresado > numero_max_ingresado):
        numero_max_ingresado = numero_ingresado
        
    if(numero_min_ingresado == None or  numero_ingresado < numero_min_ingresado):
        numero_min_ingresado = numero_ingresado


print(f"el numero maximo es {numero_max_ingresado}")
print(f"el numero minimo es {numero_min_ingresado}")