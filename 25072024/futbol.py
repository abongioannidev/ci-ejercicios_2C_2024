'''

Para una tienda de deportes se necesita un programa que permita ingresar los datos de los jugadores de fútbol que han comprado una camiseta, 
hasta que el cliente quiera. 
Por cada jugador, se ingresa:

Nombre del jugador
Equipo al que pertenece (validar "Barcelona", "Real Madrid", "Bayern Munich").
Posición en el campo (validar "delantero", "defensa", "portero").
Edad (entre 18 y 40),
Precio de la camiseta (mas de 5 digitos, sin ceros a la izquierda).


Precio de la camiseta (mas de 5 digitos, si ceros a la izquierda).
Se pide informar por print
1- El porcentaje de camisetas vendidas por equipo [Barcelona: 40%, Real Madrid: 40%, Bayer Munich: 20%] la suma debe dar 100%.
2- El importe total recaudado por la venta de camisetas.
3- Promedio de edad de los jugadores que compraron camisetas.
4- Nombre, equipo y posición del jugador más longevo.
'''

pregunta = "s"
contador_real = 0
contador_barza = 0
contador_bayer = 0
acumulador_precios = 0
acumulador_edades = 0

edad_maxima = None
nombre_max_edad = ""
equipo_max_edad = ""
posicion_max_edad = ""


while pregunta == "s":
    
    
    #aca empiezo a pedir datos
    nombre = input("Ingrese el nombre del jugador: ")
    
    equipo = input("Ingrese el equipo al que pertenece (barcelona real bayer): ")
    
    while equipo != "barcelona" and equipo != "real" and equipo != "bayer":
        equipo = input("Error, Ingrese el equipo al que pertenece (barcelona real bayer): ")
    
    posicion = input("Ingrese la posicion en el campo (delantero, defensa, portero): ")
    
    while posicion != "defensa" and posicion != "delantero" and posicion != "portero":
         posicion = input("Error, Ingrese la posicion en el campo (delantero, defensa, portero): ")
    
    edad = int(input("Ingrese la edad del jugador: "))
    
    while edad < 18 or edad > 40:
        edad = int(input("Error, Ingrese la edad del jugador: "))
        
    precio_camiseta = float(input("Ingrese el precio de la camiseta: "))
    
    while precio_camiseta < 10_000:
        precio_camiseta = float(input("Error, Ingrese el precio de la camiseta: "))
        
    
    
    if equipo == "real":
        contador_real = contador_real + 1
    else:
        if equipo == "barcelona":
            contador_barza = contador_barza + 1
        else:
            contador_bayer = contador_bayer + 1
    
    acumulador_precios = acumulador_precios + precio_camiseta  
    
    acumulador_edades = acumulador_edades + edad
    
    
    if(edad_maxima == None or edad > edad_maxima):
        edad_maxima = edad
        nombre_max_edad = nombre
        equipo_max_edad = equipo
        posicion_max_edad = posicion
    
    #esta mallll lo de abajo
    
    # if equipo == "real":
    #     contador_real = contador_real + 1
        
    # if equipo == "barcelona":
    #     contador_barza = contador_barza + 1
        
    # if equipo == "bayer":
    #     contador_bayer = contador_bayer + 1
        
    
    pregunta = input("Quiere seguir ingresando datos? (s o n): ") #es lo ultimo
#estoy fuera del while principal, hago calculos que no necesito mientras el usuario ingresa informacion

total_ventas = contador_real + contador_barza + contador_bayer

porcentaje_barza = contador_barza / total_ventas * 100
porcentaje_bayer = contador_bayer / total_ventas * 100
porcentaje_real = contador_real / total_ventas * 100


promedio_edades = acumulador_edades / total_ventas

print(f"[Barcelona: {porcentaje_barza}%, Real Madrid: {porcentaje_real}%, Bayer Munich: {porcentaje_bayer}%]")
print(f"El importe total recaudado es {acumulador_precios}")
print(f"El nombre de la persona mas longeva es {nombre_max_edad}\nEl equipo es {equipo_max_edad}\nLa pos es {posicion_max_edad}\n y su edad es {edad_maxima}")

# print(f'''
#       El nombre de la persona mas longeva es {nombre_max_edad}
#       El equipo es {equipo_max_edad}
#       La pos es {posicion_max_edad} 
#       y su edad es {edad_maxima}
# ''')