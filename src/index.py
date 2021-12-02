'''
elaborar un cajero automatico que tenga 0 en la cuenta y tenga las opciones para retirar efectivo tambien que pueda
depositar en una cuenta ><
'''

if __name__ == "__main__":
  import os
  from helpers.funcionesCajero import generaNumCuenta, generarIdRandom,obtenerMenuS
  from helpers.soFunctions import crearJson 
 
  from helpers.funcionesCrud import obtenerUsuarioPorNumDCuenta,getDb,actualizarSaldo
  opcionMenu1 = {"1", "2", "3"}
  opcionMenu2 = {"1", "2"}
  usuarioActual = False
  print(getDb())
  while True:
    usuarios = getDb()
    print("Bienvenido al cajero automatico")
    print("desea iniciar cajero, 1.-SI, 2.-NO")
    op = input(":")

    if op == "1": 
      while True: 
        print("1 - Crear cuenta")
        print("2 - Ingresar")
        op2 = input(":")
        if op2 == "1":
            print("ingrese su nombre")
            nombre = input(":")
            print("ingrese su contraseña")
            contrasena = input(":")
            nuevoUsuario = {
              "id": generarIdRandom(),
              "nombre": nombre,
              "cuenta": generaNumCuenta(),
              "contrasena": contrasena,
              "saldo": 0
            }
            crearJson(nuevoUsuario)

            print("cuenta creada!!")
        elif op2 == "2":
            while True:
              try:
                numCuenta= int(input("digite numero de cuenta: "))
                break
              except ValueError:
                os.system("clear")
                print("El valor ingresado no es correcto")

            contrasena= input("digite su contraseña: ")

            user = obtenerUsuarioPorNumDCuenta(numCuenta)
            if user:
              if user["contrasena"] == contrasena and user["cuenta"] == numCuenta:
                print(f"Bienvenido {user['nombre']}")
                usuarioActual = user
                numOp = obtenerMenuS([
                  {
                    "nombreOpcion": "Depositar",
                    "valorMenu": "1"
                  },
                  {
                    "nombreOpcion": "Retirar",
                    "valorMenu": "2"
                  },
                  {
                    "nombreOpcion": "Mostrar efectivo de la cuenta",
                    "valorMenu": "3"
                  },
                  {
                    "nombreOpcion": "Salir",
                    "valorMenu": "4"
                  }
                ])

                if numOp == "1":
                  while True:
                    try:
                      saldo = int(input("digite monto a depositar: "))
                      break
                    except ValueError:
                      os.system("clear")
                      print("El valor ingresado no es correcto")

                  actualizarSaldo(usuarios, usuarioActual["id"], saldo, "deposito")
                  print("deposito exitoso")
                
                elif numOp == "2":
                  while True:
                    try:
                      saldo = int(input("digite monto a retirar: "))
                      break
                    except ValueError:
                      os.system("clear")
                      print("El valor ingresado no es correcto")

                  actualizarSaldo(usuarios, usuarioActual["id"], saldo, "retiro")
                  print("retiro exitoso")
                
                elif numOp == "3":
                    print(f"tu saldo es de: {usuarioActual['saldo']} ")
                  
    elif op == "2":
      break
    else:
      os.system("clear")
      print("Error al seleccionar")