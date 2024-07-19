nota1 = int(input('Ingrese la nota numero 1: ')) 
nota2 = int(input('Ingrese la nota numero 2: ')) 
nota3 = int(input('Ingrese la nota numero 3: ')) 
nombre = input('Digite el nombre del estudiante:') 
materia = input('Nombre de la materia : ') 
promedio = (nota1 + nota2 + nota3) / 3
if promedio <40:
    print(f"Aprobo con {promedio}.")
else:
    print(f"No aprobo co {promedio}.")
print(f"El nombre del estudiante es {nombre} y la materia es {materia}.")