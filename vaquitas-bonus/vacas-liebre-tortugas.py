import os
import random
import time
import threading

inicioPuente = 10
largoPuente = 20

cantVacas = 5
cantLiebres = 4

class Vaca(threading.Thread):
  def __init__(self):
    super().__init__()
    self.posicion = 0
    self.velocidad = random.uniform(0.1, 0.8)

  def avanzar(self):
    time.sleep(1.5-self.velocidad)
    self.posicion += 1


  def dibujar(self):
    print(' ' * self.posicion + '🐮') # si no funciona, cambiá por 'V' 

  def run(self):
      while(True): 
        self.avanzar()
        while self.posicion == inicioPuente - 2:
          semaforoPuente.acquire()
          self.avanzar()
        while self.posicion == inicioPuente + largoPuente + 2:
          semaforoPuente.release()
          self.avanzar()
        while self.posicion == 100:
          self.posicion = 0
      
class Liebre(threading.Thread):
  def __init__(self):
    super().__init__()
    self.posicion = 0
    self.velocidad = random.uniform(0.8, 0.9)

  def avanzar(self):
    time.sleep(1-self.velocidad)
    self.posicion += 1


  def dibujar(self):
    print(' ' * self.posicion + '🐇')

  def run(self):
      while(True): 
        self.avanzar()
        while self.posicion == inicioPuente - 2:
          semaforoPuente.acquire()
          self.avanzar()
        while self.posicion == inicioPuente + largoPuente + 2:
          semaforoPuente.release()
          self.avanzar()
        while self.posicion == 100:
          self.posicion = 0

class Tortuga(threading.Thread):
  def __init__(self):
    super().__init__()
    self.posicion = 0

  def avanzar(self):
    time.sleep(3)
    self.posicion += 1

  def dibujar(self):
    print(' ' * self.posicion + '🐢') 

  def run(self):
      while(True): 
        self.avanzar()
        while self.posicion == inicioPuente - 2:
          semaforoPuente.acquire()
          self.avanzar()
        while self.posicion == inicioPuente + largoPuente + 2:
          semaforoPuente.release()
          self.avanzar()
        while self.posicion == 100:
          self.posicion = 0


vacas = []
liebres =[]

for i in range(cantVacas):
  v = Vaca()
  vacas.append(v)
  v.start() # si la clase hereda de Thread, el .start() siempre corre run() de la clase.

for i in range(cantLiebres):
    l = Liebre()
    liebres.append(l)
    l.start()

t = Tortuga()
t.start()

def cls():
  os.system('cls' if os.name=='nt' else 'clear')

def dibujarPuente():
  print(' ' * inicioPuente + '=' * largoPuente)

semaforoPuente = threading.Semaphore(1)

while(True):
  cls()
  print('Apretá Ctrl + C varias veces para salir...')
  print()
  dibujarPuente()
  for v in vacas:
    v.dibujar()
  for l in liebres:
    l.dibujar()
  t.dibujar()
  dibujarPuente()
  time.sleep(0.2)
