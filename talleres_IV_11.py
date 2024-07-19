positivos = 0
negativos = 0
suma = 0
cantidad = int(input("Digite la cantidad de numeros: "))
i = 0
while (i <= cantidad):
    numero = float(input("Digite el numero: "))
    i = i + 1
    if numero <=0:
        negativos = negativos+ 1 
    else:
        positivos = positivos + 1
        suma = suma + numero    
print(f"La suma total de los numero es de {suma}, con {negativos} estos numero negativos y estos numeros {positivos} positivos.")