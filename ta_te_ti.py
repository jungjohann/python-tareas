"""### Ta-Te-Ti

Construir un Ta-Te-Ti (tres en raya) que se juegue contra otro jugador. El usuario deberá indicar la posición en la que 
desea jugar su ficha. Pueden utilizar una matriz para simular el tablero de juego."""

import numpy as np

tablero = [[" "," "," "],[" "," "," "],[" "," "," "]]
jugador1 ="X"
jugador2 ="O"
turno = 0
vuelta = 0
def victoria():
    if tablero[0][0] != " " and tablero[0][0] == tablero[0][1] and tablero[0][1] == tablero[0][2]:
        return False 
    elif tablero[1][0] != " " and tablero[1][0] == tablero[1][1] and tablero[1][1] == tablero[1][2]:
        return False 
    elif tablero[2][0] != " " and tablero[2][0] == tablero[2][1] and tablero[2][1] == tablero[2][2]:
        return False 
    if tablero[0][0] != " " and tablero[0][0] == tablero[1][0] and tablero[1][0] == tablero[2][0]:
        return False 
    elif tablero[0][1] != " " and tablero[0][1] == tablero[1][1] and tablero[1][1] == tablero[2][1]:
        return False 
    elif tablero[0][2] != " " and tablero[0][2] == tablero[1][2] and tablero[1][2] == tablero[2][2]:
        return False  
    elif tablero[0][0] != " " and tablero[0][0] == tablero[1][1] and tablero[1][1] == tablero[2][2]:
        return False 
    elif tablero[0][2] != " " and tablero[0][2] == tablero[1][1] and tablero[1][1] == tablero[2][0]:
        return False 
    else:
        
        return True
        

while True:
    a = np.array(tablero)
    print(a)
    if vuelta == 9:
        print("Empate")
        break
    
    if victoria():
        
        if turno == 0:
            print("Turno de X")
            x = int(input("Fila: "))
            y = int(input("Columna: "))
            if tablero[x][y] == " ":
                tablero[x][y] = jugador1
                turno = 1
                vuelta += 1
            else:
                print("Casilla ocupada")
        else:
            print("Turno de O")
            x = int(input("Fila: "))   
            y = int(input("Columna: "))
            if tablero[x][y] == " ":
                tablero[x][y] = jugador2
                turno = 0
                vuelta += 1
            else:
                print("Casilla ocupada") 
    else:
        print("Juego terminado")
        if turno == 0:
            print("Gano O")
            break
        else:
            print("Gano X")
            break

