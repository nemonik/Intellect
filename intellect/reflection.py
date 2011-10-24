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
reflection

Description: Functions for performing introspection

Initial Version: Feb 1, 2011

@author: Michael Joseph Walsh
"""

import inspect, types, logging

FUNCTION = "function"
BUILTIN_FUNCTION = "built-in function"
INSTANCE_METHOD = "instance method"
CLASS_METHOD= classmethod
STATIC_METHOD = staticmethod
PROPERTY = property
DATA = "data"

def log(msg, name = "intellect", level = logging.DEBUG):
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

    logging.getLogger(name).log(level, "{0} :: {1}".format(__name__, msg))


def is_method(object, name):
    '''
    does this class have this method?
    '''
    return (inspect_class_for_attribute(object, name)[0] in [INSTANCE_METHOD, CLASS_METHOD, STATIC_METHOD])


def has_attribute(object, name):
    '''
    does this object have this attribute in other words does it have this
    (instance/class/static) method, property, or global?
    '''
    return (inspect_class_for_attribute(object, name)) != (None, None, None)


def is_instance_method(object, name):
    '''
    does this class have this method?
    '''
    return (inspect(object, name)[0] is INSTANCE_METHOD)


def is_class_method(object, name):
    '''
    does this class have this class method?
    '''
    return (inspect_class_for_attribute(object, name)[0] is CLASS_METHOD)


def is_static_method(object, name):
    '''
    does this class have this static method?
    '''
    return (inspect_class_for_attribute(object, name)[0] is STATIC_METHOD)


def is_property(object, name):
    '''
    does this class have this property?
    '''
    return (inspect_class_for_attribute(object, name)[0] is PROPERTY)


def is_data(object, name):
    '''
    does this class have this global or attribute?
    '''
    return (inspect_class_for_attribute(object, name)[0] is DATA)


def inspect_class_for_attribute(object, name):
    '''
    For a given object inspects it for the existence of named instance/class/static method,
    property, and data element (global or attribute) attribute; and returns in tuple form
    (kind, obj, homeClass)
    '''

    if name in dir(object):
        if name in object.__dict__:
            obj = object.__dict__[name]
        else:
            obj = getattr(object, name)

        homeClass = getattr(obj, "__objclass__", None)

        if homeClass is None:
            for base in inspect.getmro(object):
                if name in base.__dict__:
                    homeClass = base
                    break

        if ((homeClass is not None) and (name in homeClass.__dict__)):
            obj = homeClass.__dict__[name]
            obj_via_getattr = getattr(object, name)

        if isinstance(obj, staticmethod):
            kind = staticmethod
        elif isinstance(obj, classmethod):
            kind = CLASS_METHOD
        elif isinstance(obj, property):
            kind = PROPERTY
        elif (inspect.ismethod(obj_via_getattr) or
              inspect.ismethoddescriptor(obj_via_getattr)):
            kind = INSTANCE_METHOD
        else:
            kind = DATA

        return (kind, obj, homeClass)
    else:
        return (None, None, None)


def inspect_module_for_attribute(module, name):
    '''
    For a given module inspects it for the existence of named built-in,
    functions, and data attributes; and returns in tuple form
    (kind, obj)
    '''
    if inspect.ismodule(module):

        names = dir(module)

        if name in names:

            if name in module.__dict__:
                obj = module.__dict__[name]
            else:
                obj = getattr(module, name)

            if isinstance(obj, types.FunctionType):
                kind = FUNCTION
            elif isinstance(obj, types.BuiltinFunctionType):
                kind = BUILTIN_FUNCTION
            else:
                kind = DATA

            return (kind, obj)
        else:
            return (None, None, None)
    else:
        raise TypeError("parameter 'module' must be a Module, not an instance of a class, nor a Class.")


def for_class_list(klazz, type):
    '''
    A wrapper to for_object_list-method for evaluating just Class-type objects
    '''
    if inspect.isclass(klazz):
        return for_object_list(klazz, type)
    else:
        raise TypeError("parameter 'klazz' was not a Class, but an instance object.")


def for_object_list(object, type):
    '''
    For a given object inspects it for the existence of named instance/class/static method,
    property, and data element (global or attribute) attribute; and returns in tuple form
    (kind, obj, homeClass)
    '''
    value = []
    names = dir(object)

    for name in names:
        if name in object.__dict__:
            obj = object.__dict__[name]
        else:
            obj = getattr(object, name)

        homeClass = getattr(obj, "__objclass__", None)

        if homeClass is None:
            for base in inspect.getmro(object):
                if name in base.__dict__:
                    homeClass = base
                    break

        if ((homeClass is not None) and (name in homeClass.__dict__)):
            obj = homeClass.__dict__[name]
            obj_via_getattr = getattr(object, name)

        if isinstance(obj, staticmethod):
            kind = staticmethod
        elif isinstance(obj, classmethod):
            kind = CLASS_METHOD
        elif isinstance(obj, property):
            kind = PROPERTY
        elif (inspect.ismethod(obj_via_getattr) or
              inspect.ismethoddescriptor(obj_via_getattr)):
            kind = INSTANCE_METHOD
        else:
            kind = DATA

        print name, kind, obj

        if (kind is type):
            value.append(name)

    return value


def for_module_list(module, type):
    '''
    For a given module list either the built-in or data attributes.

    Example:

    for_module_list(__builtins__, BUILTIN)

    Will return a list of all the Python interpreter built-in functions

    '''

    value = []

    if inspect.ismodule(module):
        names = dir(module)

        for name in names:

            if name in module.__dict__:
                obj = module.__dict__[name]
            else:
                obj = getattr(module, name)

            if isinstance(obj, types.FunctionType):
                kind = FUNCTION
            elif isinstance(obj, types.BuiltinFunctionType):
                kind = BUILTIN_FUNCTION
            else:
                kind = DATA

            if (kind is type):
                value.append(name)

    return value


def class_from_string(className, policy):
    """
    Returns class object

    Args:
        className: A string holding either the class identifier or local name.
        policy: Policy providing ImportFrom objects to inspect.

    Raises:
        PolicyException, if the class wasn't declared in a fromImport statement in the policy file
    """

    identifier = ""
    dottedName = ""

    importFromClass = class_from_str("intellect.Node.ImportFrom")

    importFroms = [importStmt.importStmt for importStmt in policy.importStmts if isinstance(importStmt.importStmt, importFromClass)]

    if not importFroms:
        raise SyntaxError("{0} was not declared in a importFrom statement in the policy file: '{1}'".format(className, policy.path))
    else:
        for importFrom in reversed(importFroms):
            for importAsName in reversed(importFrom.importAsNames.importAsNames):
                if importAsName.localName is not None and importAsName.localName == className:
                    # finding a match matching the localname for the className,
                    # hold the class's dottedName and identifier for later use
                    matchedImportFrom = importFrom # used for raising PolicyException
                    dottedName = importFrom.dottedName
                    identifier = importAsName.identifier
                    break
                elif importAsName.localName is None and importAsName.identifier == className:
                    # finding a match matching the localname for the className,
                    # hold the class's dottedName and identifier for later use
                    matchedImportFrom = importFrom # used for raising PolicyException
                    dottedName = importFrom.dottedName
                    identifier = importAsName.identifier
                    break

            if identifier:
                break

        if not identifier:
            # the className was not imported, raise a PolicyException
            # TODO: include the line to assist the policy author
            raise SyntaxError("{0} was not declared in a fromImport statement in the policy file: '{1}'".format(className, policy.path))
        else:
            # otherwise return the class

            try:
                module = __import__(str(dottedName), globals(), locals(), [identifier])
            except ImportError as detail:
                raise SyntaxError("{0} at line: {1} in policy file: {2}".format(detail, matchedImportFrom.line, policy.path))

            try:
                klazz = getattr(module, identifier)
            except AttributeError:
                raise SyntaxError("'{0}' does not exist in module imported from at line: {1} in policy file: '{2}'".format(identifier, matchedImportFrom.line, policy.path))

            # return the class
            log("returning {0} for '{1}'".format(klazz, className))

            return klazz


def module_from_string(moduleName, policy):
    """
    Returns module object

    Args:
        module: A string holding either the module identifier or local name.
        policy: Policy providing ImportFrom objects to inspect.

    Raises:
        PolicyException, if the module wasn't declared in a importName statement in the policy file
    """

    dottedName = ""

    importNameClass = class_from_str("intellect.Node.ImportName")

    importNames = [importStmt.importStmt for importStmt in policy.importStmts if isinstance(importStmt.importStmt, importNameClass)]

    if not importNames:
        raise SyntaxError("{0} was not declared in a importName statement in the policy file: '{1}'".format(moduleName, policy.path))
    else:
        for importName in importNames:

            # first check all the localNames
            for dottedAsName in importName.dottedAsNames.dottedAsNames:
                if dottedAsName.localName is not None and dottedAsName.localName == moduleName:
                    # finding a match matching the localname for the moduleName,
                    # hold the module's dottedName for later use
                    matchedImportName = importName # used for raising PolicyException
                    dottedName = dottedAsName.dottedName
                    break
                elif dottedAsName.dottedName == moduleName:
                        # finding a matching identifier,
                        # hold the class's dottedName and identifier for later use
                        matchedImportName = importName # used for raising PolicyException
                        dottedName = moduleName
                        break

            if dottedName:
                break

        if not dottedName:
            # the className was not imported, raise a PolicyException
            # TODO: include the line to assist the policy author
            raise SyntaxError("{0} was not declared in a importName statement in the policy file: '{1}'".format(moduleName, policy.path))
        else:
            # otherwise return the module
            try:
                # return the package object
                module = __import__(str(dottedName))
                # then dynamically load the module from the package
                components = str(dottedName).split('.')
                for comp in components[1:]:
                    module = getattr(module, comp)

            except ImportError as detail:
                raise SyntaxError("{0} at line: {1} in policy file: '{2}'".format(detail, matchedImportName.line, policy.path))

            # returning the module, not the package...
            log("returning a {0}".format(module))

            return module


def class_from_str(name):
    '''
        Returns a Class object from dottedName.identifier str such as
        'intellect.Intellect.Intellect'.
    '''
    dottedName, identifier = name.rsplit('.', 1)
    module = __import__(str(dottedName), globals(), locals(), [identifier])
    klazz = getattr(module, identifier)

    log("returning {0} for {1}".format(klazz, name))
    return klazz
