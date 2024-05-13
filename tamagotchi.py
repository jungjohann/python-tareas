"""
### **Ejercicio: Tamagotchi**

Crea una clase llamada **`Tamagotchi`** que tenga los siguientes atributos:

- **`nombre`**
- **`nivel_energia`** (inicializado en 100)
- **`nivel_hambre`** (inicializado en 0)
- **`nivel_felicidad`** (inicializado en 50)
- `**humor`** (enojado, triste, indiferente, feliz, eufórico) *depende de `**nivel_felicidad**`
- **`esta_vivo`** (inicializado en True)

> Pueden agregar más atributos si lo consideran necesario.

La clase Tamagotchi debe tener los siguientes métodos:

1. **`mostrar_estado`**: Muestra en consola el nombre del Tamagotchi y sus niveles actuales de energía,
    hambre y estado de humor.   
2. **`alimentar`**: Disminuye el nivel de hambre en 10 y disminuye el nivel de energía en 15.
3. **`jugar`**: Aumenta el nivel de felicidad en 20, disminuye el nivel de energía en 18 y aumenta el nivel 
    de hambre en 10.
4. **`dormir`**: Aumenta el nivel de energía en 40 y aumenta el nivel de hambre en 5.

Además, implementa un método llamado **`verificar_estado`** que revise si el Tamagotchi está vivo. Un Tamagotchi 
está vivo mientras su nivel de energía sea mayor que cero. Si el nivel de hambre llega a 20, cada vez que se 
realice una acción que no sea `**alimentar**` deberá reducir los puntos de energía en 20 puntos y la felicidad 
perderá 30 puntos. Si el nivel de energía llega a cero, el Tamagotchi muere y el atributo **`esta_vivo`** debe 
ser False."""

class tamagotchi():
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel_energia = 100
        self.nivel_hambre = 0
        self.nivel_felicidad = 50
        self.esta_vivo = True
        
    def humor(self):
        if self.nivel_felicidad <= 10:
            return "enojado"
        elif self.nivel_felicidad <= 35:
            return "triste"
        elif self.nivel_felicidad <= 50:
            return "indiferente"
        elif self.nivel_felicidad <= 75:
            return "feliz"
        else :
            return "euforoico"
    
def mostrar_estado(self):
    
    print(f"{self.nombre}:")
    print(f"  Energia: {self.nivel_energia}")
    print(f"  Hambre: {self.nivel_hambre}")
    print(f"  Felicidad: {self.nivel_felicidad}")
    print(f"  Humor: {self.humor()}")
    

def alimentar(self):
    self.nivel_hambre -= 10
    self.nivel_energia -= 15
    verificar_estado(self)
def jugar(self):
    self.nivel_felicidad += 20
    self.nivel_energia -= 18
    self.nivel_hambre += 10
    verificar_estado(self)
def dormir(self):
    self.nivel_energia += 40
    verificar_estado(self)

def verificar_estado(self):
    if self.nivel_hambre >= 20 and self.nivel_energia > 0:
        self.nivel_energia -= 20
        self.nivel_felicidad -= 30
    if self.nivel_energia <= 0:
        self.esta_vivo = False
        print("")
        print ("El Tamagotchi ha muerto")
        print ("")



nombre =  input("ingrese el nombre del tamagotchi: ")
tamagotchi = tamagotchi(nombre)

while tamagotchi.esta_vivo:
    print(" ")
    print(" **********Tamagotchi**********")
    print("1. Alimentar")
    print("2. Jugar")
    print("3. Dormir")
    print("4. Mostrar estado")
    print("5. Salir")
    print("")
    opcion = int(input("Selecciona una opcion: "))
    

    if opcion == 1:
        alimentar(tamagotchi)
    elif opcion == 2:
        jugar(tamagotchi)
    elif opcion == 3:
        dormir(tamagotchi)
    elif opcion == 4:
        mostrar_estado(tamagotchi)
    elif opcion == 5:
        break