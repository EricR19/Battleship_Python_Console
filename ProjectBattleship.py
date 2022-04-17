
import random
from tkinter import Menu


def inicializarBarcosComputador():
    listCpu = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for x in range(5):
        randomPosition = random.randint(0, 19)

        if listCpu[randomPosition] > 0:
            while listCpu[randomPosition] != 0:
                randomPosition = random.randint(0, 19)

        listCpu[randomPosition] = x+1

    return listCpu


def inicializarBarcosJugador():
    listJugador = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for x in range(5):
        pos = input('Ingrese la posicion donde desea colocar los barcos del 1 al 20 ')
        if listJugador[int(pos) - 1] > 0:
            while listJugador[int(pos) - 1] > 0:
                pos = input(
                    'La posicion indicada ya esta ocupada, por favor ingrese una nueva posicion ')
        listJugador[int(pos) - 1] = x+1

    return listJugador


def imprimirMenu():
    menu = ''
    while menu != '4':
        menu = input('Este es el menu, por favor indique una opcion: \n 1: Inicializar Juego \n 2: Imprimir donde estan los barcos \n 3: Jugar \n 4: Salir del juego \n')
        if menu == '1':
            iniciadosCpu = inicializarBarcosComputador()
            iniciadosJugador = inicializarBarcosJugador()
        if menu == '2':
            print(iniciadosCpu)
            print(iniciadosJugador)
        if menu == '3':
            barcosDerribados = 0
            barcosDerribadosCpu = 0
            turno = 0
            while barcosDerribados != 5:
                if turno != 20:
                    disparo = input('Ingrese la posicion donde desea disparar: ')
                    barcosDerribados = hacerDisparos(
                        iniciadosCpu, int(disparo), barcosDerribados)
                    turno+=1
                    barcosDerribadosCpu = hacerDisparosCpu(iniciadosJugador,barcosDerribadosCpu)
                    print('Turno: '+str(turno))
                    if turno == 20:
                        break
                    if barcosDerribadosCpu == 5:
                        break
            if barcosDerribados == barcosDerribadosCpu:
                print('Empate Barcos Derribados por el Jugador: '+str(barcosDerribados) +'\n Barcos derribados por la CPU ' +str(barcosDerribadosCpu)) 
                barcosDerribadosCpu= 0
                barcosDerribados = 0
                menu = '1' 
            if barcosDerribados > barcosDerribadosCpu:
                print('El ganador fue usted barcos derribados: ' +str(barcosDerribados) +'\n Barcos derribados por la CPU ' +str(barcosDerribadosCpu))
                barcosDerribadosCpu= 0
                barcosDerribados = 0
                menu = '1'
            else:
                print('El ganador fue la CPU barcos derribados: '+str(barcosDerribadosCpu) +'\n Barcos derribados por usted ' +str(barcosDerribados)) 
                barcosDerribadosCpu= 0
                barcosDerribados = 0
                menu = '1'   
            

        if menu == '4':
            print('4')


def hacerDisparos(listaCpu, disparo, barcosDerribadosJgd):
    if listaCpu[int(disparo) - 1] == 0:
        print('-1')
    else:
        print('Barco derribado por usted ' + str(listaCpu[int(disparo) - 1]))
        listaCpu[int(disparo) - 1] =0
        barcosDerribadosJgd += 1
    return barcosDerribadosJgd

def hacerDisparosCpu(listaJugador, barcosDerribadosCpu):
    disparoRandomCpu = random.randint(1,20)

    if listaJugador[disparoRandomCpu -1] == 0:
        print('-1')
    else:
        print('Barco derribado por la CPU ' +str(listaJugador[disparoRandomCpu -1]))
        listaJugador[disparoRandomCpu -1] = 0
        barcosDerribadosCpu+=1
    return barcosDerribadosCpu


def game():
    imprimirMenu()


game()
