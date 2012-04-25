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
Node

Description:
    Contains all the Node objects for the Policy grammar and forms the model.

Initial Version:
    Feb 9, 2011

@author: Michael Joseph Walsh
"""

import logging, types, collections, keyword, uuid

import intellect.reflection as reflection

from intellect.Callable import Callable
import intellect.IO as IO


class Node(object):
    '''
    All Policy Domain Specific Language (DSL) Nodes extend this node.
    '''

    def __init__(self, children = None, line = None, column = None):
        '''
        Node Initializer
        '''

        if not children:
            children = []
        elif not isinstance(children, list):
            children = [children]

        self._children = children
        self._line = line
        self._column = column

        self._file = None


    def __str__(self):
        '''
        Returns a str for this node and its children for what they represent
        in the policy.
        '''
        value = ""

        for child in self._children:

            value += str(child) + " "

        value = value.rstrip()

        return value


    def str_tree(self, text = "", indentCount = 0):
        '''
        Returns a textual tree representation of the Node and its
        children nodes.  Used for debugging purposes.
        '''
        text = text + "   "*indentCount + self.__class__.__name__ + "\n"

        for child in self._children:
            if isinstance(child, Node):
                text += child.str_tree("", indentCount + 1)
            else:
                text += "   "*(indentCount + 1) + child + "\n"

        return text


    @property
    def children(self):
        '''
        Returns a list, either empty or containing one or more children Node
        objects for this node.
        '''
        return self._children


    @children.setter
    def children(self, value):
        '''
        Sets the children list for this node.
        '''
        if not isinstance(value, (list, types.NoneType)):
            raise TypeError, "Parameter 'value' must be a List or NoneType."

        if value is None:
            value = []

        self._children = value


    def first_child(self):
        '''
        Returns the node's first child, if it has one; otherwise, None.
        '''
        if (not self.children):
            return None
        else:
            return self.children[0]


    def append_child(self, child):
        '''
        Appends a child to the node.  The child can be either a basestring
        or Node object, and nothing else.
        '''

        # cannot add None
        if not child:
            raise TypeError, "Parameter 'child' cannot be None."

        # must be either a basestring or Node object
        if not isinstance(child, (basestring, Node)):
            raise TypeError, "Parameter 'child' must be a basetring or Node."

        # if children is not yet a list, make it a list object
        if not self.children:
            self.children = []

        # append the bloody damn child
        self.children.append(child)


    def append_children(self, children):
        '''
        Append a list of siblings to the node
        '''

        # can't add None
        if not children:
            raise TypeError, "Parameter 'children' cannot be an empty list."

        # must be a list
        if not isinstance(children, list):
            raise TypeError, "Parameter 'children' must be a list."

        # iterate through the children to be added and
        # verify they are of the correct type, if not
        # raise a TypeError
        for child in children:
            if not isinstance(child, (basestring, Node)):
                raise TypeError, str(child) + " must be a basetring or Node."

        # if children is not yet a list, make it a list object
        if not self.children:
            self.children = []

        # append the bloody damn siblings
        self.children.extend(children)


    def insert_child_at(self, index, child):
        '''
        Inserts a sibling at a given position. The first argument is the
        index of the element before which to insert, so a.insert(0, child)
        inserts at the front of the list of children, and
        a.insert(len(self.children), child) is equivalent to append_child(child).
        Parameter 'index' cannot be a value less than 0 or greater than
        len(self.children)
        '''

        # cann't add None
        if not child:
            raise TypeError, "Parameter 'child' cannot be None."

        # must be either a basestring or Node object
        if not isinstance(child, (basestring, Node)):
            raise TypeError, "Parameter 'child' must be a basetring or Node."

        # if children is not yet a list, make it a list object
        if not self.children:
            self.children = []

        if index > len(self.children) or index < 0:
            raise ValueError, "Parameter 'index' cannot be a value less than 0 or greater than {0}. A value of {1} was passed.".format(len(self.children), index)

        self.children.insert(index, child)


    def insert_children_at(self, index, children):
        '''
        Inserts siblings at a given position. The first argument is the
        index of the element before which to insert, so a.insert(0, child)
        inserts at the front of the list of children, and
        a.insert(len(self.children), child) is equivalent to append_child(child).
        Index cannot be a value less than 0 or greater than len(self.children)
        '''

        # can't add None
        if not children:
            raise TypeError, "Parameter 'children' cannot be an empty list."

        # must be a list
        if not isinstance(children, list):
            raise TypeError, "Parameter 'children' must be a list."

        # iterate through the children to be added and
        # verify they are of the correct type, if not
        # raise a TypeError
        for child in children:
            if not isinstance(child, (basestring, Node)):
                raise TypeError, str(child) + " must be a basetring or Node."

        # if children is not yet a list, make it a list object
        if not self.children:
            self.children = []

        # insert the bloody damn siblings
        for child in children:
            self.insert_child_at(index, children)
            index += 1


    @property
    def line(self):
        '''
        Get the int value for the line in the policy file
        corresponding to this node.

        Used when raising errors or debugging.
        '''
        return self._line


    @line.setter
    def line(self, value):
        '''
        Set the corresponding int value for the line
        in policy file that corresponds to this node.

        Used when raising errors or debugging.
        '''

        # must be a int or None object otherwise
        # raise a TypeError
        if isinstance(value, (int, types.NoneType)):
            self._line = value
        else:
            raise TypeError, "Must be an int or NoneType."


    @property
    def column(self):
        '''
        Get the corresponding int value for the column
        in policy file that begins this node.

        Used when raising errors or debugging.

        TODO:  The value I am getting from ANTLR3
        is off as I am post parsing the token stream.
        So, I stripped the code out of the
        grammar setting this value.
        '''
        return self._column


    @column.setter
    def column(self, value):
        '''
        Set int value for the column number in the policy
        file corresponding to this node. Used when raising
        errors or debugging.

        TODO:  The value I was getting from ANTLR3
        seemed off.  So, I stripped the code out of the
        grammar setting this value.
        '''
        if isinstance(value, (int, types.NoneType)):
            self._column = value
        else:
            raise TypeError, "Must be an int."


    @property
    def file(self):
        '''
        Returns the File Node that defines this Node.
        '''
        return self._file


    @file.setter
    def file(self, value):
        '''
        The File Node that defines this node
        '''
        if isinstance(value, File):
            self._file = value
        else:
            raise TypeError, "'file' must be of type File."


    def append_global(self, object_reference, value):
        #print locals()
        self.globals[object_reference] = value


    def log(self, msg, name = "intellect", level = logging.DEBUG):
        '''
        Logs at the 'level' for the messaged 'msg'

        Args:
            name: the name of the logger
            level:  must be either logging.DEBUG, logging.INFO, logging.WARNING,
                logging.ERROR, logging.CRITICAL
            msg: message string
        '''

        if level not in [logging.DEBUG, logging.INFO, logging.WARNING,
                logging.ERROR, logging.CRITICAL]:
            raise ValueError, "'level' must be either logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL"

        logging.getLogger(name).log(level, "{0}.{1} :: {2}".format(self.__class__.__module__, self.__class__.__name__, msg))


    @staticmethod
    def filter_to_list(type, node, list = None):
        '''
        Returns a list of nodes of 'type' parameter found
        in the tree who's parent node is the 'node' parameter.

        Args:
            node: The parent node to start from.
            type: A class which extends Node.
            list: Initially set to [], used to pass the
                list around so that matches can be appended
                to it.
        '''

        if list is None:
            list = []

        for child in node.children:
            if isinstance(child, Node):
                if isinstance(child, type):
                    list.append(child)
                Node.filter_to_list(type, child, list)

        return list


    @staticmethod
    def is_name(string):
        '''
        Returns True, if the string parameter is a grammar defined NAME token

        Args:
            string: str to validate
        '''
        if not isinstance(string, basestring):
            # Name tokens must be a str object.
            return False
        else:
            if not string:
                #Name tokens cannot be empty str object.
                return False

            if not string[0].isalpha() and string[0] != "_":
                #Name tokens must begin with an alpha character
                return False

            for char in string[1:]:
                if not char.isalpha() and char != "_" and not char.isdigit():
                    return False

        return True


    @staticmethod
    def unique_identifier(expressionStr, identifier):
        '''
        Returns a unique identifier protecting against collisions with
        'identifier' with identifiers found in 'expression'
        '''
        if expressionStr.find(identifier) == -1:
            return identifier

        keepTrying = True

        while (keepTrying):
            collisionProtectedIdentifier = ((identifier + "_") if identifier else "") + str(uuid.uuid1()).replace("-", "_")
            if expressionStr.find(collisionProtectedIdentifier) == -1:
                keepTrying = False

        return collisionProtectedIdentifier



# S P E C I F I C   N O D E   C L A S S E S

class Policy(Node):
    '''
    A Policy node. The entrant Node for the Policy DSL.
    Meaning: you start here to reason...
    '''


    def __str__(self):
        '''
        Returns a str representation of the policy.
        '''
        value = ""

        for child in self.children:
            value += str(child) + "\n"

        return value


    def __init__(self, children = None,  line = None, column = None):

        super(Policy,self).__init__(children, line, column)

        self._intellect = None
        self._globals = {}
        self._halt = False


    @property
    def intellect(self):
        '''
        Returns the associated Intellect object executing the policy.
        '''
        return self._intellect


    @intellect.setter
    def intellect(self, value):
        '''
        Associates the Intellect object executing the policy to the policy so
        that the policy can call its methods, etc...
        '''
        if isinstance(value, reflection.class_from_str("intellect.Intellect.Intellect")):
            self._intellect = value
        else:
            raise TypeError, "'intellect' must be of type Intellect."


    @property
    def globals(self):
        '''
        Returns the policy's globals.

        Contains both imports and policy attributes.
        '''
        return self._globals


    @globals.setter
    def globals(self, value):
        '''
        Sets the policy's globals.
        '''
        if isinstance(value, dict):
            self._globals = value
        else:
            raise TypeError, "'globals' must be of type dictionary."


    @property
    def halt(self):
        '''
        Returns the policy's halt flag.
        '''
        return self._halt


    @halt.setter
    def halt(self, value):
        '''
        Sets the policy's halt flag.
        '''
        if isinstance(value, bool):
            self._halt = value
        else:
            raise TypeError, "'halt' must be of type bool."


    @property
    def files(self):
        '''
        Convienance method to return all the policy files
        comprising the policy.  Otherwise, once could simply
        call the children properties method on this instance.
        Calling this just makes the code more readable.
        '''
        return self.children


    @files.setter
    def files(self, value):
        '''
        Convienance method to set the policy files
        comprising the policy.  Otherwise, once could simply
        call the children setter method on this instance.
        Calling this just makes the code more readable.
        '''
        self.children = value


    @property
    def file_paths(self):
        '''
        Convienance method to return the policy file paths
        as a list.

        None is returned for file nodes learned from strings.
        '''
        return [file_node.path for file_node in self.files]


    @property
    def importStmts(self):
        '''
        Returns either an empty list or a list containing
        one or more ImportStmt objects
        '''

        importStmts = []

        for file in self.files:
            importStmts.extend(file.importStmts)

        return importStmts


    @property
    def ruleStmts(self):
        '''
        Returns either an empty list or a list containing
        one or more RuleStmt objects
        '''
        ruleStmts = []

        for file in self.files:
            ruleStmts.extend(file.ruleStmts)

        return ruleStmts


    @property
    def attributeStmts(self):
        '''
        Returns either an empty list or a list containing
        one or more AttributeStmts
        '''
        attributeStmts = []

        for file in self.files:
            attributeStmts.extend(file.attributeStmts)

        return attributeStmts


    def eval(self, agenda):
        '''
        Eval the policy
        '''

        # reset halt to false
        self.halt = False

        if not isinstance(agenda, (list, types.NoneType)):
            raise TypeError, "Parameter 'agenda' must be a List or NoneType."

        if not agenda:
            agenda = ["MAIN"]

        self.log("agenda: {0}".format(agenda))

        # put the imports into the policy's global namespace
        for importStmt in self.importStmts:
            try:
                self.log("Evaluating: {0}".format(importStmt))
                exec(str(importStmt), self.globals)
            except ImportError as error:
                raise ImportError, error.message + " at line: {0} from policy file: '{1}'".format(importStmt.line, importStmt.file.path)

        # put the policy attributes into the policy's global namespace
        for attributeStmt in self.attributeStmts:
            # check for issues
            for atom in [atom for atom in Node.filter_to_list(Atom, attributeStmt.expressionStmt.children[0]) if len(atom.children) is 1]:
                if atom.first_child() in keyword.kwlist:
                    raise SyntaxError, "invalid syntax:  global '{0}' is a reserved keyword: {1} from policy file: '{2}'.".format(atom.first_child(), attributeStmt.line, atom.file.path)

            # add globals to the namespace
            self.log("Evaluating: {0}".format(attributeStmt))
            exec(str(attributeStmt), self.globals)

        if self.ruleStmts:

            self.log("Evaluating ruleStmts")

            # fire the rules in order according to the agenda
            # until all fired or told to halt
            for agenda_group in agenda:

                iterator = iter(self.ruleStmts)

                while not self.halt:
                    try:
                        ruleStmt = iterator.next()
                    except StopIteration:
                        break

                    if (ruleStmt.agenda_group_id == agenda_group):
                        self.log("Evaluating: '{0}' from agenda group '{1}'".format(ruleStmt.id, ruleStmt.agenda_group_id))
                        ruleStmt.eval(self)
                    else:
                        self.log("Ignoring: '{0}' from agenda group '{1}' as it is not on the agenda".format(ruleStmt.id, ruleStmt.agenda_group_id))
                else:
                    self.log("Halting...")


class File(Node):
    '''
    A File Node containing zero or more ImportStmt or
    RuleStmt nodes.
    '''

    def __init__(self, children = None,  line = None, column = None):

        super(File,self).__init__(children, line, column)

        self._path = None

    @property
    def path(self):
        '''
        Returns source file path this node is contained in
        '''
        return self._path


    @path.setter
    def path(self, value):
        '''
        Sets the source file path this node is contained in.
        None if created from dynamically from string.
        '''
        if isinstance(value, (basestring, types.NoneType)):
            self._path = value
        else:
            raise TypeError, "'path' must be of type string or None."


    @property
    def importStmts(self):
        '''
        Returns either an empty list or a list containing
        one or more ImportStmt objects
        '''
        return [child.first_child() for child in self.children if isinstance(child.first_child(), ImportStmt)]


    @property
    def ruleStmts(self):
        '''
        Returns either an empty list or a list containing
        one or more RuleStmt objects
        '''
        return [child.first_child() for child in self.children if isinstance(child.first_child(), RuleStmt)]


    @property
    def attributeStmts(self):
        '''
        Returns either an empty list or a list containing
        one or more AttributeStmts
        '''
        return [child.first_child() for child in self.children if isinstance(child.first_child(), AttributeStmt)]



    @staticmethod
    def set_file_on_descendants(node = None, file_node = None):
        '''
        Sets this node's file property and all its descendants'
        file property to file_node.
        '''

        if not isinstance(node, (Node, types.NoneType)):
            raise TypeError, "'node' must be of type Node."

        node.file = file_node

        for child in node.children:
            if isinstance(child, Node):
                child.file = file_node
                File.set_file_on_descendants(child, file_node)


class Statement(Node):
    '''
    A Statement Node containing an import or global or rule statement
    '''



class AttributeStmt(Statement):
    '''
    An AttributeStmt (Attribute Statement) Node for a Policy Node
    '''

    @property
    def expressionStmt(self):
        '''
        Returns the ExpressionStmt object for the global.
        '''
        return self.children[0]



class RuleStmt(Statement):
    '''
    A RuleStmt (Rule Statement) Node for a Policy Node
    '''

    def __str__(self):
        '''
        Returns a str representation of RuleStmt as it would be written in a policy.
        '''

        when = self.filter_to_list(When, self)
        then = self.filter_to_list(Then, self)

        print "when : {0}".format(when)
        print "then : {0}".format(then)

        value = "rule {0}:\n".format(self.children[1])

        if when != []:
            for line in str(when[0]).splitlines():
                value += "\t" + line + "\n"

        for line in str(then[0]).splitlines():
            value += "\t" + line + "\n"

        return value


    @property
    def id(self):
        '''
        Returns the Id object for the rule.
        '''
        return self.children[1]


    @property
    def ruleAttributes(self):
        '''
        Returns the RuleAttribute nodes associated with this rule.
        '''
        return [child for child in self.children if isinstance(child, RuleAttribute)]


    @property
    def agenda_group_id(self):
        '''
        Returns the agenda_group id for the rule.
        '''

        if self.ruleAttributes:
            agenda_group = [attribute.children[0] for attribute in self.ruleAttributes if isinstance(attribute.children[0], AgendaGroup)]

            if agenda_group:
                # the last one defined wins
                return str(agenda_group[-1].id)

        # otherwise return default
        return "MAIN"


    @property
    def when(self):
        '''
        Returns the When node, if it exists otherwise None as the When node
        is optional as per the grammar.
        '''
        whenChild = [child for child in self.children if isinstance(child, When)]

        if not whenChild:
            return None
        else:
            return whenChild[0]


    @property
    def then(self):
        '''
        Returns the mandatory Then node.
        '''
        return [child for child in self.children if isinstance(child, Then)][0]


    def eval(self, policy):
        '''
        Evaluate the RuleStmt over known objects held within the associated
        Intellect object.
        '''
        self.log("Evaluating rule: '{0}' from policy file: '{1}'".format(self.id, self.file.path))

        if self.when:
            whenResults = self.when.eval(policy, self)
        else:
            # Automatically fire the Then portion of the rule, if no When
            # portion exists.
            Result = collections.namedtuple('Result', 'fireThen, matches, objectBinding')

            whenResults = Result(fireThen = True, matches = [], objectBinding = None)

        self.log("When results for '{0}':  {1}".format(self.id, whenResults))

        if whenResults.fireThen:
            # fire the Then portion of the rule
            self.then.eval(policy, self, whenResults.matches, whenResults.objectBinding)
        else:
            self.log("When portion of {0} evaluated false, not firing Then portion".format(self.id))



class RuleAttribute(Node):
    '''
    A RuleAttribute Node containing an AgendaGroup attribute for a Rule Statement
    '''



class AgendaGroup(Node):
    '''
    An AgendaGroup Node
    '''

    @property
    def id(self):
        '''
        Returns the Id object for the AgendaGroup.
        '''
        return self.children[1]



class When(Node):
    '''
    A When Node for a RuleStmt Node.
    '''
    def __str__(self):
        '''
        Returns a str representation of When as it would be written in a policy.
        '''
        value = "when:\n"
        value += "\t{0}".format(self.ruleCondition)

        return value


    @property
    def ruleCondition(self):
        '''
        Returns a RuleCondition object.
        '''
        filter = [child for child in self.children if isinstance(child, RuleCondition)]

        if not filter:  # True, if filter is []
            return None
        else:
            return filter[0]


    @ruleCondition.setter
    def ruleCondition(self, value):
        raise NotImplementedError, "ruleCondition property cannot be set."


    def eval(self, policy, ruleStmt):
        '''
        Evaluate the when portion.
        '''

        # If True trigger the Then portion of the Rule; otherwise, don't.
        fireThen = False

        # Hold the learned object's matching the ClassConstraint.constraint
        matches = []

        # Holds the object binding for the ClassConstraint, if it exists;
        # otherwise is None
        objectBinding = None

        # Holds the Class-type described by ClassConstraint.name, if it exists;
        # otherwise is None
        klazz = None

        if self.ruleCondition:

            # The When portion of the rule has a RuleCondition

            classConstraint = self.ruleCondition.notCondition.condition.classConstraint

            #self.log(classConstraint.str_tree())

            # Determine the ClassConstraint.name'ed class-type
            klazz = reflection.class_from_string(classConstraint.name, policy)

            if classConstraint.constraint:

                # create 'localScope' dict and add 'policy' and 'klazz' to it
                localScope = {}
                localScope["policy"] = policy
                localScope["klazz"] = klazz

                # Rewrite the ClassConstraint.constraint
                rewrittenConstraint = When.rewrite(classConstraint.constraint, Constraint(), klazz)

                # Build the list comprehension used to filter the learned
                # objects down to matches for the ClassConstraint Constraint
                code = "matches = [fact for fact in policy.intellect.knowledge if "

                # Restrict the list comprehension to just the
                # ClassConstraint.name'ed class-type
                code += "isinstance(fact, klazz) and "

                # Append 'not' prior to the Constraint, if the negated
                code += "not (" if self.ruleCondition.notCondition.is_negated() else ""

                # Use the rewritten ClassConstraint Constraint to filter the
                # learned objects
                code += str(rewrittenConstraint) + (")" if self.ruleCondition.notCondition.is_negated() else "") + "]"

                self.log("Filter using the following list comprehension: {0}".format(code))

                try:
                    # Execute the dynamically built list comprehension code

                    self.log("policy.globals.keys = {0}".format(policy.globals.keys()))
                    self.log("localScope = {0}".format(localScope.keys()))
                    exec(code, policy.globals, localScope)

                    matches = localScope["matches"]

                except Exception as error:
                    raise SyntaxError("{0} in rule: '{1}', near line: {2} in policy file: '{3}'".format(error, ruleStmt.id, self.line, self.file.path))

                self.log("The matches found in memory: {0}".format(matches))
            else:
                # not having a ClassConstraint.constraint
                if not self.ruleCondition.notCondition.is_negated():
                    # match all the learned objects of ClassConstraint.name'ed class-type
                    self.log("match all the learned objects of ClassConstraint.name'ed class-type")
                    matches = [fact for fact in policy.intellect.knowledge if reflection.is_instance(fact, klazz)]
                else:
                    # match all the learned objects that are not the ClassConstraint.name'ed class-type
                    self.log("match all the learned objects that are not the ClassConstraint.name'ed class-type")
                    matches = [fact for fact in policy.intellect.knowledge if not reflection.is_instance(fact, klazz)]

                self.log("The matches found in memory: {0}".format(matches))

            if classConstraint.objectBinding:
                # hold the objectBinding, if it exists for later use
                objectBinding = classConstraint.objectBinding
                self.log("objectBinding is '{0}'".format(objectBinding))

            if self.ruleCondition.notCondition.condition.exists:
                #"The Condition holds an Exists token

                if not matches:
                    fireThen = False
                else:
                    # matches exist for the ClassConstraint.constraint,
                    # fire the Then portion of the rule
                    self.log("classConstraint prepended with 'exists'.")
                    fireThen = True
                    # the following no longer of relevance
                    matches = []
                    objectBinding = None
            else:
                # The Condition does not hold an Exists token
                if not matches:
                    fireThen = False
                    objectBinding= None
                else:
                    fireThen = True
        else:
            # The default is to fire then portion of the rule, if the When
            # portion of the rule has no RuleCondition
            fireThen = True

        # Create a new named tuple to hold the results
        Result = collections.namedtuple('Result', 'fireThen, matches, objectBinding')

        return Result(fireThen = fireThen, matches = matches, objectBinding = objectBinding)


    @staticmethod
    def rewrite(original, rewritten, klazz):
        '''
        A recursive method used to rewrite a Constraint object so that learned objects may
        be filtered.

        Args:
            original: Constraint to be rewritten.
            rewritten: used in recursion, the object to be written into.
            klazz: the object name by the ClassConstraint.name
        '''
        for child in original.children:
            if isinstance(child, Node):
                if isinstance(child, Power):
                    # inspect and rewrite, if necessary
                    if isinstance(child.first_child(), Atom) \
                        and Node.is_name(child.first_child().first_child()) \
                        and reflection.has_attribute(klazz, child.first_child().first_child()):
                        # The classConstraint.name used to signify the class the
                        # the constraint corresponds to has this (instance /
                        # class / static) method, property, or global.  So,
                        # rewrite the Constraint object by prepending "fact"
                        # before the first Atom object in this particular Power
                        # node.
                        #
                        # TODO: need a better string then "fact" as this may
                        # may already be used in the constraint
                        power = Power( [Atom( "fact" ), Trailer( [".", child.first_child().first_child()] )] )
                        rewritten.append_child( power )

                        if (len(child.children) > 1):
                            for c in child.children[1:]:
                                twin = type(c)()
                                power.append_child(When.rewrite(c, twin, klazz))
                    else:
                        # nothing matched to rewrite; so, clone
                        twin = type(child)()
                        rewritten.append_child(When.rewrite(child, twin, klazz))

                else:
                    # handle a child Node that is not of Power node
                    twin = type(child)()

                    rewritten.append_child(When.rewrite(child, twin, klazz))

            else:
                # handle a child that is a string
                rewritten.append_child(child)

        return rewritten



class Then(Node):
    '''
    A Then node for a RuleStmt Node.
    '''
    def __str__(self):
        '''
        Returns a str representation of Then as it would be written in a policy.
        '''
        value = "then:\n"

        for action in self.actions:
            for line in str(action).splitlines():
                value += "\t" + line + "\n"

        return value


    @property
    def actions(self):
        '''
        Returns a list of one one or more Action objects.
        '''
        return [child for child in self.children if isinstance(child, Action)]


    def eval(self, policy, ruleStmt, matches, objectBinding):
        '''
        Evaluate then portion.
        '''

        localScope = {}
        localScope["policy"] = policy

        # Insert into localScope all of Intellect's methods decorated as callable
        for method_name in [method_name for method_name in dir(policy.intellect) if isinstance(getattr(policy.intellect, method_name), Callable)]:
            if method_name in localScope:
                raise RuntimeWarning, "'Intellect method {0}' is already in local scope of the Then portion of rule: '{1}', define near line: {2} in policy file: '{3}'.  Consider renaming method.".format(method_name, ruleStmt.id, ruleStmt.line, self.file.path)
            else:
                localScope[method_name] = getattr(policy.intellect, method_name)

        if matches != []:
            # fire each action in sequence for each match
            for match in matches:

                localScope["match"] = match

                # process the actions
                for action in self.actions:

                    # needed as the Action object wraps the actual Action
                    actualAction = action.action

                    if isinstance(actualAction, ForgetAction):
                        # search through the objects that have been learned
                        # and delete the match

                        policy.intellect.forget(match)

                    elif isinstance(actualAction, LearnAction):

                        # create a newObject with the arguments, if provided,
                        # and append it to learned objects in memory
                        #
                        # TODO: use of the identifier "newFact" may
                        # be a  problem down the road...
                        code = "new_fact" + " = " + actualAction.name + "(" + (str(actualAction.argList) if actualAction.argList != None else "") +")"

                        self.log("Code to be run for learnAction in rule: '{0}' at line: {1} in the policy file: '{2}':\n{3}".format(ruleStmt.id, actualAction.line, self.file.path, code))

                        try:
                            # Execute the code
                            exec(str(code), policy.globals, localScope)
                        except Exception as error:
                            raise SyntaxError("{0} in rule: '{1}' at line: {2} in the policy file: '{3}'".format(error, ruleStmt.id, actualAction.line, self.file.path))

                        policy.intellect.learn(localScope["new_fact"])

                    elif isinstance(actualAction, ModifyAction):

                        # enumerate through known objects looking for the
                        # match, once found modify it using the
                        # PropertyAssignments described by the
                        # ModifyAction statement
                        for knowledgeIndex, fact in enumerate(policy.intellect.knowledge):
                            # TODO: modify the line below
                            if id(match) == id(fact):

                                for propertyAssignment in actualAction.propertyAssignments:

                                    try:
                                        self.log("value" + " = " + str(Then.rewrite(propertyAssignment.constraint, Constraint(), objectBinding)))
                                        exec("value" + " = " + str(Then.rewrite(propertyAssignment.constraint, Constraint(), objectBinding)), policy.globals, localScope)
                                    except Exception as error:
                                        raise SyntaxError("{0} in rule: '{1}' near line: {2} in the policy file: '{3}'".format(error, ruleStmt.id, actualAction.line, self.file.path))

                                    #if localScope["value"]:

                                    self.log("modifying {0} property {1} with value of {2} with assignment of {3}".format(objectBinding, propertyAssignment, localScope["value"], propertyAssignment.assignment))

                                    if (str(propertyAssignment.assignment) == "="):
                                        setattr(policy.intellect.knowledge[knowledgeIndex], propertyAssignment.name, localScope["value"])
                                    elif  (str(propertyAssignment.assignment) == "+="):
                                        setattr(policy.intellect.knowledge[knowledgeIndex], propertyAssignment.name, getattr(policy.intellect.knowledge[knowledgeIndex], propertyAssignment.name) + localScope["value"])
                                    elif  (str(propertyAssignment.assignment) == "-="):
                                        setattr(policy.intellect.knowledge[knowledgeIndex], propertyAssignment.name, getattr(policy.intellect.knowledge[knowledgeIndex], propertyAssignment.name) - localScope["value"])
                                    elif  (str(propertyAssignment.assignment) == "*="):
                                        setattr(policy.intellect.knowledge[knowledgeIndex], propertyAssignment.name, getattr(policy.intellect.knowledge[knowledgeIndex], propertyAssignment.name) * localScope["value"])
                                    elif  (str(propertyAssignment.assignment) == "/="):
                                        setattr(policy.intellect.knowledge[knowledgeIndex], propertyAssignment.name, getattr(policy.intellect.knowledge[knowledgeIndex], propertyAssignment.name) / localScope["value"])
                                    elif  (str(propertyAssignment.assignment) == "%="):
                                        setattr(policy.intellect.knowledge[knowledgeIndex], propertyAssignment.name, getattr(policy.intellect.knowledge[knowledgeIndex], propertyAssignment.name) % localScope["value"])
                                    elif  (str(propertyAssignment.assignment) == "&="):
                                        setattr(policy.intellect.knowledge[knowledgeIndex], propertyAssignment.name, getattr(policy.intellect.knowledge[knowledgeIndex], propertyAssignment.name) & localScope["value"])
                                    elif  (str(propertyAssignment.assignment) == "|="):
                                        setattr(policy.intellect.knowledge[knowledgeIndex], propertyAssignment.name, getattr(policy.intellect.knowledge[knowledgeIndex], propertyAssignment.name) | localScope["value"])
                                    elif  (str(propertyAssignment.assignment) == "^="):
                                        setattr(policy.intellect.knowledge[knowledgeIndex], propertyAssignment.name, getattr(policy.intellect.knowledge[knowledgeIndex], propertyAssignment.name) ^ localScope["value"])
                                    elif  (str(propertyAssignment.assignment) == "<<="):
                                        setattr(policy.intellect.knowledge[knowledgeIndex], propertyAssignment.name, getattr(policy.intellect.knowledge[knowledgeIndex], propertyAssignment.name) << localScope["value"])
                                    elif  (str(propertyAssignment.assignment) == ">>="):
                                        setattr(policy.intellect.knowledge[knowledgeIndex], propertyAssignment.name, getattr(policy.intellect.knowledge[knowledgeIndex], propertyAssignment.name) >> localScope["value"])
                                    else:
                                        setattr(policy.intellect.knowledge[knowledgeIndex], propertyAssignment.name, getattr(policy.intellect.knowledge[knowledgeIndex], propertyAssignment.name) // localScope["value"])

                                    # if had ended here

                                break

                    elif isinstance(actualAction, HaltAction):

                        policy.halt = True

                        self.log("Halt called in rule: '{0}' from policy file: '{1}'.".format(ruleStmt.id, self.file.path))

                        break

                    elif isinstance(actualAction, AttributeAction):

                        code = actualAction.write_prepend()
                        code += str(Then.rewrite(actualAction.children[1], SimpleStmt(), objectBinding))

                        self.execute(policy, ruleStmt, localScope, code)

                    else:

                        # Handle SimpleStmt

                        # Rewrite the statement
                        code = str(Then.rewrite(actualAction, SimpleStmt(), objectBinding))

                        self.execute(policy, ruleStmt, localScope, code)

        else:

            # fire each action in sequence, but only once

            for action in self.actions:

                # needed as the Action object wraps the actual Action
                actualAction = action.action

                if isinstance(actualAction, ForgetAction):

                    # As the ForgetAction acts on a specific match, one cannot
                    # have ForgetAction statements in then-portion of a rule
                    # who's when-portion evaluated on "exists".
                    raise SyntaxError, "forgetAction cannot exist in then portion as when portion is written for '{0}' at line: {1} in Policy: {2}".format(ruleStmt.id, actualAction.line, self.file.path)

                elif isinstance(actualAction, LearnAction):

                    # create a newObject with the arguments, if provided,
                    # and append it to learned objects in memory
                    code = "new_fact" + " = " + actualAction.name + "(" + (str(actualAction.argList) if actualAction.argList != None else "") +")"

                    self.log("Code to be run for learnAction in rule: '{0}' at line: {1} in the policy file: '{2}':\n{3}".format(ruleStmt.id, actualAction.line, self.file.path, code))

                    try:
                        # Execute the code
                        exec(str(code), policy.globals, localScope)
                    except Exception as error:
                        raise SyntaxError("{0} in rule: '{1}' at line: {2} in the policy file: '{3}'".format(error, ruleStmt.id, actualAction.line, self.file.path))

                    policy.intellect.learn(localScope["new_fact"])

                elif isinstance(actualAction, ModifyAction):

                    # As the ModifyAction acts on a specific match, one cannot
                    # have ModifyeAction statements in then-portion of a rule
                    # who's when-portion evaluated on "exists".

                    raise SyntaxError, "modifyAction cannot exist in then portion as when portion is written for '{0}' at line: {1} in Policy: {2}".format(ruleStmt.id, actualAction.line, self.file.path())
                elif isinstance(actualAction, HaltAction):

                    policy.halt = True

                    self.log("Halt called in rule: '{0}' from policy file: '{1}'.".format(ruleStmt.id, self.file.path))

                    break

                elif isinstance(actualAction, AttributeAction):

                    code = actualAction.write_prepend()

                    # No rewriting is necessary as ObjectBindings are not used
                    # in Action statements when the when-portion evaluated on
                    # "exists".
                    code += str(actualAction.children[1])

                    self.execute(policy, ruleStmt, localScope, code)

                else:
                    # Handle SimpleStmt

                    # No rewriting is necessary as ObjectBindings are not used
                    # in Action statements when the when-portion evaluated on
                    # "exists".
                    code = str(actualAction)
                    self.execute(policy, ruleStmt, localScope, code)



    def execute(self, policy, ruleStmt, localScope, code):
        '''
        Executes the code
        '''

        self.log("Code to be run for simpleStatement in rule: '{0}' near line: {1} in the policy file: '{2}':\n{3}".format(ruleStmt.id, self.line, self.file.path, code))

        try:
            # Execute the code, wrapped to collect stdout
            with IO.RedirectStdOut() as stdout:
                exec(str(code), policy.globals, localScope)

            print stdout.getvalue()

        except Exception as error:
            raise SyntaxError("{0} in rule: '{1}' near line: {2} in the policy file: '{3}'".format(error, ruleStmt.id, self.line, self.file.path))


    @staticmethod
    def rewrite(original, rewritten, objectBinding):
        '''
        A recursive method used to rewrite a SimpleStmt object using
        the objectBinding

        Args:
            original: the Node to be rewritten
            rewritten: rewritten: used in recursion, the object to be written into.
            objectBinding: the objectBinding to be replaced with string "match"

        Returns:
            The rewritten Node
        '''
        for child in original.children:

            if isinstance(child, Node):

                if isinstance(child, Atom):

                    # inspect and rewrite, if necessary
                    if child.first_child() == objectBinding:
                        # Replace the Atom containing the objectBinding with
                        # with an Atom containing simply the str "match"
                        #
                        # TODO: need a better string then "match" as this may
                        # may already be used in the constraint
                        rewritten.append_child( Atom("match") )
                    else:
                        # nothing matched to rewrite; so, clone
                        twin = type(child)()
                        rewritten.append_child(Then.rewrite(child, twin, objectBinding))

                else:
                    # handle a child Node that is not of Power node
                    twin = type(child)()

                    rewritten.append_child(Then.rewrite(child, twin, objectBinding))

            else:
                # handle a child that is a string
                rewritten.append_child(child)

        return rewritten



class Id(Node):
    '''
    A ID Node for a RuleStmt (Rule Statement) of GlobalStmt (Global Statement) Node.
    '''

    def __str__(self):
        '''
        A str representation of the node.

        Quotes around Strings are stripped.
        '''
        return str(self.first_child()).strip('"')



class RuleCondition(Node):
    '''
    A RuleCondition node for a RuleStmt node.
    '''

    @property
    def notCondition(self):
        return self.first_child()



class NotCondition(Node):
    '''
    A NotCondition node.
    '''

    def is_negated(self):
        '''
        Returns True if the Condition object is negated;
        otherwise, False.
        '''
        value = False

        for child in self.children:
            if (child == "not"):
                value = not value
            else:
                break

        return value


    @property
    def condition(self):
        '''
        Returns the Condition object
        '''
        return [child for child in self.children if isinstance(child, Condition)][0]



class Condition(Node):
    '''
    A Condition node.
    '''

    @property
    def exists(self):
        '''
        Returns to true if the ClassConstraint is prepended with "exists"
        '''
        return self.first_child() == "exists"


    @property
    def classConstraint(self):
        '''
        Returns the ClassConstraint object
        '''
        return [child for child in self.children if isinstance(child, ClassConstraint)][0]



class ClassConstraint(Node):
    '''
    A ClassConstraint node.
    '''

    @property
    def objectBinding(self):
        '''
        Return an objectBinding str, if one exists otherwise None
        '''
        if isinstance(self.first_child(), basestring) and self.first_child().startswith("$"):
            return self.first_child()
        else:
            return None


    @property
    def name(self):
        '''
        Returns the class name (as per the grammar a ClassConstraint must have one.)
        '''
        if self.children[1] == ":=":
            return self.children[2]
        else:
            return self.first_child()


    @property
    def constraint(self):
        '''
        Returns a Constraint object, if one exists otherwise None
        '''
        filter = [child for child in self.children if isinstance(child, Constraint)]

        if not filter:  # True, if filter is []
            return None
        else:
            return filter[0]



class Action(Node):
    '''
    An Action node.
    '''
    def __str__(self):
        '''
        Returns a str representation of Action as it would be written in a policy.
        '''
        value = str(self.action)

        return value


    @property
    def action(self):
        '''
        Returns either a ForgetAction, LearnAction, ModifyAction, or SimpleStmt
        object
        '''
        return self.first_child()



class SimpleStmt(Node):
    '''
    A SimpleStmt node.
    '''



class PrintStmt(Node):
    '''
    A PrintStmt node.
    '''



class AttributeAction(Node):
    '''
    An AttributeAction node.
    '''


    @property
    def expressionStmt(self):
        '''
        Returns the ExpressionStmt object for the attribute action.
        '''
        return self.children[1]


    def write_prepend(self):
        """
        Writes a prepend for the statement to allow it to be processed by a Python exec statement
        """
        returnStmt = "global "

        for object_reference in [atom.first_child() for atom in Node.filter_to_list(Atom, self.expressionStmt.children[0]) if len(atom.children) is 1]:
            returnStmt += object_reference + ", "

        return ("; ").join(returnStmt.rsplit(", ", 1))



class ForgetAction(Node):
    '''
    A ForgetAction node.
    '''
    @property
    def objectBinding(self):
        '''
        Returns a str representing the object binding to be forgotten/deleted
        '''
        return self.children[1]



class LearnAction(Node):
    '''
    An LearnAction node.
    '''
    @property
    def name(self):
        '''
        Returns the identifier of the object to be learned/inserted
        '''
        return self.children[1]


    @property
    def argList(self):
        '''
        Returns an ArgList object, if one exists otherwise None
        '''
        filter = [child for child in self.children if isinstance(child, ArgumentList)]

        if not filter:  # True, if filter is []
            return None
        else:
            return filter[0]



class ModifyAction(Node):
    '''
    A ModifyAction node.
    '''

    def __str__(self):
        '''
        Returns a str representation of Modify as it would be written in a policy.
        '''
        value = "modify {0}:\n".format(self.objectBinding)

        for propertyAssignment in self.propertyAssignments:
            value += "\t{0}\n".format(propertyAssignment)

        return value


    @property
    def objectBinding(self):
        '''
        Returns a str representing the object binding
        '''
        return self.children[1]


    @property
    def propertyAssignments(self):
        '''
        Returns a list of PropertyAssignment nodes
        '''
        return [child for child in self.children if isinstance(child, PropertyAssignment)]



class HaltAction(Node):
    '''
    A HaltAction node.
    '''


class PropertyAssignment(Node):
    '''
    A PropertyAssignment.
    '''

    @property
    def name(self):
        '''
        Returns the name of the property
        '''
        return self.first_child()


    @property
    def assignment(self):
        '''
        Returns an Assignment object
        '''
        return self.children[1]


    @property
    def constraint(self):
        '''
        Returns a Constraint object
        '''
        return self.children[2]



class ExpressionStmt(Node):
    '''
    An ExpressionStmt node.
    '''



class Assignment(Node):
    '''
    An Assignment node.
    '''



class ImportStmt(Node):
    '''
    An ImportStmt node
    '''

    @property
    def importStmt(self):
        return self.first_child()



class ImportName(Node):
    '''
    An ImportName node/
    '''

    @property
    def dottedAsNames(self):
        '''
        returns DottedAsNames object
        '''
        return self.children[1]



class ImportFrom(Node):
    '''
    An ImportFrom node
    '''

    @property
    def dottedName(self):
        '''
        returns DottedName object
        '''
        return self.children[1]


    @property
    def importAsNames(self):
        '''
        returns ImportAsNames object
        '''
        return [child for child in self.children if isinstance(child, ImportAsNames)][0]



class ImportAsNames(Node):
    '''
    An ImportAsNames node
    '''

    @property
    def importAsNames(self):
        '''
        Returns a list of ImportAsName objects
        '''
        return [child for child in self.children if isinstance(child, ImportAsName)]



class ImportAsName(Node):
    '''
    An ImportAsName node
    '''

    @property
    def identifier(self):
        '''
        Returns the source identifier/name of the class
        '''
        return self.first_child();


    @property
    def localName(self):
        '''
        Returns the local name used in the policy to refer to the class,
        or None meaning there is no local name.
        '''
        if len(self.children) == 3:
            return self.children[2]
        else:
            return None



class DottedAsNames(Node):
    '''
    A DottedAsNames node.
    '''

    @property
    def dottedAsNames(self):
        '''
        Returns a list of DottedAsName objects
        '''
        return [child for child in self.children if isinstance(child, DottedAsName)]



class DottedAsName(Node):
    '''
    A DottedAsName node.
    '''

    @property
    def dottedName(self):
        '''
        Returns a DottedName object
        '''
        return self.first_child();


    @property
    def localName(self):
        '''
        Returns the local name used in the policy to refer to the module,
        or None meaning there is no local name.
        '''
        if len(self.children) == 3:
            return self.children[2]
        else:
            return None



class DottedName(Node):
    '''
    A DottedName node.
    '''

    def __str__(self):
        '''
        returns dotted name as a string w/ no spaces around the dots
        '''
        return "".join(self.children)



class Constraint(Node):
    '''
    A Constraint node.
    '''



class OrConstraint(Node):
    '''
    An OrConstraint node.
    '''



class AndConstraint(Node):
    '''
    An AndConstraint node.
    '''



class NotConstraint(Node):
    '''
    A NotConstraint node.
    '''



class Comparison(Node):
    '''
    A Comparison node.
    '''



class ComparisonOperation(Node):
    '''
    A ComparisonOperation node.
    '''



class Expression(Node):
    '''
    An Expression node.
    '''



class BitwiseOrExpr(Node):
    '''
    A BitwiseOrExpr node.
    '''



class BitwiseXorExpr(Node):
    '''
    A BitwiseXorExpr node.
    '''



class BitwiseAndExpr(Node):
    '''
    A BitwiseAndExpr node.
    '''



class ShiftExpr(Node):
    '''
    A ShiftExpr node.
    '''



class ArithExpr(Node):
    '''
    A ArithExpr node.
    '''



class Term(Node):
    '''
    A Term node.
    '''



class Factor(Node):
    '''
    A Factor node.
    '''



class Power(Node):
    '''
    A Power node.
    '''

    def __str__(self):
        '''
        Returns a str for this the node and its children for what they represent
        in the policy.
        '''
        value = ""

        for child in self.children:
            value += str(child)

        return value


    @property
    def atom(self):
        '''
        Returns Atom object
        '''
        return self.first_child()


    @property
    def trailers(self):
        '''
        Return list of Trailer objects
        '''
        return [child for child in self.children if isinstance(child, Trailer)]


    @property
    def factor(self):
        '''
        Returns a Factor object, if one exists otherwise None
        '''
        filter = [child for child in self.children if isinstance(child, Factor)]

        if not filter:  # True, if filter is []
            return None
        else:
            return filter[0]



class Atom(Node):
    '''
    An Atom node.
    '''
    def __str__(self):
        '''
        Returns a str for this the node and its children for what they represent
        in the policy.
        '''
        value = ""

        for child in self.children:
            value += str(child)

        return value



class ListMaker(Node):
    '''
    A ListMaker node.
    '''
    def __str__(self):
        '''
        Returns a str representation of ListMaker as it would be written in a
        policy.
        '''
        value = ""

        for child in self.children:

            value += str(child)

            if (child == ","):
                value += " "

        value = value.rstrip()

        return value



class ComparisonList(Node):
    '''
    A ComparisonList node.
    '''

    def __str__(self):
        '''
        Returns a str representation of ComparisonList as it would be written
        in a policy.
        '''
        value = ""

        for child in self.children:

            value += str(child)

            if (child == ","):
                value += " "

        value = value.rstrip()

        return value



class Trailer(Node):
    '''
    A Trailer node.
    '''
    def __str__(self):
        '''
        Returns a str for this the node and its children for what they represent
        in the policy.
        '''
        value = ""

        for child in self.children:
            value += str(child)

        return value



class ExpressionList(Node):
    '''
    An ExpressionList Node.
    '''



class DictMaker(Node):
    '''
    A DictMaker node.
    '''



class ArgumentList(Node):
    '''
    An Argumentlist node.
    '''

    def __str__(self):
        '''
        Returns a str representation of ArgumentList as it would be written in a
        policy.
        '''
        value = ""

        for child in self.children:

            value += str(child)

            if (child == ","):
                value += " "

        value = value.rstrip()

        return value
