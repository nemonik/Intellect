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
ClassA

Description: Intellect test fact

Initial Version: Feb 2, 2011

@author: Michael Joseph Walsh
"""

class ClassA(object):
    '''
    An example fact
    '''

    globalInClassA_1 = "a global"
    globalInClassA_2 = "another global"

    def __init__(self, property0 = None, property1 = None):
        '''
        ClassA initializer
        '''
        self.attribute1 = "attribute1's value"
        self.__hiddenAttribute1 = "super secret hidden attribute. nah!"

        self.property0 = property0
        self.property1 = property1

        print "created an instance of ClassA"

    @property
    def property0(self):
        return self._property0

    @property0.setter
    def property0(self, value):
        self._property0 = value

    @property
    def property1(self):
        return self._property1

    @property1.setter
    def property1(self, value):
        self._property1 = value

    def someMethod(self):
        print("someMethod called")

    @staticmethod
    def classAStaticMethod(self):
        print("classAStaticMethod called")

    def classASomeOtherMethod(self):
        print("classASomeOtherMethd called")

    def __classAHiddenMethod(self):
        print("classAHiddenMethod called")