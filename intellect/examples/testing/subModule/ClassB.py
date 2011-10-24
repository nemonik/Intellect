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
ClassB

Description: Intellect test fact

Initial Version: Feb 2, 2011

@author: Michael Joseph Walsh
"""

from intellect.examples.testing.ClassA import ClassA

class ClassB(ClassA):
    '''
    An example fact
    '''

    globalInClassB="a global only in class B"

    def __init__(self, property0 = None, property1 = None, property2 = None):
        '''
        ClassB initializer
        '''
        self.attribute2 = "attribute2's value"
        self.__hiddenAttribute2 = "another super secret hidden attribute. nah!"

        self.property0 = property0
        self.property1 = property1
        self.property2 = property2
        self.modified = False

        print "created an instance of ClassB"

    @property
    def property2(self):
        return self._property2

    @property2.setter
    def property2(self, value):
        print "setting property2 to {0}".format(value)
        self._property2 = value

    @property
    def modified(self):
        return self._modified

    @modified.setter
    def modified(self, value):
        print "setting modified to {0}".format(value)
        self._modified = value

    def aMethod(self):
        return "a"

    def trueValue(self):
        return True

    @staticmethod
    def classBStaticMethod(self):
        # and here
        print("classBStatciMethod called")

    def classBSomeOtherMethod(self):
        # and here
        print("classBSomeOtherMethod called")

    def __classBHiddenMethod(self):
        # something goes here
        print("classBHiddenMethod called")