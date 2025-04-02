temp_fah=float(input("Ingrese la temperatura en Fahrenheit: "))
temp_cel=temp_fah-32
temp_cel=temp_cel*5
temp_cel=temp_cel/9
temp_kel=temp_cel+273.15
print( f"grados celsius {temp_cel:.2f}")
print(f"La temperatura en Kelvin {temp_kel:.2f}")