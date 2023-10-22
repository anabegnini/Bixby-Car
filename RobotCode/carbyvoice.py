from carwalk import Carwalk
import time
import threading


class Car(threading.Thread, Carwalk):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):  
        while True:  
            if (self.queue.hasItem):
                time.sleep(0.5)
                call = self.queue.catch()
                print('Executando a ação: ', call)
                getattr(self, call)()    