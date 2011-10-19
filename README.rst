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

* To install via `setuptools <http://peak.telecommunity.com/DevCenter/setuptools>`_ use ``easy_install -U Intellect``
* To install via `pip <http://www.pip-installer.org/en/latest/installing.html>`_ use ``pip install Intellect``
* To install via `pypm <http://code.activestate.com/pypm/>`_ use ``pypm install intellect``
* Or download the latest source from `Master <http://github.com/nemonik/Intellect/archives/master>`_ or the most recent tagged release `Tagged Releases <https://github.com/nemonik/Intellect/tags>`_, unpack, and run ``python setup.py install`` 


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


6. Facts (Data being reasoned over)
-----------------------------------

The interpreter, the rules engine, and the remainder of the code such as 
objects for conferring discrete network conditions, referred to as "facts",
are also authored in Python. Python's approach to the object-oriented programming
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

7. The Policy DSL
-----------------

Example with policy files can be found at the path `Intellect/src/intellect/examples <https://github.com/nemonik/Intellect/tree/master/src/intellect/examples>`_. 
Policy files must follow the Policy grammar as define in `Intellect/src/intellect/grammar/Policy.g <https://raw.github.com/nemonik/Intellect/master/src/intellect/grammar/Policy.g>`_. 
The rest of this section documents the grammar of policy domain-specific language.

7.1 Import Statements (``ImportStmts``)
---------------------------------------

Import statements basically follow Python's with a few limitations.  For
example, The wild card form of import is not supported for the reasons
elaborated `here <http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html#importing>`_
and follow the Python 2.7.2 grammar. ``ImportStmt`` statements exist only at the same
level of ``ruleStmt`` statements as per the grammar, and are typically at the top of a
policy file, but are not limited to. In fact, if you break up your policy across several 
files the last imported as class or module wins as the one being named.

.. _7.2:

7.2 Attribute Statements (``attribute``)
----------------------------------------

.. figure:: https://github.com/nemonik/Intellect/raw/master/images/attributeStmt.jpg
   
   The syntax diagram for a ``attributeStmt``.

``attributeStmt`` statements are expressions used to create policy attributes, a form of
globals, that are accessible from rules.

For example, a policy could be written::

	import logging
	
	first_sum = 0
	second_sum = 0
	
	rule "set both first_sum and second_sum to 1":
		agenda-group "test_d"
		then:
			attribute (first_sum, second_sum) = (1,1)
			log("first_sum is {0}".format(first_sum), "example", logging.DEBUG)
			log("second_sum is {0}".format(second_sum), "example", logging.DEBUG)
	
	rule "add 2":
		agenda-group "test_d"
		then:
			attribute first_sum += 2
			attribute second_sum += 2
			log("first_sum is {0}".format(first_sum), "example", logging.DEBUG)
			log("second_sum is {0}".format(second_sum), "example", logging.DEBUG)
	
	rule "add 3":
		agenda-group "test_d"
		then:
			attribute first_sum += 3
			attribute second_sum += 3
			log("first_sum is {0}".format(first_sum), "example", logging.DEBUG)
			log("second_sum is {0}".format(second_sum), "example", logging.DEBUG)
	
	rule "add 4":
		agenda-group "test_d"
		then:
			attribute first_sum += 4
			attribute second_sum += 4
			log("first_sum is {0}".format(first_sum), "example", logging.DEBUG)
			log("second_sum is {0}".format(second_sum), "example", logging.DEBUG)
			halt
	
	rule "should never get here":
		agenda-group "test_d"
		then:
			log("Then how did I get here?", "example", logging.DEBUG)

containing the two ``atributeStmt`` statements::

	first_sum = 0
	second_sum = 0 

The following rules will increment these two attributes using ``attributeAction``
statements.

Code to exercise this policy would look like so::

	class MyIntellect(Intellect):
		pass
	
	if __name__ == "__main__":
	
		# set up logging for the example
		logger = logging.getLogger('example')
		logger.setLevel(logging.DEBUG)
	
		consoleHandler = logging.StreamHandler(stream=sys.stdout)
		consoleHandler.setFormatter(logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s%(message)s'))
		logger.addHandler(consoleHandler)
	
		myIntellect = MyIntellect()
	
		policy_d = myIntellect.learn("./rulesets/test_d.policy")
	
		myIntellect.reason(["test_d"])

and the logging output from the execution of the above would be::

	2011-10-04 23:56:51,681 example      DEBUG   __main__.MyIntellect :: first_sum is 1
	2011-10-04 23:56:51,682 example      DEBUG   __main__.MyIntellect :: second_sum is 1
	2011-10-04 23:56:51,683 example      DEBUG   __main__.MyIntellect :: first_sum is 3
	2011-10-04 23:56:51,683 example      DEBUG   __main__.MyIntellect :: second_sum is 3
	2011-10-04 23:56:51,685 example      DEBUG   __main__.MyIntellect :: first_sum is 6
	2011-10-04 23:56:51,685 example      DEBUG   __main__.MyIntellect :: second_sum is 6
	2011-10-04 23:56:51,687 example      DEBUG   __main__.MyIntellect :: first_sum is 10
	2011-10-04 23:56:51,687 example      DEBUG   __main__.MyIntellect :: second_sum is 10

See section 7.3.3.1.2_ ``attributeAction`` for another example.

7.3 Rule Statements (``ruleStmt``)
----------------------------------

.. figure:: https://github.com/nemonik/Intellect/raw/master/images/ruleStmt.jpg
   
   The syntax diagram for a ``ruleStmt``.

A rule statement at its simplest looks like so::

	rule "print":	
		then:
			print("hello world!!!!")

The rule ``"print"`` will always activate and output ``hello world!!!!`` to the 
``sys.stdout``.

A rule will always have an identifier (``id``) in either a ``NAME`` or ``STRING``
token form following Python's naming and ``String`` conventions.

Generally, a rule will have both a ``when`` portion containing the condition 
of the rule, as of now a ``ruleCondition``, and an ``action`` described by the 
``then`` portion. The ``action`` can be thought of in Python-terms as having more 
specifically a suite of one ore more actions.

Depending on the evaluation of ``condition``, facts in knowledge will be matched 
and then operated over in the action of the rule. 

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

7.3.1 ``agenda-group`` rule property
------------------------------------

.. figure:: https://github.com/nemonik/Intellect/raw/master/images/agendaGroup.jpg
   
   The syntax diagram for a ``agendaGroup``.

Optionally, a rule may have an ``agenda-group`` property that allows it to be 
grouped in to agenda groups, and fired on an agenda.

See sections 7.2_ ``attribute`` and 7.3.3.1.2_ ``attributeAction`` for examples 
of the use of this property.

7.3.2 When
----------

.. figure:: https://github.com/nemonik/Intellect/raw/master/images/when.jpg
   
   The syntax diagram for a ``when``.

If present in rule, it defines the condition on which the rule will be activated.

7.3.2.1 Rule Condition (``condition``)
--------------------------------------

.. figure:: https://github.com/nemonik/Intellect/raw/master/images/condition.jpg
   
   The syntax diagram for a ``condition``.
   
A rule may have an optional condition, a boolean evaluation, on the state of objects 
in knowledge defined by a Class Constraint (``classConstraint``), and may be 
optionally prepended with ``exists`` as follows::

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
the action if ``exists`` prepends the ``classContraint``.

Currently, the DSL only supports a single ``classConstraint``, but work is ongoing
to support more than one.

7.3.2.1.1 A Class Constraint (``classConstraint``)
--------------------------------------------------

.. figure:: https://github.com/nemonik/Intellect/raw/master/images/classConstraint.jpg
   
   The syntax diagram for a ``classConsraint``.

A ``classContraint`` defines how an objects in knowledge will be matched.  It defines an 
``OBJECTBINDING``, the Python name of the object's class and the optional ``constraint`` 
by which objects will be matched in knowledge.

The ``OBJECTBINDING`` is a ``NAME`` token following Python's naming convention prepended
with a dollar-sign (``$``).

As in the case of the Rule Condition example::

			exists $classB := ClassB(property1.startswith("apple") and property2>5 and test.greaterThanTen(property2) and aMethod() == "a")


``$classB`` is the ``OBJECTBINDING`` that binds the matches of facts of type
``ClassB`` in knowledge matching the ``constraint``.

An ``OBJECTBINDING`` can be further used in the action of the rule, but not in the 
case where the ``condition`` is prepended with ``exists`` as in the example.

7.3.2.1.2 A Constraint
----------------------

A ``constraint`` follows the same basic ``and``, ``or``, and ``not`` grammar that Python
follows.

As in the case of the Rule Condition example::

			exists $classB := ClassB(property1.startswith("apple") and property2>5 and test.greaterThanTen(property2) and aMethod() == "a")

All ``ClassB`` type facts are matched in knowledge that have ``property1`` attributes
that ``startwith`` ``apple``, and ``property2`` attributes greater than ``5`` before 
evaluated in hand with ``exist`` statement.  More on the rest of the constraint follows
in the sections below.

7.3.2.1.2.1 Using Regular Expressions
-------------------------------------

You can also use regular expressions in constraint by simply importing the
regular expression library straight from Python and then using like so as
in the case of the Rule Condition example::

			$classB := ClassB( re.search(r"\bapple\b", property1)!=None and property2>5 and test.greaterThanTen(property2) and aMethod() == "a")

The regular expression ``r"\bapple\b"`` search is performed on ``property1`` of
objects of type ``ClassB`` in knowledge.

7.3.2.1.2.2 Using Methods
-------------------------

To rewrite a complicated ``constraint``:
````````````````````````````````````````

If you are writing a very complicated ``constraint`` consider moving the 
evaluation necessary for the ``constraint`` into a method of fact being 
reasoned over to increase readability.

As in the case of the Rule Condition example, it could be rewritten to::

			$classB := ClassB(property1ContainsTheStrApple() and property2>5 and test.greaterThanTen(property2) and aMethod() == "a")

If you were to add the method to ClassB::

	def property1ContainsTheStrApple()
		return re.search(r"\bapple\b", property1) != None

Of a class and/or instance:
```````````````````````````

This example, also demonstrates how the ``test`` module function ``greaterThanTen`` 
can be messaged the instance's ``property2`` attribute and the function's return 
evaluated, and a call to the instance's ``aMethod`` method can be evaluated for 
a return of ``"a"``.

7.3.3 Then
----------

.. figure:: https://github.com/nemonik/Intellect/raw/master/images/then.jpg
   
   The syntax diagram for a ``then``.

Is used to define the suite of one-or-more ``action`` statements to be called
firing the rule, when the rule is said to be activated.

7.3.3.1 Rule Action (Suite of Actions)
--------------------------------------

.. figure:: https://github.com/nemonik/Intellect/raw/master/images/action.jpg
   
   The syntax diagram for an ``action``.

Rules may have a suite of one or more actions used in process of doing something, 
typically  to achieve an aim.

7.3.3.1.1 Simple Statements (``simpleStmt``)
--------------------------------------------

.. figure:: https://github.com/nemonik/Intellect/raw/master/images/simpleStmt.jpg
   
   The syntax diagram for a ``simpleStmt``.

``simpleStmts`` are supported actions of a rule, and so one can do the following::

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

To keep the policy files from turning into just another Python script you
will want to keep as little code out of the suite of actions and thus the  policy 
file was possible...  You will want to focus on using ``modify``, ``delete``, 
``insert``, ``halt`` before heavily using large amounts of simple statements.  This
is why ``action`` supports a limited Python grammar.  ``if``, ``for``, ``while`` etc
are not supported, only Python's ``expressionStmt`` statements are supported.

.. _7.3.3.1.2:

7.3.3.1.2 ``attributeAction``
-----------------------------

.. figure:: https://github.com/nemonik/Intellect/raw/master/images/attributeStmt.jpg
   
   The syntax diagram for a ``attributeStmt``.
   
``attributeAction`` actions are used to create, delete, or modify a policy 
attribute.

For example::

	i = 0
	
	rule rule_e:
		agenda-group "1"
		then:
			attribute i = i + 1
			print i
	
	rule rule_f:
		agenda-group "2"
		then:
			attribute i = i + 1
			print i
	
	rule rule_g:
		agenda-group "3"
		then:
			attribute i = i + 1
			print i
	
	rule rule_h:
		agenda-group "4"
		then:
			# the 'i' variable is scoped to then portion of the rule
			i = 0
			print i
	
	rule rule_i:
		agenda-group "5"
		then:
			attribute i += 1
			print i
			# the 'i' variable is scoped to then portion of the rule
			i = 0
	
	rule rule_j:
		agenda-group "6"
		then:
			attribute i += 1
			print i

If the rules engine is instructed to reason seeking to activate 
rules on agenda in the order describe by the Python list
``["1", "2", "3", "4", "5", "6"]`` like so::

	class MyIntellect(Intellect):
		pass
	
	if __name__ == "__main__":
	
		myIntellect = MyIntellect()
	
		policy_c = myIntellect.learn("./rulesets/test_c.policy")
	
		myIntellect.reason(["1", "2", "3", "4", "5", "6"])

The following output will result::

	1
	2
	3
	0
	4
	5

When firing ``rule_e`` the policy attribute ``i`` will be incremented by a value 
of ``1``, and print ``1``, same with ``rule_f`` and ``rule_g``, but ``rule_h`` 
prints 0. The reason for this is the ``i`` variable is scoped to ``then`` portion 
of the rule. ``Rule_i`` further illustrates scoping:  the policy attribute ``i``
is further incremented by ``1`` and is printed, and then a variable ``i`` scoped to
``then`` portion of the rule initialized to ``0``, but this has no impact on
the policy attribute ``i`` for when ``rule_j`` action is executed firing the rule
the value of ``6`` is printed.

7.3.3.1.3 ``learn`` action
--------------------------

.. figure:: https://github.com/nemonik/Intellect/raw/master/images/learnAction.jpg
   :scale: 50 %
   
   The syntax diagram for a ``learnAction``.

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

7.3.3.1.4 ``forget`` action
---------------------------

.. figure:: https://github.com/nemonik/Intellect/raw/master/images/forgetAction.jpg
   
   The syntax diagram for a ``forgetAction``.


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

7.3.3.1.5 ``modify`` action
---------------------------

.. figure:: https://github.com/nemonik/Intellect/raw/master/images/modifyAction.jpg
   
   The syntax diagram for a ``modifyAction``.

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
etc)  and then use this property to evaluate in the proceeding rule.


7.3.3.1.6 ``halt`` action
-------------------------

.. figure:: https://github.com/nemonik/Intellect/raw/master/images/haltAction.jpg
   
   The syntax diagram for a ``haltAction``.

The following rule::

	rule "End policy":
		then:
			log("Finished reasoning over policy.", "example", logging.DEBUG)
			halt

illustrates the use of a ``halt`` action to tell the rules engine to halt 
reasoning over the policy.

8. Creating and using a Rules Engine with a single policy
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