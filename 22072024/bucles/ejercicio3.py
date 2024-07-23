'''
nombre:
apellido:
---
TP: Bucles 03
---
Enunciado:

Mostrar la suma de los números desde el 1 hasta el 10.


'''

contador = 0
acumulador = 0

while contador < 10:
    contador += 1
    # acumulador = acumulador + contador
    acumulador += contador
    print(f"vuelta {contador}")
    
print(f"la suma de los numeros del 1 al 10 es {acumulador}")
print("fin del programa")