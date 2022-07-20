# Escribe un programa capaz de mostrar todos los números
# impares desde un número de inicio y otro final.
# Por ejemplo: teniendo numero_inicial = 2 
# y numero_final = 8, el programa debe imprimir por consola: [3, 5, 7]

numero_inicial = input("Ingrese número de inicio: ")
numero_final = input("Ingrese número de final: ")
numeros_impares = []

while True:
    if (numero_inicial.isnumeric() and numero_inicial.isnumeric()) and (int(numero_inicial) < int(numero_final)):
        for numero in range(int(numero_inicial),int(numero_final)+1):
            if numero % 2 != 0:
                numeros_impares.append(numero)
        break
    else:
        print("Ingrese los números correctamente")
        numero_inicial = input("Ingrese número de inicio: ")
        numero_final = input("Ingrese número de final: ")


print(numeros_impares)