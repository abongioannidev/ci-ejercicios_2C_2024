'''
nombre:
apellido:
---
TP: Bucles 04
---
Enunciado:

Mostrar la suma de los números pares desde el 1 hasta el 10.


'''

contador = 0
acumulador_pares = 0

while contador < 10:
    contador += 1
    resto = contador % 2
    if(resto == 0):
        acumulador_pares = acumulador_pares + contador

    
    
print(f"la suma de los numeros pares es {acumulador_pares}")
print("fin del la app")
    