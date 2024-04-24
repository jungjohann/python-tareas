"""### Batalla naval

Crear un programa que permita jugar la batalla naval entre dos jugadores.
Cada uno debe ubicar un barco que contiene 3 secciones. Luego cada jugador 
tira una bomba por turno indicando la posición en x y la posición en y. Si 
acierta, esa sección del barco queda destruida y se muestra un mensaje por 
pantalla. Gana el jugador que logre destruir el barco completo del rival."""

import numpy as np
import random

def llenadobarco1():
    return

mapa_lleno1 = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
mapa_lleno2 = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

mapa1 = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
mapa2 = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]



a = np.array(mapa_lleno1)
b = np.array(mapa_lleno2)
c = np.array(mapa1)
d = np.array(mapa2)

# llenado barco jugador 1
def llenado1():
    posicion = int(input("Por favor la orientacion del barco 1 (0 = horizontal, 1 = vertical, 2 = diagonal derecha, 3 = diagonal izquierda): "))
    while posicion != 0 and posicion != 1 and posicion != 2 and posicion != 3:
        print("Por favor ingresa una orientacion valida")
        posicion = int(input("Por favor ingresa la orientacion del barco 1 (0 = horizontal, 1 = vertical, 2 = diagonal derecha, 3 = diagonal izquierda): "))
    imprimirmapa1()
    if posicion == 0: #barco en horizontal
        print("barco 1 horizontal")
        inicio = int(input(" eliga la fila en la que ubicara el barco 1: "))
        while inicio < 0 or inicio > 2:
            print("Por favor ingresa una fila valida")
            inicio = int(input("Por favor ingresa la fila en la que ubicara el barco 1: "))
        print("barco 1 ubicado en la fila", inicio)
        for i in range(3):
            mapa_lleno1[inicio][i] = "X"
    elif posicion == 1: #barco en vertical
        print("barco 1 vertical")
        inicio = int(input("eliga la columna en la que ubicara el barco 1: "))
        while inicio < 0 or inicio > 2:
            print("Por favor ingresa una columna valida")
            inicio = int(input("Por favor ingresa la columna en la que ubicara el barco 1: "))
        print("barco 1 ubicado en la columna", inicio)
        for i in range(3):
            mapa_lleno1[i][inicio] = "X"
    elif posicion == 2: #barco en diagonal a la derecha
        print("barco 1 diagonal a la derecha")
        for i in range(3):
            mapa_lleno1[i][i] = "X"
    elif posicion == 3: #barco en diagonal a la izquierda
        print("barco 1 diagonal a la izquierda")
        for i in range(3):
            mapa_lleno1[i][2-i] = "X"
pass


# llenado barco jugador 2   
def llenado2():
    posicion = int(input("Por favor la orientacion del barco 2 (0 = horizontal, 1 = vertical, 2 = diagonal derecha, 3 = diagonal izquierda): "))
    while posicion != 0 and posicion != 1 and posicion != 2 and posicion != 3:
        print("Por favor ingresa una orientacion valida")
        posicion = int(input("Por favor ingresa la orientacion del barco 2 (0 = horizontal, 1 = vertical, 2 = diagonal derecha, 3 = diagonal izquierda): "))
    imprimirmapa2()
    if posicion == 0: #barco en horizontal
        print("barco 2 horizontal")
        inicio = int(input(" eliga la fila en la que ubicara el barco 2: "))
        while inicio < 0 or inicio > 2:
            print("Por favor ingresa una fila valida")
            inicio = int(input("Por favor ingresa la fila en la que ubicara el barco 2: "))
        print("barco 2 ubicado en la fila", inicio)
        for i in range(3):
            mapa_lleno2[inicio][i] = "X"
    elif posicion == 1: #barco en vertical
        print("barco 2 vertical")
        inicio = int(input("eliga la columna en la que ubicara el barco 2: "))
        while inicio < 0 or inicio > 2:
            print("Por favor ingresa una columna valida")
            inicio = int(input("Por favor ingresa la columna en la que ubicara el barco 2: "))
        print("barco 2 ubicado en la columna", inicio)
        for i in range(3):
            mapa_lleno2[i][inicio] = "X"
    elif posicion == 2: #barco en diagonal a la derecha
        print("barco 2 diagonal a la derecha")
        for i in range(3):
            mapa_lleno2[i][i] = "X"
    elif posicion == 3: #barco en diagonal a la izquierda
        print("barco 2 diagonal a la izquierda")
        for i in range(3):
            mapa_lleno2[i][2-i] = "X"
pass
def imprimirmapa1():
    c = np.array(mapa1)
    print(c)
pass

def imprimirmapa2():
    d = np.array(mapa2)
    print(d)
pass

def juego():
    contador1 = 0
    contador2 = 0
    while True:
        imprimirmapa1()
        print("jugador 1")
        X = int(input("elige coordenada X ( 0 - 2 ): "))
        while X < 0 or X > 2:
            print("Por favor ingresa una coordenada valida ( 0 - 2 )")
            X = int(input("elige coordenada X ( 0 - 2 ): "))
        Y = int(input("elige coordenada Y ( 0 - 2 ):  "))
        while Y < 0 or  Y > 2: 
            print("Por favor ingresa una coordenada valida ( 0 - 2 )")
            Y = int(input("elige coordenada Y ( 0 - 2 ):  "))
        mapa1[X][Y] = "O"
        if mapa_lleno2[X][Y] == "X":
            print("has acertado")
            mapa1[X][Y] = "*"
            contador1 += 1
        if contador1 == 3:     
            print("***HAS GANADO***")
            break
        imprimirmapa2()
        print("jugador 2")
        X = int(input("elige coordenada X ( 0 - 2 ): "))
        while X < 0 or X > 2:
            print("Por favor ingresa una coordenada valida ( 0 - 2 )")
            X = int(input("elige coordenada X ( 0 - 2 ): "))
        Y = int(input("elige coordenada Y ( 0 - 2 ):  "))
        while Y < 0 or  Y > 2: 
            print("Por favor ingresa una coordenada valida ( 0 - 2 )")
            Y = int(input("elige coordenada Y ( 0 - 2 ):  "))
        mapa2[X][Y] = "O"
        if mapa_lleno1[X][Y] == "X":
            print("has acertado")
            mapa2[X][Y] = "*"
            contador2 += 1
        if contador2 == 3:
            print("***HAS GANADO***")
            break
pass
llenado1()
llenado2()
juego()




