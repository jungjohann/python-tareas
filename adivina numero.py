### Adivina el número (juego)

#Crear un programa en el que el usuario deberá adivinar el número que la máquina escogió. Deben utilizar la librería `random` 
# para generar la elección de la máquina. El usuario tendrá 5 vidas, cada vez que intente adivinar, recibirá como respuesta 
# “El número es mayor” o “El número es menor” según corresponda, y perderá una vida. Ganará cuando logre adivinar el número 
# elegido por la máquina.

import random

azar = int(random.randint(0,50))


i = 1
while i < 5:
    num = int(input("ingresa un numero entre 1 y 50 :  "))
    if num == azar:
        print( " ¡¡ adivinaste felicidades !!")
        break
    elif num < azar :
        print ( i,"° pista : El número es mayor " )
    elif num > azar:
        print ( i,"° pista : El número es menor " )
    i+=1
if i == 5:
    
    print ("los siento perdiste el numero era ",azar )