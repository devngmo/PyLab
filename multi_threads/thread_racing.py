from ast import arg
import json
import os
from random import Random
import threading, time

racers = {}
rnd = Random()

def updateRace(racer):
    racers[racer] = 0
    for i in range(10):
        delay = rnd.randint(1,10)
        racers[racer] += delay
        os.system('cls')
        print(json.dumps(racers))
        time.sleep(delay)


a = threading.Thread(target=updateRace, args=('A'))
b = threading.Thread(target=updateRace, args=('B'))
c = threading.Thread(target=updateRace, args=('C'))
a.start()
b.start()
c.start()
a.join()
b.join()
c.join()

print('Done')

