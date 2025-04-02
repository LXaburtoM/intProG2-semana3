def calcular_imc():

    peso = float(input("Ingrese su peso en kilogramos: "))
    
    altura = float(input("Ingrese su altura en metros: "))
    
    altura_cuadrada = altura ** 2
    
    imc = peso / altura_cuadrada
    
    imc_multiplicado = imc * 100
   
    imc_redondeado = round(imc_multiplicado, 2)
    
    print(f"Peso ingresado: {peso} kg")
    
    print(f"Altura ingresada: {altura} m")
    
    print(f"Valor del IMC calculado: {imc_redondeado}")
   
    if imc < 18.5:
        clasificacion = "Bajo peso"
    elif 18.5 <= imc < 24.9:
        clasificacion = "Peso normal"
    elif 25 <= imc < 29.9:
        clasificacion = "Sobrepeso"
    else:
        clasificacion = "Obesidad"
    
    print(f"Clasificación del IMC: {clasificacion}")

calcular_imc()