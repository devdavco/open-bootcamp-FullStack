import time 
def main():
    hora = time.localtime().tm_hour

    if hora > 19:
        print("Es hora de ir a casa")
    else:
        print("Te quedan:", 19 - hora," horas de trabajo")

if __name__ == '__main__':
    main()