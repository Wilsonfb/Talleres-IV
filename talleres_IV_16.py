pares = 0 
i = 500
for i in range (5000):
    numero = i %2 == 0
    if numero:
        pares = pares + 1
        i = i + 1
        print("Es par.")
    else:
        print("Es impar.")
        i = i + 1
print(f"La cantidad de numeros pares es de {pares}.")