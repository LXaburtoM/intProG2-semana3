def calcular_tiempo_pelicula():
    
    duracion_pelicula = float(input("Ingrese la duración de la película en minutos: "))
    
    duracion_comerciales_previos = float(input("Ingrese la duración de los comerciales previos en minutos: "))
    
    cantidad_pausas = int(input("Ingrese la cantidad de pausas comerciales durante la película: "))
    
    duracion_pausa = float(input("Ingrese la duración de cada pausa comercial en minutos: "))
    
    total_comerciales_durante_pelicula = cantidad_pausas * duracion_pausa
    
    duracion_con_comerciales_previos = duracion_pelicula + duracion_comerciales_previos
    
    duracion_total = duracion_con_comerciales_previos + total_comerciales_durante_pelicula
    
    print(f"Duración original de la película: {duracion_pelicula:.2f} minutos")
    
    duracion_comerciales_totales = duracion_comerciales_previos + total_comerciales_durante_pelicula
    print(f"Duración total de los comerciales: {duracion_comerciales_totales:.2f} minutos")
    
    print(f"Tiempo total de la proyección: {duracion_total:.2f} minutos")


calcular_tiempo_pelicula()