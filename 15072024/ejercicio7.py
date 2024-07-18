'''
nombre:
apellido:
---
Ejercicio: entrada_salida_07
---
Enunciado:
Realizar un programa que a partir del ingreso de un sueldo (valor flotante) muestre dicho valor con un incremento del 15%.
'''

PORCENTAJE = 15
sueldo_ingresado_str = input("ingrese el sueldo del empleado: ")
sueldo_float = float(sueldo_ingresado_str)

valor_variable = sueldo_float * PORCENTAJE/100
sueldo_final = sueldo_float + valor_variable

print(f"el sueldo ingresado es {sueldo_float}")
print(f"el valor a incrementar es {valor_variable}")
print(f"el sueldo final con incremento es  {sueldo_final}")
