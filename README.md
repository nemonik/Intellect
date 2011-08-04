_My appologies, a better readme will follow..._

# Overview

Intellect is a DSL (“Domain-Specific Language”) and Rule Engine for Python
Auhtored by Michael Joseph Walsh for expressing policies to orchestrate and
control a dynamic network defense cyber-security platform being researched
in The MITRE Corporation's Innovation Program. 

The language and rule engine form a "production rule system", where computer
algorithms are used to provide some form of artificial intelligence, which
consists primarily of a set of rules about behavior. For platform, the 
network defender uses the DSL to confer policy, how the platform is to 
respond to network events mounted over covert network channels, but there 
are no direct ties written into the language nor the rule engine
to cyber-security, and thus the system in its entirety could be more broadly
used in other domains.

Many production rule system implementations have been open-sourced, such as
JBoss Drools, Rools, Jess, Lisa, et cetera. These are available for other
languages for expressing production rules, but it is the author's belief 
that Python is under-represented, and as such the language and rule engine 
could benefit from an open source release.

The MITRE Corporation was granted release August 4, 2011.

Thus, releasing the domain-specific language (DSL) and Rule Engine to Open
Source in the hopes doing so will extend its use and increase its chances 
for possible adoption, while at the same time mature the project with more 
intereted eyeballs being placed on it.

# Walkthrough

A walkthrough to get you jump-started.

## Dependencies

You need to download and install the  ANTLR3 Python Runtime.

Tested on Python 2.7.1 and 2.7.2. 

## The Policy DSL

### Background 

Starting out, it was initially assumed the platform would be integrated with
the best Open Source rules engine available for Python as there are
countless implementation for Ruby, Java, and Perl, but surprisingly found
none fitting the project's needs. This led to the thought of inventing one;
simply typing the keywords “python rules engine” into Google though will
return to you the advice “to not invent yet another rules language”, but
instead you are advised to “just write your rules in Python, import them,
and execute them.” The basis for this advice can be coalesced down to doing
so otherwise does not fit with the “Python Philosophy.” At the time, I did
not believe this to be true, nor fully contextualized, and yet admittedly, I
had not yet authored a line of Python code nor used ANTLR3 prior to this
effort. Looking back, I firmly believe the act of inventing a rules engine
and abstracting it behind a nomenclature that describes and illuminates a
specific domain is the best way for the network defender to think about the
problem. 

As there were no rules engines available for Python fitting the platforms
needs, a policy language and naive forward chaining rules engine were built 
from scratch. The policy language's grammar is based on a subset of Python 
language syntax.  The policy DSL is parsed and lexed with the help of the 
ANTLR3 Parse Generator and  Runtime for Python. 

The interpreter, the rules engine, and the remainder of the code such as 
objects for conferring discrete network conditions, referred to as "facts",
are also authored in Python. Python’s approach to the object-orientated programming
paradigm, where objects consist of data fields and methods, did not easily
lend itself to describing "facts". Because the data fields of a Python object 
referred to syntactically as “attributes” can and often are set on an 
instance of a class, they will not exist prior to a class’s instantiation. 
In order for a rules engine to work, it must be able to fully “introspect” an 
object instance representing a condition. This proves to be very difficult 
unless the property decorator with its two attributes, “getter” and “setter”, 
introduced in Python 2.6, are adopted and formally used for authoring these objects. 
Coincidentally, the use of the “Getter/Setter Pattern” used frequently in 
Java is singularly frowned upon in the Python developer community with the 
cheer of “Python is not Java.”

Example policy files can be foud in intellect/rulesets, and must follow 
the Policy grammar as define in intellect/grammar/Policy.g
 
### ImportStmts

Import statement basically follow Python's with a few limitations (For 
example, The wild card form of import is not supported for the reasons
elabortated
[here](http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html#importing)) 
and follow the Python 2.7.2 grammar. _ImportStmt_s exist only at the same level of 
_ruleStmt_s as per the grammar, and are typically at the top of a policy 
file, but are not limitted to. In fact if you break up your policy 
across several files the last imported as class or module wins as the
one being named.

### ruleStmt 

A rule statment at its simplest looks like so:

	22	rule "print":	
	23	        then:
	24	                print("hello world!!!!")

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
	11	        when:
	12	                not $bar := ClassD(property1 in [1,2,3])
	13	        then:
	14	                delete $bar  


### Regular Expressions in ruleCondition.classConstraint.constraints:

You can also use regular expressions in a Rules' _ruleCondition_ by 
importing the regular expression library straight from Python and 
then using like so...

From example:

	2	from intellect.testing.subModule.ClassB import ClassB 
	
	-- snip ---
	
	4	import re
	5	
	6	rule rule_a:
	7	        when:
	8	                $classB := ClassB( re.search(r"\bapple\b", "apple")!=None and property2>5 and test.greaterThanTen(property2) and aMethod() == "a")

To keep the policy files from turning into just another Pytyhon script you
will want to keep as little code out of the policy file was possible... Use
the _modify_, _delete_, _insert_ grammar defined actions in the _then_-portions of
the _ruleStmt_ as well as using _simpleStatements_. If you are writing very
complicated constraints in the when-portions of a ruleStmt, consider moving 
the constraint into a method of fact being reasoned over.

For example, the above regular expression example would become:

	4	import re
	5	
	6	rule rule_a:
	7	        when:
	8	                $classB := ClassB(property1ContainsTheStrApple() and property2>5 and test.greaterThanTen(property2) and aMethod() == "a")

If you were to add the method

	def property1ContainsTheStrApple()
       		return re.search(r"\bapple\b", property1) != None

to ClassB. 

### not'ed ruleCondition:

A _ruleCondition_ may be _not_'ed as follows:

	21	rule rule_b:
	22	        when:
	23	                not $classB := ClassB( property1.startswith("apple") and property2>5 and test.greaterThanTen(property2) and aMethod() == "a")


and thus negate the condition and return matches as such to the then-portion
of the rule to be operated on. 

### exists ruleCondition:

A ruleCondition may be prepended with _exists_ as follows:

	31	rule rule_c:
	32	        when:
	33	                exists $classB := ClassB(property1.startswith("apple") and property2>5 and test.greaterThanTen(property2) and aMethod() == "a")
	34	        then:
	35	                print("matches" + " exist")     
	36	                a = 1
	37	                b = 2
	38	                c = a + b
	39	                print(c)
	40	                test.helloworld()               
	41	                # call MyIntellect's bar method as it is decorated as callable
	42			bar()

and thus the _then_-portion of the _ruleStmt_ will be called once if there are
any object in memory matching the condition. The _action_ statements
_modify_ and _delete_ may not be used in the _then_-portion of a ruleStmt, 
if _exists_' pre-pends the _when_-portions's _ruleCondition_. 

### modify, delete, and insert actions:

Earlier, I mentioned the use of _modify_, _delete_, _insert_ grammar 
defined _action_s in the _then_-portions of a rule.

The following:
 
	13	                modify $classB:
	14	                        # add " hell world" to 'property1' of 'ClassB' matches
	15	                        property1 = $classB.property1 + " " + test.helloworld()
	16	                        # return true from the ClassB's 'trueValue()' methond and use it to set the matches modified property
	17	                        modified = $classB.trueValue()
	18	                        # increment the matche's 'property2' value by 1000
	19	                        property2 = $classB.property2 + 1000

illustrates the use of a _modify_ _action_ to modify each match returned by
rule_a's _when_-portion. Cannot be used in conjunction with _exists_. The
_modify_ _action_ can also be used to chain _ruleStmts_, what you do is 
modify the fact (toggle a boolean property, set a property's value, et cetera) 
and then use this property to evaluate in the proceeding _ruleStmt_.

A rule entitlled  "delete those that don't match" might look like the following:

	10	rule "delete those that don't match":
	11	        when:
	12	                not $bar := ClassD(property1 in [1,2,3])
	13	        then:
	14	                delete $bar    

illustrates the use of a _delete_ _action_ to delete each match returned by
the rule's _when_-portion. Cannot be used in conjunction with _exists_.

For _insert_, rule "insert ClassD" might look like the following:

	26	rule "insert ClassD":
	27	        then:
	28	                insert ClassD("foobar")

and illustrates the use of an insert action to insert a ClassD fact. 

### SimpleStmt statements:

_SimpleStmts_ are supported  actions for _then_-portion of a rule, and so one 
can do the following:

	31	rule rule_c:
	32	        when:
	33	                exists $classB := ClassB(property1.startswith("apple") and property2>5 and test.greaterThanTen(property2) and aMethod() == "a")
	34	        then:
	35	                print("matches" + " exist")     
	36	                a = 1
	37	                b = 2
	38	                c = a + b
	39	                print(c)
	40	                test.helloworld()               
	41	                intellect.bar()

The simpleStmts on lines 35 through 41 can be executed if any facts in
knowledge exist matching the _ruleCondition_.


## Creating and using a Rules Engine with a policy

A rules engine is created and used like so:

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


