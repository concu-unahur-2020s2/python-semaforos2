import os
import random
import time
import threading

inicioPuente = 10
largoPuente = 20

cantAnimalitos = 5

semaforoDeAnimalitos = threading.Lock()


class Animalitos(threading.Thread):
  def __init__(self):
    super().__init__()
    self.posicion = 0
    self.velocidad = random.uniform(0.1, 0.9)

#esta es la seccion critica del codigo
  def avanzar(self):
    time.sleep(1-self.velocidad)
    if self.posicion == inicioPuente:
      semaforoDeAnimalitos.acquire()
    self.posicion += 1
    if self.posicion == (inicioPuente + largoPuente):
      semaforoDeAnimalitos.release()
#

  def dibujar(self):
    print(' ' * self.posicion + '🐶') # si no funciona, cambiá por 'V' 

  def run(self):
    while(True):
      self.avanzar()


class Vaca(Animalitos):
    def dibujar(self):
      print(' ' * self.posicion + '🐮') # si no funciona, cambiá por 'V'


class Liebre(Animalitos):
    def dibujar(self):
      print(' ' * self.posicion + '🐰') # si no funciona, cambiá por 'V'


class Puente(threading.Thread):
  def __init__(self):
    super().__init__()
    self.inicioPuente = inicioPuente
    self.largoPuente = largoPuente

  def dibujarPuente(self):
    print(' ' * inicioPuente + '=' * largoPuente)


animalitos = []
for i in range(cantAnimalitos):
  a = Vaca()
  animalitos.append(a)

for i in range(cantAnimalitos):
  a = Liebre()
  animalitos.append(a)

  a.start() # si la clase hereda de Thread, el .start() siempre corre run() de la clase.

def cls():
  os.system('cls' if os.name=='nt' else 'clear')

puente = Puente()

while(True):
  cls()
  print('Apretá Ctrl + C varias veces para salir...')
  print()
  print(animalitos)
  puente.dibujarPuente()
  for a in animalitos:
    a.dibujar()
  puente.dibujarPuente()
  time.sleep(0.2)

