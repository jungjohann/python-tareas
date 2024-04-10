#Crear un programa que permita jugar al clásico juego piedra, papel o tijeras. El mismo debe pedir al usuario que ingrese su 
# jugada, y utilizando la librería random generar una elección para la máquina. Luego debe mostrar el ganador y preguntar al 
# usuario si desea volver a jugar.

import random
A = 0
while A == 0:
    
    azar = str(random.randint(1,3))
    eleccion = input(" elija 1 para PIEDRA, 2 para PAPEL o 2 para TIJERA : ")
    if eleccion == "1":
        if azar == "2":
            print("eleji papel yo gano")
        elif azar == "3":
            print("eleji tijeras tu ganas")
        elif azar == "1":   
            print("eleji Piedra Empatamos")
        
    if eleccion == "2":
        if azar == "3":
                print("eleji tijeras yo gano")
        elif azar == "1":
            print("eleji piedra tu ganas")
        elif azar == "2":   
            print("eleji papel Empatamos")
        
    if eleccion == "3":
        if azar == "1":
            print("eleji piedra yo gano")
        elif azar == "2":
            print("eleji papel tu ganas")
        elif azar == "3":   
            print("eleji tijera Empatamos")
        
    volver = input("quieres volver a jugar Y/N")
    if volver == "n" or volver == "N":
        A = 1        
        print("Gracias por Jugar")
           
