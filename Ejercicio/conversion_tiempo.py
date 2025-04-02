def convertir_segundos():

    total_segundos = int(input("Ingrese la cantidad total de segundos: "))
   
    horas = total_segundos // 3600  
    
    segundos_horas = horas * 3600
    
    segundos_restantes = total_segundos - segundos_horas
    
    minutos = segundos_restantes // 60  
    
    segundos_minutos = minutos * 60
    
    segundos_finales = segundos_restantes - segundos_minutos
    
    print(f"{horas} horas, {minutos} minutos y {segundos_finales} segundos.")

convertir_segundos()