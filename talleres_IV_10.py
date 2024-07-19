valor = int(input("Digite el valor del producto: "))
cantidad = int(input("Digite la cantidad: "))
total = valor * cantidad
total_15 =total*.15
total_35 =total*.35
if total <= 20000:
    total_35 = total *.35
