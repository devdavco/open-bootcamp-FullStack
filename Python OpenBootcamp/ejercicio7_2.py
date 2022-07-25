import time 
def main():
    hora = time.localtime().tm_hour
    minutos = time.localtime().tm_min

    if hora >= 19:
        print("Es hora de ir a casa")
    else:
        print(f"Te quedan: {18-hora} horas y {59-minutos} minutos de trabajo")

if __name__ == '__main__':
    main()
