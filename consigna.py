import random

class Personaje:
    def __init__(self,nombre, vida, ataque, defensa, inteligencia, agilidad, fuerza):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.inteligencia = inteligencia
        self.agilidad = agilidad
        self.fuerza = fuerza
        self.turno =True
        

class Guerrero(Personaje):
    def __init__(self, nombre, vida, ataque, defensa, inteligencia, agilidad, fuerza, arma):
        super().__init__(nombre, vida, ataque, defensa, inteligencia, agilidad, fuerza)
        self.arma = arma
        self.daño = self.fuerza + self.ataque + self.arma #Guerrero (influye su fuerza y su ataque base + ataque del arma)
        self.volador = False


class Mago(Personaje):
    def __init__(self, nombre, vida, ataque, defensa, inteligencia, agilidad, fuerza, libro):
        super().__init__(nombre, vida, ataque, defensa, inteligencia, agilidad, fuerza)
        self.libro = libro
        self.daño = self.inteligencia + self.ataque + self.libro  #Mago (influye su inteligencia y su ataque base + ataque del arma)
        self.volador = False
    

class arquero(Personaje):
    def __init__(self, nombre, vida, ataque, defensa, inteligencia, agilidad, fuerza, arco):
        super().__init__(nombre, vida, ataque, defensa, inteligencia, agilidad, fuerza)
        self.arco = arco
        self.daño =self.agilidad + self.ataque + self.arco #Arquero (influye su agilidad y su ataque base + ataque del arma)
        self.volador = False

class Asesino(Personaje):
    def __init__(self, nombre, vida, ataque, defensa, inteligencia, agilidad, fuerza, daga):
        super().__init__(nombre, vida, ataque, defensa, inteligencia, agilidad, fuerza)
        self.daga = daga
        self.daño = ((self.agilidad + self.inteligencia)/2) + self.ataque + self.daga #Asesino (influye su agilidad e inteligencia, y su ataque base + ataque del arma)
        self.volador = False
    

class Enemigos(Personaje):
    def __init__(self, nombre, vida, ataque, defensa, inteligencia, agilidad, fuerza):
        super().__init__(nombre, vida, ataque, defensa, inteligencia, agilidad, fuerza)
        
class Orco(Enemigos):
    def __init__(self, nombre, vida, ataque, defensa, inteligencia, agilidad, fuerza):
        super().__init__(nombre, vida, ataque, defensa, inteligencia, agilidad, fuerza)
        self.volador = False

class Linch(Enemigos):
    def __init__(self, nombre, vida, ataque, defensa, inteligencia, agilidad, fuerza ):
        super().__init__(nombre, vida, ataque, defensa, inteligencia, agilidad, fuerza)
        self.volador = False

class Sombra(Enemigos):
    def __init__(self, nombre, vida, ataque, defensa, inteligencia, agilidad, fuerza):
        super().__init__(nombre, vida, ataque, defensa, inteligencia, agilidad, fuerza)
        self.volador = False

class Gargola(Enemigos, object):
    def __init__(self, nombre, vida, ataque, defensa, inteligencia, agilidad, fuerza):
        super().__init__(nombre, vida, ataque, defensa, inteligencia, agilidad, fuerza)
        self.volador = True
        

def crear_jugador():
    nombre = input( "elegir  nombre del personaje: ")
    clase = int(input("elegir clase: 1.guerrero, 2.mago, 3.arquero, 4.asesino"))
    if clase == 1:
        jugador = Guerrero(nombre,100,10,8,5,5,10,0)
        arma = int(input("elegir arma : 1- hacha +2 fuerza +2 daño  o 2 - espada + 2 defensa +2 daño"))
        if arma == 1:
            jugador.arma = 2
            jugador.fuerza += 2
        elif arma == 2:
            jugador.arma = 2
            jugador.defensa +=2
    elif clase == 2:
        jugador = Mago(nombre, 60, 20, 5, 20, 5, 5, 0)
        arma = int(input("elegir Grimorio : 1- libro de fuego +4 daño  o 2- libro de hielo + 2 defensa + 2 daño"))
        if arma == 1:
            jugador.libro = 4
        elif arma == 2:
            jugador.libro = 2
            jugador.defensa +=2
    elif clase == 3:
        jugador = arquero(nombre, 80, 15, 5, 5, 20, 5, 0)
        arma = int(input("elegir arma : 1- arco corto +2 daño + 2 agilidad  o 2 - arco largo + 3 de daño + 1 defensa"))
        if arma == 1:
            jugador.arco = 2
            jugador.agilidad +=2
        elif arma == 2:
            jugador.arco = 3
            jugador.defensa +=1
    elif clase == 4:
        jugador = Asesino(nombre, 60, 10, 5, 15, 20, 5, 0)
        arma = int(input("elegir arma : 1- daga curva +2 daño +2 agilidad  o 2 - daga corta + 2 defensa + 2 daño"))
        if arma == 1:
            jugador.daga = 2
            jugador.agilidad +=2
        elif arma == 2:
            jugador.daga = 2
            jugador.defensa +=2
    return jugador
    
def mostrar_jugador(jugador):    
    print (jugador)
    
    print( "******************************")
    print("nombre: ",jugador.nombre)
    print("puntos de vida: ",jugador.vida)
    print("ataque: ",jugador.ataque)
    print("defensa: ",jugador.defensa)
    print("inteligencia: ",jugador.inteligencia)
    print("agilidad: ",jugador.agilidad)
    print("fuerza: ",jugador.fuerza)
    print("Daño: ",jugador.daño)
    print( "******************************")

    
def mostrar_enemigo(enemigo):    
    print (enemigo)
    
    print( "******************************")
    print("nombre: ",enemigo.nombre)
    print("puntos de vida: ",enemigo.vida)
    print("ataque: ",enemigo.ataque)
    print("defensa: ",enemigo.defensa)
    print("inteligencia: ",enemigo.inteligencia)
    print("agilidad: ",enemigo.agilidad)
    print("fuerza: ",enemigo.fuerza)
    print("Daño: ",enemigo.ataque)
    print( "******************************")


def esta_vivo(jugador):
    if jugador.vida > 0:
        return True
    else:
        return False
def morir(jugador):
    jugador.vida = 0
    
    print(" ****** EL PERSONAJE A MUERTO ******")
    
def atacar_enemigo(jugador, enemigo):
    daño = (jugador.ataque - enemigo.defensa)
    if enemigo.vida > 0:
        if enemigo.volador == True:
            suerte = random.randint(1,100)
            if suerte < 50:
                enemigo.vida -= daño
                print("has realizado : ", daño," puntos de daño")
                if enemigo.vida < 0:
                    enemigo.vida = 0
                    print("el enemigo a muerto")
                else:
                    print("el enemigo tiene ", enemigo.vida, "puntos de vida")
            else:
                print("el enemigo a esquivado")
        else:
            
            enemigo.vida -= daño
            print("has realizado : ", daño," puntos de daño")
            if enemigo.vida < 0:
                enemigo.vida = 0
                print("el enemigo a muerto")
            else:
                print("el enemigo tiene ", enemigo.vida, "puntos de vida")
    else:
        print("el enemigo ya a muerto")  
def atacar_jugador (enemigo,jugador):
    daño = (enemigo.ataque - jugador.defensa)
    if jugador.vida > 0:
        if jugador.volador == True:
            suerte = random.randint(1,100)
            if suerte < 50:
                jugador.vida -= daño
                print("has recibido : ", daño," puntos de daño")
                if jugador.vida < 0:
                    morir(jugador)     
                else:
                    print("te quedan ", jugador.vida, "puntos de vida")
            else:
                print("has esquivado")
        else:
            
            jugador.vida -= daño
            print("has recibido : ", daño," puntos de daño")
            if jugador.vida < 0:
                morir(jugador)     
            else:
                print("te quedan ", jugador.vida, "puntos de vida")
    else:
        print("el enemigo ya a muerto")
        
def batalla_aleatoria(jugador, enemigos):
    ganador = False
    
    while  not ganador:
        enemigo = random.choice(enemigos)
        print("Te ataca un enemigo, es un/a : ", enemigo.nombre)
        print(" Tu turno")
        atacar_enemigo(jugador, enemigo)
        if enemigo.vida <= 0:
            ganador = jugador
        else:    
            atacar_jugador(enemigo, jugador)
        if jugador.vida <= 0:
                ganador = enemigo
        else:
            print("------------------")
    print("El ganador es: ", ganador.nombre)




enemigo1 = Orco("Orco",40,10,5,5,5,10)
enemigo2 = Gargola("Gargola", 60, 8, 10, 5, 20, 5)
enemigo3 = Sombra("Sombra", 15, 9, 10, 20, 5, 5)
enemigo4 = Linch("Linch", 100, 7, 10, 20, 5, 5)

enemigos =[enemigo1, enemigo2, enemigo3, enemigo4]
jugador = crear_jugador()
mostrar_jugador(jugador)
print("------------------")
print("Iniciando la Aventura")
for i in range(random.randint(1,10)):
    batalla_aleatoria(jugador, enemigos)
    if jugador.vida <= 0:
        break










































