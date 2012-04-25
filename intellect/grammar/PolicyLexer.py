# $ANTLR 3.1.3 Mar 17, 2009 19:23:44 /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g 2012-04-19 12:49:36

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EXPONENT=84
BACKQUOTE=80
SLASHEQUAL=38
STAR=64
CIRCUMFLEXEQUAL=42
LETTER=82
TRIAPOS=85
GREATEREQUAL=52
COMPLEX=77
ASSIGNEQUAL=24
NOT=21
EOF=-1
NOTEQUAL=55
LEADING_WS=90
MINUSEQUAL=36
VBAR=58
RPAREN=10
NAME=12
IMPORT=7
GREATER=50
INSERT=31
DOUBLESTAREQUAL=45
LESS=49
COMMENT=91
RBRACK=71
RULE=15
LCURLY=72
INT=74
DELETE=29
RIGHTSHIFT=27
DOUBLESLASHEQUAL=46
WS=89
VBAREQUAL=41
OR=47
LONGINT=75
FORGET=28
FROM=8
LESSEQUAL=53
PERCENTEQUAL=39
DOLLAR=79
MODIFY=32
DOUBLESLASH=67
LBRACK=70
CONTINUED_LINE=88
OBJECTBINDING=23
DOUBLESTAR=69
HALT=33
ESC=87
ATTRIBUTE=25
DEDENT=5
FLOAT=76
RIGHTSHIFTEQUAL=44
AND=48
LEARN=30
INDENT=4
LPAREN=9
PLUSEQUAL=35
AS=13
SLASH=65
THEN=20
IN=56
COMMA=11
IS=57
AMPER=60
EQUAL=51
TILDE=68
LEFTSHIFTEQUAL=43
LEFTSHIFT=61
PLUS=62
EXISTS=22
DIGIT=83
DOT=14
AGENDAGROUP=18
PERCENT=66
MINUS=63
SEMI=78
PRINT=26
COLON=16
TRIQUOTE=86
AMPEREQUAL=40
NEWLINE=6
WHEN=19
RCURLY=73
ASSIGN=34
GLOBAL=81
STAREQUAL=37
CIRCUMFLEX=59
STRING=17
ALT_NOTEQUAL=54


class PolicyLexer(Lexer):

    grammarFileName = "/Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 17, 2009 19:23:44")
    antlr_version_str = "3.1.3 Mar 17, 2009 19:23:44"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(PolicyLexer, self).__init__(input, state)


        self.dfa9 = self.DFA9(
            self, 9,
            eot = self.DFA9_eot,
            eof = self.DFA9_eof,
            min = self.DFA9_min,
            max = self.DFA9_max,
            accept = self.DFA9_accept,
            special = self.DFA9_special,
            transition = self.DFA9_transition
            )

        self.dfa16 = self.DFA16(
            self, 16,
            eot = self.DFA16_eot,
            eof = self.DFA16_eof,
            min = self.DFA16_min,
            max = self.DFA16_max,
            accept = self.DFA16_accept,
            special = self.DFA16_special,
            transition = self.DFA16_transition
            )

        self.dfa46 = self.DFA46(
            self, 46,
            eot = self.DFA46_eot,
            eof = self.DFA46_eof,
            min = self.DFA46_min,
            max = self.DFA46_max,
            accept = self.DFA46_accept,
            special = self.DFA46_special,
            transition = self.DFA46_transition
            )

        self.dfa47 = self.DFA47(
            self, 47,
            eot = self.DFA47_eot,
            eof = self.DFA47_eof,
            min = self.DFA47_min,
            max = self.DFA47_max,
            accept = self.DFA47_accept,
            special = self.DFA47_special,
            transition = self.DFA47_transition
            )


                             
        self.implicitLineJoiningLevel = 0
        self.startPosition = -1





    # $ANTLR start "LPAREN"
    def mLPAREN(self, ):

        try:
            _type = LPAREN
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:387:3: ( '(' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:387:5: '('
            pass 
            self.match(40)
            #action start
            self.implicitLineJoiningLevel += 1
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LPAREN"



    # $ANTLR start "RPAREN"
    def mRPAREN(self, ):

        try:
            _type = RPAREN
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:391:3: ( ')' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:391:5: ')'
            pass 
            self.match(41)
            #action start
            self.implicitLineJoiningLevel -= 1
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RPAREN"



    # $ANTLR start "LBRACK"
    def mLBRACK(self, ):

        try:
            _type = LBRACK
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:395:3: ( '[' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:395:5: '['
            pass 
            self.match(91)
            #action start
            self.implicitLineJoiningLevel += 1
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LBRACK"



    # $ANTLR start "RBRACK"
    def mRBRACK(self, ):

        try:
            _type = RBRACK
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:399:3: ( ']' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:399:5: ']'
            pass 
            self.match(93)
            #action start
            self.implicitLineJoiningLevel -= 1
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RBRACK"



    # $ANTLR start "LCURLY"
    def mLCURLY(self, ):

        try:
            _type = LCURLY
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:403:3: ( '{' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:403:5: '{'
            pass 
            self.match(123)
            #action start
            self.implicitLineJoiningLevel += 1
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LCURLY"



    # $ANTLR start "RCURLY"
    def mRCURLY(self, ):

        try:
            _type = RCURLY
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:407:3: ( '}' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:407:5: '}'
            pass 
            self.match(125)
            #action start
            self.implicitLineJoiningLevel -= 1
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RCURLY"



    # $ANTLR start "COLON"
    def mCOLON(self, ):

        try:
            _type = COLON
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:411:3: ( ':' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:411:5: ':'
            pass 
            self.match(58)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COLON"



    # $ANTLR start "COMMA"
    def mCOMMA(self, ):

        try:
            _type = COMMA
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:415:3: ( ',' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:415:5: ','
            pass 
            self.match(44)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COMMA"



    # $ANTLR start "DOT"
    def mDOT(self, ):

        try:
            _type = DOT
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:419:3: ( '.' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:419:5: '.'
            pass 
            self.match(46)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DOT"



    # $ANTLR start "SEMI"
    def mSEMI(self, ):

        try:
            _type = SEMI
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:423:3: ( ';' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:423:5: ';'
            pass 
            self.match(59)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SEMI"



    # $ANTLR start "PLUS"
    def mPLUS(self, ):

        try:
            _type = PLUS
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:427:3: ( '+' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:427:5: '+'
            pass 
            self.match(43)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PLUS"



    # $ANTLR start "MINUS"
    def mMINUS(self, ):

        try:
            _type = MINUS
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:431:3: ( '-' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:431:5: '-'
            pass 
            self.match(45)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MINUS"



    # $ANTLR start "STAR"
    def mSTAR(self, ):

        try:
            _type = STAR
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:435:3: ( '*' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:435:5: '*'
            pass 
            self.match(42)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STAR"



    # $ANTLR start "DOLLAR"
    def mDOLLAR(self, ):

        try:
            _type = DOLLAR
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:439:3: ( '$' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:439:5: '$'
            pass 
            self.match(36)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DOLLAR"



    # $ANTLR start "SLASH"
    def mSLASH(self, ):

        try:
            _type = SLASH
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:443:3: ( '/' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:443:5: '/'
            pass 
            self.match(47)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SLASH"



    # $ANTLR start "VBAR"
    def mVBAR(self, ):

        try:
            _type = VBAR
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:447:3: ( '|' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:447:5: '|'
            pass 
            self.match(124)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "VBAR"



    # $ANTLR start "AMPER"
    def mAMPER(self, ):

        try:
            _type = AMPER
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:451:3: ( '&' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:451:5: '&'
            pass 
            self.match(38)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "AMPER"



    # $ANTLR start "LESS"
    def mLESS(self, ):

        try:
            _type = LESS
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:455:3: ( '<' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:455:5: '<'
            pass 
            self.match(60)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LESS"



    # $ANTLR start "GREATER"
    def mGREATER(self, ):

        try:
            _type = GREATER
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:459:3: ( '>' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:459:5: '>'
            pass 
            self.match(62)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "GREATER"



    # $ANTLR start "ASSIGN"
    def mASSIGN(self, ):

        try:
            _type = ASSIGN
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:463:3: ( '=' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:463:5: '='
            pass 
            self.match(61)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ASSIGN"



    # $ANTLR start "PERCENT"
    def mPERCENT(self, ):

        try:
            _type = PERCENT
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:467:3: ( '%' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:467:5: '%'
            pass 
            self.match(37)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PERCENT"



    # $ANTLR start "BACKQUOTE"
    def mBACKQUOTE(self, ):

        try:
            _type = BACKQUOTE
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:471:3: ( '`' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:471:5: '`'
            pass 
            self.match(96)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "BACKQUOTE"



    # $ANTLR start "CIRCUMFLEX"
    def mCIRCUMFLEX(self, ):

        try:
            _type = CIRCUMFLEX
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:475:3: ( '^' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:475:5: '^'
            pass 
            self.match(94)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "CIRCUMFLEX"



    # $ANTLR start "TILDE"
    def mTILDE(self, ):

        try:
            _type = TILDE
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:479:3: ( '~' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:479:5: '~'
            pass 
            self.match(126)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "TILDE"



    # $ANTLR start "EQUAL"
    def mEQUAL(self, ):

        try:
            _type = EQUAL
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:483:3: ( '==' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:483:5: '=='
            pass 
            self.match("==")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "EQUAL"



    # $ANTLR start "ASSIGNEQUAL"
    def mASSIGNEQUAL(self, ):

        try:
            _type = ASSIGNEQUAL
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:487:3: ( ':=' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:487:5: ':='
            pass 
            self.match(":=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ASSIGNEQUAL"



    # $ANTLR start "NOTEQUAL"
    def mNOTEQUAL(self, ):

        try:
            _type = NOTEQUAL
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:491:3: ( '!=' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:491:5: '!='
            pass 
            self.match("!=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NOTEQUAL"



    # $ANTLR start "ALT_NOTEQUAL"
    def mALT_NOTEQUAL(self, ):

        try:
            _type = ALT_NOTEQUAL
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:495:3: ( '<>' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:495:5: '<>'
            pass 
            self.match("<>")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ALT_NOTEQUAL"



    # $ANTLR start "LESSEQUAL"
    def mLESSEQUAL(self, ):

        try:
            _type = LESSEQUAL
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:499:3: ( '<=' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:499:5: '<='
            pass 
            self.match("<=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LESSEQUAL"



    # $ANTLR start "LEFTSHIFT"
    def mLEFTSHIFT(self, ):

        try:
            _type = LEFTSHIFT
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:503:3: ( '<<' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:503:5: '<<'
            pass 
            self.match("<<")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LEFTSHIFT"



    # $ANTLR start "GREATEREQUAL"
    def mGREATEREQUAL(self, ):

        try:
            _type = GREATEREQUAL
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:507:3: ( '>=' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:507:5: '>='
            pass 
            self.match(">=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "GREATEREQUAL"



    # $ANTLR start "RIGHTSHIFT"
    def mRIGHTSHIFT(self, ):

        try:
            _type = RIGHTSHIFT
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:511:3: ( '>>' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:511:5: '>>'
            pass 
            self.match(">>")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RIGHTSHIFT"



    # $ANTLR start "PLUSEQUAL"
    def mPLUSEQUAL(self, ):

        try:
            _type = PLUSEQUAL
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:515:3: ( '+=' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:515:5: '+='
            pass 
            self.match("+=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PLUSEQUAL"



    # $ANTLR start "MINUSEQUAL"
    def mMINUSEQUAL(self, ):

        try:
            _type = MINUSEQUAL
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:519:3: ( '-=' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:519:5: '-='
            pass 
            self.match("-=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MINUSEQUAL"



    # $ANTLR start "DOUBLESTAR"
    def mDOUBLESTAR(self, ):

        try:
            _type = DOUBLESTAR
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:523:3: ( '**' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:523:5: '**'
            pass 
            self.match("**")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DOUBLESTAR"



    # $ANTLR start "STAREQUAL"
    def mSTAREQUAL(self, ):

        try:
            _type = STAREQUAL
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:527:3: ( '*=' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:527:5: '*='
            pass 
            self.match("*=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STAREQUAL"



    # $ANTLR start "DOUBLESLASH"
    def mDOUBLESLASH(self, ):

        try:
            _type = DOUBLESLASH
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:531:3: ( '//' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:531:5: '//'
            pass 
            self.match("//")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DOUBLESLASH"



    # $ANTLR start "SLASHEQUAL"
    def mSLASHEQUAL(self, ):

        try:
            _type = SLASHEQUAL
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:535:3: ( '/=' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:535:5: '/='
            pass 
            self.match("/=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SLASHEQUAL"



    # $ANTLR start "VBAREQUAL"
    def mVBAREQUAL(self, ):

        try:
            _type = VBAREQUAL
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:539:3: ( '|=' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:539:5: '|='
            pass 
            self.match("|=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "VBAREQUAL"



    # $ANTLR start "PERCENTEQUAL"
    def mPERCENTEQUAL(self, ):

        try:
            _type = PERCENTEQUAL
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:543:3: ( '%=' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:543:5: '%='
            pass 
            self.match("%=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PERCENTEQUAL"



    # $ANTLR start "AMPEREQUAL"
    def mAMPEREQUAL(self, ):

        try:
            _type = AMPEREQUAL
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:547:3: ( '&=' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:547:5: '&='
            pass 
            self.match("&=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "AMPEREQUAL"



    # $ANTLR start "CIRCUMFLEXEQUAL"
    def mCIRCUMFLEXEQUAL(self, ):

        try:
            _type = CIRCUMFLEXEQUAL
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:551:3: ( '^=' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:551:5: '^='
            pass 
            self.match("^=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "CIRCUMFLEXEQUAL"



    # $ANTLR start "LEFTSHIFTEQUAL"
    def mLEFTSHIFTEQUAL(self, ):

        try:
            _type = LEFTSHIFTEQUAL
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:555:3: ( '<<=' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:555:5: '<<='
            pass 
            self.match("<<=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LEFTSHIFTEQUAL"



    # $ANTLR start "RIGHTSHIFTEQUAL"
    def mRIGHTSHIFTEQUAL(self, ):

        try:
            _type = RIGHTSHIFTEQUAL
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:559:3: ( '>>=' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:559:5: '>>='
            pass 
            self.match(">>=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RIGHTSHIFTEQUAL"



    # $ANTLR start "DOUBLESTAREQUAL"
    def mDOUBLESTAREQUAL(self, ):

        try:
            _type = DOUBLESTAREQUAL
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:563:3: ( '**=' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:563:5: '**='
            pass 
            self.match("**=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DOUBLESTAREQUAL"



    # $ANTLR start "DOUBLESLASHEQUAL"
    def mDOUBLESLASHEQUAL(self, ):

        try:
            _type = DOUBLESLASHEQUAL
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:567:3: ( '//=' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:567:5: '//='
            pass 
            self.match("//=")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DOUBLESLASHEQUAL"



    # $ANTLR start "GLOBAL"
    def mGLOBAL(self, ):

        try:
            _type = GLOBAL
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:571:3: ( 'global' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:571:5: 'global'
            pass 
            self.match("global")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "GLOBAL"



    # $ANTLR start "ATTRIBUTE"
    def mATTRIBUTE(self, ):

        try:
            _type = ATTRIBUTE
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:575:3: ( 'attribute' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:575:5: 'attribute'
            pass 
            self.match("attribute")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ATTRIBUTE"



    # $ANTLR start "RULE"
    def mRULE(self, ):

        try:
            _type = RULE
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:579:3: ( 'rule' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:579:5: 'rule'
            pass 
            self.match("rule")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RULE"



    # $ANTLR start "AGENDAGROUP"
    def mAGENDAGROUP(self, ):

        try:
            _type = AGENDAGROUP
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:583:3: ( 'agenda-group' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:583:5: 'agenda-group'
            pass 
            self.match("agenda-group")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "AGENDAGROUP"



    # $ANTLR start "WHEN"
    def mWHEN(self, ):

        try:
            _type = WHEN
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:587:3: ( 'when' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:587:5: 'when'
            pass 
            self.match("when")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WHEN"



    # $ANTLR start "EXISTS"
    def mEXISTS(self, ):

        try:
            _type = EXISTS
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:591:3: ( 'exists' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:591:5: 'exists'
            pass 
            self.match("exists")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "EXISTS"



    # $ANTLR start "THEN"
    def mTHEN(self, ):

        try:
            _type = THEN
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:595:3: ( 'then' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:595:5: 'then'
            pass 
            self.match("then")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "THEN"



    # $ANTLR start "MODIFY"
    def mMODIFY(self, ):

        try:
            _type = MODIFY
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:599:3: ( 'modify' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:599:5: 'modify'
            pass 
            self.match("modify")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MODIFY"



    # $ANTLR start "INSERT"
    def mINSERT(self, ):

        try:
            _type = INSERT
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:603:3: ( 'insert' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:603:5: 'insert'
            pass 
            self.match("insert")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INSERT"



    # $ANTLR start "LEARN"
    def mLEARN(self, ):

        try:
            _type = LEARN
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:607:3: ( 'learn' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:607:5: 'learn'
            pass 
            self.match("learn")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LEARN"



    # $ANTLR start "DELETE"
    def mDELETE(self, ):

        try:
            _type = DELETE
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:611:3: ( 'delete' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:611:5: 'delete'
            pass 
            self.match("delete")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "DELETE"



    # $ANTLR start "FORGET"
    def mFORGET(self, ):

        try:
            _type = FORGET
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:615:3: ( 'forget' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:615:5: 'forget'
            pass 
            self.match("forget")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FORGET"



    # $ANTLR start "HALT"
    def mHALT(self, ):

        try:
            _type = HALT
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:619:3: ( 'halt' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:619:5: 'halt'
            pass 
            self.match("halt")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "HALT"



    # $ANTLR start "PRINT"
    def mPRINT(self, ):

        try:
            _type = PRINT
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:623:3: ( 'print' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:623:5: 'print'
            pass 
            self.match("print")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PRINT"



    # $ANTLR start "IMPORT"
    def mIMPORT(self, ):

        try:
            _type = IMPORT
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:627:3: ( 'import' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:627:5: 'import'
            pass 
            self.match("import")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "IMPORT"



    # $ANTLR start "FROM"
    def mFROM(self, ):

        try:
            _type = FROM
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:631:3: ( 'from' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:631:5: 'from'
            pass 
            self.match("from")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FROM"



    # $ANTLR start "AND"
    def mAND(self, ):

        try:
            _type = AND
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:635:3: ( 'and' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:635:5: 'and'
            pass 
            self.match("and")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "AND"



    # $ANTLR start "OR"
    def mOR(self, ):

        try:
            _type = OR
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:639:3: ( 'or' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:639:5: 'or'
            pass 
            self.match("or")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OR"



    # $ANTLR start "IN"
    def mIN(self, ):

        try:
            _type = IN
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:643:3: ( 'in' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:643:5: 'in'
            pass 
            self.match("in")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "IN"



    # $ANTLR start "IS"
    def mIS(self, ):

        try:
            _type = IS
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:647:3: ( 'is' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:647:5: 'is'
            pass 
            self.match("is")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "IS"



    # $ANTLR start "AS"
    def mAS(self, ):

        try:
            _type = AS
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:651:3: ( 'as' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:651:5: 'as'
            pass 
            self.match("as")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "AS"



    # $ANTLR start "NOT"
    def mNOT(self, ):

        try:
            _type = NOT
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:655:3: ( 'not' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:655:5: 'not'
            pass 
            self.match("not")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NOT"



    # $ANTLR start "LETTER"
    def mLETTER(self, ):

        try:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:660:3: ( ( 'a' .. 'z' | 'A' .. 'Z' ) )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:660:5: ( 'a' .. 'z' | 'A' .. 'Z' )
            pass 
            if (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "LETTER"



    # $ANTLR start "DIGIT"
    def mDIGIT(self, ):

        try:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:665:3: ( ( '0' .. '9' ) )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:665:5: ( '0' .. '9' )
            pass 
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:665:5: ( '0' .. '9' )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:665:6: '0' .. '9'
            pass 
            self.matchRange(48, 57)







        finally:

            pass

    # $ANTLR end "DIGIT"



    # $ANTLR start "FLOAT"
    def mFLOAT(self, ):

        try:
            _type = FLOAT
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:669:3: ( '.' ( DIGIT )+ ( EXPONENT )? | ( DIGIT )+ '.' EXPONENT | ( DIGIT )+ ( '.' ( ( DIGIT )+ ( EXPONENT )? )? | EXPONENT ) )
            alt9 = 3
            alt9 = self.dfa9.predict(self.input)
            if alt9 == 1:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:669:5: '.' ( DIGIT )+ ( EXPONENT )?
                pass 
                self.match(46)
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:669:9: ( DIGIT )+
                cnt1 = 0
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if ((48 <= LA1_0 <= 57)) :
                        alt1 = 1


                    if alt1 == 1:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:669:9: DIGIT
                        pass 
                        self.mDIGIT()


                    else:
                        if cnt1 >= 1:
                            break #loop1

                        eee = EarlyExitException(1, self.input)
                        raise eee

                    cnt1 += 1
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:669:16: ( EXPONENT )?
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if (LA2_0 == 69 or LA2_0 == 101) :
                    alt2 = 1
                if alt2 == 1:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:669:17: EXPONENT
                    pass 
                    self.mEXPONENT()





            elif alt9 == 2:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:670:5: ( DIGIT )+ '.' EXPONENT
                pass 
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:670:5: ( DIGIT )+
                cnt3 = 0
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if ((48 <= LA3_0 <= 57)) :
                        alt3 = 1


                    if alt3 == 1:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:670:5: DIGIT
                        pass 
                        self.mDIGIT()


                    else:
                        if cnt3 >= 1:
                            break #loop3

                        eee = EarlyExitException(3, self.input)
                        raise eee

                    cnt3 += 1
                self.match(46)
                self.mEXPONENT()


            elif alt9 == 3:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:671:5: ( DIGIT )+ ( '.' ( ( DIGIT )+ ( EXPONENT )? )? | EXPONENT )
                pass 
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:671:5: ( DIGIT )+
                cnt4 = 0
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if ((48 <= LA4_0 <= 57)) :
                        alt4 = 1


                    if alt4 == 1:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:671:5: DIGIT
                        pass 
                        self.mDIGIT()


                    else:
                        if cnt4 >= 1:
                            break #loop4

                        eee = EarlyExitException(4, self.input)
                        raise eee

                    cnt4 += 1
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:671:12: ( '.' ( ( DIGIT )+ ( EXPONENT )? )? | EXPONENT )
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if (LA8_0 == 46) :
                    alt8 = 1
                elif (LA8_0 == 69 or LA8_0 == 101) :
                    alt8 = 2
                else:
                    nvae = NoViableAltException("", 8, 0, self.input)

                    raise nvae

                if alt8 == 1:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:671:13: '.' ( ( DIGIT )+ ( EXPONENT )? )?
                    pass 
                    self.match(46)
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:671:17: ( ( DIGIT )+ ( EXPONENT )? )?
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if ((48 <= LA7_0 <= 57)) :
                        alt7 = 1
                    if alt7 == 1:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:671:18: ( DIGIT )+ ( EXPONENT )?
                        pass 
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:671:18: ( DIGIT )+
                        cnt5 = 0
                        while True: #loop5
                            alt5 = 2
                            LA5_0 = self.input.LA(1)

                            if ((48 <= LA5_0 <= 57)) :
                                alt5 = 1


                            if alt5 == 1:
                                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:671:18: DIGIT
                                pass 
                                self.mDIGIT()


                            else:
                                if cnt5 >= 1:
                                    break #loop5

                                eee = EarlyExitException(5, self.input)
                                raise eee

                            cnt5 += 1
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:671:25: ( EXPONENT )?
                        alt6 = 2
                        LA6_0 = self.input.LA(1)

                        if (LA6_0 == 69 or LA6_0 == 101) :
                            alt6 = 1
                        if alt6 == 1:
                            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:671:26: EXPONENT
                            pass 
                            self.mEXPONENT()








                elif alt8 == 2:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:671:41: EXPONENT
                    pass 
                    self.mEXPONENT()





            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FLOAT"



    # $ANTLR start "LONGINT"
    def mLONGINT(self, ):

        try:
            _type = LONGINT
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:675:3: ( INT ( 'l' | 'L' ) )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:675:5: INT ( 'l' | 'L' )
            pass 
            self.mINT()
            if self.input.LA(1) == 76 or self.input.LA(1) == 108:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LONGINT"



    # $ANTLR start "EXPONENT"
    def mEXPONENT(self, ):

        try:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:680:3: ( ( 'e' | 'E' ) ( '+' | '-' )? ( DIGIT )+ )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:680:5: ( 'e' | 'E' ) ( '+' | '-' )? ( DIGIT )+
            pass 
            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:680:17: ( '+' | '-' )?
            alt10 = 2
            LA10_0 = self.input.LA(1)

            if (LA10_0 == 43 or LA10_0 == 45) :
                alt10 = 1
            if alt10 == 1:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:
                pass 
                if self.input.LA(1) == 43 or self.input.LA(1) == 45:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse




            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:680:32: ( DIGIT )+
            cnt11 = 0
            while True: #loop11
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if ((48 <= LA11_0 <= 57)) :
                    alt11 = 1


                if alt11 == 1:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:680:32: DIGIT
                    pass 
                    self.mDIGIT()


                else:
                    if cnt11 >= 1:
                        break #loop11

                    eee = EarlyExitException(11, self.input)
                    raise eee

                cnt11 += 1




        finally:

            pass

    # $ANTLR end "EXPONENT"



    # $ANTLR start "INT"
    def mINT(self, ):

        try:
            _type = INT
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:684:3: ( '0' ( 'x' | 'X' ) ( DIGIT | 'a' .. 'f' | 'A' .. 'F' )+ | '0' ( DIGIT )* | '1' .. '9' ( DIGIT )* )
            alt15 = 3
            LA15_0 = self.input.LA(1)

            if (LA15_0 == 48) :
                LA15_1 = self.input.LA(2)

                if (LA15_1 == 88 or LA15_1 == 120) :
                    alt15 = 1
                else:
                    alt15 = 2
            elif ((49 <= LA15_0 <= 57)) :
                alt15 = 3
            else:
                nvae = NoViableAltException("", 15, 0, self.input)

                raise nvae

            if alt15 == 1:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:684:5: '0' ( 'x' | 'X' ) ( DIGIT | 'a' .. 'f' | 'A' .. 'F' )+
                pass 
                self.match(48)
                if self.input.LA(1) == 88 or self.input.LA(1) == 120:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse

                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:684:21: ( DIGIT | 'a' .. 'f' | 'A' .. 'F' )+
                cnt12 = 0
                while True: #loop12
                    alt12 = 4
                    LA12 = self.input.LA(1)
                    if LA12 == 48 or LA12 == 49 or LA12 == 50 or LA12 == 51 or LA12 == 52 or LA12 == 53 or LA12 == 54 or LA12 == 55 or LA12 == 56 or LA12 == 57:
                        alt12 = 1
                    elif LA12 == 97 or LA12 == 98 or LA12 == 99 or LA12 == 100 or LA12 == 101 or LA12 == 102:
                        alt12 = 2
                    elif LA12 == 65 or LA12 == 66 or LA12 == 67 or LA12 == 68 or LA12 == 69 or LA12 == 70:
                        alt12 = 3

                    if alt12 == 1:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:684:23: DIGIT
                        pass 
                        self.mDIGIT()


                    elif alt12 == 2:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:684:31: 'a' .. 'f'
                        pass 
                        self.matchRange(97, 102)


                    elif alt12 == 3:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:684:44: 'A' .. 'F'
                        pass 
                        self.matchRange(65, 70)


                    else:
                        if cnt12 >= 1:
                            break #loop12

                        eee = EarlyExitException(12, self.input)
                        raise eee

                    cnt12 += 1


            elif alt15 == 2:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:685:5: '0' ( DIGIT )*
                pass 
                self.match(48)
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:685:9: ( DIGIT )*
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if ((48 <= LA13_0 <= 57)) :
                        alt13 = 1


                    if alt13 == 1:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:685:9: DIGIT
                        pass 
                        self.mDIGIT()


                    else:
                        break #loop13


            elif alt15 == 3:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:686:5: '1' .. '9' ( DIGIT )*
                pass 
                self.matchRange(49, 57)
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:686:14: ( DIGIT )*
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if ((48 <= LA14_0 <= 57)) :
                        alt14 = 1


                    if alt14 == 1:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:686:14: DIGIT
                        pass 
                        self.mDIGIT()


                    else:
                        break #loop14


            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INT"



    # $ANTLR start "COMPLEX"
    def mCOMPLEX(self, ):

        try:
            _type = COMPLEX
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:690:3: ( INT ( 'j' | 'J' ) | FLOAT ( 'j' | 'J' ) )
            alt16 = 2
            alt16 = self.dfa16.predict(self.input)
            if alt16 == 1:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:690:5: INT ( 'j' | 'J' )
                pass 
                self.mINT()
                if self.input.LA(1) == 74 or self.input.LA(1) == 106:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse



            elif alt16 == 2:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:691:5: FLOAT ( 'j' | 'J' )
                pass 
                self.mFLOAT()
                if self.input.LA(1) == 74 or self.input.LA(1) == 106:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COMPLEX"



    # $ANTLR start "NAME"
    def mNAME(self, ):

        try:
            _type = NAME
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:695:3: ( ( LETTER | '_' ) ( LETTER | '_' | DIGIT )* )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:695:5: ( LETTER | '_' ) ( LETTER | '_' | DIGIT )*
            pass 
            if (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:695:21: ( LETTER | '_' | DIGIT )*
            while True: #loop17
                alt17 = 4
                LA17 = self.input.LA(1)
                if LA17 == 65 or LA17 == 66 or LA17 == 67 or LA17 == 68 or LA17 == 69 or LA17 == 70 or LA17 == 71 or LA17 == 72 or LA17 == 73 or LA17 == 74 or LA17 == 75 or LA17 == 76 or LA17 == 77 or LA17 == 78 or LA17 == 79 or LA17 == 80 or LA17 == 81 or LA17 == 82 or LA17 == 83 or LA17 == 84 or LA17 == 85 or LA17 == 86 or LA17 == 87 or LA17 == 88 or LA17 == 89 or LA17 == 90 or LA17 == 97 or LA17 == 98 or LA17 == 99 or LA17 == 100 or LA17 == 101 or LA17 == 102 or LA17 == 103 or LA17 == 104 or LA17 == 105 or LA17 == 106 or LA17 == 107 or LA17 == 108 or LA17 == 109 or LA17 == 110 or LA17 == 111 or LA17 == 112 or LA17 == 113 or LA17 == 114 or LA17 == 115 or LA17 == 116 or LA17 == 117 or LA17 == 118 or LA17 == 119 or LA17 == 120 or LA17 == 121 or LA17 == 122:
                    alt17 = 1
                elif LA17 == 95:
                    alt17 = 2
                elif LA17 == 48 or LA17 == 49 or LA17 == 50 or LA17 == 51 or LA17 == 52 or LA17 == 53 or LA17 == 54 or LA17 == 55 or LA17 == 56 or LA17 == 57:
                    alt17 = 3

                if alt17 == 1:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:695:23: LETTER
                    pass 
                    self.mLETTER()


                elif alt17 == 2:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:695:32: '_'
                    pass 
                    self.match(95)


                elif alt17 == 3:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:695:38: DIGIT
                    pass 
                    self.mDIGIT()


                else:
                    break #loop17



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NAME"



    # $ANTLR start "OBJECTBINDING"
    def mOBJECTBINDING(self, ):

        try:
            _type = OBJECTBINDING
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:699:3: ( DOLLAR NAME )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:699:5: DOLLAR NAME
            pass 
            self.mDOLLAR()
            self.mNAME()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OBJECTBINDING"



    # $ANTLR start "STRING"
    def mSTRING(self, ):

        try:
            _type = STRING
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:703:3: ( ( 'r' | 'u' | 'ur' )? ( '\\'\\'\\'' ( options {greedy=false; } : TRIAPOS )* '\\'\\'\\'' | '\"\"\"' ( options {greedy=false; } : TRIQUOTE )* '\"\"\"' | '\"' ( ESC | ~ ( '\\\\' | '\\n' | '\"' ) )* '\"' | '\\'' ( ESC | ~ ( '\\\\' | '\\n' | '\\'' ) )* '\\'' ) )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:703:5: ( 'r' | 'u' | 'ur' )? ( '\\'\\'\\'' ( options {greedy=false; } : TRIAPOS )* '\\'\\'\\'' | '\"\"\"' ( options {greedy=false; } : TRIQUOTE )* '\"\"\"' | '\"' ( ESC | ~ ( '\\\\' | '\\n' | '\"' ) )* '\"' | '\\'' ( ESC | ~ ( '\\\\' | '\\n' | '\\'' ) )* '\\'' )
            pass 
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:703:5: ( 'r' | 'u' | 'ur' )?
            alt18 = 4
            LA18_0 = self.input.LA(1)

            if (LA18_0 == 114) :
                alt18 = 1
            elif (LA18_0 == 117) :
                LA18_2 = self.input.LA(2)

                if (LA18_2 == 114) :
                    alt18 = 3
                elif (LA18_2 == 34 or LA18_2 == 39) :
                    alt18 = 2
            if alt18 == 1:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:703:6: 'r'
                pass 
                self.match(114)


            elif alt18 == 2:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:703:10: 'u'
                pass 
                self.match(117)


            elif alt18 == 3:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:703:14: 'ur'
                pass 
                self.match("ur")



            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:704:5: ( '\\'\\'\\'' ( options {greedy=false; } : TRIAPOS )* '\\'\\'\\'' | '\"\"\"' ( options {greedy=false; } : TRIQUOTE )* '\"\"\"' | '\"' ( ESC | ~ ( '\\\\' | '\\n' | '\"' ) )* '\"' | '\\'' ( ESC | ~ ( '\\\\' | '\\n' | '\\'' ) )* '\\'' )
            alt23 = 4
            LA23_0 = self.input.LA(1)

            if (LA23_0 == 39) :
                LA23_1 = self.input.LA(2)

                if (LA23_1 == 39) :
                    LA23_3 = self.input.LA(3)

                    if (LA23_3 == 39) :
                        alt23 = 1
                    else:
                        alt23 = 4
                elif ((0 <= LA23_1 <= 9) or (11 <= LA23_1 <= 38) or (40 <= LA23_1 <= 65535)) :
                    alt23 = 4
                else:
                    nvae = NoViableAltException("", 23, 1, self.input)

                    raise nvae

            elif (LA23_0 == 34) :
                LA23_2 = self.input.LA(2)

                if (LA23_2 == 34) :
                    LA23_5 = self.input.LA(3)

                    if (LA23_5 == 34) :
                        alt23 = 2
                    else:
                        alt23 = 3
                elif ((0 <= LA23_2 <= 9) or (11 <= LA23_2 <= 33) or (35 <= LA23_2 <= 65535)) :
                    alt23 = 3
                else:
                    nvae = NoViableAltException("", 23, 2, self.input)

                    raise nvae

            else:
                nvae = NoViableAltException("", 23, 0, self.input)

                raise nvae

            if alt23 == 1:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:704:9: '\\'\\'\\'' ( options {greedy=false; } : TRIAPOS )* '\\'\\'\\''
                pass 
                self.match("'''")
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:704:18: ( options {greedy=false; } : TRIAPOS )*
                while True: #loop19
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if (LA19_0 == 39) :
                        LA19_1 = self.input.LA(2)

                        if (LA19_1 == 39) :
                            LA19_3 = self.input.LA(3)

                            if (LA19_3 == 39) :
                                alt19 = 2
                            elif ((0 <= LA19_3 <= 38) or (40 <= LA19_3 <= 65535)) :
                                alt19 = 1


                        elif ((0 <= LA19_1 <= 38) or (40 <= LA19_1 <= 65535)) :
                            alt19 = 1


                    elif ((0 <= LA19_0 <= 38) or (40 <= LA19_0 <= 65535)) :
                        alt19 = 1


                    if alt19 == 1:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:704:43: TRIAPOS
                        pass 
                        self.mTRIAPOS()


                    else:
                        break #loop19
                self.match("'''")


            elif alt23 == 2:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:705:9: '\"\"\"' ( options {greedy=false; } : TRIQUOTE )* '\"\"\"'
                pass 
                self.match("\"\"\"")
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:705:15: ( options {greedy=false; } : TRIQUOTE )*
                while True: #loop20
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if (LA20_0 == 34) :
                        LA20_1 = self.input.LA(2)

                        if (LA20_1 == 34) :
                            LA20_3 = self.input.LA(3)

                            if (LA20_3 == 34) :
                                alt20 = 2
                            elif ((0 <= LA20_3 <= 33) or (35 <= LA20_3 <= 65535)) :
                                alt20 = 1


                        elif ((0 <= LA20_1 <= 33) or (35 <= LA20_1 <= 65535)) :
                            alt20 = 1


                    elif ((0 <= LA20_0 <= 33) or (35 <= LA20_0 <= 65535)) :
                        alt20 = 1


                    if alt20 == 1:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:705:40: TRIQUOTE
                        pass 
                        self.mTRIQUOTE()


                    else:
                        break #loop20
                self.match("\"\"\"")


            elif alt23 == 3:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:706:9: '\"' ( ESC | ~ ( '\\\\' | '\\n' | '\"' ) )* '\"'
                pass 
                self.match(34)
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:706:13: ( ESC | ~ ( '\\\\' | '\\n' | '\"' ) )*
                while True: #loop21
                    alt21 = 3
                    LA21_0 = self.input.LA(1)

                    if (LA21_0 == 92) :
                        alt21 = 1
                    elif ((0 <= LA21_0 <= 9) or (11 <= LA21_0 <= 33) or (35 <= LA21_0 <= 91) or (93 <= LA21_0 <= 65535)) :
                        alt21 = 2


                    if alt21 == 1:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:706:14: ESC
                        pass 
                        self.mESC()


                    elif alt21 == 2:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:706:18: ~ ( '\\\\' | '\\n' | '\"' )
                        pass 
                        if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 33) or (35 <= self.input.LA(1) <= 91) or (93 <= self.input.LA(1) <= 65535):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse



                    else:
                        break #loop21
                self.match(34)


            elif alt23 == 4:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:707:9: '\\'' ( ESC | ~ ( '\\\\' | '\\n' | '\\'' ) )* '\\''
                pass 
                self.match(39)
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:707:14: ( ESC | ~ ( '\\\\' | '\\n' | '\\'' ) )*
                while True: #loop22
                    alt22 = 3
                    LA22_0 = self.input.LA(1)

                    if (LA22_0 == 92) :
                        alt22 = 1
                    elif ((0 <= LA22_0 <= 9) or (11 <= LA22_0 <= 38) or (40 <= LA22_0 <= 91) or (93 <= LA22_0 <= 65535)) :
                        alt22 = 2


                    if alt22 == 1:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:707:15: ESC
                        pass 
                        self.mESC()


                    elif alt22 == 2:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:707:19: ~ ( '\\\\' | '\\n' | '\\'' )
                        pass 
                        if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 38) or (40 <= self.input.LA(1) <= 91) or (93 <= self.input.LA(1) <= 65535):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse



                    else:
                        break #loop22
                self.match(39)






            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STRING"



    # $ANTLR start "TRIQUOTE"
    def mTRIQUOTE(self, ):

        try:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:713:2: ( ( '\"' )? ( '\"' )? ( ESC | ~ ( '\\\\' | '\"' ) )+ )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:713:4: ( '\"' )? ( '\"' )? ( ESC | ~ ( '\\\\' | '\"' ) )+
            pass 
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:713:4: ( '\"' )?
            alt24 = 2
            LA24_0 = self.input.LA(1)

            if (LA24_0 == 34) :
                alt24 = 1
            if alt24 == 1:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:713:4: '\"'
                pass 
                self.match(34)



            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:713:9: ( '\"' )?
            alt25 = 2
            LA25_0 = self.input.LA(1)

            if (LA25_0 == 34) :
                alt25 = 1
            if alt25 == 1:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:713:9: '\"'
                pass 
                self.match(34)



            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:713:14: ( ESC | ~ ( '\\\\' | '\"' ) )+
            cnt26 = 0
            while True: #loop26
                alt26 = 3
                LA26_0 = self.input.LA(1)

                if (LA26_0 == 92) :
                    alt26 = 1
                elif ((0 <= LA26_0 <= 33) or (35 <= LA26_0 <= 91) or (93 <= LA26_0 <= 65535)) :
                    alt26 = 2


                if alt26 == 1:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:713:15: ESC
                    pass 
                    self.mESC()


                elif alt26 == 2:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:713:19: ~ ( '\\\\' | '\"' )
                    pass 
                    if (0 <= self.input.LA(1) <= 33) or (35 <= self.input.LA(1) <= 91) or (93 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    if cnt26 >= 1:
                        break #loop26

                    eee = EarlyExitException(26, self.input)
                    raise eee

                cnt26 += 1




        finally:

            pass

    # $ANTLR end "TRIQUOTE"



    # $ANTLR start "TRIAPOS"
    def mTRIAPOS(self, ):

        try:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:718:3: ( ( '\\'' )? ( '\\'' )? ( ESC | ~ ( '\\\\' | '\\'' ) )+ )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:718:5: ( '\\'' )? ( '\\'' )? ( ESC | ~ ( '\\\\' | '\\'' ) )+
            pass 
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:718:5: ( '\\'' )?
            alt27 = 2
            LA27_0 = self.input.LA(1)

            if (LA27_0 == 39) :
                alt27 = 1
            if alt27 == 1:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:718:5: '\\''
                pass 
                self.match(39)



            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:718:11: ( '\\'' )?
            alt28 = 2
            LA28_0 = self.input.LA(1)

            if (LA28_0 == 39) :
                alt28 = 1
            if alt28 == 1:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:718:11: '\\''
                pass 
                self.match(39)



            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:718:17: ( ESC | ~ ( '\\\\' | '\\'' ) )+
            cnt29 = 0
            while True: #loop29
                alt29 = 3
                LA29_0 = self.input.LA(1)

                if (LA29_0 == 92) :
                    alt29 = 1
                elif ((0 <= LA29_0 <= 38) or (40 <= LA29_0 <= 91) or (93 <= LA29_0 <= 65535)) :
                    alt29 = 2


                if alt29 == 1:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:718:18: ESC
                    pass 
                    self.mESC()


                elif alt29 == 2:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:718:22: ~ ( '\\\\' | '\\'' )
                    pass 
                    if (0 <= self.input.LA(1) <= 38) or (40 <= self.input.LA(1) <= 91) or (93 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    if cnt29 >= 1:
                        break #loop29

                    eee = EarlyExitException(29, self.input)
                    raise eee

                cnt29 += 1




        finally:

            pass

    # $ANTLR end "TRIAPOS"



    # $ANTLR start "ESC"
    def mESC(self, ):

        try:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:723:5: ( '\\\\' . )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:723:10: '\\\\' .
            pass 
            self.match(92)
            self.matchAny()




        finally:

            pass

    # $ANTLR end "ESC"



    # $ANTLR start "CONTINUED_LINE"
    def mCONTINUED_LINE(self, ):

        try:
            _type = CONTINUED_LINE
            _channel = DEFAULT_CHANNEL

            newline = None

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:727:3: ( '\\\\' ( '\\r' )? '\\n' ( ' ' | '\\t' )* (newline= NEWLINE | ) )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:727:5: '\\\\' ( '\\r' )? '\\n' ( ' ' | '\\t' )* (newline= NEWLINE | )
            pass 
            self.match(92)
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:727:10: ( '\\r' )?
            alt30 = 2
            LA30_0 = self.input.LA(1)

            if (LA30_0 == 13) :
                alt30 = 1
            if alt30 == 1:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:727:12: '\\r'
                pass 
                self.match(13)



            self.match(10)
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:727:25: ( ' ' | '\\t' )*
            while True: #loop31
                alt31 = 2
                LA31_0 = self.input.LA(1)

                if (LA31_0 == 9 or LA31_0 == 32) :
                    alt31 = 1


                if alt31 == 1:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:
                    pass 
                    if self.input.LA(1) == 9 or self.input.LA(1) == 32:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop31
            #action start
            _channel=HIDDEN 
            #action end
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:728:7: (newline= NEWLINE | )
            alt32 = 2
            LA32_0 = self.input.LA(1)

            if (LA32_0 == 10 or (12 <= LA32_0 <= 13)) :
                alt32 = 1
            else:
                alt32 = 2
            if alt32 == 1:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:728:9: newline= NEWLINE
                pass 
                newlineStart1557 = self.getCharIndex()
                self.mNEWLINE()
                newline = CommonToken(
                    input=self.input, 
                    type=INVALID_TOKEN_TYPE,
                    channel=DEFAULT_CHANNEL,
                    start=newlineStart1557,
                    stop=self.getCharIndex()-1
                    )
                #action start
                self.emit( ClassicToken( NEWLINE, newline.text ) ) 
                #action end


            elif alt32 == 2:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:730:9: 
                pass 





            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "CONTINUED_LINE"



    # $ANTLR start "NEWLINE"
    def mNEWLINE(self, ):

        try:
            _type = NEWLINE
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:734:3: ( ( ( '\\u000C' )? ( '\\r' )? '\\n' )+ )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:734:5: ( ( '\\u000C' )? ( '\\r' )? '\\n' )+
            pass 
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:734:5: ( ( '\\u000C' )? ( '\\r' )? '\\n' )+
            cnt35 = 0
            while True: #loop35
                alt35 = 2
                LA35_0 = self.input.LA(1)

                if (LA35_0 == 10 or (12 <= LA35_0 <= 13)) :
                    alt35 = 1


                if alt35 == 1:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:734:7: ( '\\u000C' )? ( '\\r' )? '\\n'
                    pass 
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:734:7: ( '\\u000C' )?
                    alt33 = 2
                    LA33_0 = self.input.LA(1)

                    if (LA33_0 == 12) :
                        alt33 = 1
                    if alt33 == 1:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:734:9: '\\u000C'
                        pass 
                        self.match(12)



                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:734:21: ( '\\r' )?
                    alt34 = 2
                    LA34_0 = self.input.LA(1)

                    if (LA34_0 == 13) :
                        alt34 = 1
                    if alt34 == 1:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:734:23: '\\r'
                        pass 
                        self.match(13)



                    self.match(10)


                else:
                    if cnt35 >= 1:
                        break #loop35

                    eee = EarlyExitException(35, self.input)
                    raise eee

                cnt35 += 1
            #action start
                                                   
            if self.startPosition == 0 or self.implicitLineJoiningLevel > 0:
                _channel=HIDDEN
                
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "NEWLINE"



    # $ANTLR start "WS"
    def mWS(self, ):

        try:
            _type = WS
            _channel = DEFAULT_CHANNEL

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:741:3: ({...}? => ( ' ' | '\\t' )+ )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:741:5: {...}? => ( ' ' | '\\t' )+
            pass 
            if not ((self.startPosition > 0 )):
                raise FailedPredicateException(self.input, "WS", " self.startPosition > 0 ")

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:741:36: ( ' ' | '\\t' )+
            cnt36 = 0
            while True: #loop36
                alt36 = 2
                LA36_0 = self.input.LA(1)

                if (LA36_0 == 9 or LA36_0 == 32) :
                    alt36 = 1


                if alt36 == 1:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:
                    pass 
                    if self.input.LA(1) == 9 or self.input.LA(1) == 32:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    if cnt36 >= 1:
                        break #loop36

                    eee = EarlyExitException(36, self.input)
                    raise eee

                cnt36 += 1
            #action start
            _channel=HIDDEN 
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WS"



    # $ANTLR start "LEADING_WS"
    def mLEADING_WS(self, ):

        try:
            _type = LEADING_WS
            _channel = DEFAULT_CHANNEL

            spaces = 0 
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:746:3: ({...}? => ({...}? ( ' ' | '\\t' )+ | ( ' ' | '\\t' )+ ( ( '\\r' )? '\\n' )* ) )
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:746:5: {...}? => ({...}? ( ' ' | '\\t' )+ | ( ' ' | '\\t' )+ ( ( '\\r' )? '\\n' )* )
            pass 
            if not ((self.startPosition == 0 )):
                raise FailedPredicateException(self.input, "LEADING_WS", " self.startPosition == 0 ")

            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:747:7: ({...}? ( ' ' | '\\t' )+ | ( ' ' | '\\t' )+ ( ( '\\r' )? '\\n' )* )
            alt41 = 2
            LA41_0 = self.input.LA(1)

            if (LA41_0 == 32) :
                LA41_1 = self.input.LA(2)

                if ((self.implicitLineJoiningLevel > 0)) :
                    alt41 = 1
                elif (True) :
                    alt41 = 2
                else:
                    nvae = NoViableAltException("", 41, 1, self.input)

                    raise nvae

            elif (LA41_0 == 9) :
                LA41_2 = self.input.LA(2)

                if ((self.implicitLineJoiningLevel > 0)) :
                    alt41 = 1
                elif (True) :
                    alt41 = 2
                else:
                    nvae = NoViableAltException("", 41, 2, self.input)

                    raise nvae

            else:
                nvae = NoViableAltException("", 41, 0, self.input)

                raise nvae

            if alt41 == 1:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:747:9: {...}? ( ' ' | '\\t' )+
                pass 
                if not ((self.implicitLineJoiningLevel > 0)):
                    raise FailedPredicateException(self.input, "LEADING_WS", "self.implicitLineJoiningLevel > 0")

                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:747:46: ( ' ' | '\\t' )+
                cnt37 = 0
                while True: #loop37
                    alt37 = 2
                    LA37_0 = self.input.LA(1)

                    if (LA37_0 == 9 or LA37_0 == 32) :
                        alt37 = 1


                    if alt37 == 1:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:
                        pass 
                        if self.input.LA(1) == 9 or self.input.LA(1) == 32:
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse



                    else:
                        if cnt37 >= 1:
                            break #loop37

                        eee = EarlyExitException(37, self.input)
                        raise eee

                    cnt37 += 1
                #action start
                _channel=HIDDEN 
                #action end


            elif alt41 == 2:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:748:11: ( ' ' | '\\t' )+ ( ( '\\r' )? '\\n' )*
                pass 
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:748:11: ( ' ' | '\\t' )+
                cnt38 = 0
                while True: #loop38
                    alt38 = 3
                    LA38_0 = self.input.LA(1)

                    if (LA38_0 == 32) :
                        alt38 = 1
                    elif (LA38_0 == 9) :
                        alt38 = 2


                    if alt38 == 1:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:748:16: ' '
                        pass 
                        self.match(32)
                        #action start
                        spaces += 1 
                        #action end


                    elif alt38 == 2:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:749:15: '\\t'
                        pass 
                        self.match(9)
                        #action start
                                            
                        spaces += 8
                        spaces -= (spaces % 8)
                                           
                        #action end


                    else:
                        if cnt38 >= 1:
                            break #loop38

                        eee = EarlyExitException(38, self.input)
                        raise eee

                    cnt38 += 1
                #action start
                self.emit(ClassicToken(LEADING_WS, ' '*spaces)) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:754:16: ( ( '\\r' )? '\\n' )*
                while True: #loop40
                    alt40 = 2
                    LA40_0 = self.input.LA(1)

                    if (LA40_0 == 10 or LA40_0 == 13) :
                        alt40 = 1


                    if alt40 == 1:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:754:18: ( '\\r' )? '\\n'
                        pass 
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:754:18: ( '\\r' )?
                        alt39 = 2
                        LA39_0 = self.input.LA(1)

                        if (LA39_0 == 13) :
                            alt39 = 1
                        if alt39 == 1:
                            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:754:19: '\\r'
                            pass 
                            self.match(13)



                        self.match(10)
                        #action start
                                                       
                        if self._state.token is not None:
                            self._state.token.setChannel(99)
                        else:
                            _channel=HIDDEN
                        	               
                        #action end


                    else:
                        break #loop40






            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "LEADING_WS"



    # $ANTLR start "COMMENT"
    def mCOMMENT(self, ):

        try:
            _type = COMMENT
            _channel = DEFAULT_CHANNEL

            _channel=HIDDEN 
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:766:3: ({...}? => ( ' ' | '\\t' )* '#' (~ '\\n' )* ( '\\n' )+ | {...}? => '#' (~ '\\n' )* )
            alt46 = 2
            alt46 = self.dfa46.predict(self.input)
            if alt46 == 1:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:766:5: {...}? => ( ' ' | '\\t' )* '#' (~ '\\n' )* ( '\\n' )+
                pass 
                if not ((self.startPosition == 0 )):
                    raise FailedPredicateException(self.input, "COMMENT", " self.startPosition == 0 ")

                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:766:37: ( ' ' | '\\t' )*
                while True: #loop42
                    alt42 = 2
                    LA42_0 = self.input.LA(1)

                    if (LA42_0 == 9 or LA42_0 == 32) :
                        alt42 = 1


                    if alt42 == 1:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:
                        pass 
                        if self.input.LA(1) == 9 or self.input.LA(1) == 32:
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse



                    else:
                        break #loop42
                self.match(35)
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:766:53: (~ '\\n' )*
                while True: #loop43
                    alt43 = 2
                    LA43_0 = self.input.LA(1)

                    if ((0 <= LA43_0 <= 9) or (11 <= LA43_0 <= 65535)) :
                        alt43 = 1


                    if alt43 == 1:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:766:54: ~ '\\n'
                        pass 
                        if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 65535):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse



                    else:
                        break #loop43
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:766:62: ( '\\n' )+
                cnt44 = 0
                while True: #loop44
                    alt44 = 2
                    LA44_0 = self.input.LA(1)

                    if (LA44_0 == 10) :
                        alt44 = 1


                    if alt44 == 1:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:766:62: '\\n'
                        pass 
                        self.match(10)


                    else:
                        if cnt44 >= 1:
                            break #loop44

                        eee = EarlyExitException(44, self.input)
                        raise eee

                    cnt44 += 1


            elif alt46 == 2:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:767:7: {...}? => '#' (~ '\\n' )*
                pass 
                if not ((self.startPosition > 0 )):
                    raise FailedPredicateException(self.input, "COMMENT", " self.startPosition > 0 ")

                self.match(35)
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:767:42: (~ '\\n' )*
                while True: #loop45
                    alt45 = 2
                    LA45_0 = self.input.LA(1)

                    if ((0 <= LA45_0 <= 9) or (11 <= LA45_0 <= 65535)) :
                        alt45 = 1


                    if alt45 == 1:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:767:43: ~ '\\n'
                        pass 
                        if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 65535):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse



                    else:
                        break #loop45


            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COMMENT"



    def mTokens(self):
        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:8: ( LPAREN | RPAREN | LBRACK | RBRACK | LCURLY | RCURLY | COLON | COMMA | DOT | SEMI | PLUS | MINUS | STAR | DOLLAR | SLASH | VBAR | AMPER | LESS | GREATER | ASSIGN | PERCENT | BACKQUOTE | CIRCUMFLEX | TILDE | EQUAL | ASSIGNEQUAL | NOTEQUAL | ALT_NOTEQUAL | LESSEQUAL | LEFTSHIFT | GREATEREQUAL | RIGHTSHIFT | PLUSEQUAL | MINUSEQUAL | DOUBLESTAR | STAREQUAL | DOUBLESLASH | SLASHEQUAL | VBAREQUAL | PERCENTEQUAL | AMPEREQUAL | CIRCUMFLEXEQUAL | LEFTSHIFTEQUAL | RIGHTSHIFTEQUAL | DOUBLESTAREQUAL | DOUBLESLASHEQUAL | GLOBAL | ATTRIBUTE | RULE | AGENDAGROUP | WHEN | EXISTS | THEN | MODIFY | INSERT | LEARN | DELETE | FORGET | HALT | PRINT | IMPORT | FROM | AND | OR | IN | IS | AS | NOT | FLOAT | LONGINT | INT | COMPLEX | NAME | OBJECTBINDING | STRING | CONTINUED_LINE | NEWLINE | WS | LEADING_WS | COMMENT )
        alt47 = 80
        alt47 = self.dfa47.predict(self.input)
        if alt47 == 1:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:10: LPAREN
            pass 
            self.mLPAREN()


        elif alt47 == 2:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:17: RPAREN
            pass 
            self.mRPAREN()


        elif alt47 == 3:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:24: LBRACK
            pass 
            self.mLBRACK()


        elif alt47 == 4:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:31: RBRACK
            pass 
            self.mRBRACK()


        elif alt47 == 5:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:38: LCURLY
            pass 
            self.mLCURLY()


        elif alt47 == 6:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:45: RCURLY
            pass 
            self.mRCURLY()


        elif alt47 == 7:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:52: COLON
            pass 
            self.mCOLON()


        elif alt47 == 8:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:58: COMMA
            pass 
            self.mCOMMA()


        elif alt47 == 9:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:64: DOT
            pass 
            self.mDOT()


        elif alt47 == 10:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:68: SEMI
            pass 
            self.mSEMI()


        elif alt47 == 11:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:73: PLUS
            pass 
            self.mPLUS()


        elif alt47 == 12:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:78: MINUS
            pass 
            self.mMINUS()


        elif alt47 == 13:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:84: STAR
            pass 
            self.mSTAR()


        elif alt47 == 14:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:89: DOLLAR
            pass 
            self.mDOLLAR()


        elif alt47 == 15:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:96: SLASH
            pass 
            self.mSLASH()


        elif alt47 == 16:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:102: VBAR
            pass 
            self.mVBAR()


        elif alt47 == 17:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:107: AMPER
            pass 
            self.mAMPER()


        elif alt47 == 18:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:113: LESS
            pass 
            self.mLESS()


        elif alt47 == 19:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:118: GREATER
            pass 
            self.mGREATER()


        elif alt47 == 20:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:126: ASSIGN
            pass 
            self.mASSIGN()


        elif alt47 == 21:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:133: PERCENT
            pass 
            self.mPERCENT()


        elif alt47 == 22:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:141: BACKQUOTE
            pass 
            self.mBACKQUOTE()


        elif alt47 == 23:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:151: CIRCUMFLEX
            pass 
            self.mCIRCUMFLEX()


        elif alt47 == 24:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:162: TILDE
            pass 
            self.mTILDE()


        elif alt47 == 25:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:168: EQUAL
            pass 
            self.mEQUAL()


        elif alt47 == 26:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:174: ASSIGNEQUAL
            pass 
            self.mASSIGNEQUAL()


        elif alt47 == 27:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:186: NOTEQUAL
            pass 
            self.mNOTEQUAL()


        elif alt47 == 28:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:195: ALT_NOTEQUAL
            pass 
            self.mALT_NOTEQUAL()


        elif alt47 == 29:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:208: LESSEQUAL
            pass 
            self.mLESSEQUAL()


        elif alt47 == 30:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:218: LEFTSHIFT
            pass 
            self.mLEFTSHIFT()


        elif alt47 == 31:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:228: GREATEREQUAL
            pass 
            self.mGREATEREQUAL()


        elif alt47 == 32:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:241: RIGHTSHIFT
            pass 
            self.mRIGHTSHIFT()


        elif alt47 == 33:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:252: PLUSEQUAL
            pass 
            self.mPLUSEQUAL()


        elif alt47 == 34:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:262: MINUSEQUAL
            pass 
            self.mMINUSEQUAL()


        elif alt47 == 35:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:273: DOUBLESTAR
            pass 
            self.mDOUBLESTAR()


        elif alt47 == 36:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:284: STAREQUAL
            pass 
            self.mSTAREQUAL()


        elif alt47 == 37:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:294: DOUBLESLASH
            pass 
            self.mDOUBLESLASH()


        elif alt47 == 38:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:306: SLASHEQUAL
            pass 
            self.mSLASHEQUAL()


        elif alt47 == 39:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:317: VBAREQUAL
            pass 
            self.mVBAREQUAL()


        elif alt47 == 40:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:327: PERCENTEQUAL
            pass 
            self.mPERCENTEQUAL()


        elif alt47 == 41:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:340: AMPEREQUAL
            pass 
            self.mAMPEREQUAL()


        elif alt47 == 42:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:351: CIRCUMFLEXEQUAL
            pass 
            self.mCIRCUMFLEXEQUAL()


        elif alt47 == 43:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:367: LEFTSHIFTEQUAL
            pass 
            self.mLEFTSHIFTEQUAL()


        elif alt47 == 44:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:382: RIGHTSHIFTEQUAL
            pass 
            self.mRIGHTSHIFTEQUAL()


        elif alt47 == 45:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:398: DOUBLESTAREQUAL
            pass 
            self.mDOUBLESTAREQUAL()


        elif alt47 == 46:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:414: DOUBLESLASHEQUAL
            pass 
            self.mDOUBLESLASHEQUAL()


        elif alt47 == 47:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:431: GLOBAL
            pass 
            self.mGLOBAL()


        elif alt47 == 48:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:438: ATTRIBUTE
            pass 
            self.mATTRIBUTE()


        elif alt47 == 49:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:448: RULE
            pass 
            self.mRULE()


        elif alt47 == 50:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:453: AGENDAGROUP
            pass 
            self.mAGENDAGROUP()


        elif alt47 == 51:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:465: WHEN
            pass 
            self.mWHEN()


        elif alt47 == 52:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:470: EXISTS
            pass 
            self.mEXISTS()


        elif alt47 == 53:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:477: THEN
            pass 
            self.mTHEN()


        elif alt47 == 54:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:482: MODIFY
            pass 
            self.mMODIFY()


        elif alt47 == 55:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:489: INSERT
            pass 
            self.mINSERT()


        elif alt47 == 56:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:496: LEARN
            pass 
            self.mLEARN()


        elif alt47 == 57:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:502: DELETE
            pass 
            self.mDELETE()


        elif alt47 == 58:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:509: FORGET
            pass 
            self.mFORGET()


        elif alt47 == 59:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:516: HALT
            pass 
            self.mHALT()


        elif alt47 == 60:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:521: PRINT
            pass 
            self.mPRINT()


        elif alt47 == 61:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:527: IMPORT
            pass 
            self.mIMPORT()


        elif alt47 == 62:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:534: FROM
            pass 
            self.mFROM()


        elif alt47 == 63:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:539: AND
            pass 
            self.mAND()


        elif alt47 == 64:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:543: OR
            pass 
            self.mOR()


        elif alt47 == 65:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:546: IN
            pass 
            self.mIN()


        elif alt47 == 66:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:549: IS
            pass 
            self.mIS()


        elif alt47 == 67:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:552: AS
            pass 
            self.mAS()


        elif alt47 == 68:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:555: NOT
            pass 
            self.mNOT()


        elif alt47 == 69:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:559: FLOAT
            pass 
            self.mFLOAT()


        elif alt47 == 70:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:565: LONGINT
            pass 
            self.mLONGINT()


        elif alt47 == 71:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:573: INT
            pass 
            self.mINT()


        elif alt47 == 72:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:577: COMPLEX
            pass 
            self.mCOMPLEX()


        elif alt47 == 73:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:585: NAME
            pass 
            self.mNAME()


        elif alt47 == 74:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:590: OBJECTBINDING
            pass 
            self.mOBJECTBINDING()


        elif alt47 == 75:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:604: STRING
            pass 
            self.mSTRING()


        elif alt47 == 76:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:611: CONTINUED_LINE
            pass 
            self.mCONTINUED_LINE()


        elif alt47 == 77:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:626: NEWLINE
            pass 
            self.mNEWLINE()


        elif alt47 == 78:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:634: WS
            pass 
            self.mWS()


        elif alt47 == 79:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:637: LEADING_WS
            pass 
            self.mLEADING_WS()


        elif alt47 == 80:
            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:1:648: COMMENT
            pass 
            self.mCOMMENT()







    # lookup tables for DFA #9

    DFA9_eot = DFA.unpack(
        u"\3\uffff\1\4\2\uffff"
        )

    DFA9_eof = DFA.unpack(
        u"\6\uffff"
        )

    DFA9_min = DFA.unpack(
        u"\1\56\1\uffff\1\56\1\105\2\uffff"
        )

    DFA9_max = DFA.unpack(
        u"\1\71\1\uffff\2\145\2\uffff"
        )

    DFA9_accept = DFA.unpack(
        u"\1\uffff\1\1\2\uffff\1\3\1\2"
        )

    DFA9_special = DFA.unpack(
        u"\6\uffff"
        )

            
    DFA9_transition = [
        DFA.unpack(u"\1\1\1\uffff\12\2"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\3\1\uffff\12\2\13\uffff\1\4\37\uffff\1\4"),
        DFA.unpack(u"\1\5\37\uffff\1\5"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #9

    class DFA9(DFA):
        pass


    # lookup tables for DFA #16

    DFA16_eot = DFA.unpack(
        u"\7\uffff"
        )

    DFA16_eof = DFA.unpack(
        u"\7\uffff"
        )

    DFA16_min = DFA.unpack(
        u"\3\56\2\uffff\2\56"
        )

    DFA16_max = DFA.unpack(
        u"\1\71\1\170\1\152\2\uffff\2\152"
        )

    DFA16_accept = DFA.unpack(
        u"\3\uffff\1\2\1\1\2\uffff"
        )

    DFA16_special = DFA.unpack(
        u"\7\uffff"
        )

            
    DFA16_transition = [
        DFA.unpack(u"\1\3\1\uffff\1\1\11\2"),
        DFA.unpack(u"\1\3\1\uffff\12\5\13\uffff\1\3\4\uffff\1\4\15\uffff"
        u"\1\4\14\uffff\1\3\4\uffff\1\4\15\uffff\1\4"),
        DFA.unpack(u"\1\3\1\uffff\12\6\13\uffff\1\3\4\uffff\1\4\32\uffff"
        u"\1\3\4\uffff\1\4"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\3\1\uffff\12\5\13\uffff\1\3\4\uffff\1\4\32\uffff"
        u"\1\3\4\uffff\1\4"),
        DFA.unpack(u"\1\3\1\uffff\12\6\13\uffff\1\3\4\uffff\1\4\32\uffff"
        u"\1\3\4\uffff\1\4")
    ]

    # class definition for DFA #16

    class DFA16(DFA):
        pass


    # lookup tables for DFA #46

    DFA46_eot = DFA.unpack(
        u"\2\uffff\2\4\1\uffff"
        )

    DFA46_eof = DFA.unpack(
        u"\5\uffff"
        )

    DFA46_min = DFA.unpack(
        u"\1\11\1\uffff\2\0\1\uffff"
        )

    DFA46_max = DFA.unpack(
        u"\1\43\1\uffff\2\uffff\1\uffff"
        )

    DFA46_accept = DFA.unpack(
        u"\1\uffff\1\1\2\uffff\1\2"
        )

    DFA46_special = DFA.unpack(
        u"\1\2\1\uffff\1\1\1\0\1\uffff"
        )

            
    DFA46_transition = [
        DFA.unpack(u"\1\1\26\uffff\1\1\2\uffff\1\2"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\3\1\1\ufff5\3"),
        DFA.unpack(u"\12\3\1\1\ufff5\3"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #46

    class DFA46(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA46_3 = input.LA(1)

                 
                index46_3 = input.index()
                input.rewind()
                s = -1
                if (LA46_3 == 10) and ((self.startPosition == 0 )):
                    s = 1

                elif ((0 <= LA46_3 <= 9) or (11 <= LA46_3 <= 65535)) and (((self.startPosition > 0 ) or (self.startPosition == 0 ))):
                    s = 3

                else:
                    s = 4

                 
                input.seek(index46_3)
                if s >= 0:
                    return s
            elif s == 1: 
                LA46_2 = input.LA(1)

                 
                index46_2 = input.index()
                input.rewind()
                s = -1
                if ((0 <= LA46_2 <= 9) or (11 <= LA46_2 <= 65535)) and (((self.startPosition > 0 ) or (self.startPosition == 0 ))):
                    s = 3

                elif (LA46_2 == 10) and ((self.startPosition == 0 )):
                    s = 1

                else:
                    s = 4

                 
                input.seek(index46_2)
                if s >= 0:
                    return s
            elif s == 2: 
                LA46_0 = input.LA(1)

                 
                index46_0 = input.index()
                input.rewind()
                s = -1
                if (LA46_0 == 9 or LA46_0 == 32) and ((self.startPosition == 0 )):
                    s = 1

                elif (LA46_0 == 35) and (((self.startPosition > 0 ) or (self.startPosition == 0 ))):
                    s = 2

                 
                input.seek(index46_0)
                if s >= 0:
                    return s

            nvae = NoViableAltException(self_.getDescription(), 46, _s, input)
            self_.error(nvae)
            raise nvae
    # lookup tables for DFA #47

    DFA47_eot = DFA.unpack(
        u"\7\uffff\1\64\1\uffff\1\66\1\uffff\1\70\1\72\1\75\1\76\1\102\1"
        u"\104\1\106\1\112\1\115\1\117\1\121\1\uffff\1\123\2\uffff\17\54"
        u"\2\152\1\54\4\uffff\1\163\1\165\3\uffff\1\166\5\uffff\1\171\4\uffff"
        u"\1\173\10\uffff\1\175\2\uffff\1\177\7\uffff\4\54\1\u0084\5\54\1"
        u"\u008b\1\54\1\u008d\6\54\1\u0094\1\54\2\uffff\1\166\1\152\3\uffff"
        u"\1\152\1\54\16\uffff\3\54\1\u00a3\1\uffff\6\54\1\uffff\1\54\1\uffff"
        u"\6\54\1\uffff\1\u00b1\3\152\1\166\2\uffff\1\166\2\uffff\1\166\3"
        u"\54\1\uffff\1\u00b8\1\u00b9\1\54\1\u00bb\6\54\1\u00c2\1\u00c3\1"
        u"\54\3\uffff\1\166\3\54\2\uffff\1\54\1\uffff\3\54\1\u00ce\2\54\2"
        u"\uffff\1\u00d1\1\uffff\1\166\1\u00d2\2\54\1\u00d5\1\u00d6\1\u00d7"
        u"\1\u00d8\1\uffff\1\u00d9\1\u00da\2\uffff\1\54\7\uffff\1\54\1\u00dd"
        u"\1\uffff"
        )

    DFA47_eof = DFA.unpack(
        u"\u00de\uffff"
        )

    DFA47_min = DFA.unpack(
        u"\1\11\6\uffff\1\75\1\uffff\1\60\1\uffff\2\75\1\52\1\101\1\57\2"
        u"\75\1\74\3\75\1\uffff\1\75\2\uffff\1\154\1\147\1\42\1\150\1\170"
        u"\1\150\1\157\1\155\2\145\1\157\1\141\2\162\1\157\2\56\1\42\4\uffff"
        u"\2\11\3\uffff\1\60\5\uffff\1\75\4\uffff\1\75\10\uffff\1\75\2\uffff"
        u"\1\75\7\uffff\1\157\1\164\1\145\1\144\1\60\1\154\1\145\1\151\1"
        u"\145\1\144\1\60\1\160\1\60\1\141\1\154\1\162\1\157\1\154\1\151"
        u"\1\60\1\164\1\60\1\uffff\1\60\1\56\1\uffff\1\53\1\uffff\1\56\1"
        u"\42\1\uffff\1\0\1\uffff\1\0\1\uffff\1\53\10\uffff\1\142\1\162\1"
        u"\156\1\60\1\uffff\1\145\1\156\1\163\1\156\1\151\1\145\1\uffff\1"
        u"\157\1\uffff\1\162\1\145\1\147\1\155\1\164\1\156\1\uffff\5\60\1"
        u"\53\2\60\1\uffff\2\60\1\141\1\151\1\144\1\uffff\2\60\1\164\1\60"
        u"\1\146\2\162\1\156\1\164\1\145\2\60\1\164\1\uffff\1\53\2\60\1\154"
        u"\1\142\1\141\2\uffff\1\163\1\uffff\1\171\2\164\1\60\1\145\1\164"
        u"\2\uffff\4\60\1\165\1\55\4\60\1\uffff\2\60\2\uffff\1\164\7\uffff"
        u"\1\145\1\60\1\uffff"
        )

    DFA47_max = DFA.unpack(
        u"\1\176\6\uffff\1\75\1\uffff\1\71\1\uffff\3\75\1\172\3\75\2\76\2"
        u"\75\1\uffff\1\75\2\uffff\1\154\1\164\1\165\1\150\1\170\1\150\1"
        u"\157\1\163\2\145\1\162\1\141\2\162\1\157\1\170\1\154\1\162\4\uffff"
        u"\2\43\3\uffff\1\152\5\uffff\1\75\4\uffff\1\75\10\uffff\1\75\2\uffff"
        u"\1\75\7\uffff\1\157\1\164\1\145\1\144\1\172\1\154\1\145\1\151\1"
        u"\145\1\144\1\172\1\160\1\172\1\141\1\154\1\162\1\157\1\154\1\151"
        u"\1\172\1\164\1\146\1\uffff\1\152\1\154\1\uffff\1\71\1\uffff\1\154"
        u"\1\47\1\uffff\1\0\1\uffff\1\0\1\uffff\1\71\10\uffff\1\142\1\162"
        u"\1\156\1\172\1\uffff\1\145\1\156\1\163\1\156\1\151\1\145\1\uffff"
        u"\1\157\1\uffff\1\162\1\145\1\147\1\155\1\164\1\156\1\uffff\1\172"
        u"\3\154\1\152\2\71\1\152\1\uffff\1\71\1\152\1\141\1\151\1\144\1"
        u"\uffff\2\172\1\164\1\172\1\146\2\162\1\156\1\164\1\145\2\172\1"
        u"\164\1\uffff\2\71\1\152\1\154\1\142\1\141\2\uffff\1\163\1\uffff"
        u"\1\171\2\164\1\172\1\145\1\164\2\uffff\1\172\1\71\1\152\1\172\1"
        u"\165\1\55\4\172\1\uffff\2\172\2\uffff\1\164\7\uffff\1\145\1\172"
        u"\1\uffff"
        )

    DFA47_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\1\3\1\4\1\5\1\6\1\uffff\1\10\1\uffff\1\12\13\uffff"
        u"\1\26\1\uffff\1\30\1\33\22\uffff\1\111\1\113\1\114\1\115\2\uffff"
        u"\1\120\1\32\1\7\1\uffff\1\11\1\41\1\13\1\42\1\14\1\uffff\1\44\1"
        u"\15\1\16\1\112\1\uffff\1\46\1\17\1\47\1\20\1\51\1\21\1\34\1\35"
        u"\1\uffff\1\22\1\37\1\uffff\1\23\1\31\1\24\1\50\1\25\1\52\1\27\26"
        u"\uffff\1\107\2\uffff\1\106\1\uffff\1\110\2\uffff\1\120\1\uffff"
        u"\1\117\1\uffff\1\105\1\uffff\1\55\1\43\1\56\1\45\1\53\1\36\1\54"
        u"\1\40\4\uffff\1\103\6\uffff\1\101\1\uffff\1\102\6\uffff\1\100\10"
        u"\uffff\1\116\5\uffff\1\77\15\uffff\1\104\6\uffff\1\61\1\63\1\uffff"
        u"\1\65\6\uffff\1\76\1\73\12\uffff\1\70\2\uffff\1\74\1\57\1\uffff"
        u"\1\62\1\64\1\66\1\67\1\75\1\71\1\72\2\uffff\1\60"
        )

    DFA47_special = DFA.unpack(
        u"\1\2\57\uffff\1\0\1\1\101\uffff\1\3\1\uffff\1\4\150\uffff"
        )

            
    DFA47_transition = [
        DFA.unpack(u"\1\61\1\57\1\uffff\2\57\22\uffff\1\60\1\31\1\55\1\62"
        u"\1\16\1\25\1\21\1\55\1\1\1\2\1\15\1\13\1\10\1\14\1\11\1\17\1\51"
        u"\11\52\1\7\1\12\1\22\1\24\1\23\2\uffff\32\54\1\3\1\56\1\4\1\27"
        u"\1\54\1\26\1\33\2\54\1\43\1\36\1\44\1\32\1\45\1\41\2\54\1\42\1"
        u"\40\1\50\1\47\1\46\1\54\1\34\1\54\1\37\1\53\1\54\1\35\3\54\1\5"
        u"\1\20\1\6\1\30"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\63"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\65"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\67"),
        DFA.unpack(u"\1\71"),
        DFA.unpack(u"\1\73\22\uffff\1\74"),
        DFA.unpack(u"\32\77\4\uffff\1\77\1\uffff\32\77"),
        DFA.unpack(u"\1\100\15\uffff\1\101"),
        DFA.unpack(u"\1\103"),
        DFA.unpack(u"\1\105"),
        DFA.unpack(u"\1\111\1\110\1\107"),
        DFA.unpack(u"\1\113\1\114"),
        DFA.unpack(u"\1\116"),
        DFA.unpack(u"\1\120"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\122"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\124"),
        DFA.unpack(u"\1\126\6\uffff\1\127\4\uffff\1\130\1\125"),
        DFA.unpack(u"\1\55\4\uffff\1\55\115\uffff\1\131"),
        DFA.unpack(u"\1\132"),
        DFA.unpack(u"\1\133"),
        DFA.unpack(u"\1\134"),
        DFA.unpack(u"\1\135"),
        DFA.unpack(u"\1\137\1\136\4\uffff\1\140"),
        DFA.unpack(u"\1\141"),
        DFA.unpack(u"\1\142"),
        DFA.unpack(u"\1\143\2\uffff\1\144"),
        DFA.unpack(u"\1\145"),
        DFA.unpack(u"\1\146"),
        DFA.unpack(u"\1\147"),
        DFA.unpack(u"\1\150"),
        DFA.unpack(u"\1\153\1\uffff\12\154\13\uffff\1\156\4\uffff\1\157"
        u"\1\uffff\1\155\13\uffff\1\151\14\uffff\1\156\4\uffff\1\157\1\uffff"
        u"\1\155\13\uffff\1\151"),
        DFA.unpack(u"\1\153\1\uffff\12\160\13\uffff\1\156\4\uffff\1\157"
        u"\1\uffff\1\155\30\uffff\1\156\4\uffff\1\157\1\uffff\1\155"),
        DFA.unpack(u"\1\55\4\uffff\1\55\112\uffff\1\161"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\61\1\164\2\uffff\1\164\22\uffff\1\60\2\uffff\1\162"),
        DFA.unpack(u"\1\61\1\164\2\uffff\1\164\22\uffff\1\60\2\uffff\1\162"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\65\13\uffff\1\167\4\uffff\1\157\32\uffff\1\167"
        u"\4\uffff\1\157"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\170"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\172"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\174"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\176"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u0080"),
        DFA.unpack(u"\1\u0081"),
        DFA.unpack(u"\1\u0082"),
        DFA.unpack(u"\1\u0083"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\1\u0085"),
        DFA.unpack(u"\1\u0086"),
        DFA.unpack(u"\1\u0087"),
        DFA.unpack(u"\1\u0088"),
        DFA.unpack(u"\1\u0089"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\22\54\1\u008a"
        u"\7\54"),
        DFA.unpack(u"\1\u008c"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\1\u008e"),
        DFA.unpack(u"\1\u008f"),
        DFA.unpack(u"\1\u0090"),
        DFA.unpack(u"\1\u0091"),
        DFA.unpack(u"\1\u0092"),
        DFA.unpack(u"\1\u0093"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\1\u0095"),
        DFA.unpack(u"\12\u0096\7\uffff\6\u0098\32\uffff\6\u0097"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\u0099\13\uffff\1\u009a\4\uffff\1\157\32\uffff\1"
        u"\u009a\4\uffff\1\157"),
        DFA.unpack(u"\1\153\1\uffff\12\154\13\uffff\1\156\4\uffff\1\157"
        u"\1\uffff\1\155\30\uffff\1\156\4\uffff\1\157\1\uffff\1\155"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u009b\1\uffff\1\u009b\2\uffff\12\u009c"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\153\1\uffff\12\160\13\uffff\1\156\4\uffff\1\157"
        u"\1\uffff\1\155\30\uffff\1\156\4\uffff\1\157\1\uffff\1\155"),
        DFA.unpack(u"\1\55\4\uffff\1\55"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\uffff"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u009e\1\uffff\1\u009e\2\uffff\12\u009f"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00a0"),
        DFA.unpack(u"\1\u00a1"),
        DFA.unpack(u"\1\u00a2"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00a4"),
        DFA.unpack(u"\1\u00a5"),
        DFA.unpack(u"\1\u00a6"),
        DFA.unpack(u"\1\u00a7"),
        DFA.unpack(u"\1\u00a8"),
        DFA.unpack(u"\1\u00a9"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00aa"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00ab"),
        DFA.unpack(u"\1\u00ac"),
        DFA.unpack(u"\1\u00ad"),
        DFA.unpack(u"\1\u00ae"),
        DFA.unpack(u"\1\u00af"),
        DFA.unpack(u"\1\u00b0"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\12\u0096\7\uffff\6\u0098\3\uffff\1\157\1\uffff\1\155"
        u"\24\uffff\6\u0097\3\uffff\1\157\1\uffff\1\155"),
        DFA.unpack(u"\12\u0096\7\uffff\6\u0098\3\uffff\1\157\1\uffff\1\155"
        u"\24\uffff\6\u0097\3\uffff\1\157\1\uffff\1\155"),
        DFA.unpack(u"\12\u0096\7\uffff\6\u0098\3\uffff\1\157\1\uffff\1\155"
        u"\24\uffff\6\u0097\3\uffff\1\157\1\uffff\1\155"),
        DFA.unpack(u"\12\u0099\13\uffff\1\u00b2\4\uffff\1\157\32\uffff\1"
        u"\u00b2\4\uffff\1\157"),
        DFA.unpack(u"\1\u00b3\1\uffff\1\u00b3\2\uffff\12\u00b4"),
        DFA.unpack(u"\12\u009c"),
        DFA.unpack(u"\12\u009c\20\uffff\1\157\37\uffff\1\157"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\u009f"),
        DFA.unpack(u"\12\u009f\20\uffff\1\157\37\uffff\1\157"),
        DFA.unpack(u"\1\u00b5"),
        DFA.unpack(u"\1\u00b6"),
        DFA.unpack(u"\1\u00b7"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\1\u00ba"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\1\u00bc"),
        DFA.unpack(u"\1\u00bd"),
        DFA.unpack(u"\1\u00be"),
        DFA.unpack(u"\1\u00bf"),
        DFA.unpack(u"\1\u00c0"),
        DFA.unpack(u"\1\u00c1"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\1\u00c4"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00c5\1\uffff\1\u00c5\2\uffff\12\u00c6"),
        DFA.unpack(u"\12\u00b4"),
        DFA.unpack(u"\12\u00b4\20\uffff\1\157\37\uffff\1\157"),
        DFA.unpack(u"\1\u00c7"),
        DFA.unpack(u"\1\u00c8"),
        DFA.unpack(u"\1\u00c9"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00ca"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00cb"),
        DFA.unpack(u"\1\u00cc"),
        DFA.unpack(u"\1\u00cd"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\1\u00cf"),
        DFA.unpack(u"\1\u00d0"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\12\u00c6"),
        DFA.unpack(u"\12\u00c6\20\uffff\1\157\37\uffff\1\157"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\1\u00d3"),
        DFA.unpack(u"\1\u00d4"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00db"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\u00dc"),
        DFA.unpack(u"\12\54\7\uffff\32\54\4\uffff\1\54\1\uffff\32\54"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #47

    class DFA47(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA47_48 = input.LA(1)

                 
                index47_48 = input.index()
                input.rewind()
                s = -1
                if (LA47_48 == 35) and ((self.startPosition == 0 )):
                    s = 114

                elif (LA47_48 == 32) and (((self.startPosition > 0 ) or (self.startPosition == 0 ))):
                    s = 48

                elif (LA47_48 == 10 or LA47_48 == 13) and ((self.startPosition == 0 )):
                    s = 116

                elif (LA47_48 == 9) and (((self.startPosition > 0 ) or (self.startPosition == 0 ))):
                    s = 49

                else:
                    s = 115

                 
                input.seek(index47_48)
                if s >= 0:
                    return s
            elif s == 1: 
                LA47_49 = input.LA(1)

                 
                index47_49 = input.index()
                input.rewind()
                s = -1
                if (LA47_49 == 35) and ((self.startPosition == 0 )):
                    s = 114

                elif (LA47_49 == 32) and (((self.startPosition > 0 ) or (self.startPosition == 0 ))):
                    s = 48

                elif (LA47_49 == 10 or LA47_49 == 13) and ((self.startPosition == 0 )):
                    s = 116

                elif (LA47_49 == 9) and (((self.startPosition > 0 ) or (self.startPosition == 0 ))):
                    s = 49

                else:
                    s = 117

                 
                input.seek(index47_49)
                if s >= 0:
                    return s
            elif s == 2: 
                LA47_0 = input.LA(1)

                 
                index47_0 = input.index()
                input.rewind()
                s = -1
                if (LA47_0 == 40):
                    s = 1

                elif (LA47_0 == 41):
                    s = 2

                elif (LA47_0 == 91):
                    s = 3

                elif (LA47_0 == 93):
                    s = 4

                elif (LA47_0 == 123):
                    s = 5

                elif (LA47_0 == 125):
                    s = 6

                elif (LA47_0 == 58):
                    s = 7

                elif (LA47_0 == 44):
                    s = 8

                elif (LA47_0 == 46):
                    s = 9

                elif (LA47_0 == 59):
                    s = 10

                elif (LA47_0 == 43):
                    s = 11

                elif (LA47_0 == 45):
                    s = 12

                elif (LA47_0 == 42):
                    s = 13

                elif (LA47_0 == 36):
                    s = 14

                elif (LA47_0 == 47):
                    s = 15

                elif (LA47_0 == 124):
                    s = 16

                elif (LA47_0 == 38):
                    s = 17

                elif (LA47_0 == 60):
                    s = 18

                elif (LA47_0 == 62):
                    s = 19

                elif (LA47_0 == 61):
                    s = 20

                elif (LA47_0 == 37):
                    s = 21

                elif (LA47_0 == 96):
                    s = 22

                elif (LA47_0 == 94):
                    s = 23

                elif (LA47_0 == 126):
                    s = 24

                elif (LA47_0 == 33):
                    s = 25

                elif (LA47_0 == 103):
                    s = 26

                elif (LA47_0 == 97):
                    s = 27

                elif (LA47_0 == 114):
                    s = 28

                elif (LA47_0 == 119):
                    s = 29

                elif (LA47_0 == 101):
                    s = 30

                elif (LA47_0 == 116):
                    s = 31

                elif (LA47_0 == 109):
                    s = 32

                elif (LA47_0 == 105):
                    s = 33

                elif (LA47_0 == 108):
                    s = 34

                elif (LA47_0 == 100):
                    s = 35

                elif (LA47_0 == 102):
                    s = 36

                elif (LA47_0 == 104):
                    s = 37

                elif (LA47_0 == 112):
                    s = 38

                elif (LA47_0 == 111):
                    s = 39

                elif (LA47_0 == 110):
                    s = 40

                elif (LA47_0 == 48):
                    s = 41

                elif ((49 <= LA47_0 <= 57)):
                    s = 42

                elif (LA47_0 == 117):
                    s = 43

                elif ((65 <= LA47_0 <= 90) or LA47_0 == 95 or (98 <= LA47_0 <= 99) or (106 <= LA47_0 <= 107) or LA47_0 == 113 or LA47_0 == 115 or LA47_0 == 118 or (120 <= LA47_0 <= 122)):
                    s = 44

                elif (LA47_0 == 34 or LA47_0 == 39):
                    s = 45

                elif (LA47_0 == 92):
                    s = 46

                elif (LA47_0 == 10 or (12 <= LA47_0 <= 13)):
                    s = 47

                elif (LA47_0 == 32) and (((self.startPosition > 0 ) or (self.startPosition == 0 ))):
                    s = 48

                elif (LA47_0 == 9) and (((self.startPosition > 0 ) or (self.startPosition == 0 ))):
                    s = 49

                elif (LA47_0 == 35) and (((self.startPosition > 0 ) or (self.startPosition == 0 ))):
                    s = 50

                 
                input.seek(index47_0)
                if s >= 0:
                    return s
            elif s == 3: 
                LA47_115 = input.LA(1)

                 
                index47_115 = input.index()
                input.rewind()
                s = -1
                if ((self.startPosition > 0 )):
                    s = 157

                elif (((((self.startPosition == 0 )) and ((self.implicitLineJoiningLevel > 0))) or (self.startPosition == 0 ))):
                    s = 116

                 
                input.seek(index47_115)
                if s >= 0:
                    return s
            elif s == 4: 
                LA47_117 = input.LA(1)

                 
                index47_117 = input.index()
                input.rewind()
                s = -1
                if ((self.startPosition > 0 )):
                    s = 157

                elif (((((self.startPosition == 0 )) and ((self.implicitLineJoiningLevel > 0))) or (self.startPosition == 0 ))):
                    s = 116

                 
                input.seek(index47_117)
                if s >= 0:
                    return s

            nvae = NoViableAltException(self_.getDescription(), 47, _s, input)
            self_.error(nvae)
            raise nvae
 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(PolicyLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
