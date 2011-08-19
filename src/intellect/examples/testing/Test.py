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
test

Description: Test module

Initial Version: Feb 23, 2011

@author: Michael Joseph Walsh
"""
def helloworld():
    """
    Returns "hello world" annd prints "returning 'hello world'" to the
        sys.stdout
    """
    print "returning 'hello world'"
    return "hello world"

def greaterThanTen(n):
    """
    Returns True if 'n' is greater than 10
    """
    return n>10


class MyClass(object):

    def __init__(self):
        self._globals = {}

    @property
    def globals(self):
        return self._globals

    @globals.setter
    def globals(self, value):
        self._globals = value


a = MyClass()

locals = {}

exec("a = 1" ,a.globals, locals)

print "globals = {0}".format([g for g in a.globals if not g.startswith("__")])
print "locals = {0}".format(locals)

exec("a += 1", a.globals, locals)

print "globals = {0}".format([g for g in a.globals if not g.startswith("__")])
print "locals = {0}".format(locals)

a.globals["b"] = 5

print "globals = {0}".format([g for g in a.globals if not g.startswith("__")])
print "locals = {0}".format(locals)

exec("global b;b += 1", a.globals, locals)