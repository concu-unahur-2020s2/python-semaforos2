import os
import random
import time
import threading

inicioPuente = 10
largoPuente = 20

cantVacas = 5
vacasACruzar = int(input("Ingrese la cantidad de vacas a cruzar a la vez:"))

semaforoPuente = threading.Semaphore(vacasACruzar)

class Vaca(threading.Thread):
  def __init__(self):
    super().__init__()
    self.posicion = 0
    self.velocidad = random.uniform(0.1, 0.9)

  def avanzar(self):
    time.sleep(1-self.velocidad)
    self.posicion += 1
    

  def dibujar(self):
    print(' ' * self.posicion + 'V') # si no funciona, cambiá por 'V' 

  def run(self):
    while self.posicion != inicioPuente and self.posicion != largoPuente:
      self.avanzar()
    while (True):
      semaforoPuente.acquire()
      try:
        if self.posicion < largoPuente:
          self.avanzar()
      finally:
        semaforoPuente.release()
 
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