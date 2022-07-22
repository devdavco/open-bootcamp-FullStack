def num_primo():
    numero = int(input("Ingrese un número entero: "))
    if numero > 1:
        for x in range(2,numero):
            if numero % x == 0:
                return f"Número {numero} no es Primo"
            else:
                return f"Número {numero} es 7Primo"
    else:
        return "Número debe ser mayor a cero"




print(num_primo())
