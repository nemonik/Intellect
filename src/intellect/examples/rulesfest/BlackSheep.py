'''
Created on Aug 18, 2011

@author: walsh
'''

import logging, time

import thread, random
from threading import Lock

def grow_wool(sheep):
    while True:
        # sleep for some amount seconds
        #time.sleep(random.randint(1, 10))
        
        time.sleep(random.randint(2, 5))

        logging.getLogger("example").debug("{0}: adding some wool".format(sheep.name))

        # add a bag of wool
        sheep.bags_of_wool = sheep.bags_of_wool + 1

        if sheep.bags_of_wool == 3:
            logging.getLogger("example").debug("{0}: wait around for retirement".format(sheep.name))
            break

class BlackSheep():

    number = 0

    def __init__(self):
        '''
        BlackSheep Initializer
        '''
        self.bags_of_wool = 0
        BlackSheep.number = BlackSheep.number + 1
        self._name = "Sheep #{0}".format(BlackSheep.number)

        self.lock = Lock()
        
        thread.start_new_thread(grow_wool, (self,))


    @property
    def name(self):
        return self._name

    @property
    def bags_of_wool(self):
        self.lock.acquire()
        value = self._bags_of_wool
        self.lock.release()
        return value

    @bags_of_wool.setter
    def bags_of_wool(self, value):
        self.lock.acquire()
        self._bags_of_wool = value
        self.lock.release()

