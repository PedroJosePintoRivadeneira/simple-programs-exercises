# Exercise 3. Escriba un programa que calcule el promedio de 4 notas ingresadas por el usuario:

#Primera nota: 55
#Segunda nota: 71
#Tercera nota: 46
#Cuarta nota: 87
#El promedio es: 64.75

data_1 = int(input("First note "))
data_2 = int(input("Second note "))
data_3 = int(input("Third note "))
data_4 = int(input("Fourth note "))

sum = (data_1 + data_2 + data_3 + data_4)
amount = 4
average = sum / amount

print(f"The average is: {average}")
