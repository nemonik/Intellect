"""
Copyright (c) 2011, The MITRE Corporation.
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

"""
ExerciseIntellect

Description: Exercises the Intellect grammar

Initial Version: Dec 29, 2011

@author: Michael Joseph Walsh
"""
import sys, traceback, logging

from intellect.Intellect import Intellect
from intellect.examples.testing.ClassA import ClassA

if __name__ == "__main__":

    # tune down logging inside Intellect
    logger = logging.getLogger('intellect')
    logger.setLevel(logging.DEBUG) # change this to ERROR for less output
    consoleHandler = logging.StreamHandler(stream=sys.stdout)
    consoleHandler.setFormatter(logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s%(message)s'))
    logger.addHandler(consoleHandler)

    # set up logging for the example
    logger = logging.getLogger('example')
    logger.setLevel(logging.DEBUG)

    consoleHandler = logging.StreamHandler(stream=sys.stdout)
    consoleHandler.setFormatter(logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s%(message)s'))
    logger.addHandler(consoleHandler)

    print "*"*80
    print """create an instance of MyIntellect extending Intellect, create some facts, and exercise the grammar"""
    print "*"*80

    try:
        myIntellect = Intellect()

        policy_a = myIntellect.learn("./rulesets/test_f.policy")

        myIntellect.learn(ClassA( property1="apple"))
        #myIntellect.learn(ClassA( property1="pear"))
        #myIntellect.learn(ClassA( property1="grape"))
        
        #logger.debug("reasoning over policy w/ objects in memory")

        myIntellect.reason()
    except Exception as e:
        traceback.print_exc(limit=sys.getrecursionlimit(), file=sys.stdout)
