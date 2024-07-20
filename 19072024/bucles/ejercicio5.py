'''
nombre:
apellido:
---
TP: Bucles 05
---
Enunciado:

Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. Mostrar por pantalla.


'''
cantidad_ingresos = 0
suma_numeros_ingresados = 0
# intentos =int(input("Cuantos numeros quiere ingresar?: "))
intentos =10
while(cantidad_ingresos < intentos):
    cantidad_ingresos +=1 #contador
    numero = int(input(f"Ingrese el numero {cantidad_ingresos} :"))
    suma_numeros_ingresados = suma_numeros_ingresados + numero

promedio = suma_numeros_ingresados / cantidad_ingresos



print(suma_numeros_ingresados)
print(f"El promedio es {promedio}")