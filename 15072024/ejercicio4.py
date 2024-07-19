'''
nombre:
apellido:
---
Ejercicio: entrada_salida_04
---
Enunciado:
Realizar un programa que permita el ingreso de dos números. Realizar la suma de los mismos 
y mostrar el resultado por pantalla con el siguiente formato: “La suma de los dos números es: ___”
'''
#Ingreso de datos
mensaje =  "La suma de los dos números es: "
numero_uno = input("Ingrese el primer numero: ")
numero_dos = input("Ingrese el segundo numero: ")

#Conversion de datos ingresados
numero_uno_int = int(numero_uno)
numero_dos_int = int(numero_dos)

#Procesamiento de la informacion
resultado_suma = numero_uno_int + numero_dos_int

mensaje = mensaje + str(resultado_suma)



#Muestreo de resultado 
print(mensaje)