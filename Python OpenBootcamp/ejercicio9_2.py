from functools import reduce


def num_impares(lista):
    if lista %2 != 0:
        return True
    return False

lista = [1,2,3,4,5,6,7,8,9,10]


resultado_filter = filter(num_impares ,lista)
# print(list(resultado_filter))

resultado_reduce = reduce(lambda a,b:a+b,resultado_filter)

print(list(resultado_filter))
print(resultado_reduce)

