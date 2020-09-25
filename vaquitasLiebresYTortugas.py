import os
import random
import time
import threading
import sys

inicioPuente = 10
largoPuente = 20

cantVacas = 2
cantLiebres = 3
cantTortugas = 1

ordenDelPastor = threading.Semaphore()

class Vaca(threading.Thread):
  def __init__(self):
    super().__init__()
    self.posicion = 0
    self.velocidad = random.uniform(0.4, 0.6)

  def avanzar(self):
    if (self.posicion == inicioPuente - 1):
        ordenDelPastor.acquire()

    time.sleep(1-self.velocidad)
    self.posicion += 1

    if (self.posicion == inicioPuente + largoPuente):
        ordenDelPastor.release()
    
  def dibujar(self):
    print(' ' * self.posicion + '🐮') # si no funciona, cambiá por 'V' 

  def run(self):
    while(True):
      self.avanzar()

# Me tentó hacer una clase Animal y ver como se usar la herencia en python, pero me pareció que es mejor verlo en otro momento y 
# que no rendía que me queme el bocho con eso ahora

class Liebre(threading.Thread):
  def __init__(self):
    super().__init__()
    self.posicion = 0
    self.velocidad = random.uniform(0.7, 0.9)

  def avanzar(self):
    if (self.posicion == inicioPuente - 1):
        ordenDelPastor.acquire()

    time.sleep(1-self.velocidad)
    self.posicion += 1

    if (self.posicion == inicioPuente + largoPuente):
        ordenDelPastor.release()
    
  def dibujar(self):
    print(' ' * self.posicion + '🐰') # conejo, liebre, es lo mismo

  def run(self):
    while(True):
      self.avanzar()

class Tortuga(threading.Thread):
  def __init__(self):
    super().__init__()
    self.posicion = 0
    self.velocidad = random.uniform(0.1, 0.3)

  def avanzar(self):
    if (self.posicion == inicioPuente - 1):
        ordenDelPastor.acquire()

    time.sleep(1-self.velocidad)
    self.posicion += 1

    if (self.posicion == inicioPuente + largoPuente):
        ordenDelPastor.release()
    
  def dibujar(self):
    print(' ' * self.posicion + '🐢') # que la tortuga vaya haciendo un moonwalk quizás tiene que ver con que vaya más lento, no? (no había un iconito mejor)

  def run(self):
    while(True):
      self.avanzar()


vacas = []
liebres = []
tortugas = []

for i in range(cantVacas):
  v = Vaca()
  vacas.append(v)
  v.start() # si la clase hereda de Thread, el .start() siempre corre run() de la clase.

for j in range(cantLiebres):
  l = Liebre()
  liebres.append(l)
  l.start()

for k in range(cantTortugas):
  t = Tortuga()
  tortugas.append(t)
  t.start()


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
  for l in liebres:
    l.dibujar()
  for t in tortugas:
    t.dibujar()
  dibujarPuente()
  time.sleep(0.2)