"""
Copyright (c) 2011, Michael Joseph Walsh.
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
Created on Aug 17, 2011

@author: Michael Joseph Walsh
'''

import sys, logging, time, random

from intellect.Intellect import Intellect

from intellect.examples.rulesfest.BuyOrder import BuyOrder

class MyIntellect(Intellect):
    pass


if __name__ == '__main__':

    # tune down logging inside Intellect
    logger = logging.getLogger('intellect')
    logger.setLevel(logging.ERROR)
    consoleHandler = logging.StreamHandler(stream=sys.stdout)
    consoleHandler.setFormatter(logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s%(message)s'))
    logger.addHandler(consoleHandler)

    # set up logging for the example
    logger = logging.getLogger('example')
    logger.setLevel(logging.DEBUG)

    consoleHandler = logging.StreamHandler(stream=sys.stdout)
    consoleHandler.setFormatter(logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s%(message)s'))
    logger.addHandler(consoleHandler)


    logging.getLogger("example").debug("Creating reasoning engine.")
    myIntellect = MyIntellect()

    logging.getLogger("example").debug("Asking the engine to learn my policy.")
    policy = myIntellect.learn("./rulesets/example.policy")

    #print myIntellect.policy.str_tree("semantic model:")

    max_buy_orders_to_start = input('Provide the maximum number possible buy orders to start with:  ')
    
    buy_order_to_start =random.randint(1, max_buy_orders_to_start)

    logging.getLogger("example").debug("Asking the engine to learn a BuyOrder for {0} sheep.".format(buy_order_to_start))
    myIntellect.learn(BuyOrder(buy_order_to_start))

    myIntellect.reason()

    while True:
        logging.getLogger("example").debug("{0} in knowledge.".format(myIntellect.knowledge))
        time.sleep(5)
        logging.getLogger("example").debug("Messaging reasoning engine to reason.")
        myIntellect.reason()
