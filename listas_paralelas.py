import os

notas_primer_parcial = []
notas_segundo_parcial = []
promedio_notas = []

print("\nPrimer parcial\n")
for nota in range(5):
    nota_ingresada = input("Por favor ingrese la nota: ")

    while nota_ingresada.isalpha() or nota_ingresada == '':
        nota_ingresada = input("Por favor ingrese una nota correcta: ")
    
    nota_ingresada = float(nota_ingresada)

    notas_primer_parcial.append(nota_ingresada)

    print(f"Nota ingresada: {nota_ingresada}")

os.system("cls")
print("Segundo parcial\n")
for nota in range(5):
    nota_ingresada = input("Por favor ingrese la nota: ")

    while nota_ingresada.isalpha() or nota_ingresada == '':
        nota_ingresada = input("Por favor ingrese una nota correcta: ")
    
    nota_ingresada = float(nota_ingresada)

    notas_segundo_parcial.append(nota_ingresada)
    print(f"Nota ingresada: {nota_ingresada}")
os.system("cls")
for nota in range(5):
    promedio = (notas_primer_parcial[nota] + notas_segundo_parcial[nota]) / 2
    promedio_notas.append(promedio)

print("\nPrimer parcial")
for nota in range(len(notas_primer_parcial)):
    print(notas_primer_parcial[nota])
print("\nSegundo parcial")
for nota in range(len(notas_segundo_parcial)):
    print(notas_segundo_parcial[nota])
print("\nPromedios\n")
for promedio in promedio_notas:
    print(promedio)
