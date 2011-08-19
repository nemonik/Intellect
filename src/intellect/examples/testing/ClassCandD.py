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
ClassCandD

Description: Intellect test facts

Initial Version: Feb 2, 2011

@author: Michael Joseph Walsh
"""

class ClassC(object):
    '''
    An example fact.
    '''
    
    globalInClassC="a global only in ClassC"

    def __init__(self, property1 = None, property2 = None):
        '''
        ClassC initializer
        '''
        self.property1 = property1
        self.property2 = property2

    def someMethod(self):
        print("someMethod called")         

    @property
    def property1(self):
        return self._property1

    @property1.setter
    def property1(self, value):
        self._property1 = value

    @property1.deleter
    def property1(self):
        del self._property1

    @property
    def property2(self):
        return self._property2

    @property2.setter
    def property2(self, value):
        self._property2 = value

    @property2.deleter
    def property2(self):
        del self._property2
 
        
class ClassD(object):
    '''
    An example fact.
    '''
    
    globalInClassD="a global only in ClassD"
    
    def __init__(self, property1 = None):
        '''
        ClassD initializer
        '''
        self.property1 = property1

    def someMethod(self):
        print("someMethod called")  

    @property
    def property1(self):
        return self._property1

    @property1.setter
    def property1(self, value):
        self._property1 = value
        
    @property1.deleter
    def property1(self):
        del self._property1