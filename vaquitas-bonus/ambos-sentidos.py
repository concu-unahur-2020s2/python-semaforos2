import os
import random
import time
import threading

inicioPuente = 10
largoPuente = 20

cantVacas = 5

class Vaca(threading.Thread):
    def __init__(self, posicionInicial, accion):
        super().__init__()
        self.posicion = posicionInicial
        self.velocidad = random.uniform(0.1, 0.9)
        if accion == 'avanzar': 
            self.accion = self.avanzar
        elif accion == 'retroceder':
            self.accion = self.retroceder
        else:
            raise Exception("Accion invalida")

    def avanzar(self):
        time.sleep(1-self.velocidad)
        self.posicion += 1

        while self.posicion == inicioPuente - 2:
            semaforoPuente.acquire()
            time.sleep(1-self.velocidad)
            self.posicion += 1
        while self.posicion == inicioPuente + largoPuente + 2:
            semaforoPuente.release()
            time.sleep(1-self.velocidad)
            self.posicion += 1
        while self.posicion == 50:
            self.posicion = 48

    def retroceder(self):
        time.sleep(1-self.velocidad)
        self.posicion -= 1

        while self.posicion == inicioPuente + largoPuente + 2:
            semaforoPuente.acquire()
            time.sleep(1-self.velocidad)
            self.posicion -= 1
        while self.posicion == inicioPuente - 2:
            semaforoPuente.release()
            time.sleep(1-self.velocidad)
            self.posicion -= 1
        while self.posicion == 0:
            self.posicion = 2

     
    def dibujar(self):
        print(' ' * self.posicion + '🐮') # si no funciona, cambiá por 'V' 

    def run(self):
        while(True): 
            self.accion()
            
            
      
      
vacas = []

for i in range(cantVacas):
    v = Vaca(0, "avanzar")
    vacas.append(v)
    v.start() # si la clase hereda de Thread, el .start() siempre corre run() de la clase.

for i in range(cantVacas):
    v = Vaca(50, "retroceder")
    vacas.append(v)
    v.start()

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
    dibujarPuente()
    time.sleep(0.2)
