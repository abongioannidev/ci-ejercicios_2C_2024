'''
nombre:
apellido:
---
TP: Condicionales 02
---
Enunciado:

A partir del ingreso de una edad, determinar si la persona es mayor de edad. Si es mayor o igual que 18 se mostrará el mensaje “UD ES MAYOR DE EDAD”.


'''

#_ ingreso edad del user
edad = int(input("Ingrese su edad: "))

if edad > 17: # 18, 19 , 20 , 21 ,22,etc
    print('UD ES MAYOR DE EDAD')