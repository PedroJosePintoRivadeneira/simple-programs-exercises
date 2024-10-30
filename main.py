#Exercise 5. Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número con los dígitos en orden inverso:

#Ingrese numero: 345
#543
#Ingrese numero: 241
#142

number = int(input("Enter number "))

invert = int(str(number)[::-1])

if 100 <= invert <= 999:
    print(f"{invert}")
else:

    print("Please enter a 3 digit integer")
