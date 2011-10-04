*My apologies, a better readme will follow.*

Intellect
=========

:Info: Intellect is a Domain-specific language and Rules Engine for Python.
:Author: Michael Joseph Walsh

1. What is Intellect
--------------------

Intellect is a DSL ("Domain-Specific Language") and Rule Engine for Python
I authored for expressing policies to orchestrate and control a dynamic
network defense cyber-security platform being researched in The 
MITRE Corporation's Innovation Program. 

The rules engine provides an intellect, a form of artificial intelligence,
a faculty of reasoning and understanding objectively over a working memory. 
The memory retains knowledge relevant to the system, and a set of rules
authored in the DSL that describe a necessary behavior to achieve some
goal.  Each rule has an optional condition, and a suite of one or more
actions.  These actions either further direct the behavior of the system,
and/or further inform the system.  The engine starts with some facts,
truths known about past or present circumstances, and uses rules to infer
more facts.  These facts fire more rules, that infer more facts and so
on.

For the platform in the Innovation Program, the network defender uses
the DSL to confer policy,  how the platform is to respond to network
events mounted over covert network channels, but there are no direct
ties written into the language nor the rule engine to cyber security
and thus the system in its entirety can be more  broadly used in
other domains.

2. Installation
---------------

If you have `setuptools <http://peak.telecommunity.com/DevCenter/setuptools>`_
you can use ``easy_install -U Intellect``, or download the source from
`GitHub <http://github.com/nemonik/Intellect>`_ and run ``python setup.py install``.

3. Dependencies
---------------

* ANTLR3 Python Runtime 3.1.3
* Python itself, if you don't already have it.  I tested the code on Python 2.7.1 and 2.7.2. 

4. Contribution
---------------

The source code is available under the BSD 4-clause license. If you have ideas, 
code, bug reports, or fixes you would like to contribute please do so.

Bugs and feature requests can be filed at `Github <http://github.com/nemonik/Intellect>`_.

5. Background
-------------

Many production rule system implementations have been open-sourced, such as
JBoss Drools, Rools, Jess, Lisa, et cetera.  If you're familiar with the 
Drools syntax, Intellect's syntax should look familiar. (I'm not saying it 
is based on it, because it is not entirely, but I found as I was working
the syntax I would check with Drools and if made sense to push in the 
direction of Drools, this is what I did.)  The aforementioned implementations
are available for other languages for expressing production rules, but it is 
my belief that Python is under-represented, and as such it was my thought the
language and rule engine could benefit from being open sourced, and so I put
a request in. 

The MITRE Corporation granted release August 4, 2011.

Thus, releasing the domain-specific language (DSL) and Rule Engine to Open
Source in the hopes doing so will extend its use and increase its chances 
for possible adoption, while at the same time mature the project with more 
interested eyeballs being placed on it.

Starting out, it was initially assumed the aforementioned platform would 
be integrated with the best Open Source rules engine available for 
Python as there are countless implementation for Ruby, Java, and Perl, 
but surprisingly I found none fitting the project's needs. This led to 
the thought of inventing one; simply typing the keywords "python rules 
engine" into Google though will return to you the advice "to not invent 
yet another rules language", but instead you are advised to "just write 
your rules in Python, import them, and execute them." The basis for this 
advice can be coalesced down to doing so otherwise does not fit with the 
"Python Philosophy." At the time, I did not believe this to be true, nor 
fully contextualized, and yet admittedly, I had not yet authored a line 
of Python code (Yes, you're looking at my first Python program. So,
please give me a break.) nor used  ANTLR3 prior to this effort. Looking 
back, I firmly believe the act of inventing a rules engine and abstracting it 
behind a nomenclature that describes and illuminates a specific domain is 
the best way for in case of aforementioned platform the network defender 
to think about the problem. Like I said though the DSL and rules engine
could be used for anything needing a "production rule system".

As there were no rules engines available for Python fitting the platforms
needs, a policy language and naive forward chaining rules engine were built 
from scratch. The policy language's grammar is based on a subset of Python 
language syntax.  The policy DSL is parsed and lexed with the help of the 
ANTLR3 Parse Generator and  Runtime for Python. 

6. Walkthrough
--------------

A walkthrough to get you jump-started.

7. Facts (Data being reasoned over)
-----------------------------------

The interpreter, the rules engine, and the remainder of the code such as 
objects for conferring discrete network conditions, referred to as "facts",
are also authored in Python. Python's approach to the object-orientated programming
paradigm, where objects consist of data fields and methods, did not easily
lend itself to describing "facts". Because the data fields of a Python object 
referred to syntactically as "attributes" can and often are set on an 
instance of a class, they will not exist prior to a class's instantiation. 
In order for a rules engine to work, it must be able to fully introspect an 
object instance representing a condition. This proves to be very difficult 
unless the property decorator with its two attributes, "getter" and "setter", 
introduced in Python 2.6, are adopted and formally used for authoring these objects. 
Coincidentally, the use of the "Getter/Setter Pattern" used frequently in 
Java is singularly frowned upon in the Python developer community with the 
cheer of "Python is not Java".

So, you will need to author your facts as Python object's who attributes 
are formally denoted as properties like so for the attributes you would like to
reason over::

	class ClassA(object):
		'''
		An example fact
		'''
	
		def __init__(self, property0 = None, property1 = None):
			'''
			ClassA initializer
			'''
			self._property0 = property0
	
		@property
		def property0(self):
			return self._property0
	
		@property0.setter
		def property0(self, value):
			self._property0 = value

8. The Policy DSL
-----------------

Example policy files can be found at the path ``intellect/rulesets``, and must follow
the Policy grammar as define in ``intellect/grammar/Policy.g``.

8.1 Import Statements (``ImportStmts``)
---------------------------------------

Import statement basically follow Python's with a few limitations (For
example, The wild card form of import is not supported for the reasons
elaborated `here <http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html#importing>`_
and follow the Python 2.7.2 grammar. ``ImportStmt`` statements exist only at the same
level of ``ruleStmt`` statements as per the grammar, and are typically at the top of a
policy file, but are not limited to. In fact, if you break up your policy across several 
files the last imported as class or module wins as the one being named.

8.2 Attribute Statements (``attribute``)
----------------------------------------

To be written.

8.3 Rule Statements (``ruleStmt``)
----------------------------------

A rule statement at its simplest looks like so::

	rule "print":	
		then:
			print("hello world!!!!")

The rule ``print`` will always print ``hello world!!!!`` to the ``sys.stdout``.

More generally, a rule will have both a condition, the ``when`` portion containing
as of now a single ``ruleCondition``, and an action, more specifically a suite of 
one ore more actions, described by the ``then`` portion. Depending on the evaluation 
of condition, facts in knowledge will be matched and then operated over in the action 
of the rule. 

Such as in the rule ``"delete those that don't match"``, all facts in knowledge 
of type ``ClassD`` who's ``property1`` value is either a ``1`` or ``2`` or ``3``
will be deleted in action of the rule.

::

	from intellect.testing.ClassCandD import ClassD
		
	rule "delete those that don't match":
		when:
			not $bar := ClassD(property1 in [1,2,3])
		then:
			delete $bar


8.4.1 Rule Condition
--------------------

A rule may have an optional boolean evaluation on the state of objects in knowledge.

8.4.1.1 Using Regular Expressions
---------------------------------

You can also use regular expressions in rule condition by simply importing the
regular expression library straight from Python and then using like so::
	
	from intellect.testing.subModule.ClassB import ClassB 

	import re
	
	rule rule_a:
		when:
			$classB := ClassB( re.search(r"\bapple\b", "apple")!=None and property2>5 and test.greaterThanTen(property2) and aMethod() == "a")


To keep the policy files from turning into just another Python script you
will want to keep as little code out of the suite of actions and thus the  policy 
file was possible... 

Use the ``modify``, ``delete``, ``insert`` grammar defined actions as well as 
using ``simpleStatements``. If you are writing very complicated constraints 
for a condition, consider moving the constraint into a method of fact being 
reasoned over.

For example, the above regular expression example would become::

	import re
	
	rule rule_a:
		when:
			$classB := ClassB(property1ContainsTheStrApple() and property2>5 and test.greaterThanTen(property2) and aMethod() == "a")


If you were to add the method to ClassB::

	def property1ContainsTheStrApple()
		return re.search(r"\bapple\b", property1) != None

8.4.1.2 Using ``not``
---------------------

Using ``not`` will return true when something does not exist. A ``ruleCondition``
may be inveresed as follows::

	rule rule_b:
		when:
			not $classB := ClassB( property1.startswith("apple") and property2>5 and test.greaterThanTen(property2) and aMethod() == "a")


and thus negate the condition and return matches to the action of the rule to 
be operated on. 

8.4.1.3 Using ``exists``
------------------------

A ruleCondition may be prepended with ``exists`` as follows::

	rule rule_c:
		when:
			exists $classB := ClassB(property1.startswith("apple") and property2>5 and test.greaterThanTen(property2) and aMethod() == "a")
		then:
			print( "matches" + " exist" )
			a = 1
			b = 2
			c = a + b
			print(c)
			test.helloworld()
			# call MyIntellect's bar method as it is decorated as callable
			bar()

and thus the action will be called once if there are any object in memory matching 
the condition. The action statements ``modify`` and ``delete`` may not be used in 
the action if ``exists`` pre-pends the a conditon's ``ruleCondition``.

8.4.2 Rule Action (Suite of Actions)
------------------------------------

Rules may have one or more actions used in process of doing something, typically 
to achieve an aim.

Earlier, I mentioned the use of ``modify``, ``delete``, ``insert`` grammar 
defined actions of a rule, but these actions may also be ``halt`` and simple 
statements e.g. ``print``, and ``attribute`` statements.

8.4.2.1 ``learn`` action
------------------------

A rule entitled ``"Time to buy new sheep?"`` might look like the following::

	rule "Time to buy new sheep?":
		when:
			$buyOrder := BuyOrder( )
		then:
			print( "Buying a new sheep." )
			modify $buyOrder:
				count = $buyOrder.count - 1
			learn BlackSheep()


The rule above illustrates the use of a ``learn`` action to learn/insert 
a ``BlackSheep`` fact. The same rule can also be written as the following
using ``insert``::

	rule "Time to buy new sheep?":
		when:
			$buyOrder := BuyOrder( )
		then:
			print( "Buying a new sheep." )
			modify $buyOrder:
				count = $buyOrder.count - 1
			insert BlackSheep()

8.4.2.2 ``modify`` action
-------------------------

The following rule::

	rule "Time to buy new sheep?":
		when:
			$buyOrder := BuyOrder( )
		then:
			print( "Buying a new sheep." )
			modify $buyOrder:
				count = $buyOrder.count - 1
			learn BlackSheep()


illustrates the use of a ``modify`` action to modify each ``BuyOrder`` match 
returned by the rule's condition. Cannot be used in conjunction with ``exists``
rule conditions. The ``modify`` action can also be used to chain rules, what 
you do is modify the fact (toggle a boolean property, set a property's value,
et cetera)  and then use this property to evaluate in the proceeding rule.

8.4.2.3 ``forget`` action
-------------------------

A rule entitled ``"Remove empty buy orders"`` might look like the following::

	rule "Remove empty buy orders":
		when:
			$buyOrder := BuyOrder( count == 0 )
		then:
			forget $buyOrder


The rule above illustrates the use of a ``forget`` action to forget/delete 
each match returned by the rule's condition. The same rule can also be written 
as the following using ``delete``::

	rule "Remove empty buy orders":
		when:
			$buyOrder := BuyOrder( count == 0 )
		then:
			delete $buyOrder


Note: cannot be used in conjunction with ``exists``.

8.4.2.4 ``halt`` action
-----------------------

The following rule::

	rule "End policy":
		then:
			log("Finished reasoning over policy.", "example", logging.DEBUG)
			halt

illustrates the use of a ``halt`` action to tell the rules engine to halt 
reasoning over the policy.

8.4.2.5 Simple Statements (``SimpleStmt``)
------------------------------------------

``SimpleStmts`` are supported actions of a rule, and so one can do the following::

	rule rule_c:
		when:
			exists $classB := ClassB(property1.startswith("apple") and property2>5 and test.greaterThanTen(property2) and aMethod() == "a")
		then:
			print("matches" + " exist")
			a = 1
			b = 2
			c = a + b
			print(c)
			test.helloworld()
			bar()

The ``simpleStmt`` in the action will be executed if any facts in knowledge 
exist matching the condition.

8.4.2.6 ``attribute`` statements
--------------------------------

To be written.

8.4.3 ``agenda-group`` rule property
------------------------------------

Optionally, a rules may have an ``agenda-group`` property that allows it to be 
grouped in to agenda groups, and fired on an agenda.

*More to follow...*


9. Creating and using a Rules Engine with a single policy
---------------------------------------------------------

At its simplest a rules engine can be created and used like so::

	import sys, logging
	
	from intellect.Intellect import Intellect
	from intellect.Intellect import Callable
	
	# set up logging
	logging.basicConfig(level=logging.DEBUG,
	format='%(asctime)s %(name)-12s%(levelname)-8s%(message)s', stream=sys.stdout)
	
	intellect = Intellect()
	
	policy_a = intellect.learn("../rulesets/test_a.policy")
	
	intellect.reason()
	
	intellect.forget_all()


It may be preferable for you to sub-class ``intellect.Intellect.Intellect`` class in 
order to add ``@Callable`` decorated methods that will in turn permit these methods
to be called from the action of the rule.
 
For example, ``MyIntellect`` is created to sub-class ``Intellect``::

	import sys, logging
	
	from intellect.Intellect import Intellect
	from intellect.Intellect import Callable

	class MyIntellect(Intellect):
	
		@Callable
		def bar(self):
			self.log(logging.DEBUG, ">>>>>>>>>>>>>>  called MyIntellect's bar method as it was decorated as callable.")
	
	if __name__ == "__main__":
	
		# set up logging
		logging.basicConfig(level=logging.DEBUG,
			format='%(asctime)s %(name)-12s%(levelname)-8s%(message)s',
			#filename="rules.log")
			stream=sys.stdout)
	
		print "*"*80
		print """create an instance of MyIntellect extending Intellect, create some facts, and exercise the MyIntellect's ability to learn and forget"""
		print "*"*80
	
		myIntellect = MyIntellect()
	
		policy_a = myIntellect.learn("../rulesets/test_a.policy")
	
		myIntellect.reason()
	
		myIntellect.forget_all()


The policy could then be authored, where the ``MyIntellect`` class's ``bar`` method 
is called for matches to the rule condition, like so::

	from intellect.testing.subModule.ClassB import ClassB
	import intellect.testing.Test as Test
	import logging
	
	fruits_of_interest = ["apple", "grape", "mellon", "pear"]
	count = 5
	
	rule rule_a:
		agenda-group test_a
		when:
			$classB := ClassB( property1 in fruits_of_interest and property2>count ) 
		then:
			# mark the 'ClassB' matches in memory as modified
			modify $classB:
				property1 = $classB.property1 + " pie"
				modified = True
				# increment the match's 'property2' value by 1000
				property2 = $classB.property2 + 1000
	
			attribute count = $classB.property2
			print "count = {0}".format( count )
	
			# call MyIntellect's bar method as it is decorated as callable
			bar()
			log(logging.DEBUG, "rule_a fired")