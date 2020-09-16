import os
import random
import time
import threading
from puente import*

inicioPuente = 10
largoPuente = 20

cantACruzar = int(input("cantidad de vacas a cruzar: "))     # cantidad de vacas que pueden cruzar a la vez

semaforo = threading.Semaphore(cantACruzar)


cantVacas = 5

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
    while (True):
      self.avanzar()
      try:
        if self.posicion == inicioPuente -2 :
          semaforo.acquire()
      finally:
        if self.posicion == largoPuente + inicioPuente:
          semaforo.release()


vacas = []
for i in range(cantVacas):
  v = Vaca()
  vacas.append(v)
  v.start() # si la clase hereda de Thread, el .start() siempre corre run() de la clase.

def cls():
  os.system('cls' if os.name=='nt' else 'clear')

puente1 = Puente(10,20)
puente2 = Puente(40,10)
  

while(True):
  cls()
  print('Apretá Ctrl + C varias veces para salir...')
  puente1.dibujarPuente()
  puente2.dibujarPuente()
  for v in vacas:
    v.dibujar()
  puente1.dibujarPuente()
  puente2.dibujarPuente()
  time.sleep(0.2)
