# Escribe un programa que pregunte al usuario su edad 
# y muestre por pantalla si es mayor de edad o no.
#Parte 4 Ejercicio1
edad = input("Ingrese su edad: ")

while True:

    if edad.isnumeric() and int(edad) >= 18:
        print("Eres mayor de edad")
        break
    elif edad.isnumeric() and int(edad)  < 18:
        print("No eres mayor de edad")
        break
    else:
        print("Ingresa un dato válido")
        edad = input("Ingrese su edad: ")
        
