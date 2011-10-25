"""
Copyright (c) 2011, Michael Jospeh Walsh.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the distribution.
3. All advertising materials mentioning features or use of this software
   must display the following acknowledgement:
   This product includes software developed by the author.
4. Neither the name of the author nor the
   names of its contributors may be used to endorse or promote products
   derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE AUTHOR ''AS IS'' AND ANY
EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

'''
Created on Aug 18, 2011

@author: Michael Joseph Walsh
'''

import logging, time
import thread, random
from threading import Lock

from intellect.examples.rulesfest.BagOfWool import BagOfWool

def grow_wool(sheep):
    while True:
        
        time.sleep(random.randint(2, 5))

        logging.getLogger("example").debug("{0}: Grew a bag of wool.".format(sheep.name))
        sheep.bags_of_wool.append(BagOfWool())

        if len(sheep.bags_of_wool) == 3:
            logging.getLogger("example").debug("{0}: Waiting around for retirement.".format(sheep.name))
            break

class BlackSheep():
    '''
        Used to signify a black sheep
    '''

    number = 0

    def __init__(self):
        '''
        BlackSheep Initializer
        '''
        self.bags_of_wool = []
        BlackSheep.number = BlackSheep.number + 1
        self.name = "Sheep #{0}".format(BlackSheep.number)

        logging.getLogger("example").debug("Creating {0}.".format(self.name))

        self.lock = Lock()
        thread.start_new_thread(grow_wool, (self,))


    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def bags_of_wool(self):
        return self._bags_of_wool

    @bags_of_wool.setter
    def bags_of_wool(self, value):
        self.lock.acquire()
        self._bags_of_wool = value
        self.lock.release()


if __name__ == '__main__':
    sheep = BlackSheep()

    while True:
        time.sleep(5)
        print len(sheep.bags_of_wool)

        if len(sheep.bags_of_wool) == 3:
            break
