while True: 
    num1 = float(input("Digite el numero 1: "))
    num2 = float(input("Digite el numero 2: "))
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    divicion = num1 / num2
    while (num1 >0) and (num2 >0): 
        print("""
              1.Sumar.
              2.Restar.
              3.Multiplicar.
              4.Dividir.
              5.Salir. """)
        menu = float(input("Digite lo que quiere hacer: "))
        if menu == 1:
            print(f"La suma de los dos numeros es de {suma}.")
        elif menu == 2:
            print(f"La resta de los dos numeros es de {resta}.")
        elif menu == 3:
            print(f"La multiplicacion de los dos numeros es de {multiplicacion}.")
        elif menu == 4:
            print(f"La divcion de los dos numeros es de {divicion}.")
        elif menu == 5:
            print("Saliste del programa.")
            break
        else:
            print("Vuelve a intertar.")