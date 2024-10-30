# Exercise 8. Escriba un programa que entregue la parte decimal de un número real ingresado por el usuario.

#Ingrese un numero: 4.5
#0.5
#Ingrese un numero: -1.19
#0.19

number = float(input("Enter a number "))

decimal_part = round(abs(number - int(number)), 3)

print(f"{decimal_part}")
