mayores = 0
cantidad = int(input("Digite la cantidad de personas: "))
i = 0
while i in range (cantidad):
    edad = int(input("Digite la edad de la persona: "))
    i = i + 1
    if edad >=69:
        mayores = mayores + 1
        print("La persona es mayor de edad.")
    else:
        print("La persona no es mayor de edad.")
print(f"La cantidad de personas mayores es de {mayores}.")