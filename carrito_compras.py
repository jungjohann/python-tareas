"""### Carrito de compras

Diseñar un programa que simule un carrito de compras, el mismo debe contar con un menú que contenga las 
siguientes opciones:

1. Agregar producto
2. Eliminar producto
3. Ver lista de compras
4. Finalizar compra
5. Salir

Los productos disponibles son:

Leche $50 - Galletas $35 - Gaseosa $87 - Huevos $66 - Aceite $110 - Pan $20

Al finalizar la compra, debe “imprimirse” el ticket de compra, el cual contendrá la lista de productos y el precio final."""


def menu():
    print(" "  )
    print("======== MENU ========")
    
    print("1.- Agregar producto")
    print("2.- Eliminar producto")
    print("3.- Ver lista de compras")
    print("4.- Finalizar compra")
    print("5.- Salir")
    opcion = input("Ingrese una opción: ")
    return opcion

def eliminar():
    print("MENU ELIMINAR PRODUCTO"  )
    print("elija el numero del poducto a eliminar:")
    num_prod = input(print("1-Leche - 2-Galletas - 3-Gaseosa - 4-Huevos - 5-Aceite - 6-Pan- 7 salir"))
    if num_prod == "1":
        
        print("la cantidad a del producto en l lista es de", lista_productos[0][1], ":")
        cant = int(input("Ingrese la cantidad: "))
        lista_productos[0][1] = lista_productos[0][1] - cant
        
    elif num_prod == "2":
        
        print("la cantidad a del producto en l lista es de", lista_productos[1][1], ":")
        cant = int(input("Ingrese la cantidad: "))
        lista_productos[1][1] = lista_productos[1][1] - cant
    elif num_prod == "3":
        print("la cantidad a del producto en l lista es de", lista_productos[2][1], ":")
        
        cant = int(input("Ingrese la cantidad: "))
        lista_productos[2][1] = lista_productos[2][1] - cant
    elif num_prod == "4":
        
        print("la cantidad a del producto en l lista es de", lista_productos[3][1], ":")
        cant = int(input("Ingrese la cantidad: "))
        lista_productos[3][1] = lista_productos[3][1] - cant
    elif num_prod == "5":
        print("la cantidad a del producto en l lista es de", lista_productos[4][1], ":")
        
        cant = int(input("Ingrese la cantidad: "))
        lista_productos[4][1] = lista_productos[4][1] - cant
    elif num_prod == "6":
        
        print("la cantidad a del producto en l lista es de", lista_productos[5][1], ":")
        cant = int(input("Ingrese la cantidad: "))
        lista_productos[5][1] = lista_productos[5][1] - cant
    elif num_prod == "7":
        print("vuelva pronto")    
    return  

def ticket():
    carrito_compras = lista_productos.copy()
    for i in range(len(carrito_compras)):
        carrito_compras[i][1] = carrito_compras[i][1] * lista_precios[i][1]
        if carrito_compras[i][1] != 0:
            print(carrito_compras[i][0], "$", carrito_compras[i][1])
    return

def agregar():
    print("MENU AGREGAR PRODUCTO"  )
    print("elija el numero del poducto a agregar:")
    num_prod = input(print("1-Leche - 2-Galletas - 3-Gaseosa - 4-Huevos - 5-Aceite - 6-Pan- 7 salir"))
    if num_prod == "1":
        
        cant = int(input("Ingrese la cantidad: "))
        lista_productos[0][1] = lista_productos[0][1] + cant
        
    elif num_prod == "2":
        
        cant = int(input("Ingrese la cantidad: "))
        lista_productos[1][1] = lista_productos[1][1] + cant
    elif num_prod == "3":
        
        cant = int(input("Ingrese la cantidad: "))
        lista_productos[2][1] = lista_productos[2][1] + cant
    elif num_prod == "4":
        
        cant = int(input("Ingrese la cantidad: "))
        lista_productos[3][1] = lista_productos[3][1] + cant
    elif num_prod == "5":
        
        cant = int(input("Ingrese la cantidad: "))
        lista_productos[4][1] = lista_productos[4][1] + cant
    elif num_prod == "6":
        cant = int(input("Ingrese la cantidad: "))
        lista_productos[5][1] = lista_productos[5][1] + cant
    elif num_prod == "7":
        print("vuelva pronto")    
    return  
def imprimir():
    print("su lista es:")
    print(lista_productos)
    return
    
carrito_compras = []
lista_productos = [["Leche",0], ["Galletas", 0], ["Gaseosa", 0], ["Huevos", 0], ["Aceite", 0], ["Pan", 0]]
lista_precios = [["Leche",50], ["Galletas", 35], ["Gaseosa", 87], ["Huevos", 66], ["Aceite", 110], ["Pan", 20]]
while True:
    opcion = menu()
    if opcion == "1":
        agregar()
        
    elif opcion == "2":
        eliminar ()
        
    elif opcion == "3":
        imprimir()
    elif opcion == "4":
        ticket()
    elif opcion == "5":    
        break
    else:
        print("Opción inválida, intente nuevamente")
print("¡Hasta luego!")