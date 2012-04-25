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
Intellect

Description: A rules engine

Initial Version: Oct 27, 2010

@author: Michael Joseph Walsh
"""

import logging, os, re, traceback, sys

from antlr3 import FileStream, CommonTokenStream, ANTLRStringStream, RecognitionException

from intellect.grammar.PolicyParser import PolicyParser
from intellect.PolicyLexer import PolicyLexer
from intellect.Node import Policy
from intellect.Node import File
from intellect.PolicyTokenSource import PolicyTokenSource
from intellect.Callable import Callable
from intellect.IO import RedirectStdError



class Intellect(object):
    '''
    Rules engine.
    '''

    filepath_regex = re.compile(r"^(.*?/|.*?\\)?([^\./|^\.\\]+)(?:\.([^\\]*)|)$")

    def __init__(self):
        '''
        Intellect initializer.
        '''

        # initialize list to hold learned objects
        self.knowledge = []

        # initialize the hold the combined sum of the policy files
        # as a single policy.
        self.policy = Policy()


    @property
    def knowledge(self):
        """
        Returns the intellect's knowledge either a list of objects or an
            empty list.
        """
        return self._knowledge


    @knowledge.setter
    def knowledge(self, oneOrMoreObjects):
        """
        Keeper of knowledge.

        Holds facts aka objects in a list.

        Args:
            oneOrMoreObjects: Either a single facts or policy file or
                a list of facts and/or policy files.
        """

        try:
            self.knowledge
        except AttributeError:
            self._knowledge = []

        if not isinstance(oneOrMoreObjects, list):
            self.knowledge.append(oneOrMoreObjects)
        elif oneOrMoreObjects != []:
            self.knowledge.extend(oneOrMoreObjects)


    @property
    def policy(self):
        return self._policy


    @policy.setter
    def policy(self, value):
        self._policy = value


    def learn(self, identifier):
        '''
        Learns an object fact, or learns a policy by messaging learn_policy
        method with the 'identifier' as a policy path, if the identifier is
        a string.

        Args:
            fact: an object or policy file/string to learn.  Typically objects have
                annotated properties and/or methods that return values.

        Raises:
            ValueError:  The fact or policy already exists in knowledge.
            TypeError:  Raised when parameter 'identifier' is a NoneType.
        '''
        if identifier:
            if isinstance(identifier, basestring):
                return self.learn_policy(identifier)
            elif self.knowledge.count(identifier) == 0:
                self.knowledge.append(identifier)
                self.log("Learned: {0}:{1}".format(type(identifier), identifier.__dict__))
            else:
                raise ValueError, "{0}:{1} already exists in knowledge.".format(type(identifier), identifier.__dict__)
        else:
            raise TypeError, "parameter 'identifier' cannot be a NoneType."


    def learn_policy(self, identifier):
        '''
        Learn a policy file.

        Args:
            identifier: a string, either a path to a policy file or the text of the policy itself.
            Keep in mind a policy can be comprised of more than one policy file (a file containing
            valid policy DSL) or string containing policy DSL.  This way you break your rule set,
            imports, and policy attributes across any number of files.  See reason-method for more.


        Returns:
            The resulting File Node.

        Raises:
            ValueError:  if the policy already exists in knowledge.
            TypeError:  if parameter 'identifier' is a NoneType, or is not a string representing
                either a file path to a policy or the text of the policy itself.
        '''

        isFile = False

        if identifier:
            if isinstance(identifier, basestring):

                if not os.path.isfile(identifier):
                    '''
                    Try treating 'identifier' as a String containing the text
                    of a policy.
                    '''

                    stream = ANTLRStringStream(identifier)
                    lexer = PolicyLexer(stream)
                    tokens = CommonTokenStream(lexer)
                    tokens.discardOffChannelTokens = True
                    indentedSource = PolicyTokenSource(tokens)
                    tokens = CommonTokenStream(indentedSource)
                    parser = PolicyParser(tokens)

                    with RedirectStdError() as stderr:
                        try:
                            # ANTL3 may raise an exception, and doing so the stderror 
                            # will not be printed hiding the underlying problem.  GRRR!!!!
                            file_node = parser.file()
                        except Exception as e:
                            if stderr.getvalue().rstrip() != "":
                                trace = sys.exc_info()[2]
                                raise Exception(stderr.getvalue().rstrip()), None, trace
                            else:
                                raise e

                    # Some times the previous parser.file() will print to stderr,
                    # but not throw an exception.  In this case, the parser may
                    # attempt to correct and continue onward, but we should
                    # print the msg to stderr for the benefit of the policy
                    # author
                    if stderr.getvalue().rstrip() != "":
                        print >> sys.stderr, stderr.getvalue().rstrip()

                else:
                    '''
                    Try treating 'identifier' as a file path
                    '''
                    if Intellect.filepath_regex.match(identifier):
                        if os.path.exists(identifier):
                            self.log("Learning policy from file path: {0}".format(identifier))
                            stream = FileStream(identifier)
                            isFile = True
                        else:
                            raise IOError, "Policy not found: {0}".format(identifier)
                    else:
                        '''
                        assume the intention was to pass 'identifier' as a String containing the text
                        of a policy, and raise the exception.
                        '''
                        raise e

                    lexer = PolicyLexer(stream)
                    tokens = CommonTokenStream(lexer)
                    tokens.discardOffChannelTokens = True
                    indentedSource = PolicyTokenSource(tokens)
                    tokens = CommonTokenStream(indentedSource)
                    parser = PolicyParser(tokens)

                    with RedirectStdError() as stderr:
                        try:
                            # ANTL3 may raise an exception, and doing so the stderror 
                            # will not be printed hiding the underlying problem.  GRRR!!!!
                            file_node = parser.file()

                        except Exception as e:
                            if stderr.getvalue().rstrip() != "":
                                trace = sys.exc_info()[2]
                                raise Exception(stderr.getvalue().rstrip()), None, trace
                            else:
                                raise e

                    # Some times the previous parser.file() will print to stderr,
                    # but not throw an exception.  In this case, the parser may
                    # attempt to correct and continue onward, but we should
                    # print the msg to stderr for the benefit of the policy
                    # author
                    if stderr.getvalue().rstrip() != "":
                        print >> sys.stderr, stderr.getvalue().rstrip()

                # set path attribute
                file_node.path = identifier if isFile else None

                # associate the path to all descendants
                file_node.set_file_on_descendants(file_node, file_node)

                try:
                    # determine if the policy already exists in knowledge
                    self.policy.files.index(file_node)
                    raise ValueError, "Policy already exists in knowledge: {0}".format(identifier)
                except:
                    pass

                # store add the policy file to the policy
                self.policy.append_child(file_node)

                self.log("learned a policy file")

                return file_node

            else:
                raise TypeError, "parameter 'identifier' must be a string, either a file path to a policy or the text of the policy itself"
        else:
            raise TypeError, "parameter 'identifier' cannot be a NoneType."


    def learn_fact(self, identifier):
        '''
        Wrapper for 'learn' method
        '''
        self.learn(identifier)


    def forget(self, identifier):
        '''
        Forgets an id() of a fact or policy, or a string representing the path
        of a policy, or a fact.

        Args:
            identifier: is an id() of a fact or policy, or a string
                representing the path of a policy, or a fact.

        Raises:
            ValueError:  Raised when parameter 'identifier' has the right
                type but an inappropriate value.
            TypeError:  Raised when parameter 'identifier' is a NoneType.
        '''
        if identifier:
            if isinstance(identifier, int):
                # remove the fact from the knowledge
                for index, fact in enumerate(self.knowledge):
                    if identifier == id(fact):
                        self.log("Forgetting fact with id: {0} of type: {1} from knowledge. fact.__dict__: {2}".format(identifier, type(fact), fact.__dict__))
                        self.knowledge.remove(fact)
                        return
                # fact doesn't exist in memory, attempt to remove a policy file/String
                # from knowledge with this identifier
                for index, file in self.policy.files:
                    if identifier == id(file):
                        self.log("Forgetting policy loaded from file path : {0}".format(identifier.path))
                        self.policy.files.remove(file)
                        return
                # neither fact nor policy so raise an exception
                raise ValueError, "fact with id: {0} is not in knowledge".format(identifier)
            elif isinstance(identifier, basestring):
                # remove the policy file from knowledge
                try:
                    for fileIndex, file in enumerate(self.policy.files):
                        if file.path == identifier:
                            self.policy.files.pop(fileIndex)

                    self.log("Forgetting policy loaded from file path : {0}".format(identifier))
                except KeyError:
                    raise ValueError, "policy for file path: {0} is not in knowledge".format(identifier)
            elif isinstance(identifier, File):
                try:
                    index = self.policy.files.index(identifier)
                    self.policy.files.pop(index)
                    self.log("Forgetting policy loaded from file path : {0}".format(identifier.path))
                except:
                    raise ValueError, "policy: {0} not in knowledge".format(identifier.path)
            else:
                try:
                    self.knowledge.remove(identifier)
                    self.log("Forgetting fact: {0}".format(identifier))
                except:
                    raise ValueError, "fact: {0} is not in knowledge".format(identifier)
        else:
            raise TypeError, "parameter 'identifier' cannot be a NoneType."


    def forget_fact(self, identifier):
        '''
        Wrapper for 'forget' method

        Args:
            identifier: is the id() of the fact, or the fact itself to forget

        Raises:
            See forget-method 'raises'.
        '''
        self.forget(identifier)


    def forget_policy(self, identifier):
        '''
        Wrapper for 'forget' method

        Args:
            identifier: is the either the path to the policy to forget, or
            the Policy object itself.

        Raises:
            TypeError:  Raised when 'identifier' is not a basestring or Policy
                object.
            Also, see forget-method 'raises'.
        '''
        if isinstance(identifier, (basestring, File)):
            self.forget(identifier)
        else:
            raise TypeError, "parameter 'identifier': {0} was neither a path to the policy to forget, or a Policy object.".format(identifier)


    def forget_all(self):
        '''
        Forgets all facts in knowledge and the present policy
        '''
        self.knowledge = []
        self.policy = Policy()

        self.log("forgot all")


    def reason(self, agenda=None):
        '''
        Reasons across the facts in knowledge applying the policy.

        Args:
            agenda: is either the default of None or a list of agenda-group identifiers.
                If a rule is created with no agenda group attribute then the group will
                be associated with "MAIN" agenda group. If the 'agenda' attribute remains
                the default of None, then only the "MAIN" agenda group will fire.

            rule "flood the torpedo tubes":
                agenda group "firing sequence"
                when:
                  ...
                then:
                  ...

            So, in the scenario above an agenda may look like:

                agenda = ["targeting sequence", "firing sequence", "after firing sequence" ]

            First, all the rules associated with the "targeting sequence" agenda
            group will fire, then those associated with the "firing sequence"
            group...

            Note, any cumulative changes that occur to policy attributes are
            passed onto individual agenda groups.

            Remember, whatever is loaded last wins in terms of imports.  At present rule
            names are not evaluated.  So, it doesn't matter to the interpreter if you have
            two or more rules named the same, each will be evaluated.  Attributes and import
            statement are evaluated top to bottom.  Imports are evaluated first, then
            attributes, then rule statements.

        Raises:
            Any exceptions raised by the combined policy as it is evaluated will
            be raised here.
        '''

        #update the policy with the present Intellect
        self.policy.intellect = self

        # eval the policy using the described agenda
        self.policy.eval(agenda)


    @Callable
    def log(self, msg, name="intellect", level=logging.DEBUG):
        '''
        Logs at the 'level' for the messaged 'msg'

        Args:
            name: the name of the logger
            level:  must be either logging.DEBUG, logging.INFO, logging.WARNING,
                logging.ERROR, logging.CRITICAL
            msg: message string

        Raises:
            ValueError:  Raised when it receives an 'level' that is not either
                logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, or
                logging.CRITICAL.
        '''

        if level not in [logging.DEBUG, logging.INFO, logging.WARNING,
                logging.ERROR, logging.CRITICAL]:
            raise ValueError, "A value of '{0}' for 'level' is invalid, must be either logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL".format(level)

        logging.getLogger(name).log(level, "{0}.{1} :: {2}".format(self.__class__.__module__, self.__class__.__name__, msg))
