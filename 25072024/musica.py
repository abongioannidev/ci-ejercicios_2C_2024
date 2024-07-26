'''
Para una escuela de música se necesita un programa que permita ingresar los datos de los estudiantes, hasta que el cliente quiera. Por cada estudiante, 
se ingresa:
A- Nombre completo
B- Instrumento que toca (validar "guitarra", "piano", "batería").
C- Edad (entre 7 y 18),
D- Horas de estudio por semana (más de 0 y menos de 57),
E- Precio por clase (desde 200 hasta 500).

Se pide informar por print: 


1- El estudiante con más horas de estudio por semana de batería. 
2- El promedio recaudado por actividad (guitarra, piano, batería). 
3- Cantidad de estudiantes que tocan piano y tienen más de 12 años. 
4- La actividad que posee menos estudiantes.
5- Nombre completo e instrumento del estudiante más joven.

'''


pregunta = "s"
max_horas_bateria = None
contador_bateria = 0
contador_piano = 0
contador_guitarra = 0

acumulador_bateria = 0
acumulador_piano = 0
acumulador_guitarra = 0

contador_estudiantes_piano_doce = 0

min_edad_estudiante = None


while pregunta == "s":
    
    nombre = input("Ingrese un nombre: ")
    
    instrumento = input("Ingrese el instrumento (bateria, piano guitarra): ")
    
    while instrumento != "bateria" and instrumento != "piano" and instrumento != "guitarra":
        instrumento = input("Error, Ingrese el instrumento (bateria, piano guitarra): ")
    
    edad = int(input("Ingrese la edad: "))
    
    while edad < 7 or edad > 18:
        edad = int(input("Error, Ingrese la edad: "))
        
        
    horas_estudio = int(input("Ingrese la horas: "))
    
    while horas_estudio < 1 or horas_estudio > 56:
        horas_estudio = int(input("Error, Ingrese la horas: "))
        
    precio_clase = int(input("Ingrese el precio de la clase: "))
    
    while precio_clase < 200 or precio_clase > 500:
        precio_clase = int(input("Error, Ingrese el precio de la clase: "))
        
        
        
    if(instrumento == "bateria"):
        
        #punto 1
        if(max_horas_bateria == None or horas_estudio > max_horas_bateria):
            max_horas_bateria = horas_estudio 
            nombre_max_horas_bateria = nombre
    
        contador_bateria = contador_bateria + 1
        acumulador_bateria = acumulador_bateria + precio_clase
    else:
        #escribo aca
        if instrumento == "guitarra":
            contador_guitarra += 1
            acumulador_guitarra += precio_clase   
        else:
            contador_piano += 1
            acumulador_piano += precio_clase
            
            if(edad > 12):
                contador_estudiantes_piano_doce += 1
        
    if(min_edad_estudiante == None or edad < min_edad_estudiante):
        min_edad_estudiante = edad
        nombre_min_edad = nombre
        instrumento_min_edad = instrumento
    
    pregunta= input("Quiere seguir ingresando informacion (s o n)?: ")
    
if(max_horas_bateria != None):
    print(f"El estudiante con mas horas de estudio es {nombre_max_horas_bateria} sus horas son {max_horas_bateria}")


#promedios del punto 2
if(contador_guitarra > 0):
    promedio_guitarra = acumulador_guitarra / contador_guitarra
    print(f"el promedio de las guitarras es {promedio_guitarra:.2f}")
    
if(contador_bateria > 0):
    
    promedio_bateria = acumulador_bateria / contador_bateria
    print(f"el promedio de las bateria es {promedio_bateria:.2f}")
    
if(contador_piano > 0):
    promedio_piano = acumulador_piano / contador_piano
    print(f"el promedio de las piano es {promedio_piano:.2f}")
    
print(f"la cantidad de estudiantes que tocan piano y tiene mas de 12 son {contador_estudiantes_piano_doce}")


if(contador_piano < contador_bateria and contador_piano < contador_guitarra):
    print("el que menos estudiantes tiene es piano")
elif(contador_bateria < contador_guitarra):
    print("el que menos estudiantes tiene es bateria")
else:
    print("el que menos estudiantes tiene es guitarra")
    
    
    
if(min_edad_estudiante != None):
    print(f"La edad del estudiante mas joven es {min_edad_estudiante}, su nombre {nombre_min_edad}, instrumento {instrumento_min_edad}")
