#Exercise 4. Escriba un programa que convierta de centímetros a pulgadas. Una pulgada es igual a 2.54 centímetros.

#Ingrese longitud: 45
#45 cm = 17.7165 in
#Ingrese longitud: 13
#13 cm = 5.1181 in

# pulgada = centimetros / 2.54

length = float(input("Enter length "))

inch = float(length/2.54)
inch_2 = round(inch, 4)

print(f"""
{length} = {inch_2}
""")
