#Exercise 9. Un alumno desea saber que nota necesita en el tercer certamen para aprobar un ramo.
#El promedio del ramo se calcula con la siguiente formula.

#NC=(C1+C2+C3)3
#NF=NC⋅0.7+NL⋅0.3
#Donde NC
# es el promedio de certámenes, NL
# el promedio de laboratorio y NF
# la nota final.

#Escriba un programa que pregunte al usuario las notas de los dos primeros certamen y la nota de laboratorio, y muestre la nota que necesita el alumno para aprobar el ramo con nota final 60.

#Ingrese nota certamen 1: 45
#Ingrese nota certamen 2: 55
#Ingrese nota laboratorio: 65
#Necesita nota 72 en el certamen 3

contest_1 = float(input("Enter contest note 1 "))
contest_2 = float(input("Enter contest note 2 "))
laboratory_note = float(input("Enter laboratory note "))

desired_note = 60

contest_3 = ((desired_note - laboratory_note * 0.3) / 0.7) * 3 - contest_1 - contest_2

print(f"""
Need note {round(contest_3, 1)} in the contest
""")
