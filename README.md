_My apologies, a better readme will follow..._

# Intellect

:Info: Intellect is a Domain-specific language and Rules Engine for Python.  
:Author: Michael Joseph Walsh (http://github.com/nemonik)

# About

Let's clear up what Intellect is.

Intellect is a DSL ("Domain-Specific Language") and Rule Engine for Python
I authored for expressing policies to orchestrate and control a dynamic 
network defense cyber-security platform being researched in The 
MITRE Corporation's Innovation Program. 

# Installation

If you have [setuptools](http://peak.telecommunity.com/DevCenter/setuptools)
you can use ``easy_install -U Intellect``, or download the source from
[GitHub](http://github.com/nemonik/Intellect) and ``run python setup.py install``.

# Dependencies

- ANTLR3 Python Runtime 3.1.3
- Python itself, if you don't already have it.  I tested the code on
Python 2.7.1 and 2.7.2. 

## Contribution

The source code is available under the BSD 4-clause license. If you have ideas, code, bug reports, or fixes you would like to contribute please do so.

Bugs and feature requests can be filed at [Github](http://github.com/nemonik/Intellect).

# Background

The language and rule engine form a "production rule system", where computer
algorithms are used to provide some form of artificial intelligence, which
consists primarily of a set of rules about behavior. For the platform in the
Innovation Program, the network defender uses the DSL to confer policy, 
how the platform is to respond to network events mounted over covert 
network channels, but there are no direct ties written into the language 
nor the rule engine to cyber-security and thus the system in its 
entirety can be more broadly used in other domains.

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

# Background 

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


# Walkthrough

A walkthrough to get you jump-started.

## Facts (Data being reasoned over)

The interpreter, the rules engine, and the remainder of the code such as 
objects for conferring discrete network conditions, referred to as "facts",
are also authored in Python. Python's approach to the object-orientated programming
paradigm, where objects consist of data fields and methods, did not easily
lend itself to describing "facts". Because the data fields of a Python object 
referred to syntactically as â "attributes"â can and often are set on an 
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
reason over:

	1	class ClassA(object):
	2		'''
	3		An example fact
	4		'''
	5
	6		def __init__(self, property0 = None, property1 = None):
	7			'''
	8			ClassA initializer
	9			'''
	10			self._property0 = property0
	11
	12		@property
	13		def property0(self):
	14			return self._property0
	15
	16		@property0.setter
	17		def property0(self, value):
	18			self._property0 = value

## The Policy DSL

Example policy files can be found at the path _intellect/rulesets_, and must follow 
the Policy grammar as define in _intellect/grammar/Policy.g_.
 
### Import Statments (_ImportStmts_)

Import statement basically follow Python's with a few limitations (For 
example, The wild card form of import is not supported for the reasons
elaborated [here](http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html#importing)) 
and follow the Python 2.7.2 grammar. _ImportStmt_s exist only at the same level of 
_ruleStmt_s as per the grammar, and are typically at the top of a policy 
file, but are not limited to. In fact, if you break up your policy 
across several files the last imported as class or module wins as the
one being named.

### attributes

To be written.

### Rule Statements (_ruleStmt_) 

A rule statement at its simplest looks like so:

	22	rule "print":	
	23		then:
	24			print("hello world!!!!")

Rule "print" will always print "hello world!!!!" to the 'sys.stdout'.

More generally, a rule will have both a _when_- and _then_-portion, and
depending on the _when_-portion constraint will match facts in knowledge 
and return them to operated over in the _then-_portion of the rule. 

Such as in the rule "delete those that don't match", all facts of type 
ClassD who's property1 value is either a 1 or 2 or 3 will be deleted 
in _then-_portion of the rule. 

	1	from intellect.testing.ClassCandD import ClassD
	
	-- snip --
	
	10	rule "delete those that don't match":
	11		when:
	12			not $bar := ClassD(property1 in [1,2,3])
	13		then:
	14			delete $bar


### Regular Expressions in _ruleCondition_._classConstraint_._constraints_:

You can also use regular expressions in a Rule's _ruleCondition_ by 
importing the regular expression library straight from Python and 
then using like so...

From example:

	2	from intellect.testing.subModule.ClassB import ClassB 
	
	-- snip ---
	
	4	import re
	5
	6	rule rule_a:
	7		when:
	8			$classB := ClassB( re.search(r"\bapple\b", "apple")!=None and property2>5 and test.greaterThanTen(property2) and aMethod() == "a")

To keep the policy files from turning into just another Python script you
will want to keep as little code out of the policy file was possible... Use
the _modify_, _delete_, _insert_ grammar defined actions in the _then_-portions of
the _ruleStmt_ as well as using _simpleStatements_. If you are writing very
complicated constraints in the when-portions of a _ruleStmt_, consider moving 
the constraint into a method of fact being reasoned over.

For example, the above regular expression example would become:

	4	import re
	5	
	6	rule rule_a:
	7		when:
	8			$classB := ClassB(property1ContainsTheStrApple() and property2>5 and test.greaterThanTen(property2) and aMethod() == "a")

If you were to add the method to ClassB

	1	def property1ContainsTheStrApple()
	2		return re.search(r"\bapple\b", property1) != None

to ClassB. 

### _not_'ed _ruleCondition_:

A _ruleCondition_ may be _not_'ed as follows:

	21	rule rule_b:
	22		when:
	23			not $classB := ClassB( property1.startswith("apple") and property2>5 and test.greaterThanTen(property2) and aMethod() == "a")


and thus negate the condition and return matches as such to then-portion
of the rule to be operated on. 

### exists ruleCondition:

A ruleCondition may be prepended with _exists_ as follows:

	31	rule rule_c:
	32		when:
	33			exists $classB := ClassB(property1.startswith("apple") and property2>5 and test.greaterThanTen(property2) and aMethod() == "a")
	34		then:
	35			print( "matches" + " exist" )
	36			a = 1
	37			b = 2
	38			c = a + b
	39			print(c)
	40			test.helloworld()
	41			# call MyIntellect's bar method as it is decorated as callable
	42			bar()

and thus the _then_-portion of the _ruleStmt_ will be called once if there are
any object in memory matching the condition. The _action_ statements
_modify_ and _delete_ may not be used in the _then_-portion of a _ruleStmt_,
if _exists_' pre-pends the _when_-portions's _ruleCondition_.

### _agenda-group_ rule property

To be written.

###  _learn_, _modify_, _forget_, and _halt_ _actions_:

Earlier, I mentioned the use of _modify_, _delete_, _insert_ grammar 
defined _action_s in the _then_-portions of a rule.

#### _learn_ _action_

A rule entitled "Time to buy new sheep?" might look like the following:

	51	rule "Time to buy new sheep?":
	52		when:
	53			$buyOrder := BuyOrder( )
	54		then:
	55			print( "Buying a new sheep." )
	56			modify $buyOrder:
	57				count = $buyOrder.count - 1
	58			learn BlackSheep()

at line 58 illustrates the use of a _learn_ _action_ to learn/insert 
a BlackSheep fact. Line 58 can also be written as:

	58			insert BlackSheep()

#### _modify_ _action_ 

The following rule:
 
	51	rule "Time to buy new sheep?":
	52		when:
	53			$buyOrder := BuyOrder( )
	54		then:
	55			print( "Buying a new sheep." )
	56			modify $buyOrder:
	57				count = $buyOrder.count - 1
	58			learn BlackSheep()

illustrates the use of a _modify_ _action_ starting at line 56 to modify 
each BuyOrder match returned by the rule's _when_-portion. Cannot be used 
in conjunction with _exists_ rule conditions. The _modify_ _action_ can 
also be used to chain _ruleStmts_, what you do is modify the fact (toggle 
a boolean property, set a property's value, et cetera) 
and then use this property to evaluate in the proceeding _ruleStmt_.

#### _forget_ _action_

A rule entitled "Remove empty buy orders" might look like the following:

	60	rule "Remove empty buy orders":
	61		when:
	62			$buyOrder := BuyOrder( count == 0 )
	63		then:
 	64			forget $buyOrder

at line 64 illustrates the use of a _forget_ _action_ to forget/delete each match 
returned by the rule's _when_-portion. Line 64 can also be written as:

	64			delete $buyOrder

Note: cannot be used in conjunction with _exists_.

#### _halt_ _action_

The following rule:

    66	rule "End policy":
    67		then:
    68			log("Finished reasoning over policy.", "example", logging.DEBUG)
    69			halt

at line 68 illustrates the use of a _halt_ _action_ to tell the rules
engine to halt reasoning over the policy.

### Simple Statements (_SimpleStmt_):

_SimpleStmts_ are supported actions for _then_-portion of a rule, and so one 
can do the following:

	31	rule rule_c:
	32		when:
	33			exists $classB := ClassB(property1.startswith("apple") and property2>5 and test.greaterThanTen(property2) and aMethod() == "a")
	34		then:
	35			print("matches" + " exist")
	36			a = 1
	37			b = 2
	38			c = a + b
	39			print(c)
	40			test.helloworld()
	41			bar()

The _simpleStmt_s on lines 35 through 41 can be executed if any facts in
knowledge exist matching the _ruleCondition_.

### _attribute_ statements

To be written.

## Creating and using a Rules Engine with a policy

At its simplest a rules engine can be created and used like so:

	1	import sys, logging
	2	
	3	from intellect.Intellect import Intellect
	4	from intellect.Intellect import Callable
	5
	6	# set up logging
	7	logging.basicConfig(level=logging.DEBUG,
	8	format='%(asctime)s %(name)-12s%(levelname)-8s%(message)s',
	9		#filename="rules.log")
	10		stream=sys.stdout)
	11
	12	intellect = Intellect()
	13
	14	policy_a = intellect.learn("../rulesets/test_a.policy")
	15
	16	intellect.reason()
	17
	18 	intellect.forget_all()


It may be preferable for you to sub-class _intellect.Intellect.Intellect_ class in 
order to add _@Callable_ decorated methods that will in turn permit these methods
to be called from the _then_-portion of the rule.
 
For example, _MyIntellect_ is created to sub-class _Intellect_:

	1	import sys, logging
	2
	3	from intellect.Intellect import Intellect
	4	from intellect.Intellect import Callable
	5
	6	class MyIntellect(Intellect):
	7
	8		@Callable
	9		def bar(self):
	10			self.log(logging.DEBUG, ">>>>>>>>>>>>>>  called MyIntellect's bar method as it was decorated as callable.")
	11
	12	if __name__ == "__main__":
	13
	14		# set up logging
	15		logging.basicConfig(level=logging.DEBUG,
	16			format='%(asctime)s %(name)-12s%(levelname)-8s%(message)s',
	17			#filename="rules.log")
	18			stream=sys.stdout)
	19
	20		print "*"*80
	21		print """create an instance of MyIntellect extending Intellect, create some facts, and exercise the MyIntellect's ability to learn and forget"""
	22		print "*"*80
	23
	24		myIntellect = MyIntellect()
	25
	26		policy_a = myIntellect.learn("../rulesets/test_a.policy")
	27
	28		myIntellect.reason()
	29
	30		myIntellect.forget_all()

The policy could then be authored, where _MyIntellect_'s _bar_-method is called on line 24 for matches 
to the _ruleCondition_ on line 11, like so:

	1	from intellect.testing.subModule.ClassB import ClassB
	2	import intellect.testing.Test as Test
	3	import logging
	4
	5	fruits_of_interest = ["apple", "grape", "mellon", "pear"]
	6	count = 5
	7
	8	rule rule_a:
	9		agenda-group test_a
	10		when:
	11			$classB := ClassB( property1 in fruits_of_interest and property2>count ) 
	12		then:
	13			# mark the 'ClassB' matches in memory as modified
	14			modify $classB:
	15				property1 = $classB.property1 + " pie"
	16				modified = True
	17				# increment the match's 'property2' value by 1000
	18				property2 = $classB.property2 + 1000
	19
	20			attribute count = $classB.property2
	21			print "count = {0}".format( count )
	22
	23			# call MyIntellect's bar method as it is decorated as callable
	24			bar()
	25			log(logging.DEBUG, "rule_a fired")

