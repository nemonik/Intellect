'''
Created on Apr 25, 2012

@author: walsh
'''
import sys, logging

from intellect.Intellect import Intellect

class Person(object):
    '''
    An person fact
    '''

    def __init__(self, nom_de_plume=None, children=None):
        '''
        Parent initializer
        '''
        self.nom_de_plume = nom_de_plume
        self.children = children

        print "created an instance of Person w/ nom_de_plume: {0}".format(nom_de_plume)

    @property
    def nom_de_plume(self):
        return self._nom_de_plume

    @nom_de_plume.setter
    def nom_de_plume(self, value):
        self._nom_de_plume = value

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, value):
        self._children = value


if __name__ == '__main__':

    # tune down logging inside Intellect
    logger = logging.getLogger('intellect')
    logger.setLevel(logging.ERROR)
    consoleHandler = logging.StreamHandler(stream=sys.stdout)
    consoleHandler.setFormatter(logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s%(message)s'))
    logger.addHandler(consoleHandler)

    Mary = Person('Mary')
    Bob = Person('Bob')
    Michael = Person('Michael')
    David = Person('David', {Mary, Bob, Michael})

    intellect = Intellect()

    intellect.learn(David);

    try:
        policy = intellect.learn('''
from intellect.examples.testing.Question import Person

rule mary_is_a_child:
    when:
        $person := Person( children and filter(lambda x: x.nom_de_plume == 'Mary', David.children))
    then:
        print("Person with a child Mary found")

''')
    except Exception, err:
        print "This fails because the grammar doesn't support 'lambda' to keep things comprehensible, but I can modify the grammar..."
        sys.exit

    intellect.policy.str_tree("sytnax", 2)

    intellect.reason()

