'''
nombre:
apellido:
---
TP: Ferrete_lamparas
---
Enunciado:

En una ferretería se quiere implementar un sistema que permita a los usuarios saber cuánto deberán pagar por la compra de lámparas de bajo consumo. 
Se tiene en cuenta que todas las lámparas cuestan $800.
A partir de la cantidad y marca de las lámparas compradas (solo se puede comprar una marca por vez) se aplicará el siguiente descuento:
1-Si compra 6 o más  lámparas bajo consumo tiene un descuento del 50%. 
2-Si compra 5  lámparas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
3-Si compra 4  lámparas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
4-Si compra 3  lámparas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
5-Por otro lado, si el importe final con descuento suma más de $4000  se obtiene un descuento adicional de 5%.
Mostrar por pantalla: 
Marca, cantidad de lámparas, total a pagar sin descuento, el descuento obtenido si corresponde, el descuento adicional (si corresponde) y el total a pagar con descuento.

'''

COSTO_BASE = 800
porcentaje = 0
cantidad_lamparas = int(input("Ingrese la cantidad de lamparas a comprar: "))
marca = input("Ingrese la marca (ArgentinaLuz - FelipeLamparas - Osram - Philips): ")

precio_bruto = cantidad_lamparas * COSTO_BASE


if(cantidad_lamparas > 5):
    porcentaje = 50
else:
    #cant => 5 4 3 2 1 infinito negativo
    if(cantidad_lamparas > 4):
        # 5
        if(marca == "ArgentinaLuz"):
            porcentaje = 40
        else:
            porcentaje = 30
    else:
        # cant => 4 3 2 1 infinito negativo
        if( cantidad_lamparas > 3):
            #4
            if(marca == "ArgentinaLuz" or marca == "FelipeLamparas"):
                porcentaje = 25
            else:
                porcentaje = 20
        else:
            # cant => 3 2 1 infinito negativo
            if(cantidad_lamparas > 2):
                porcentaje = 5
                if(marca == "ArgentinaLuz"):
                    porcentaje = 15
                else:
                    if(marca == "FelipeLamparas"):
                        porcentaje = 10
                          

importe_a_descontar = precio_bruto * porcentaje /100
precio_final = precio_bruto - importe_a_descontar

if(precio_final > 4000):
    importe_a_descontar = precio_final * 5 /100
    precio_final = precio_final - importe_a_descontar
    print("Ademas tuviste un descuento del 5% como beneficio")
    



print(f"Ustes compro {cantidad_lamparas} de {marca} tiene un descuento del {porcentaje} %\nSu precio final es {precio_final}")






