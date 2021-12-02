import json
import os

def obtenerUsuarioPorNumDCuenta(numCuenta):
  for user in getDb():
    if user["cuenta"] == numCuenta:
      return user

def getDb():
  if os.path.exists("usersdb.json"):
    if os.stat("usersdb.json").st_size == 0:
      return []
    
    with open("usersdb.json", "r") as file:
      return json.load(file)
  else:
    return []


def actualizarSaldo(usuarios, usuarioActual, saldo, tipo):
  print(usuarioActual)
  for u in usuarios:
     if u["id"] == usuarioActual:
        if tipo == "deposito":
          u["saldo"] += saldo
        elif tipo == "retiro":
          u["saldo"] -= saldo
        with open("usersdb.json", 'w') as f:
         f.write(json.dumps(usuarios, indent=2))
         break  