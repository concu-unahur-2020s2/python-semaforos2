import os
import random
import time
import threading

inicioPuente = 10
largoPuente = 20
cantAnimalitos = 5

semaforoDeAnimalitos = threading.Lock()


class Vaca(threading.Thread):
  def __init__(self):
    super().__init__()
    self.posicion = 0
    self.velocidad = random.uniform(0.1, 0.9)
    self.corteDeVaca = ((2 * inicioPuente) + largoPuente)

  def avanzar(self):
    time.sleep(1-self.velocidad)
    self.posicion += 1

  def dibujar(self):
    print(' ' * self.posicion + '🐮') # si no funciona, cambiá por 'V'

  def run(self):
      while self.posicion <= self.corteDeVaca:
        self.avanzar()
        while self.posicion == inicioPuente - 1:
          semaforoDeAnimalitos.acquire()
          self.avanzar()
        while self.posicion == inicioPuente + largoPuente:
          semaforoDeAnimalitos.release()
          self.avanzar()


class VacaInvertida(threading.Thread):
  def __init__(self):
    super().__init__()
    self.posicion = ((2 * inicioPuente) + largoPuente)
    self.velocidad = random.uniform(0.1, 0.9)

  def avanzar(self):
    time.sleep(1-self.velocidad)
    self.posicion -= 1

  def dibujar(self):
    print(' ' * self.posicion + '🐮') # si no funciona, cambiá por 'V'

  def run(self):
      while(True): 
        self.avanzar()
        #while self.posicion == inicioPuente - 1:
        while self.posicion == inicioPuente + largoPuente:
          semaforoDeAnimalitos.acquire()
          self.avanzar()
        #while self.posicion == inicioPuente + largoPuente:
        while self.posicion == inicioPuente - 1:
          semaforoDeAnimalitos.release()
          self.avanzar()


class Puente(threading.Thread):
  def __init__(self):
    super().__init__()
    self.inicioPuente = inicioPuente
    self.largoPuente = largoPuente

  def dibujarPuente(self):
    print(' ' * inicioPuente + '=' * largoPuente)


vacas = []
vacasInvertidas = []

for i in range(cantAnimalitos):
  v = Vaca()
  vacas.append(v)
  v.start()

for i in range(cantAnimalitos):
  vi = VacaInvertida()
  vacasInvertidas.append(vi)
  vi.start()


def cls():
  os.system('cls' if os.name=='nt' else 'clear')

puente = Puente()
 
while(True):
  cls()
  print('Apretá Ctrl + C varias veces para salir...')
  print()
  puente.dibujarPuente()
  for v in vacas:
    v.dibujar()
  for vi in vacasInvertidas:
    vi.dibujar()
  puente.dibujarPuente()
  time.sleep(0.2)