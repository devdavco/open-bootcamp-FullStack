# Escribe un programa capaz de mostrar todos los números
# impares desde un número de inicio y otro final.
# Por ejemplo: teniendo numero_inicial = 2 
# y numero_final = 8, el programa debe imprimir por consola: [3, 5, 7]

numero_inicial = input("Ingrese número de inicio: ")
numero_final = input("Ingrese número de final: ")
numeros_impares = []

while True:
    if (numero_inicial.isnumeric() and numero_inicial.isnumeric()):
        if (int(numero_inicial) >= int(numero_final)):
            numero_final = input("El número final debe ser mayor que el primer número. Introduce otro: ")
        else:
            for numero in range(int(numero_inicial),int(numero_final)+1):
                if numero % 2 != 0:
                    numeros_impares.append(numero)
            break
    else:
        print("Ingrese solo números")
        numero_inicial = input("Ingrese número de inicio: ")
        numero_final = input("Ingrese número de final: ")

print(numeros_impares)
