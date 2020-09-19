import os
import random
import time
import threading

inicioPuente = 10
largoPuente = 20

cantVacas = 5


semaforoVaca = threading.Semaphore(1)
semaforoLLegada = threading.Semaphore(0)

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
    while(True):
      self.avanzar()
      while self.posicion == inicioPuente - 2:
        semaforoVaca.acquire()
        self.avanzar()
      while self.posicion == inicioPuente + largoPuente + 1:
        semaforoVaca.release() 
        self.avanzar()
      while self.posicion == (largoPuente * 2) + 13 :
        semaforoLLegada.acquire()
        semaforoVaca.acquire()
        self.avanzar()
        semaforoLLegada.release()
        semaforoVaca.release()
  
     
 
vacas = []
for i in range(cantVacas):
  v = Vaca()
  vacas.append(v)
  v.start() # si la clase hereda de Thread, el .start() siempre corre run() de la clase.

def cls():
  os.system('cls' if os.name=='nt' else 'clear')

def dibujarPuente():
  print(' ' * inicioPuente + '=' * largoPuente + ' ' * 3 + '=' * largoPuente)


while(True):
  cls()
  print('Apretá Ctrl + C varias veces para salir...')
  print()
  for v in vacas:
    v.dibujar()
  dibujarPuente()
  time.sleep(0.2)