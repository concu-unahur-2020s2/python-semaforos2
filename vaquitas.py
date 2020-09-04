import os
import random
import time
import threading
import sys

inicioPuente = 10
largoPuente = 20

cantVacas = 5
vacasQueCruzaron = []

ordenDelPastor = threading.Semaphore()

class Vaca(threading.Thread):
  def __init__(self):
    super().__init__()
    self.posicion = 0
    self.velocidad = random.uniform(0.1, 0.9)

  def avanzar(self):
    time.sleep(1-self.velocidad)
    self.posicion += 1

  def dibujar(self):
    print(' ' * self.posicion + '🐮') # si no funciona, cambiá por 'V' 

  def run(self):
    while(self.posicion != inicioPuente):
      self.avanzar()
    ordenDelPastor.acquire()

    while(True):
      if(self.posicion == largoPuente + inicioPuente):
        ordenDelPastor.release()
        vacasQueCruzaron.append(self)
      self.avanzar()



vacas = []
for i in range(cantVacas):
  v = Vaca()
  vacas.append(v)
  v.start() # si la clase hereda de Thread, el .start() siempre corre run() de la clase.

def cls():
  os.system('cls' if os.name=='nt' else 'clear')

def dibujarPuente():
  print(' ' * inicioPuente + '=' * largoPuente)

while(True):
  cls()
  print('Apretá Ctrl + C varias veces para salir...')
  print()
  dibujarPuente()
  for v in vacas:
    v.dibujar()
  dibujarPuente()
  time.sleep(0.2)
  if(len(vacasQueCruzaron) == cantVacas):
        print("Todas las vacas cruzaron el puente.")
        time.sleep(2)
        sys.exit()
