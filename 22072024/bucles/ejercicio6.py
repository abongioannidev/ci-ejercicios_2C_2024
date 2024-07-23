'''
nombre:
apellido:
---
TP: Bucles 06
---
Enunciado:
Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números ingresados y el promedio de los mismos.

'''

pregunta = "s"
acumula_ingreso = 0
contador = 0

while pregunta == "s":
    numero_ingresado = int(input("ingrese un numero: "))
    
    acumula_ingreso += numero_ingresado
    contador += 1
    
    pregunta = input("Quiere seguir ingresando numeros? (s o n): ")

promedio = acumula_ingreso / contador   
print(f"el promedio de los numeros ingresados es {promedio}")
    
print(f"la suma de los numeros ingresados es {acumula_ingreso}")
print("fin del programa")