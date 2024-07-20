# ingreso
#egreso
#variables

#if estructura de control flujo

# edad = int(input("Ingrese la edad 0 y 99: "))

# while(edad < 0 or edad > 99):
#     edad = int(input("Error re Ingrese la edad 0 y 99: "))
    
# print("Sali del while termino la app")
#imprimir desde el 1 al 10
# contador = 0
# while contador < 10 :
#     # contador = contador + 1 # forma larga
#     contador += 1
#     print(contador)
    
#Plato principal elegido ("Pizza", "Hamburguesa", "Ensalada").

plato = input("Ingrese su comida  (p - e - h): ")
plato = plato.lower()
while(plato != "h" and plato != "e" and plato != "p"):
    plato = input("Error re Ingrese su comida  (p - e - h)")
    plato = plato.lower()


print("Sali del while termino la app")