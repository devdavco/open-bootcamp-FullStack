# paises = str(input('Ingrese nombre de paises separados por comas (,) '))
paises = 'Colombia, Holanda, Argentina, Italia, Venezuela, Japón, Argentina, Alemania, suizA, nuEva Zelanda, España, COLombia'
paises_guardados = sorted(set(paises.replace(', ',',').title().split(',')),key=str.lower)

print(', '.join(paises_guardados))

# for pais in paises_guardados:
#    print(pais+ ", ",end='')
