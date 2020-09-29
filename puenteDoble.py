import os
import random
import time
import threading

inicioPuente = 10
largoPuente = 20
distanciaEntrePuentes = 5

cantAnimalitos = 5

semaforoDeAnimalitos = threading.Lock()


class Animalitos(threading.Thread):
  def __init__(self):
    super().__init__()
    self.posicion = 0
    self.velocidad = random.uniform(0.1, 0.9)

  def avanzar(self):
    time.sleep(1-self.velocidad)
    self.posicion += 1

  def dibujar(self):
    print(' ' * self.posicion + '🐶') # si no funciona, cambiá por 'V' 

  def run(self):
      while(True): 
        self.avanzar()
        inicio2doPuente=(inicioPuente+largoPuente+distanciaEntrePuentes - 1)
        while self.posicion == inicioPuente - 1 or self.posicion == inicio2doPuente :
          semaforoDeAnimalitos.acquire()
          self.avanzar()
        while self.posicion == inicioPuente + largoPuente or self.posicion == inicio2doPuente + largoPuente:
          semaforoDeAnimalitos.release()
          self.avanzar()



class Vaca(Animalitos):
    def dibujar(self):
      print(' ' * self.posicion + '🐮') # si no funciona, cambiá por 'V'

class Liebre(Animalitos):
    def dibujar(self):
      print(' ' * self.posicion + '🐰') # si no funciona, cambiá por 'V'

class Tortuga(Animalitos):
    def dibujar(self):
      print(' ' * self.posicion + '🐢') # si no funciona, cambiá por 'V' 


class Puente(threading.Thread):
  def __init__(self):
    super().__init__()
    self.inicioPuente = inicioPuente
    self.largoPuente = largoPuente

  def dibujarPuente(self):
    print(' ' * inicioPuente + '=' * largoPuente)

class PuenteDoble(Puente):
  def __init__(self):
    super().__init__()
    self.distanciaEntrePuentes = distanciaEntrePuentes
    self.inicioPuente2 = inicioPuente
    self.largoPuente2 = largoPuente

  def dibujarPuente(self):
    print(' ' * inicioPuente + '=' * largoPuente + ' ' * distanciaEntrePuentes + '=' * largoPuente)



vacas = []


for i in range(cantAnimalitos):
  v = Vaca()
  vacas.append(v)
  v.start()



def cls():
  os.system('cls' if os.name=='nt' else 'clear')


puenteDoble = PuenteDoble()
 
while(True):
  cls()
  print('Apretá Ctrl + C varias veces para salir...')
  print()
  puenteDoble.dibujarPuente()
  for v in vacas:
    v.dibujar()
  puenteDoble.dibujarPuente()
  time.sleep(0.2)