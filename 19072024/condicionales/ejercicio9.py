'''
nombre:
apellido:
---
TP: Condicionales 09
---
Enunciado:

Los argentinos nativos y por opción desde los dieciséis (16) años y los argentinos naturalizados desde los dieciocho (18) años están habilitados a votar. 
A partir del ingreso de la edad del usuario y el estado (si es naturalizado o nativo), 
se deberá informar si es o no posible que la persona concurra a votar en base a la información suministrada.

'''

edad = int(input("Ingrese la edad de la persona: "))
# estado = input("INgrese el estado de la persona ('na' para naturalizado o 'nt' para nativo): ")
# mensaje = "No puede votar"

if(edad < 0 or edad > 99):
    print("edad invalida")
    

# if(edad > 18) or (estado == "nt" and edad > 16):
#     mensaje = "Puede votar"
    


    

    

# print(mensaje)