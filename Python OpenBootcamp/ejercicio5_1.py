# Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros y otra 
# función que calcule el área de un círculo recibiendo el radio del mismo.


#Función tradicional
from cmath import pi


def calc_area_triangulo(base,altura):
    return (base*altura)/2

#Usando funcion lambda
area_triangulo = lambda b, h: b*h/2


print(calc_area_triangulo(12,8))
print (area_triangulo(12,8))


def calc_area_circulo(radio):
    pass
    return pi*(radio**2)

area_circulo = lambda radio: pi*(radio**2)


print(calc_area_circulo(20))

print(area_circulo(20))


