'''
Created on Aug 18, 2011

@author: walsh
'''

class BuyOrder(object):
    '''
    classdocs
    '''

    def __init__(self, count = 1):
        '''
        BuyOrder Initializer
        '''
        self.count = count

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value