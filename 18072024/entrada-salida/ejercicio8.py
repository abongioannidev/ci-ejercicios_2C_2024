'''
nombre:
apellido:
---
Ejercicio: entrada_salida_08
---
Enunciado:
Realizar un programa que a partir del ingreso de un sueldo y de un porcentaje de aumento, calcule y muestre el sueldo con el aumento porcentual ingresado por el usuario.
'''


sueldo_ingresado_str = input("ingrese el sueldo del empleado: ")
sueldo_float = float(sueldo_ingresado_str)

porcentaje = input("ingrese el porcentaje a incrementar: ")
porcentaje = float(porcentaje)

valor_variable = sueldo_float * porcentaje/100
sueldo_final = sueldo_float + valor_variable

print(f"el sueldo ingresado es {sueldo_float}")
print(f"el valor a incrementar es {valor_variable:.3f}")
print("el sueldo final con incremento es  {:.2f}".format(sueldo_final))