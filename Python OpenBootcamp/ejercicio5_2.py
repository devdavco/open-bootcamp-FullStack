def num_primo(numero:int)->int:
    contador = 0
    if numero > 1:
        for x in range(numero):
            if numero % 2 == 0:
                contador += 1
        if contador > 2:
            return "Número no Primo"
        else:
            return "Número Primo"
    else:
        return "Número debe ser mayor a cero"




print(num_primo(15))