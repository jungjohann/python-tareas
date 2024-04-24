"""### **Cajero Automático**

Diseñar un simulador de cajero automático, el mismo debe permitir 
ingresar dinero, retirar dinero, consultar saldo, hacer transferencia, 
y debe contener más de una cuenta permitiendo seleccionar desde cual se 
desea retirar. El mismo debe poseer una contraseña de acceso pedida al 
usuario al momento de iniciar el programa."""




def ingresar():
    print(" ingresar dinero")
    print("ingrese numero de cuenta: ")
    cuenta = str(input())
    while cuenta != '1111' and cuenta != '2222':
        cuenta = str(input("Cuenta no válida, intente nuevamente: "))
    print(f"Ud a seleccionado la cuenta {cuenta}")
    monto = int(input("Ingrese monto a ingresar : $"))
    cuentas[cuenta]["saldo"] += int(monto)
    
        
    pass

def retirar():
    print("Retirar dinero")
    print("ingrese numero de cuenta: ")
    cuenta = str(input())
    while cuenta != '1111' and cuenta != '2222':
        cuenta = str(input("Cuenta no válida, intente nuevamente: "))
    print(f"Ud a seleccionado la cuenta {cuenta}")
    monto = int(input("Ingrese monto a retirar : $"))
    if cuentas[cuenta]["saldo"] < monto:
        print("Saldo insuficiente")
    else:
        cuentas[cuenta]["saldo"] -= monto
    pass

def saldo():
    print("ingrese numero de cuenta para consultar saldo: ")
    cuenta = str(input())
    while cuenta != '1111' and cuenta != '2222':
        cuenta = str(input("Cuenta no válida, intente nuevamente: "))
    print(f"Ud a seleccionado la cuenta {cuenta}")
    print(f"El saldo de la cuenta {cuenta} es: {cuentas[cuenta]['saldo']}")
    pass

def transferencia():
    cuenta_origen = str(input("Seleccione cuenta desde la cual desea retirar: "))
    while cuenta_origen != '1111' and cuenta_origen != '2222':
        cuenta_origen = str(input("Cuenta no válida, intente nuevamente: "))
    cuenta_destino = str(input("Seleccione cuenta a la cual desea transferir: "))
    while cuenta_destino != '1111' and cuenta_destino != '2222':
        cuenta_destino = str(input("Cuenta no válida, intente nuevamente: "))
    if cuenta_origen == cuenta_destino:
        print("No se puede transferir a la misma cuenta")
    else:
        monto = int(input(f"Ingrese monto a transferir de la cuenta {cuenta_origen} a la cuenta {cuenta_destino}: "))
        cuentas[cuenta_origen]["saldo"] -= monto
        cuentas[cuenta_destino]["saldo"] += monto
    pass


cuentas = {'1111': {'saldo': 0},'2222': {'saldo': 0}
}

contraseña = input("Ingrese contraseña de acceso: ") #contraseña de acceso es 1523
intentos = 1

while contraseña != "1523" and intentos < 3:
    contraseña = input("Ingrese contraseña de acceso: ")
    intentos += 1
if contraseña == "1523":
    print("Acceso correcto")
    while True:    
        
        print()
        print("Bienvenido")
        print('''
        Ingrese una opción:
        1. Ingresar dinero
        2. Retirar dinero
        3. Consultar saldo
        4. Hacer transferencia
        5. Salir
        ''')
        menu = int(input('Opción: ')) 
        
        if menu == 1:
            ingresar()
        elif menu == 2:
            retirar()
        elif menu == 3:
            print("Consultar saldo")
            saldo()
        elif menu == 4:
            print("Hacer transferencia")
            transferencia()
        elif menu == 5:
            print("hasta luego")
            break
elif intentos == 3:
    print("acceso no permitido ")