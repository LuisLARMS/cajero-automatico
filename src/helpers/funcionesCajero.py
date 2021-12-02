#!/usr/bin/env python
import json
import os
import random

def generaNumCuenta():
    return random.randint(100000000, 999999999)

def generarIdRandom():
  return random.randint(100000000, 999999999)

def obtenerMenuS(listaMenus):
  while True:
    for value in listaMenus:
     print(f"{value['valorMenu']} .- {value['nombreOpcion']}")
  
    op = input("Ingrese el numero de la opcion que desea: ")

    for j in listaMenus:
      if j['valorMenu'] == op:
        return j['valorMenu']
       

     
