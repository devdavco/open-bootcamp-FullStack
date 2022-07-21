# Escribe un programa que sea capaz de mostrar los números del 1 al 100 en orden inverso.
numeros = []

for numero in range (1,101):
    numeros.append(numero)

print(sorted(numeros,reverse=True))


print("-----Other way-----")

# Escribe un programa que sea capaz de mostrar los números del 1 al 100 en orden inverso.
numeros = range (1,101)

print(sorted(numeros,reverse=True))
