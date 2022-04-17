
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
        pos = input('Enter your position del 1 al 20 ')
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
            while barcosDerribados != 5:
                disparo = input('Ingrese la posicion donde desea disparar: ')
                barcosDerribados = hacerDisparos(
                    iniciadosCpu, int(disparo), barcosDerribados)

        if menu == '4':
            print('4')


def hacerDisparos(listaCpu, disparo, barcosDerribadosJgd):
    if listaCpu[int(disparo) - 1] == 0:
        print('-1')
    else:
        print('Barco Derribado ' + str(listaCpu[int(disparo) - 1]))
        listaCpu[int(disparo) - 1] = 0
        barcosDerribadosJgd += 1
    return barcosDerribadosJgd


def game():
    cpu = inicializarBarcosComputador()
    print(cpu)
    jgd = inicializarBarcosJugador()
    print(jgd)


imprimirMenu()
