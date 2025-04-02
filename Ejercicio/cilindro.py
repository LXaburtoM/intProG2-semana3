import math

def calcular_volumen_area_cilindro():
    
    radio = float(input("Ingrese el radio del cilindro: "))
    
    altura = float(input("Ingrese la altura del cilindro: "))
    
    area_base = math.pi * (radio ** 2)
    
    volumen_cilindro = area_base * altura
    
    area_lateral = 2 * math.pi * radio * altura
    
    area_superficial = area_lateral + (2 * area_base)
    
    print(f"Radio ingresado: {radio:.2f} unidades")
    print(f"Altura ingresada: {altura:.2f} unidades")
    
    print(f"Volumen del cilindro: {volumen_cilindro:.2f} unidades cúbicas")

    print(f"Área superficial del cilindro: {area_superficial:.2f} unidades cuadradas")

calcular_volumen_area_cilindro()