promedio = 0
i = 0
while i <= 15:
    nota =int(input("Digite la nota: "))
    i = i + 1
    promedio = promedio + nota 
nota_final = promedio / 15
if nota_final >= 40:
    print(f"Paso la materia con {nota_final}.")
else:
    print(f"Perdio la materia con {nota_final}.")