insersion = [30,17,33,23,31,30,34,33,32,17,10,13,40,21,33,21,21,35,20,18,15,14,39,28,39,19,37,10,32,34]

def main():
    escribir_archivo()
    leer_archivo()
    pass

def escribir_archivo():
    with open('numeros.txt','w') as f:
        for line in insersion:
            f.write(f'{str(line)}\n')
        
def leer_archivo():

    with open('numeros.txt') as f:
        for numero in f:
            print(numero.strip()) 

if __name__ == '__main__':
    main()
