#TP: Condicionales 07
#Pedirle al usuario su edad, determinar si es mayor (18 años o más), niño/a (menor de 10), 
#pre-adolescente (edad entre 10 y 13 años inclusive) o adolescente (edad entre 13 y 17 años).


edad = input("ingrese su edad: ")
edad = int(edad)

# if(edad < 10):
#     mensaje = "niño" 
# else:
#     if(edad < 14):
#         mensaje = "pre adolescente"
#     else:
#         #tiene 14 o mas
#         if(edad < 18):
#             mensaje = "adolescente"
#         else:
#             mensaje = "Mayor"

if(edad > 17):
    mensaje ="Mayor"
else:
    if(edad > 12):
        mensaje ="Adolescente"
    else:
        if(edad > 10):
            mensaje = "pre adolescente"
        else:
            mensaje = "niño"
    

print(mensaje)
        