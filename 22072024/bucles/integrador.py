'''
nombre:
apellido:
---
TP: Bucles integrador
---
Enunciado:

Permitir que el usuario ingrese todos los números que desee. Los mismos deben estar comprendidos entre -10000 y 10000, y deben ser distintos de 0. Determinar:
La suma acumulada de los números negativos.
La suma acumulada de los números positivos.
La cantidad de números negativos ingresados.
El promedio de los números positivos.
El número positivo más grande.
El porcentaje de números negativos ingresados, respecto del total de ingresos.



'''

pregunta = "s"

suma_positivos = 0
suma_negativos = 0
contador_negativos = 0
contador_positivos = 0
max_num_pos = None

while pregunta == "s":
    numero_ingresado = int(input("Ingrese un numero entre -10000 y 10000: "))
    while numero_ingresado < -10000 or numero_ingresado > 10000 or numero_ingresado == 0:
        numero_ingresado = int(input("Error Ingrese un numero entre -10000 y 10000: "))
        
    if(numero_ingresado > 0):
        suma_positivos += numero_ingresado
        contador_positivos += 1
        
        if(max_num_pos == None or numero_ingresado > max_num_pos):
            max_num_pos = numero_ingresado
        
    if(numero_ingresado < 0):
        suma_negativos += numero_ingresado
        contador_negativos += 1    
    
    
    pregunta = input("Quiere seguir ingresando numeros?: ") 


if(contador_positivos > 0):
    promedio_prositivos = suma_positivos / contador_positivos
    
if(max_num_pos != None):
    print(f"el max pos  es {max_num_pos}")
    
total_ingreso = contador_negativos + contador_positivos
porcentaje_negativos = contador_negativos / total_ingreso * 100

print(f"el porcentaje de negativos es {porcentaje_negativos} %")