
def convertir_dolares():
    
    cantidad_dolares = float(input("Ingrese la cantidad en dólares: "))
    
    tasa_cambio_euros = 0.85  
    
    tasa_cambio_libras = 0.75  
    
    tasa_cambio_yenes = 110.0  
    
    cantidad_euros = cantidad_dolares * tasa_cambio_euros
    
    cantidad_libras = cantidad_dolares * tasa_cambio_libras
   
    cantidad_yenes = cantidad_dolares * tasa_cambio_yenes
    
    print(f"Cantidad en dólares: {cantidad_dolares:.2f} $")
    
    print(f"Cantidad convertida en euros: {cantidad_euros:.2f} €")
    print(f"Cantidad convertida en libras: {cantidad_libras:.2f} £")
    print(f"Cantidad convertida en yenes: {cantidad_yenes:.2f} ¥")


convertir_dolares()