#Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.

def anio_bisiesto():
    anno = int(input("Ingrese un año: "))
    if(anno % 400 == 0 or (anno%4 == 0 and anno % 100 != 0 )):
        print(f"{anno} es un año bisiesto!")
    else:
        print(f"{anno} no es un año bisiesto ")

anio_bisiesto()