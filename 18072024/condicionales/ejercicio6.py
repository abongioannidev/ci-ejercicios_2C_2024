'''
nombre:
apellido:
---
TP: Condicionales 06
---
Enunciado:

Pedirle al usuario su edad, determinar si el usuario NO es adolescente.


'''


edad = int(input("Ingrese la edad del usuario: "))


if(edad < 13 or edad > 18):
    print("el usuario NO es adolescente")

