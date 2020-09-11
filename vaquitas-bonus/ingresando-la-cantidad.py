import os
import random
import time
import threading

inicioPuente = 10
largoPuente = 20

cantVacas = 5
vacasEnElPuente= int(input("Ingrese la cantidad de vacas que cruzan a la vez: "))

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
for i in range(cantVacas):
  v = Vaca()
  vacas.append(v)
  v.start() # si la clase hereda de Thread, el .start() siempre corre run() de la clase.

def cls():
  os.system('cls' if os.name=='nt' else 'clear')

def dibujarPuente():
  print(' ' * inicioPuente + '=' * largoPuente)

semaforoPuente = threading.Semaphore(vacasEnElPuente)

while(True):
  cls()
  print('Apretá Ctrl + C varias veces para salir...')
  print()
  dibujarPuente()
  for v in vacas:
    v.dibujar()
  dibujarPuente()
  time.sleep(0.2)
