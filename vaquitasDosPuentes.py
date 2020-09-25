import os
import random
import time
import threading
import sys
from puente import *

inicioPuente = 10
largoPuente = 20
inicioPuente2 = 40
largoPuente2 = 20

puente1 = Puente(inicioPuente, largoPuente)
puente2 = Puente(inicioPuente2, largoPuente2)

cantVacas = 5

ordenDelPastor = threading.Semaphore()

class Vaca(threading.Thread):
  def __init__(self):
    super().__init__()
    self.posicion = 0
    self.velocidad = random.uniform(0.1, 0.9)

  def avanzar(self):
    if ((self.posicion == inicioPuente - 1) or (self.posicion == inicioPuente2 - 1)):
        ordenDelPastor.acquire()

    time.sleep(1-self.velocidad)
    self.posicion += 1

    if ((self.posicion == inicioPuente + largoPuente) or (self.posicion == inicioPuente2 + largoPuente2)):
        ordenDelPastor.release()
    
  def dibujar(self):
    print(' ' * self.posicion + '🐮') # si no funciona, cambiá por 'V' 

  def run(self):
    while(True):
      self.avanzar()



vacas = []
for i in range(cantVacas):
  v = Vaca()
  vacas.append(v)
  v.start() # si la clase hereda de Thread, el .start() siempre corre run() de la clase.

def cls():
  os.system('cls' if os.name=='nt' else 'clear')


while(True):
  cls()
  print('Apretá Ctrl + C varias veces para salir...')
  print()
  puente1.dibujarPuente()
  puente2.dibujarPuente()
  for v in vacas:
    v.dibujar()
  puente1.dibujarPuente()
  puente2.dibujarPuente()
  time.sleep(0.2)