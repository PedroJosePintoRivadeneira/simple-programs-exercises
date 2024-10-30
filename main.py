# Exercise 2. Escriba un programa que reciba como entrada el radio de un círculo y entregue como salida su perímetro y su área:

#Example:
#Ingrese el radio: 5
#Perimetro: 31.4
#Área: 78.5

#P=2pi*r
#A=pi*r²
#Solution 2

import math

radio = int(input("Enter the radio: "))
perimeter = round(2 * math.pi * radio, 1)
area =  round(math.pi * math.pow(radio, 2), 1)

print(f"""
Perimeter: {perimeter}
Area: {area}""")
