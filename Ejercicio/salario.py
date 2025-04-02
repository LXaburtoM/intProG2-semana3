def calcular_salario_neto():
    salario_bruto = float(input("Ingrese el salario bruto del empleado: "))
    descuentos_totales = (salario_bruto * 0.10) + (salario_bruto * 0.05) + (salario_bruto * 0.03)
    salario_neto = salario_bruto - descuentos_totales
    print(f"Salario Bruto: {salario_bruto:.2f}")
    print(f"Descuentos Totales: {descuentos_totales:.2f}")
    print(f"Salario Neto: {salario_neto:.2f}")

calcular_salario_neto()