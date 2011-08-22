# $ANTLR 3.1.3 Mar 17, 2009 19:23:44 /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g 2011-08-22 16:34:20

import sys
from antlr3 import *
from antlr3.compat import set, frozenset
         
from intellect.Node import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
SLASHEQUAL=33
BACKQUOTE=78
EXPONENT=84
STAR=62
CIRCUMFLEXEQUAL=37
LETTER=82
TRIAPOS=85
GREATEREQUAL=52
COMPLEX=75
NOT=14
ASSIGNEQUAL=17
EOF=-1
NOTEQUAL=55
LEADING_WS=90
MINUSEQUAL=31
VBAR=56
RPAREN=19
IMPORT=42
NAME=9
GREATER=50
INSERT=26
DOUBLESTAREQUAL=40
LESS=49
COMMENT=91
RBRACK=69
RULE=7
LCURLY=70
INT=72
DELETE=24
RIGHTSHIFT=22
DOUBLESLASHEQUAL=41
WS=89
VBAREQUAL=36
OR=47
LONGINT=73
FORGET=23
FROM=43
PERCENTEQUAL=34
LESSEQUAL=53
DOLLAR=77
MODIFY=27
DOUBLESLASH=65
LBRACK=68
CONTINUED_LINE=88
OBJECTBINDING=16
DOUBLESTAR=67
HALT=28
ESC=87
ATTRIBUTE=20
DEDENT=5
FLOAT=74
RIGHTSHIFTEQUAL=39
AND=48
LEARN=25
INDENT=4
LPAREN=18
PLUSEQUAL=30
AS=45
SLASH=63
THEN=13
IN=80
COMMA=44
IS=81
AMPER=58
EQUAL=51
TILDE=66
LEFTSHIFTEQUAL=38
LEFTSHIFT=59
PLUS=60
EXISTS=15
DIGIT=83
DOT=46
AGENDAGROUP=11
PERCENT=64
MINUS=61
SEMI=76
PRINT=21
COLON=8
TRIQUOTE=86
AMPEREQUAL=35
NEWLINE=6
WHEN=12
RCURLY=71
ASSIGN=29
GLOBAL=79
STAREQUAL=32
CIRCUMFLEX=57
STRING=10
ALT_NOTEQUAL=54

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "INDENT", "DEDENT", "NEWLINE", "RULE", "COLON", "NAME", "STRING", "AGENDAGROUP", 
    "WHEN", "THEN", "NOT", "EXISTS", "OBJECTBINDING", "ASSIGNEQUAL", "LPAREN", 
    "RPAREN", "ATTRIBUTE", "PRINT", "RIGHTSHIFT", "FORGET", "DELETE", "LEARN", 
    "INSERT", "MODIFY", "HALT", "ASSIGN", "PLUSEQUAL", "MINUSEQUAL", "STAREQUAL", 
    "SLASHEQUAL", "PERCENTEQUAL", "AMPEREQUAL", "VBAREQUAL", "CIRCUMFLEXEQUAL", 
    "LEFTSHIFTEQUAL", "RIGHTSHIFTEQUAL", "DOUBLESTAREQUAL", "DOUBLESLASHEQUAL", 
    "IMPORT", "FROM", "COMMA", "AS", "DOT", "OR", "AND", "LESS", "GREATER", 
    "EQUAL", "GREATEREQUAL", "LESSEQUAL", "ALT_NOTEQUAL", "NOTEQUAL", "VBAR", 
    "CIRCUMFLEX", "AMPER", "LEFTSHIFT", "PLUS", "MINUS", "STAR", "SLASH", 
    "PERCENT", "DOUBLESLASH", "TILDE", "DOUBLESTAR", "LBRACK", "RBRACK", 
    "LCURLY", "RCURLY", "INT", "LONGINT", "FLOAT", "COMPLEX", "SEMI", "DOLLAR", 
    "BACKQUOTE", "GLOBAL", "IN", "IS", "LETTER", "DIGIT", "EXPONENT", "TRIAPOS", 
    "TRIQUOTE", "ESC", "CONTINUED_LINE", "WS", "LEADING_WS", "COMMENT"
]




class PolicyParser(Parser):
    grammarFileName = "/Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 17, 2009 19:23:44")
    antlr_version_str = "3.1.3 Mar 17, 2009 19:23:44"
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(PolicyParser, self).__init__(input, state, *args, **kwargs)

        self.dfa34 = self.DFA34(
            self, 34,
            eot = self.DFA34_eot,
            eof = self.DFA34_eof,
            min = self.DFA34_min,
            max = self.DFA34_max,
            accept = self.DFA34_accept,
            special = self.DFA34_special,
            transition = self.DFA34_transition
            )

        self.dfa54 = self.DFA54(
            self, 54,
            eot = self.DFA54_eot,
            eof = self.DFA54_eof,
            min = self.DFA54_min,
            max = self.DFA54_max,
            accept = self.DFA54_accept,
            special = self.DFA54_special,
            transition = self.DFA54_transition
            )

        self.dfa58 = self.DFA58(
            self, 58,
            eot = self.DFA58_eot,
            eof = self.DFA58_eof,
            min = self.DFA58_min,
            max = self.DFA58_max,
            accept = self.DFA58_accept,
            special = self.DFA58_special,
            transition = self.DFA58_transition
            )

        self.dfa60 = self.DFA60(
            self, 60,
            eot = self.DFA60_eot,
            eof = self.DFA60_eof,
            min = self.DFA60_min,
            max = self.DFA60_max,
            accept = self.DFA60_accept,
            special = self.DFA60_special,
            transition = self.DFA60_transition
            )






                


        



    # $ANTLR start "file"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:61:1: file returns [object] : ( ( NEWLINE | statement )+ | EOF );
    def file(self, ):

        object = None

        statement1 = None


        object = File() 
        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:63:3: ( ( NEWLINE | statement )+ | EOF )
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if ((NEWLINE <= LA2_0 <= RULE) or (NAME <= LA2_0 <= STRING) or LA2_0 == NOT or LA2_0 == OBJECTBINDING or LA2_0 == LPAREN or (IMPORT <= LA2_0 <= FROM) or (PLUS <= LA2_0 <= MINUS) or LA2_0 == TILDE or LA2_0 == LBRACK or LA2_0 == LCURLY or (INT <= LA2_0 <= COMPLEX)) :
                    alt2 = 1
                elif (LA2_0 == EOF) :
                    alt2 = 2
                else:
                    nvae = NoViableAltException("", 2, 0, self.input)

                    raise nvae

                if alt2 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:63:5: ( NEWLINE | statement )+
                    pass 
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:63:5: ( NEWLINE | statement )+
                    cnt1 = 0
                    while True: #loop1
                        alt1 = 3
                        LA1_0 = self.input.LA(1)

                        if (LA1_0 == NEWLINE) :
                            alt1 = 1
                        elif (LA1_0 == RULE or (NAME <= LA1_0 <= STRING) or LA1_0 == NOT or LA1_0 == OBJECTBINDING or LA1_0 == LPAREN or (IMPORT <= LA1_0 <= FROM) or (PLUS <= LA1_0 <= MINUS) or LA1_0 == TILDE or LA1_0 == LBRACK or LA1_0 == LCURLY or (INT <= LA1_0 <= COMPLEX)) :
                            alt1 = 2


                        if alt1 == 1:
                            # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:63:7: NEWLINE
                            pass 
                            self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_file78)


                        elif alt1 == 2:
                            # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:63:17: statement
                            pass 
                            self._state.following.append(self.FOLLOW_statement_in_file82)
                            statement1 = self.statement()

                            self._state.following.pop()
                            #action start
                            object.append_child( statement1 ) 
                            #action end


                        else:
                            if cnt1 >= 1:
                                break #loop1

                            eee = EarlyExitException(1, self.input)
                            raise eee

                        cnt1 += 1


                elif alt2 == 2:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:64:5: EOF
                    pass 
                    self.match(self.input, EOF, self.FOLLOW_EOF_in_file93)



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "file"


    # $ANTLR start "statement"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:67:1: statement returns [object] : ( importStmt | attributeStmt | ruleStmt );
    def statement(self, ):

        object = None

        importStmt2 = None

        attributeStmt3 = None

        ruleStmt4 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:68:3: ( importStmt | attributeStmt | ruleStmt )
                alt3 = 3
                LA3 = self.input.LA(1)
                if LA3 == IMPORT or LA3 == FROM:
                    alt3 = 1
                elif LA3 == NAME or LA3 == STRING or LA3 == NOT or LA3 == OBJECTBINDING or LA3 == LPAREN or LA3 == PLUS or LA3 == MINUS or LA3 == TILDE or LA3 == LBRACK or LA3 == LCURLY or LA3 == INT or LA3 == LONGINT or LA3 == FLOAT or LA3 == COMPLEX:
                    alt3 = 2
                elif LA3 == RULE:
                    alt3 = 3
                else:
                    nvae = NoViableAltException("", 3, 0, self.input)

                    raise nvae

                if alt3 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:68:5: importStmt
                    pass 
                    self._state.following.append(self.FOLLOW_importStmt_in_statement111)
                    importStmt2 = self.importStmt()

                    self._state.following.pop()
                    #action start
                    object = Statement( importStmt2, importStmt2.line, importStmt2.column ) 
                    #action end


                elif alt3 == 2:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:69:5: attributeStmt
                    pass 
                    self._state.following.append(self.FOLLOW_attributeStmt_in_statement120)
                    attributeStmt3 = self.attributeStmt()

                    self._state.following.pop()
                    #action start
                    object = Statement( attributeStmt3 ) 
                    #action end


                elif alt3 == 3:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:70:5: ruleStmt
                    pass 
                    self._state.following.append(self.FOLLOW_ruleStmt_in_statement129)
                    ruleStmt4 = self.ruleStmt()

                    self._state.following.pop()
                    #action start
                    object = Statement( ruleStmt4, ruleStmt4.line, ruleStmt4.column ) 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "statement"


    # $ANTLR start "attributeStmt"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:73:1: attributeStmt returns [object] : expressionStmt ;
    def attributeStmt(self, ):

        object = None

        expressionStmt5 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:74:3: ( expressionStmt )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:74:5: expressionStmt
                pass 
                self._state.following.append(self.FOLLOW_expressionStmt_in_attributeStmt152)
                expressionStmt5 = self.expressionStmt()

                self._state.following.pop()
                #action start
                object = AttributeStmt( expressionStmt5 ) 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "attributeStmt"


    # $ANTLR start "ruleStmt"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:77:1: ruleStmt returns [object] : RULE id COLON NEWLINE INDENT ( ruleAttribute )* ( when )? then DEDENT ;
    def ruleStmt(self, ):

        object = None

        RULE6 = None
        COLON8 = None
        id7 = None

        ruleAttribute9 = None

        when10 = None

        then11 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:78:3: ( RULE id COLON NEWLINE INDENT ( ruleAttribute )* ( when )? then DEDENT )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:78:5: RULE id COLON NEWLINE INDENT ( ruleAttribute )* ( when )? then DEDENT
                pass 
                RULE6=self.match(self.input, RULE, self.FOLLOW_RULE_in_ruleStmt172)
                self._state.following.append(self.FOLLOW_id_in_ruleStmt174)
                id7 = self.id()

                self._state.following.pop()
                COLON8=self.match(self.input, COLON, self.FOLLOW_COLON_in_ruleStmt176)
                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_ruleStmt178)
                #action start
                object = RuleStmt( [ RULE6.text, id7, COLON8.text ], RULE6.getLine(), RULE6.getCharPositionInLine() ) 
                #action end
                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_ruleStmt188)
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:79:14: ( ruleAttribute )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == AGENDAGROUP) :
                        alt4 = 1


                    if alt4 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:79:16: ruleAttribute
                        pass 
                        self._state.following.append(self.FOLLOW_ruleAttribute_in_ruleStmt192)
                        ruleAttribute9 = self.ruleAttribute()

                        self._state.following.pop()
                        #action start
                        object.append_child( ruleAttribute9 ) 
                        #action end


                    else:
                        break #loop4
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:80:14: ( when )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == WHEN) :
                    alt5 = 1
                if alt5 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:80:16: when
                    pass 
                    self._state.following.append(self.FOLLOW_when_in_ruleStmt214)
                    when10 = self.when()

                    self._state.following.pop()
                    #action start
                    object.append_child( when10 ) 
                    #action end



                self._state.following.append(self.FOLLOW_then_in_ruleStmt234)
                then11 = self.then()

                self._state.following.pop()
                #action start
                object.append_child( then11 ) 
                #action end
                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_ruleStmt239)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "ruleStmt"


    # $ANTLR start "id"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:84:1: id returns [object] : ( NAME | STRING );
    def id(self, ):

        object = None

        NAME12 = None
        STRING13 = None

        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:85:3: ( NAME | STRING )
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if (LA6_0 == NAME) :
                    alt6 = 1
                elif (LA6_0 == STRING) :
                    alt6 = 2
                else:
                    nvae = NoViableAltException("", 6, 0, self.input)

                    raise nvae

                if alt6 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:85:5: NAME
                    pass 
                    NAME12=self.match(self.input, NAME, self.FOLLOW_NAME_in_id257)
                    #action start
                    object = Id( NAME12.text ) 
                    #action end


                elif alt6 == 2:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:86:5: STRING
                    pass 
                    STRING13=self.match(self.input, STRING, self.FOLLOW_STRING_in_id268)
                    #action start
                    object = Id( STRING13.text ) 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "id"


    # $ANTLR start "ruleAttribute"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:89:1: ruleAttribute returns [object] : agendaGroup ;
    def ruleAttribute(self, ):

        object = None

        agendaGroup14 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:90:3: ( agendaGroup )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:90:5: agendaGroup
                pass 
                self._state.following.append(self.FOLLOW_agendaGroup_in_ruleAttribute289)
                agendaGroup14 = self.agendaGroup()

                self._state.following.pop()
                #action start
                object = RuleAttribute( agendaGroup14, agendaGroup14.line, agendaGroup14.column ) 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "ruleAttribute"


    # $ANTLR start "agendaGroup"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:93:1: agendaGroup returns [object] : AGENDAGROUP id NEWLINE ;
    def agendaGroup(self, ):

        object = None

        AGENDAGROUP15 = None
        id16 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:94:3: ( AGENDAGROUP id NEWLINE )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:94:5: AGENDAGROUP id NEWLINE
                pass 
                AGENDAGROUP15=self.match(self.input, AGENDAGROUP, self.FOLLOW_AGENDAGROUP_in_agendaGroup309)
                self._state.following.append(self.FOLLOW_id_in_agendaGroup311)
                id16 = self.id()

                self._state.following.pop()
                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_agendaGroup313)
                #action start
                object = AgendaGroup( [ AGENDAGROUP15.text, id16 ], AGENDAGROUP15.getLine(), AGENDAGROUP15.getCharPositionInLine() ) 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "agendaGroup"


    # $ANTLR start "when"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:97:1: when returns [object] : WHEN COLON NEWLINE INDENT ( ruleCondition )? DEDENT ;
    def when(self, ):

        object = None

        WHEN17 = None
        COLON18 = None
        ruleCondition19 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:98:3: ( WHEN COLON NEWLINE INDENT ( ruleCondition )? DEDENT )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:98:5: WHEN COLON NEWLINE INDENT ( ruleCondition )? DEDENT
                pass 
                WHEN17=self.match(self.input, WHEN, self.FOLLOW_WHEN_in_when333)
                COLON18=self.match(self.input, COLON, self.FOLLOW_COLON_in_when335)
                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_when337)
                #action start
                object = When( [WHEN17.text, COLON18.text], WHEN17.getLine(), WHEN17.getCharPositionInLine() ) 
                #action end
                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_when347)
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:99:14: ( ruleCondition )?
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == NAME or (NOT <= LA7_0 <= OBJECTBINDING)) :
                    alt7 = 1
                if alt7 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:99:16: ruleCondition
                    pass 
                    self._state.following.append(self.FOLLOW_ruleCondition_in_when351)
                    ruleCondition19 = self.ruleCondition()

                    self._state.following.pop()
                    #action start
                    object.append_child( ruleCondition19 ) 
                    #action end



                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_when358)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "when"


    # $ANTLR start "then"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:102:1: then returns [object] : THEN COLON NEWLINE INDENT ( action )+ DEDENT ;
    def then(self, ):

        object = None

        THEN20 = None
        COLON21 = None
        action22 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:103:3: ( THEN COLON NEWLINE INDENT ( action )+ DEDENT )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:103:5: THEN COLON NEWLINE INDENT ( action )+ DEDENT
                pass 
                THEN20=self.match(self.input, THEN, self.FOLLOW_THEN_in_then376)
                COLON21=self.match(self.input, COLON, self.FOLLOW_COLON_in_then378)
                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_then380)
                #action start
                object = Then( [THEN20.text, COLON21.text], THEN20.getLine(), THEN20.getCharPositionInLine() ) 
                #action end
                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_then390)
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:104:14: ( action )+
                cnt8 = 0
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if ((NAME <= LA8_0 <= STRING) or LA8_0 == NOT or LA8_0 == OBJECTBINDING or LA8_0 == LPAREN or (ATTRIBUTE <= LA8_0 <= PRINT) or (FORGET <= LA8_0 <= HALT) or (PLUS <= LA8_0 <= MINUS) or LA8_0 == TILDE or LA8_0 == LBRACK or LA8_0 == LCURLY or (INT <= LA8_0 <= COMPLEX)) :
                        alt8 = 1


                    if alt8 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:104:16: action
                        pass 
                        self._state.following.append(self.FOLLOW_action_in_then394)
                        action22 = self.action()

                        self._state.following.pop()
                        #action start
                        object.append_child( action22 ) 
                        #action end


                    else:
                        if cnt8 >= 1:
                            break #loop8

                        eee = EarlyExitException(8, self.input)
                        raise eee

                    cnt8 += 1
                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_then401)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "then"


    # $ANTLR start "ruleCondition"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:107:1: ruleCondition returns [object] : notCondition NEWLINE ;
    def ruleCondition(self, ):

        object = None

        notCondition23 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:108:3: ( notCondition NEWLINE )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:108:5: notCondition NEWLINE
                pass 
                self._state.following.append(self.FOLLOW_notCondition_in_ruleCondition419)
                notCondition23 = self.notCondition()

                self._state.following.pop()
                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_ruleCondition421)
                #action start
                object = RuleCondition(notCondition23) 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "ruleCondition"


    # $ANTLR start "notCondition"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:111:1: notCondition returns [object] : ( NOT )* condition ;
    def notCondition(self, ):

        object = None

        NOT24 = None
        condition25 = None


        object = NotCondition() 
        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:113:3: ( ( NOT )* condition )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:113:5: ( NOT )* condition
                pass 
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:113:5: ( NOT )*
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == NOT) :
                        alt9 = 1


                    if alt9 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:113:7: NOT
                        pass 
                        NOT24=self.match(self.input, NOT, self.FOLLOW_NOT_in_notCondition449)
                        #action start
                        object.append_child( NOT24.text ) 
                        #action end


                    else:
                        break #loop9
                self._state.following.append(self.FOLLOW_condition_in_notCondition456)
                condition25 = self.condition()

                self._state.following.pop()
                #action start
                object.append_child( condition25 ) 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "notCondition"


    # $ANTLR start "condition"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:116:1: condition returns [object] : ( EXISTS )? classConstraint ;
    def condition(self, ):

        object = None

        EXISTS26 = None
        classConstraint27 = None


        object = Condition() 
        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:118:3: ( ( EXISTS )? classConstraint )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:118:5: ( EXISTS )? classConstraint
                pass 
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:118:5: ( EXISTS )?
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == EXISTS) :
                    alt10 = 1
                if alt10 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:118:7: EXISTS
                    pass 
                    EXISTS26=self.match(self.input, EXISTS, self.FOLLOW_EXISTS_in_condition484)
                    #action start
                    object.append_child( EXISTS26.text ) 
                    #action end



                self._state.following.append(self.FOLLOW_classConstraint_in_condition491)
                classConstraint27 = self.classConstraint()

                self._state.following.pop()
                #action start
                object.append_child( classConstraint27 ) 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "condition"


    # $ANTLR start "classConstraint"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:121:1: classConstraint returns [object] : ( OBJECTBINDING ASSIGNEQUAL )? NAME LPAREN ( constraint )? RPAREN ;
    def classConstraint(self, ):

        object = None

        OBJECTBINDING28 = None
        ASSIGNEQUAL29 = None
        NAME30 = None
        LPAREN31 = None
        RPAREN33 = None
        constraint32 = None


        object = ClassConstraint() 
        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:123:3: ( ( OBJECTBINDING ASSIGNEQUAL )? NAME LPAREN ( constraint )? RPAREN )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:123:5: ( OBJECTBINDING ASSIGNEQUAL )? NAME LPAREN ( constraint )? RPAREN
                pass 
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:123:5: ( OBJECTBINDING ASSIGNEQUAL )?
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if (LA11_0 == OBJECTBINDING) :
                    alt11 = 1
                if alt11 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:123:7: OBJECTBINDING ASSIGNEQUAL
                    pass 
                    OBJECTBINDING28=self.match(self.input, OBJECTBINDING, self.FOLLOW_OBJECTBINDING_in_classConstraint519)
                    ASSIGNEQUAL29=self.match(self.input, ASSIGNEQUAL, self.FOLLOW_ASSIGNEQUAL_in_classConstraint521)
                    #action start
                    object.append_children( [ OBJECTBINDING28.text, ASSIGNEQUAL29.text] ) 
                    #action end



                NAME30=self.match(self.input, NAME, self.FOLLOW_NAME_in_classConstraint534)
                LPAREN31=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_classConstraint536)
                #action start
                object.append_children( [NAME30.text, LPAREN31.text] ); object.line = NAME30.getLine() 
                #action end
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:124:109: ( constraint )?
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if ((NAME <= LA12_0 <= STRING) or LA12_0 == NOT or LA12_0 == OBJECTBINDING or LA12_0 == LPAREN or (PLUS <= LA12_0 <= MINUS) or LA12_0 == TILDE or LA12_0 == LBRACK or LA12_0 == LCURLY or (INT <= LA12_0 <= COMPLEX)) :
                    alt12 = 1
                if alt12 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:124:111: constraint
                    pass 
                    self._state.following.append(self.FOLLOW_constraint_in_classConstraint542)
                    constraint32 = self.constraint()

                    self._state.following.pop()
                    #action start
                    object.append_child( constraint32 ) 
                    #action end



                RPAREN33=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_classConstraint549)
                #action start
                object.append_child( RPAREN33.text ) 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "classConstraint"


    # $ANTLR start "action"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:127:1: action returns [object] : ( simpleStmt | attributeAction | learnAction | forgetAction | modifyAction | haltAction );
    def action(self, ):

        object = None

        simpleStmt34 = None

        attributeAction35 = None

        learnAction36 = None

        forgetAction37 = None

        modifyAction38 = None

        haltAction39 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:128:3: ( simpleStmt | attributeAction | learnAction | forgetAction | modifyAction | haltAction )
                alt13 = 6
                LA13 = self.input.LA(1)
                if LA13 == NAME or LA13 == STRING or LA13 == NOT or LA13 == OBJECTBINDING or LA13 == LPAREN or LA13 == PRINT or LA13 == PLUS or LA13 == MINUS or LA13 == TILDE or LA13 == LBRACK or LA13 == LCURLY or LA13 == INT or LA13 == LONGINT or LA13 == FLOAT or LA13 == COMPLEX:
                    alt13 = 1
                elif LA13 == ATTRIBUTE:
                    alt13 = 2
                elif LA13 == LEARN or LA13 == INSERT:
                    alt13 = 3
                elif LA13 == FORGET or LA13 == DELETE:
                    alt13 = 4
                elif LA13 == MODIFY:
                    alt13 = 5
                elif LA13 == HALT:
                    alt13 = 6
                else:
                    nvae = NoViableAltException("", 13, 0, self.input)

                    raise nvae

                if alt13 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:128:5: simpleStmt
                    pass 
                    self._state.following.append(self.FOLLOW_simpleStmt_in_action569)
                    simpleStmt34 = self.simpleStmt()

                    self._state.following.pop()
                    #action start
                    object = Action( simpleStmt34, simpleStmt34.line, simpleStmt34.column ) 
                    #action end


                elif alt13 == 2:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:129:5: attributeAction
                    pass 
                    self._state.following.append(self.FOLLOW_attributeAction_in_action583)
                    attributeAction35 = self.attributeAction()

                    self._state.following.pop()
                    #action start
                    object = Action( attributeAction35, attributeAction35.line, attributeAction35.column ) 
                    #action end


                elif alt13 == 3:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:130:5: learnAction
                    pass 
                    self._state.following.append(self.FOLLOW_learnAction_in_action592)
                    learnAction36 = self.learnAction()

                    self._state.following.pop()
                    #action start
                    object = Action( learnAction36, learnAction36.line, learnAction36.column ) 
                    #action end


                elif alt13 == 4:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:131:5: forgetAction
                    pass 
                    self._state.following.append(self.FOLLOW_forgetAction_in_action604)
                    forgetAction37 = self.forgetAction()

                    self._state.following.pop()
                    #action start
                    object = Action( forgetAction37, forgetAction37.line, forgetAction37.column ) 
                    #action end


                elif alt13 == 5:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:132:5: modifyAction
                    pass 
                    self._state.following.append(self.FOLLOW_modifyAction_in_action616)
                    modifyAction38 = self.modifyAction()

                    self._state.following.pop()
                    #action start
                    object = Action( modifyAction38, modifyAction38.line, modifyAction38.column ) 
                    #action end


                elif alt13 == 6:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:133:5: haltAction
                    pass 
                    self._state.following.append(self.FOLLOW_haltAction_in_action628)
                    haltAction39 = self.haltAction()

                    self._state.following.pop()
                    #action start
                    object = Action( haltAction39, haltAction39.line, haltAction39.column ) 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "action"


    # $ANTLR start "simpleStmt"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:136:1: simpleStmt returns [object] : ( expressionStmt | printStmt );
    def simpleStmt(self, ):

        object = None

        expressionStmt40 = None

        printStmt41 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:137:3: ( expressionStmt | printStmt )
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if ((NAME <= LA14_0 <= STRING) or LA14_0 == NOT or LA14_0 == OBJECTBINDING or LA14_0 == LPAREN or (PLUS <= LA14_0 <= MINUS) or LA14_0 == TILDE or LA14_0 == LBRACK or LA14_0 == LCURLY or (INT <= LA14_0 <= COMPLEX)) :
                    alt14 = 1
                elif (LA14_0 == PRINT) :
                    alt14 = 2
                else:
                    nvae = NoViableAltException("", 14, 0, self.input)

                    raise nvae

                if alt14 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:137:5: expressionStmt
                    pass 
                    self._state.following.append(self.FOLLOW_expressionStmt_in_simpleStmt654)
                    expressionStmt40 = self.expressionStmt()

                    self._state.following.pop()
                    #action start
                    object = SimpleStmt( expressionStmt40 ) 
                    #action end


                elif alt14 == 2:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:138:5: printStmt
                    pass 
                    self._state.following.append(self.FOLLOW_printStmt_in_simpleStmt668)
                    printStmt41 = self.printStmt()

                    self._state.following.pop()
                    #action start
                    object = SimpleStmt( printStmt41, printStmt41.line, printStmt41.column ) 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "simpleStmt"


    # $ANTLR start "attributeAction"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:141:1: attributeAction returns [object] : ATTRIBUTE expressionStmt ;
    def attributeAction(self, ):

        object = None

        ATTRIBUTE42 = None
        expressionStmt43 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:142:3: ( ATTRIBUTE expressionStmt )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:142:5: ATTRIBUTE expressionStmt
                pass 
                ATTRIBUTE42=self.match(self.input, ATTRIBUTE, self.FOLLOW_ATTRIBUTE_in_attributeAction699)
                self._state.following.append(self.FOLLOW_expressionStmt_in_attributeAction701)
                expressionStmt43 = self.expressionStmt()

                self._state.following.pop()
                #action start
                object = AttributeAction( [ ATTRIBUTE42.text, expressionStmt43 ] , ATTRIBUTE42.getLine(), ATTRIBUTE42.getCharPositionInLine() ) 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "attributeAction"


    # $ANTLR start "printStmt"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:145:1: printStmt returns [object] : PRINT (comparisonList1= comparisonList | RIGHTSHIFT comparisonList2= comparisonList )? NEWLINE ;
    def printStmt(self, ):

        object = None

        PRINT44 = None
        RIGHTSHIFT45 = None
        comparisonList1 = None

        comparisonList2 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:146:3: ( PRINT (comparisonList1= comparisonList | RIGHTSHIFT comparisonList2= comparisonList )? NEWLINE )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:146:5: PRINT (comparisonList1= comparisonList | RIGHTSHIFT comparisonList2= comparisonList )? NEWLINE
                pass 
                PRINT44=self.match(self.input, PRINT, self.FOLLOW_PRINT_in_printStmt721)
                #action start
                object = PrintStmt( PRINT44.text, PRINT44.getLine(), PRINT44.getCharPositionInLine() ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:147:7: (comparisonList1= comparisonList | RIGHTSHIFT comparisonList2= comparisonList )?
                alt15 = 3
                LA15_0 = self.input.LA(1)

                if ((NAME <= LA15_0 <= STRING) or LA15_0 == NOT or LA15_0 == OBJECTBINDING or LA15_0 == LPAREN or (PLUS <= LA15_0 <= MINUS) or LA15_0 == TILDE or LA15_0 == LBRACK or LA15_0 == LCURLY or (INT <= LA15_0 <= COMPLEX)) :
                    alt15 = 1
                elif (LA15_0 == RIGHTSHIFT) :
                    alt15 = 2
                if alt15 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:147:9: comparisonList1= comparisonList
                    pass 
                    self._state.following.append(self.FOLLOW_comparisonList_in_printStmt735)
                    comparisonList1 = self.comparisonList()

                    self._state.following.pop()
                    #action start
                    object.append_child( comparisonList1 ) 
                    #action end


                elif alt15 == 2:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:148:9: RIGHTSHIFT comparisonList2= comparisonList
                    pass 
                    RIGHTSHIFT45=self.match(self.input, RIGHTSHIFT, self.FOLLOW_RIGHTSHIFT_in_printStmt747)
                    self._state.following.append(self.FOLLOW_comparisonList_in_printStmt751)
                    comparisonList2 = self.comparisonList()

                    self._state.following.pop()
                    #action start
                    object.append_children( [RIGHTSHIFT45.text, comparisonList2] ) 
                    #action end



                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_printStmt758)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "printStmt"


    # $ANTLR start "forgetAction"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:151:1: forgetAction returns [object] : ( FORGET | DELETE ) OBJECTBINDING NEWLINE ;
    def forgetAction(self, ):

        object = None

        FORGET46 = None
        DELETE47 = None
        OBJECTBINDING48 = None

        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:152:3: ( ( FORGET | DELETE ) OBJECTBINDING NEWLINE )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:152:5: ( FORGET | DELETE ) OBJECTBINDING NEWLINE
                pass 
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:152:5: ( FORGET | DELETE )
                alt16 = 2
                LA16_0 = self.input.LA(1)

                if (LA16_0 == FORGET) :
                    alt16 = 1
                elif (LA16_0 == DELETE) :
                    alt16 = 2
                else:
                    nvae = NoViableAltException("", 16, 0, self.input)

                    raise nvae

                if alt16 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:152:7: FORGET
                    pass 
                    FORGET46=self.match(self.input, FORGET, self.FOLLOW_FORGET_in_forgetAction778)
                    #action start
                    object = ForgetAction( FORGET46.text, FORGET46.getLine(), FORGET46.getCharPositionInLine() ) 
                    #action end


                elif alt16 == 2:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:153:9: DELETE
                    pass 
                    DELETE47=self.match(self.input, DELETE, self.FOLLOW_DELETE_in_forgetAction790)
                    #action start
                    object = ForgetAction( DELETE47.text, DELETE47.getLine(), DELETE47.getCharPositionInLine() ) 
                    #action end



                OBJECTBINDING48=self.match(self.input, OBJECTBINDING, self.FOLLOW_OBJECTBINDING_in_forgetAction803)
                #action start
                object.append_child( OBJECTBINDING48.text ) 
                #action end
                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_forgetAction807)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "forgetAction"


    # $ANTLR start "learnAction"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:157:1: learnAction returns [object] : ( LEARN | INSERT ) NAME LPAREN ( argumentList )? RPAREN NEWLINE ;
    def learnAction(self, ):

        object = None

        LEARN49 = None
        INSERT50 = None
        NAME51 = None
        LPAREN52 = None
        RPAREN54 = None
        argumentList53 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:158:3: ( ( LEARN | INSERT ) NAME LPAREN ( argumentList )? RPAREN NEWLINE )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:158:5: ( LEARN | INSERT ) NAME LPAREN ( argumentList )? RPAREN NEWLINE
                pass 
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:158:5: ( LEARN | INSERT )
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if (LA17_0 == LEARN) :
                    alt17 = 1
                elif (LA17_0 == INSERT) :
                    alt17 = 2
                else:
                    nvae = NoViableAltException("", 17, 0, self.input)

                    raise nvae

                if alt17 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:158:7: LEARN
                    pass 
                    LEARN49=self.match(self.input, LEARN, self.FOLLOW_LEARN_in_learnAction827)
                    #action start
                    object = LearnAction( LEARN49.text, LEARN49.getLine(), LEARN49.getCharPositionInLine() ) 
                    #action end


                elif alt17 == 2:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:159:9: INSERT
                    pass 
                    INSERT50=self.match(self.input, INSERT, self.FOLLOW_INSERT_in_learnAction839)
                    #action start
                    object = LearnAction( INSERT50.text, INSERT50.getLine(), INSERT50.getCharPositionInLine() ) 
                    #action end



                NAME51=self.match(self.input, NAME, self.FOLLOW_NAME_in_learnAction854)
                LPAREN52=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_learnAction856)
                #action start
                object.append_children( [NAME51.text, LPAREN52.text] ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:161:9: ( argumentList )?
                alt18 = 2
                LA18_0 = self.input.LA(1)

                if ((NAME <= LA18_0 <= STRING) or LA18_0 == NOT or LA18_0 == OBJECTBINDING or LA18_0 == LPAREN or (PLUS <= LA18_0 <= MINUS) or LA18_0 == TILDE or LA18_0 == LBRACK or LA18_0 == LCURLY or (INT <= LA18_0 <= COMPLEX)) :
                    alt18 = 1
                if alt18 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:161:11: argumentList
                    pass 
                    self._state.following.append(self.FOLLOW_argumentList_in_learnAction870)
                    argumentList53 = self.argumentList()

                    self._state.following.pop()
                    #action start
                    object.append_child( argumentList53 ) 
                    #action end



                RPAREN54=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_learnAction877)
                #action start
                object.append_child( RPAREN54.text ) 
                #action end
                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_learnAction881)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "learnAction"


    # $ANTLR start "modifyAction"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:164:1: modifyAction returns [object] : MODIFY OBJECTBINDING COLON NEWLINE INDENT ( propertyAssignment )+ DEDENT ;
    def modifyAction(self, ):

        object = None

        MODIFY55 = None
        OBJECTBINDING56 = None
        COLON57 = None
        propertyAssignment58 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:165:3: ( MODIFY OBJECTBINDING COLON NEWLINE INDENT ( propertyAssignment )+ DEDENT )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:165:5: MODIFY OBJECTBINDING COLON NEWLINE INDENT ( propertyAssignment )+ DEDENT
                pass 
                MODIFY55=self.match(self.input, MODIFY, self.FOLLOW_MODIFY_in_modifyAction899)
                OBJECTBINDING56=self.match(self.input, OBJECTBINDING, self.FOLLOW_OBJECTBINDING_in_modifyAction901)
                COLON57=self.match(self.input, COLON, self.FOLLOW_COLON_in_modifyAction903)
                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_modifyAction905)
                #action start
                object = ModifyAction( [MODIFY55.text, OBJECTBINDING56.text, COLON57.text], MODIFY55.getLine(), MODIFY55.getCharPositionInLine() ) 
                #action end
                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_modifyAction915)
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:166:14: ( propertyAssignment )+
                cnt19 = 0
                while True: #loop19
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if (LA19_0 == NAME) :
                        alt19 = 1


                    if alt19 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:166:16: propertyAssignment
                        pass 
                        self._state.following.append(self.FOLLOW_propertyAssignment_in_modifyAction919)
                        propertyAssignment58 = self.propertyAssignment()

                        self._state.following.pop()
                        #action start
                        object.append_child( propertyAssignment58 ) 
                        #action end


                    else:
                        if cnt19 >= 1:
                            break #loop19

                        eee = EarlyExitException(19, self.input)
                        raise eee

                    cnt19 += 1
                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_modifyAction926)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "modifyAction"


    # $ANTLR start "haltAction"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:169:1: haltAction returns [object] : HALT NEWLINE ;
    def haltAction(self, ):

        object = None

        HALT59 = None

        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:170:3: ( HALT NEWLINE )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:170:5: HALT NEWLINE
                pass 
                HALT59=self.match(self.input, HALT, self.FOLLOW_HALT_in_haltAction944)
                #action start
                object = HaltAction( HALT59.text, HALT59.getLine(), HALT59.getCharPositionInLine() ) 
                #action end
                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_haltAction948)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "haltAction"


    # $ANTLR start "propertyAssignment"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:173:1: propertyAssignment returns [object] : NAME assignment constraint NEWLINE ;
    def propertyAssignment(self, ):

        object = None

        NAME60 = None
        assignment61 = None

        constraint62 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:174:3: ( NAME assignment constraint NEWLINE )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:174:5: NAME assignment constraint NEWLINE
                pass 
                NAME60=self.match(self.input, NAME, self.FOLLOW_NAME_in_propertyAssignment966)
                self._state.following.append(self.FOLLOW_assignment_in_propertyAssignment968)
                assignment61 = self.assignment()

                self._state.following.pop()
                self._state.following.append(self.FOLLOW_constraint_in_propertyAssignment970)
                constraint62 = self.constraint()

                self._state.following.pop()
                #action start
                object = PropertyAssignment( [NAME60.text, assignment61, constraint62] ) 
                #action end
                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_propertyAssignment974)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "propertyAssignment"


    # $ANTLR start "expressionStmt"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:177:1: expressionStmt returns [object] : comparisonList1= comparisonList ( assignment comparisonList2= comparisonList )? NEWLINE ;
    def expressionStmt(self, ):

        object = None

        comparisonList1 = None

        comparisonList2 = None

        assignment63 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:178:3: (comparisonList1= comparisonList ( assignment comparisonList2= comparisonList )? NEWLINE )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:178:5: comparisonList1= comparisonList ( assignment comparisonList2= comparisonList )? NEWLINE
                pass 
                self._state.following.append(self.FOLLOW_comparisonList_in_expressionStmt994)
                comparisonList1 = self.comparisonList()

                self._state.following.pop()
                #action start
                object = ExpressionStmt( comparisonList1 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:179:7: ( assignment comparisonList2= comparisonList )?
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if ((ASSIGN <= LA20_0 <= DOUBLESLASHEQUAL)) :
                    alt20 = 1
                if alt20 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:179:9: assignment comparisonList2= comparisonList
                    pass 
                    self._state.following.append(self.FOLLOW_assignment_in_expressionStmt1006)
                    assignment63 = self.assignment()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_comparisonList_in_expressionStmt1010)
                    comparisonList2 = self.comparisonList()

                    self._state.following.pop()
                    #action start
                    object.append_children( [assignment63, comparisonList2] ) 
                    #action end



                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_expressionStmt1017)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "expressionStmt"


    # $ANTLR start "assignment"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:182:1: assignment returns [object] : ( ASSIGN | PLUSEQUAL | MINUSEQUAL | STAREQUAL | SLASHEQUAL | PERCENTEQUAL | AMPEREQUAL | VBAREQUAL | CIRCUMFLEXEQUAL | LEFTSHIFTEQUAL | RIGHTSHIFTEQUAL | DOUBLESTAREQUAL | DOUBLESLASHEQUAL );
    def assignment(self, ):

        object = None

        ASSIGN64 = None
        PLUSEQUAL65 = None
        MINUSEQUAL66 = None
        STAREQUAL67 = None
        SLASHEQUAL68 = None
        PERCENTEQUAL69 = None
        AMPEREQUAL70 = None
        VBAREQUAL71 = None
        CIRCUMFLEXEQUAL72 = None
        LEFTSHIFTEQUAL73 = None
        RIGHTSHIFTEQUAL74 = None
        DOUBLESTAREQUAL75 = None
        DOUBLESLASHEQUAL76 = None

        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:183:3: ( ASSIGN | PLUSEQUAL | MINUSEQUAL | STAREQUAL | SLASHEQUAL | PERCENTEQUAL | AMPEREQUAL | VBAREQUAL | CIRCUMFLEXEQUAL | LEFTSHIFTEQUAL | RIGHTSHIFTEQUAL | DOUBLESTAREQUAL | DOUBLESLASHEQUAL )
                alt21 = 13
                LA21 = self.input.LA(1)
                if LA21 == ASSIGN:
                    alt21 = 1
                elif LA21 == PLUSEQUAL:
                    alt21 = 2
                elif LA21 == MINUSEQUAL:
                    alt21 = 3
                elif LA21 == STAREQUAL:
                    alt21 = 4
                elif LA21 == SLASHEQUAL:
                    alt21 = 5
                elif LA21 == PERCENTEQUAL:
                    alt21 = 6
                elif LA21 == AMPEREQUAL:
                    alt21 = 7
                elif LA21 == VBAREQUAL:
                    alt21 = 8
                elif LA21 == CIRCUMFLEXEQUAL:
                    alt21 = 9
                elif LA21 == LEFTSHIFTEQUAL:
                    alt21 = 10
                elif LA21 == RIGHTSHIFTEQUAL:
                    alt21 = 11
                elif LA21 == DOUBLESTAREQUAL:
                    alt21 = 12
                elif LA21 == DOUBLESLASHEQUAL:
                    alt21 = 13
                else:
                    nvae = NoViableAltException("", 21, 0, self.input)

                    raise nvae

                if alt21 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:183:5: ASSIGN
                    pass 
                    ASSIGN64=self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_assignment1035)
                    #action start
                    object = Assignment( ASSIGN64.text ) 
                    #action end


                elif alt21 == 2:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:184:5: PLUSEQUAL
                    pass 
                    PLUSEQUAL65=self.match(self.input, PLUSEQUAL, self.FOLLOW_PLUSEQUAL_in_assignment1054)
                    #action start
                    object = Assignment( PLUSEQUAL65.text ) 
                    #action end


                elif alt21 == 3:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:185:5: MINUSEQUAL
                    pass 
                    MINUSEQUAL66=self.match(self.input, MINUSEQUAL, self.FOLLOW_MINUSEQUAL_in_assignment1070)
                    #action start
                    object = Assignment( MINUSEQUAL66.text ) 
                    #action end


                elif alt21 == 4:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:186:5: STAREQUAL
                    pass 
                    STAREQUAL67=self.match(self.input, STAREQUAL, self.FOLLOW_STAREQUAL_in_assignment1085)
                    #action start
                    object = Assignment( STAREQUAL67.text ) 
                    #action end


                elif alt21 == 5:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:187:5: SLASHEQUAL
                    pass 
                    SLASHEQUAL68=self.match(self.input, SLASHEQUAL, self.FOLLOW_SLASHEQUAL_in_assignment1101)
                    #action start
                    object = Assignment( SLASHEQUAL68.text ) 
                    #action end


                elif alt21 == 6:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:188:5: PERCENTEQUAL
                    pass 
                    PERCENTEQUAL69=self.match(self.input, PERCENTEQUAL, self.FOLLOW_PERCENTEQUAL_in_assignment1116)
                    #action start
                    object = Assignment( PERCENTEQUAL69.text ) 
                    #action end


                elif alt21 == 7:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:189:5: AMPEREQUAL
                    pass 
                    AMPEREQUAL70=self.match(self.input, AMPEREQUAL, self.FOLLOW_AMPEREQUAL_in_assignment1129)
                    #action start
                    object = Assignment( AMPEREQUAL70.text ) 
                    #action end


                elif alt21 == 8:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:190:5: VBAREQUAL
                    pass 
                    VBAREQUAL71=self.match(self.input, VBAREQUAL, self.FOLLOW_VBAREQUAL_in_assignment1144)
                    #action start
                    object = Assignment( VBAREQUAL71.text ) 
                    #action end


                elif alt21 == 9:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:191:5: CIRCUMFLEXEQUAL
                    pass 
                    CIRCUMFLEXEQUAL72=self.match(self.input, CIRCUMFLEXEQUAL, self.FOLLOW_CIRCUMFLEXEQUAL_in_assignment1160)
                    #action start
                    object = Assignment( CIRCUMFLEXEQUAL72.text ) 
                    #action end


                elif alt21 == 10:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:192:5: LEFTSHIFTEQUAL
                    pass 
                    LEFTSHIFTEQUAL73=self.match(self.input, LEFTSHIFTEQUAL, self.FOLLOW_LEFTSHIFTEQUAL_in_assignment1170)
                    #action start
                    object = Assignment( LEFTSHIFTEQUAL73.text ) 
                    #action end


                elif alt21 == 11:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:193:5: RIGHTSHIFTEQUAL
                    pass 
                    RIGHTSHIFTEQUAL74=self.match(self.input, RIGHTSHIFTEQUAL, self.FOLLOW_RIGHTSHIFTEQUAL_in_assignment1181)
                    #action start
                    object = Assignment( RIGHTSHIFTEQUAL74.text ) 
                    #action end


                elif alt21 == 12:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:194:5: DOUBLESTAREQUAL
                    pass 
                    DOUBLESTAREQUAL75=self.match(self.input, DOUBLESTAREQUAL, self.FOLLOW_DOUBLESTAREQUAL_in_assignment1191)
                    #action start
                    object = Assignment( DOUBLESTAREQUAL75.text ) 
                    #action end


                elif alt21 == 13:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:195:5: DOUBLESLASHEQUAL
                    pass 
                    DOUBLESLASHEQUAL76=self.match(self.input, DOUBLESLASHEQUAL, self.FOLLOW_DOUBLESLASHEQUAL_in_assignment1201)
                    #action start
                    object = Assignment( DOUBLESLASHEQUAL76.text ) 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "assignment"


    # $ANTLR start "importStmt"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:198:1: importStmt returns [object] : ( importName | importFrom );
    def importStmt(self, ):

        object = None

        importName77 = None

        importFrom78 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:199:3: ( importName | importFrom )
                alt22 = 2
                LA22_0 = self.input.LA(1)

                if (LA22_0 == IMPORT) :
                    alt22 = 1
                elif (LA22_0 == FROM) :
                    alt22 = 2
                else:
                    nvae = NoViableAltException("", 22, 0, self.input)

                    raise nvae

                if alt22 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:199:5: importName
                    pass 
                    self._state.following.append(self.FOLLOW_importName_in_importStmt1222)
                    importName77 = self.importName()

                    self._state.following.pop()
                    #action start
                    object = ImportStmt( children = importName77, line = importName77.line ) 
                    #action end


                elif alt22 == 2:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:200:5: importFrom
                    pass 
                    self._state.following.append(self.FOLLOW_importFrom_in_importStmt1230)
                    importFrom78 = self.importFrom()

                    self._state.following.pop()
                    #action start
                    object = ImportStmt( children = importFrom78, line = importFrom78.line ) 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "importStmt"


    # $ANTLR start "importName"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:203:1: importName returns [object] : IMPORT dottedAsNames NEWLINE ;
    def importName(self, ):

        object = None

        IMPORT79 = None
        dottedAsNames80 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:204:3: ( IMPORT dottedAsNames NEWLINE )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:204:5: IMPORT dottedAsNames NEWLINE
                pass 
                IMPORT79=self.match(self.input, IMPORT, self.FOLLOW_IMPORT_in_importName1250)
                self._state.following.append(self.FOLLOW_dottedAsNames_in_importName1252)
                dottedAsNames80 = self.dottedAsNames()

                self._state.following.pop()
                #action start
                object = ImportName( children = [IMPORT79.text, dottedAsNames80], line = IMPORT79.getLine() ) 
                #action end
                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_importName1256)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "importName"


    # $ANTLR start "importFrom"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:207:1: importFrom returns [object] : FROM dottedName IMPORT (importAsNames1= importAsNames | LPAREN importAsNames2= importAsNames RPAREN ) NEWLINE ;
    def importFrom(self, ):

        object = None

        FROM81 = None
        IMPORT83 = None
        LPAREN84 = None
        RPAREN85 = None
        importAsNames1 = None

        importAsNames2 = None

        dottedName82 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:208:3: ( FROM dottedName IMPORT (importAsNames1= importAsNames | LPAREN importAsNames2= importAsNames RPAREN ) NEWLINE )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:208:5: FROM dottedName IMPORT (importAsNames1= importAsNames | LPAREN importAsNames2= importAsNames RPAREN ) NEWLINE
                pass 
                FROM81=self.match(self.input, FROM, self.FOLLOW_FROM_in_importFrom1274)
                #action start
                object = ImportFrom( children = FROM81.text, line = FROM81.getLine() ) 
                #action end
                self._state.following.append(self.FOLLOW_dottedName_in_importFrom1278)
                dottedName82 = self.dottedName()

                self._state.following.pop()
                #action start
                object.append_child( dottedName82 ) 
                #action end
                IMPORT83=self.match(self.input, IMPORT, self.FOLLOW_IMPORT_in_importFrom1282)
                #action start
                object.append_child( IMPORT83.text ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:209:7: (importAsNames1= importAsNames | LPAREN importAsNames2= importAsNames RPAREN )
                alt23 = 2
                LA23_0 = self.input.LA(1)

                if (LA23_0 == NAME) :
                    alt23 = 1
                elif (LA23_0 == LPAREN) :
                    alt23 = 2
                else:
                    nvae = NoViableAltException("", 23, 0, self.input)

                    raise nvae

                if alt23 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:209:9: importAsNames1= importAsNames
                    pass 
                    self._state.following.append(self.FOLLOW_importAsNames_in_importFrom1296)
                    importAsNames1 = self.importAsNames()

                    self._state.following.pop()
                    #action start
                    object.append_child( importAsNames1 ) 
                    #action end


                elif alt23 == 2:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:210:9: LPAREN importAsNames2= importAsNames RPAREN
                    pass 
                    LPAREN84=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_importFrom1308)
                    self._state.following.append(self.FOLLOW_importAsNames_in_importFrom1313)
                    importAsNames2 = self.importAsNames()

                    self._state.following.pop()
                    RPAREN85=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_importFrom1315)
                    #action start
                    object.append_children( [LPAREN84.text, importAsNames2, RPAREN85.text] ) 
                    #action end



                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_importFrom1327)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "importFrom"


    # $ANTLR start "importAsNames"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:214:1: importAsNames returns [object] : importAsName1= importAsName ( COMMA importAsName2= importAsName )* ( COMMA )? ;
    def importAsNames(self, ):

        object = None

        importAsName1 = None

        importAsName2 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:215:3: (importAsName1= importAsName ( COMMA importAsName2= importAsName )* ( COMMA )? )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:215:5: importAsName1= importAsName ( COMMA importAsName2= importAsName )* ( COMMA )?
                pass 
                self._state.following.append(self.FOLLOW_importAsName_in_importAsNames1346)
                importAsName1 = self.importAsName()

                self._state.following.pop()
                #action start
                object=ImportAsNames( importAsName1 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:216:7: ( COMMA importAsName2= importAsName )*
                while True: #loop24
                    alt24 = 2
                    LA24_0 = self.input.LA(1)

                    if (LA24_0 == COMMA) :
                        LA24_1 = self.input.LA(2)

                        if (LA24_1 == NAME) :
                            alt24 = 1




                    if alt24 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:216:9: COMMA importAsName2= importAsName
                        pass 
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_importAsNames1358)
                        self._state.following.append(self.FOLLOW_importAsName_in_importAsNames1362)
                        importAsName2 = self.importAsName()

                        self._state.following.pop()
                        #action start
                        object.append_children( [",", importAsName2] ) 
                        #action end


                    else:
                        break #loop24
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:216:105: ( COMMA )?
                alt25 = 2
                LA25_0 = self.input.LA(1)

                if (LA25_0 == COMMA) :
                    alt25 = 1
                if alt25 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:216:107: COMMA
                    pass 
                    self.match(self.input, COMMA, self.FOLLOW_COMMA_in_importAsNames1371)
                    #action start
                    object.append_child( "," ) 
                    #action end







            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "importAsNames"


    # $ANTLR start "importAsName"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:219:1: importAsName returns [object] : name1= NAME ( AS name2= NAME )? ;
    def importAsName(self, ):

        object = None

        name1 = None
        name2 = None
        AS86 = None

        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:220:3: (name1= NAME ( AS name2= NAME )? )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:220:5: name1= NAME ( AS name2= NAME )?
                pass 
                name1=self.match(self.input, NAME, self.FOLLOW_NAME_in_importAsName1395)
                #action start
                object=ImportAsName( name1.text ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:220:56: ( AS name2= NAME )?
                alt26 = 2
                LA26_0 = self.input.LA(1)

                if (LA26_0 == AS) :
                    alt26 = 1
                if alt26 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:220:57: AS name2= NAME
                    pass 
                    AS86=self.match(self.input, AS, self.FOLLOW_AS_in_importAsName1400)
                    name2=self.match(self.input, NAME, self.FOLLOW_NAME_in_importAsName1404)
                    #action start
                    object.append_children( [AS86.text, name2.text] ) 
                    #action end







            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "importAsName"


    # $ANTLR start "dottedAsNames"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:223:1: dottedAsNames returns [object] : dottedAsName1= dottedAsName ( COMMA dottedAsName2= dottedAsName )* ;
    def dottedAsNames(self, ):

        object = None

        COMMA87 = None
        dottedAsName1 = None

        dottedAsName2 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:224:3: (dottedAsName1= dottedAsName ( COMMA dottedAsName2= dottedAsName )* )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:224:5: dottedAsName1= dottedAsName ( COMMA dottedAsName2= dottedAsName )*
                pass 
                self._state.following.append(self.FOLLOW_dottedAsName_in_dottedAsNames1428)
                dottedAsName1 = self.dottedAsName()

                self._state.following.pop()
                #action start
                object = DottedAsNames( dottedAsName1 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:225:7: ( COMMA dottedAsName2= dottedAsName )*
                while True: #loop27
                    alt27 = 2
                    LA27_0 = self.input.LA(1)

                    if (LA27_0 == COMMA) :
                        alt27 = 1


                    if alt27 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:225:8: COMMA dottedAsName2= dottedAsName
                        pass 
                        COMMA87=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_dottedAsNames1439)
                        self._state.following.append(self.FOLLOW_dottedAsName_in_dottedAsNames1443)
                        dottedAsName2 = self.dottedAsName()

                        self._state.following.pop()
                        #action start
                        object.append_children( [COMMA87.text, dottedAsName2] ) 
                        #action end


                    else:
                        break #loop27




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "dottedAsNames"


    # $ANTLR start "dottedAsName"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:228:1: dottedAsName returns [object] : dottedName ( AS NAME )? ;
    def dottedAsName(self, ):

        object = None

        AS89 = None
        NAME90 = None
        dottedName88 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:229:3: ( dottedName ( AS NAME )? )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:229:5: dottedName ( AS NAME )?
                pass 
                self._state.following.append(self.FOLLOW_dottedName_in_dottedAsName1465)
                dottedName88 = self.dottedName()

                self._state.following.pop()
                #action start
                object = DottedAsName( dottedName88 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:229:65: ( AS NAME )?
                alt28 = 2
                LA28_0 = self.input.LA(1)

                if (LA28_0 == AS) :
                    alt28 = 1
                if alt28 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:229:67: AS NAME
                    pass 
                    AS89=self.match(self.input, AS, self.FOLLOW_AS_in_dottedAsName1471)
                    NAME90=self.match(self.input, NAME, self.FOLLOW_NAME_in_dottedAsName1473)
                    #action start
                    object.append_children( [AS89.text, NAME90.text] ) 
                    #action end







            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "dottedAsName"


    # $ANTLR start "dottedName"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:232:1: dottedName returns [object] : name1= NAME ( DOT name2= NAME )* ;
    def dottedName(self, ):

        object = None

        name1 = None
        name2 = None
        DOT91 = None

        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:233:3: (name1= NAME ( DOT name2= NAME )* )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:233:5: name1= NAME ( DOT name2= NAME )*
                pass 
                name1=self.match(self.input, NAME, self.FOLLOW_NAME_in_dottedName1498)
                #action start
                object = DottedName( name1.text ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:234:7: ( DOT name2= NAME )*
                while True: #loop29
                    alt29 = 2
                    LA29_0 = self.input.LA(1)

                    if (LA29_0 == DOT) :
                        alt29 = 1


                    if alt29 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:234:9: DOT name2= NAME
                        pass 
                        DOT91=self.match(self.input, DOT, self.FOLLOW_DOT_in_dottedName1510)
                        name2=self.match(self.input, NAME, self.FOLLOW_NAME_in_dottedName1514)
                        #action start
                        object.append_children( [DOT91.text, name2.text] ) 
                        #action end


                    else:
                        break #loop29




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "dottedName"


    # $ANTLR start "constraint"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:237:1: constraint returns [object] : orConstraint ;
    def constraint(self, ):

        object = None

        orConstraint92 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:238:3: ( orConstraint )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:238:5: orConstraint
                pass 
                self._state.following.append(self.FOLLOW_orConstraint_in_constraint1537)
                orConstraint92 = self.orConstraint()

                self._state.following.pop()
                #action start
                object = Constraint( orConstraint92 ) 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "constraint"


    # $ANTLR start "orConstraint"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:241:1: orConstraint returns [object] : constraint1= andConstraint ( OR constraint2= andConstraint )* ;
    def orConstraint(self, ):

        object = None

        OR93 = None
        constraint1 = None

        constraint2 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:242:3: (constraint1= andConstraint ( OR constraint2= andConstraint )* )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:242:5: constraint1= andConstraint ( OR constraint2= andConstraint )*
                pass 
                self._state.following.append(self.FOLLOW_andConstraint_in_orConstraint1559)
                constraint1 = self.andConstraint()

                self._state.following.pop()
                #action start
                object = OrConstraint( constraint1 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:243:7: ( OR constraint2= andConstraint )*
                while True: #loop30
                    alt30 = 2
                    LA30_0 = self.input.LA(1)

                    if (LA30_0 == OR) :
                        alt30 = 1


                    if alt30 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:243:9: OR constraint2= andConstraint
                        pass 
                        OR93=self.match(self.input, OR, self.FOLLOW_OR_in_orConstraint1571)
                        self._state.following.append(self.FOLLOW_andConstraint_in_orConstraint1575)
                        constraint2 = self.andConstraint()

                        self._state.following.pop()
                        #action start
                        object.append_children( [OR93.text, constraint2] ) 
                        #action end


                    else:
                        break #loop30




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "orConstraint"


    # $ANTLR start "andConstraint"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:246:1: andConstraint returns [object] : constraint1= notConstraint ( AND constraint2= notConstraint )* ;
    def andConstraint(self, ):

        object = None

        AND94 = None
        constraint1 = None

        constraint2 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:247:3: (constraint1= notConstraint ( AND constraint2= notConstraint )* )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:247:5: constraint1= notConstraint ( AND constraint2= notConstraint )*
                pass 
                self._state.following.append(self.FOLLOW_notConstraint_in_andConstraint1600)
                constraint1 = self.notConstraint()

                self._state.following.pop()
                #action start
                object = AndConstraint( constraint1 )
                #action end
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:248:7: ( AND constraint2= notConstraint )*
                while True: #loop31
                    alt31 = 2
                    LA31_0 = self.input.LA(1)

                    if (LA31_0 == AND) :
                        alt31 = 1


                    if alt31 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:248:9: AND constraint2= notConstraint
                        pass 
                        AND94=self.match(self.input, AND, self.FOLLOW_AND_in_andConstraint1612)
                        self._state.following.append(self.FOLLOW_notConstraint_in_andConstraint1616)
                        constraint2 = self.notConstraint()

                        self._state.following.pop()
                        #action start
                        object.append_children( [AND94.text, constraint2] ) 
                        #action end


                    else:
                        break #loop31




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "andConstraint"


    # $ANTLR start "notConstraint"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:251:1: notConstraint returns [object] : ( NOT )* comparison ;
    def notConstraint(self, ):

        object = None

        NOT95 = None
        comparison96 = None


        object = NotConstraint() 
        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:253:3: ( ( NOT )* comparison )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:253:5: ( NOT )* comparison
                pass 
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:253:5: ( NOT )*
                while True: #loop32
                    alt32 = 2
                    LA32_0 = self.input.LA(1)

                    if (LA32_0 == NOT) :
                        alt32 = 1


                    if alt32 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:253:7: NOT
                        pass 
                        NOT95=self.match(self.input, NOT, self.FOLLOW_NOT_in_notConstraint1647)
                        #action start
                        object.append_child( NOT95.text ) 
                        #action end


                    else:
                        break #loop32
                self._state.following.append(self.FOLLOW_comparison_in_notConstraint1654)
                comparison96 = self.comparison()

                self._state.following.pop()
                #action start
                object.append_child( comparison96 ) 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "notConstraint"


    # $ANTLR start "comparison"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:256:1: comparison returns [object] : expression1= expression ( comparisonOperation expression2= expression )* ;
    def comparison(self, ):

        object = None

        expression1 = None

        expression2 = None

        comparisonOperation97 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:257:3: (expression1= expression ( comparisonOperation expression2= expression )* )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:257:5: expression1= expression ( comparisonOperation expression2= expression )*
                pass 
                self._state.following.append(self.FOLLOW_expression_in_comparison1676)
                expression1 = self.expression()

                self._state.following.pop()
                #action start
                object = Comparison( expression1 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:258:5: ( comparisonOperation expression2= expression )*
                while True: #loop33
                    alt33 = 2
                    LA33_0 = self.input.LA(1)

                    if (LA33_0 == NOT or (LESS <= LA33_0 <= NOTEQUAL) or (IN <= LA33_0 <= IS)) :
                        alt33 = 1


                    if alt33 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:258:7: comparisonOperation expression2= expression
                        pass 
                        self._state.following.append(self.FOLLOW_comparisonOperation_in_comparison1686)
                        comparisonOperation97 = self.comparisonOperation()

                        self._state.following.pop()
                        self._state.following.append(self.FOLLOW_expression_in_comparison1690)
                        expression2 = self.expression()

                        self._state.following.pop()
                        #action start
                        object.append_children( [ comparisonOperation97, expression2] ) 
                        #action end


                    else:
                        break #loop33




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "comparison"


    # $ANTLR start "comparisonOperation"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:261:1: comparisonOperation returns [object] : ( LESS | GREATER | EQUAL | GREATEREQUAL | LESSEQUAL | ALT_NOTEQUAL | NOTEQUAL | 'in' | 'not' 'in' | 'is' | 'is' 'not' ) ;
    def comparisonOperation(self, ):

        object = None

        LESS98 = None
        GREATER99 = None
        EQUAL100 = None
        GREATEREQUAL101 = None
        LESSEQUAL102 = None
        ALT_NOTEQUAL103 = None
        NOTEQUAL104 = None

        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:262:3: ( ( LESS | GREATER | EQUAL | GREATEREQUAL | LESSEQUAL | ALT_NOTEQUAL | NOTEQUAL | 'in' | 'not' 'in' | 'is' | 'is' 'not' ) )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:262:5: ( LESS | GREATER | EQUAL | GREATEREQUAL | LESSEQUAL | ALT_NOTEQUAL | NOTEQUAL | 'in' | 'not' 'in' | 'is' | 'is' 'not' )
                pass 
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:262:5: ( LESS | GREATER | EQUAL | GREATEREQUAL | LESSEQUAL | ALT_NOTEQUAL | NOTEQUAL | 'in' | 'not' 'in' | 'is' | 'is' 'not' )
                alt34 = 11
                alt34 = self.dfa34.predict(self.input)
                if alt34 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:262:7: LESS
                    pass 
                    LESS98=self.match(self.input, LESS, self.FOLLOW_LESS_in_comparisonOperation1715)
                    #action start
                    object = ComparisonOperation( LESS98.text ) 
                    #action end


                elif alt34 == 2:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:263:7: GREATER
                    pass 
                    GREATER99=self.match(self.input, GREATER, self.FOLLOW_GREATER_in_comparisonOperation1734)
                    #action start
                    object = ComparisonOperation( GREATER99.text ) 
                    #action end


                elif alt34 == 3:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:264:7: EQUAL
                    pass 
                    EQUAL100=self.match(self.input, EQUAL, self.FOLLOW_EQUAL_in_comparisonOperation1750)
                    #action start
                    object = ComparisonOperation( EQUAL100.text ) 
                    #action end


                elif alt34 == 4:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:265:7: GREATEREQUAL
                    pass 
                    GREATEREQUAL101=self.match(self.input, GREATEREQUAL, self.FOLLOW_GREATEREQUAL_in_comparisonOperation1768)
                    #action start
                    object = ComparisonOperation( GREATEREQUAL101.text ) 
                    #action end


                elif alt34 == 5:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:266:7: LESSEQUAL
                    pass 
                    LESSEQUAL102=self.match(self.input, LESSEQUAL, self.FOLLOW_LESSEQUAL_in_comparisonOperation1779)
                    #action start
                    object = ComparisonOperation( LESSEQUAL102.text ) 
                    #action end


                elif alt34 == 6:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:267:7: ALT_NOTEQUAL
                    pass 
                    ALT_NOTEQUAL103=self.match(self.input, ALT_NOTEQUAL, self.FOLLOW_ALT_NOTEQUAL_in_comparisonOperation1793)
                    #action start
                    object = ComparisonOperation( ALT_NOTEQUAL103.text ) 
                    #action end


                elif alt34 == 7:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:268:7: NOTEQUAL
                    pass 
                    NOTEQUAL104=self.match(self.input, NOTEQUAL, self.FOLLOW_NOTEQUAL_in_comparisonOperation1804)
                    #action start
                    object = ComparisonOperation( NOTEQUAL104.text ) 
                    #action end


                elif alt34 == 8:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:269:7: 'in'
                    pass 
                    self.match(self.input, IN, self.FOLLOW_IN_in_comparisonOperation1819)
                    #action start
                    object = ComparisonOperation( "in" ) 
                    #action end


                elif alt34 == 9:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:270:7: 'not' 'in'
                    pass 
                    self.match(self.input, NOT, self.FOLLOW_NOT_in_comparisonOperation1838)
                    self.match(self.input, IN, self.FOLLOW_IN_in_comparisonOperation1840)
                    #action start
                    object = ComparisonOperation( "not in" ) 
                    #action end


                elif alt34 == 10:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:271:7: 'is'
                    pass 
                    self.match(self.input, IS, self.FOLLOW_IS_in_comparisonOperation1853)
                    #action start
                    object = ComparisonOperation( "is" ) 
                    #action end


                elif alt34 == 11:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:272:7: 'is' 'not'
                    pass 
                    self.match(self.input, IS, self.FOLLOW_IS_in_comparisonOperation1872)
                    self.match(self.input, NOT, self.FOLLOW_NOT_in_comparisonOperation1874)
                    #action start
                    object = ComparisonOperation( "is not" ) 
                    #action end







            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "comparisonOperation"


    # $ANTLR start "expression"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:275:1: expression returns [object] : bitwiseOrExpr ;
    def expression(self, ):

        object = None

        bitwiseOrExpr105 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:276:3: ( bitwiseOrExpr )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:276:5: bitwiseOrExpr
                pass 
                self._state.following.append(self.FOLLOW_bitwiseOrExpr_in_expression1899)
                bitwiseOrExpr105 = self.bitwiseOrExpr()

                self._state.following.pop()
                #action start
                object = Expression( bitwiseOrExpr105 ) 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "expression"


    # $ANTLR start "bitwiseOrExpr"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:279:1: bitwiseOrExpr returns [object] : expr1= bitwiseXorExpr ( VBAR expr2= bitwiseXorExpr )* ;
    def bitwiseOrExpr(self, ):

        object = None

        VBAR106 = None
        expr1 = None

        expr2 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:280:3: (expr1= bitwiseXorExpr ( VBAR expr2= bitwiseXorExpr )* )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:280:5: expr1= bitwiseXorExpr ( VBAR expr2= bitwiseXorExpr )*
                pass 
                self._state.following.append(self.FOLLOW_bitwiseXorExpr_in_bitwiseOrExpr1921)
                expr1 = self.bitwiseXorExpr()

                self._state.following.pop()
                #action start
                object = BitwiseOrExpr( expr1 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:281:7: ( VBAR expr2= bitwiseXorExpr )*
                while True: #loop35
                    alt35 = 2
                    LA35_0 = self.input.LA(1)

                    if (LA35_0 == VBAR) :
                        alt35 = 1


                    if alt35 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:281:9: VBAR expr2= bitwiseXorExpr
                        pass 
                        VBAR106=self.match(self.input, VBAR, self.FOLLOW_VBAR_in_bitwiseOrExpr1933)
                        self._state.following.append(self.FOLLOW_bitwiseXorExpr_in_bitwiseOrExpr1937)
                        expr2 = self.bitwiseXorExpr()

                        self._state.following.pop()
                        #action start
                        object.append_children( [VBAR106.text, expr2] ) 
                        #action end


                    else:
                        break #loop35




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "bitwiseOrExpr"


    # $ANTLR start "bitwiseXorExpr"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:284:1: bitwiseXorExpr returns [object] : expr1= bitwiseAndExpr ( CIRCUMFLEX expr2= bitwiseAndExpr )* ;
    def bitwiseXorExpr(self, ):

        object = None

        CIRCUMFLEX107 = None
        expr1 = None

        expr2 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:285:3: (expr1= bitwiseAndExpr ( CIRCUMFLEX expr2= bitwiseAndExpr )* )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:285:5: expr1= bitwiseAndExpr ( CIRCUMFLEX expr2= bitwiseAndExpr )*
                pass 
                self._state.following.append(self.FOLLOW_bitwiseAndExpr_in_bitwiseXorExpr1962)
                expr1 = self.bitwiseAndExpr()

                self._state.following.pop()
                #action start
                object = BitwiseXorExpr( expr1 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:286:7: ( CIRCUMFLEX expr2= bitwiseAndExpr )*
                while True: #loop36
                    alt36 = 2
                    LA36_0 = self.input.LA(1)

                    if (LA36_0 == CIRCUMFLEX) :
                        alt36 = 1


                    if alt36 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:286:9: CIRCUMFLEX expr2= bitwiseAndExpr
                        pass 
                        CIRCUMFLEX107=self.match(self.input, CIRCUMFLEX, self.FOLLOW_CIRCUMFLEX_in_bitwiseXorExpr1974)
                        self._state.following.append(self.FOLLOW_bitwiseAndExpr_in_bitwiseXorExpr1978)
                        expr2 = self.bitwiseAndExpr()

                        self._state.following.pop()
                        #action start
                        object.append_children( [CIRCUMFLEX107.text, expr2] ) 
                        #action end


                    else:
                        break #loop36




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "bitwiseXorExpr"


    # $ANTLR start "bitwiseAndExpr"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:289:1: bitwiseAndExpr returns [object] : expr1= shiftExpr ( AMPER expr2= shiftExpr )* ;
    def bitwiseAndExpr(self, ):

        object = None

        AMPER108 = None
        expr1 = None

        expr2 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:290:3: (expr1= shiftExpr ( AMPER expr2= shiftExpr )* )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:290:5: expr1= shiftExpr ( AMPER expr2= shiftExpr )*
                pass 
                self._state.following.append(self.FOLLOW_shiftExpr_in_bitwiseAndExpr2003)
                expr1 = self.shiftExpr()

                self._state.following.pop()
                #action start
                object = BitwiseAndExpr( expr1 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:291:7: ( AMPER expr2= shiftExpr )*
                while True: #loop37
                    alt37 = 2
                    LA37_0 = self.input.LA(1)

                    if (LA37_0 == AMPER) :
                        alt37 = 1


                    if alt37 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:291:9: AMPER expr2= shiftExpr
                        pass 
                        AMPER108=self.match(self.input, AMPER, self.FOLLOW_AMPER_in_bitwiseAndExpr2015)
                        self._state.following.append(self.FOLLOW_shiftExpr_in_bitwiseAndExpr2019)
                        expr2 = self.shiftExpr()

                        self._state.following.pop()
                        #action start
                        object.append_children( [AMPER108.text, expr2] ) 
                        #action end


                    else:
                        break #loop37




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "bitwiseAndExpr"


    # $ANTLR start "shiftExpr"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:294:1: shiftExpr returns [object] : expr1= arithExpr ( ( LEFTSHIFT | RIGHTSHIFT ) expr2= arithExpr )* ;
    def shiftExpr(self, ):

        object = None

        LEFTSHIFT109 = None
        RIGHTSHIFT110 = None
        expr1 = None

        expr2 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:295:3: (expr1= arithExpr ( ( LEFTSHIFT | RIGHTSHIFT ) expr2= arithExpr )* )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:295:5: expr1= arithExpr ( ( LEFTSHIFT | RIGHTSHIFT ) expr2= arithExpr )*
                pass 
                self._state.following.append(self.FOLLOW_arithExpr_in_shiftExpr2044)
                expr1 = self.arithExpr()

                self._state.following.pop()
                #action start
                object = ShiftExpr( expr1 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:296:7: ( ( LEFTSHIFT | RIGHTSHIFT ) expr2= arithExpr )*
                while True: #loop39
                    alt39 = 2
                    LA39_0 = self.input.LA(1)

                    if (LA39_0 == RIGHTSHIFT or LA39_0 == LEFTSHIFT) :
                        alt39 = 1


                    if alt39 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:296:9: ( LEFTSHIFT | RIGHTSHIFT ) expr2= arithExpr
                        pass 
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:296:9: ( LEFTSHIFT | RIGHTSHIFT )
                        alt38 = 2
                        LA38_0 = self.input.LA(1)

                        if (LA38_0 == LEFTSHIFT) :
                            alt38 = 1
                        elif (LA38_0 == RIGHTSHIFT) :
                            alt38 = 2
                        else:
                            nvae = NoViableAltException("", 38, 0, self.input)

                            raise nvae

                        if alt38 == 1:
                            # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:296:11: LEFTSHIFT
                            pass 
                            LEFTSHIFT109=self.match(self.input, LEFTSHIFT, self.FOLLOW_LEFTSHIFT_in_shiftExpr2058)
                            #action start
                            object.append_child( LEFTSHIFT109.text ) 
                            #action end


                        elif alt38 == 2:
                            # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:296:67: RIGHTSHIFT
                            pass 
                            RIGHTSHIFT110=self.match(self.input, RIGHTSHIFT, self.FOLLOW_RIGHTSHIFT_in_shiftExpr2064)
                            #action start
                            object.append_child( RIGHTSHIFT110.text ) 
                            #action end



                        self._state.following.append(self.FOLLOW_arithExpr_in_shiftExpr2082)
                        expr2 = self.arithExpr()

                        self._state.following.pop()
                        #action start
                        object.append_child( expr2 ) 
                        #action end


                    else:
                        break #loop39




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "shiftExpr"


    # $ANTLR start "arithExpr"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:300:1: arithExpr returns [object] : term1= term ( ( PLUS | MINUS ) term2= term )* ;
    def arithExpr(self, ):

        object = None

        PLUS111 = None
        MINUS112 = None
        term1 = None

        term2 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:301:3: (term1= term ( ( PLUS | MINUS ) term2= term )* )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:301:5: term1= term ( ( PLUS | MINUS ) term2= term )*
                pass 
                self._state.following.append(self.FOLLOW_term_in_arithExpr2107)
                term1 = self.term()

                self._state.following.pop()
                #action start
                object = ArithExpr( term1 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:302:7: ( ( PLUS | MINUS ) term2= term )*
                while True: #loop41
                    alt41 = 2
                    LA41_0 = self.input.LA(1)

                    if ((PLUS <= LA41_0 <= MINUS)) :
                        alt41 = 1


                    if alt41 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:302:9: ( PLUS | MINUS ) term2= term
                        pass 
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:302:9: ( PLUS | MINUS )
                        alt40 = 2
                        LA40_0 = self.input.LA(1)

                        if (LA40_0 == PLUS) :
                            alt40 = 1
                        elif (LA40_0 == MINUS) :
                            alt40 = 2
                        else:
                            nvae = NoViableAltException("", 40, 0, self.input)

                            raise nvae

                        if alt40 == 1:
                            # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:302:11: PLUS
                            pass 
                            PLUS111=self.match(self.input, PLUS, self.FOLLOW_PLUS_in_arithExpr2121)
                            #action start
                            object.append_child( PLUS111.text ) 
                            #action end


                        elif alt40 == 2:
                            # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:302:57: MINUS
                            pass 
                            MINUS112=self.match(self.input, MINUS, self.FOLLOW_MINUS_in_arithExpr2127)
                            #action start
                            object.append_child( MINUS112.text ) 
                            #action end



                        self._state.following.append(self.FOLLOW_term_in_arithExpr2145)
                        term2 = self.term()

                        self._state.following.pop()
                        #action start
                        object.append_child( term2 ) 
                        #action end


                    else:
                        break #loop41




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "arithExpr"


    # $ANTLR start "term"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:306:1: term returns [object] : factor1= factor ( ( STAR | SLASH | PERCENT | DOUBLESLASH ) factor2= factor )* ;
    def term(self, ):

        object = None

        STAR113 = None
        SLASH114 = None
        PERCENT115 = None
        DOUBLESLASH116 = None
        factor1 = None

        factor2 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:307:3: (factor1= factor ( ( STAR | SLASH | PERCENT | DOUBLESLASH ) factor2= factor )* )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:307:5: factor1= factor ( ( STAR | SLASH | PERCENT | DOUBLESLASH ) factor2= factor )*
                pass 
                self._state.following.append(self.FOLLOW_factor_in_term2170)
                factor1 = self.factor()

                self._state.following.pop()
                #action start
                object = Term( factor1 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:308:7: ( ( STAR | SLASH | PERCENT | DOUBLESLASH ) factor2= factor )*
                while True: #loop43
                    alt43 = 2
                    LA43_0 = self.input.LA(1)

                    if ((STAR <= LA43_0 <= DOUBLESLASH)) :
                        alt43 = 1


                    if alt43 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:308:9: ( STAR | SLASH | PERCENT | DOUBLESLASH ) factor2= factor
                        pass 
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:308:9: ( STAR | SLASH | PERCENT | DOUBLESLASH )
                        alt42 = 4
                        LA42 = self.input.LA(1)
                        if LA42 == STAR:
                            alt42 = 1
                        elif LA42 == SLASH:
                            alt42 = 2
                        elif LA42 == PERCENT:
                            alt42 = 3
                        elif LA42 == DOUBLESLASH:
                            alt42 = 4
                        else:
                            nvae = NoViableAltException("", 42, 0, self.input)

                            raise nvae

                        if alt42 == 1:
                            # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:308:10: STAR
                            pass 
                            STAR113=self.match(self.input, STAR, self.FOLLOW_STAR_in_term2183)
                            #action start
                            object.append_child( STAR113.text ) 
                            #action end


                        elif alt42 == 2:
                            # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:308:56: SLASH
                            pass 
                            SLASH114=self.match(self.input, SLASH, self.FOLLOW_SLASH_in_term2189)
                            #action start
                            object.append_child( SLASH114.text ) 
                            #action end


                        elif alt42 == 3:
                            # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:309:13: PERCENT
                            pass 
                            PERCENT115=self.match(self.input, PERCENT, self.FOLLOW_PERCENT_in_term2205)
                            #action start
                            object.append_child( PERCENT115.text ) 
                            #action end


                        elif alt42 == 4:
                            # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:309:65: DOUBLESLASH
                            pass 
                            DOUBLESLASH116=self.match(self.input, DOUBLESLASH, self.FOLLOW_DOUBLESLASH_in_term2211)
                            #action start
                            object.append_child( DOUBLESLASH116.text ) 
                            #action end



                        self._state.following.append(self.FOLLOW_factor_in_term2233)
                        factor2 = self.factor()

                        self._state.following.pop()
                        #action start
                        object.append_child( factor2 ) 
                        #action end


                    else:
                        break #loop43




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "term"


    # $ANTLR start "factor"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:313:1: factor returns [object] : ( PLUS factor1= factor | MINUS factor2= factor | TILDE factor3= factor | power );
    def factor(self, ):

        object = None

        PLUS117 = None
        MINUS118 = None
        TILDE119 = None
        factor1 = None

        factor2 = None

        factor3 = None

        power120 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:314:3: ( PLUS factor1= factor | MINUS factor2= factor | TILDE factor3= factor | power )
                alt44 = 4
                LA44 = self.input.LA(1)
                if LA44 == PLUS:
                    alt44 = 1
                elif LA44 == MINUS:
                    alt44 = 2
                elif LA44 == TILDE:
                    alt44 = 3
                elif LA44 == NAME or LA44 == STRING or LA44 == OBJECTBINDING or LA44 == LPAREN or LA44 == LBRACK or LA44 == LCURLY or LA44 == INT or LA44 == LONGINT or LA44 == FLOAT or LA44 == COMPLEX:
                    alt44 = 4
                else:
                    nvae = NoViableAltException("", 44, 0, self.input)

                    raise nvae

                if alt44 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:314:5: PLUS factor1= factor
                    pass 
                    PLUS117=self.match(self.input, PLUS, self.FOLLOW_PLUS_in_factor2256)
                    self._state.following.append(self.FOLLOW_factor_in_factor2261)
                    factor1 = self.factor()

                    self._state.following.pop()
                    #action start
                    object = Factor( [PLUS117.text, factor1] ) 
                    #action end


                elif alt44 == 2:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:315:5: MINUS factor2= factor
                    pass 
                    MINUS118=self.match(self.input, MINUS, self.FOLLOW_MINUS_in_factor2269)
                    self._state.following.append(self.FOLLOW_factor_in_factor2273)
                    factor2 = self.factor()

                    self._state.following.pop()
                    #action start
                    object = Factor( [MINUS118.text, factor2] ) 
                    #action end


                elif alt44 == 3:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:316:5: TILDE factor3= factor
                    pass 
                    TILDE119=self.match(self.input, TILDE, self.FOLLOW_TILDE_in_factor2281)
                    self._state.following.append(self.FOLLOW_factor_in_factor2285)
                    factor3 = self.factor()

                    self._state.following.pop()
                    #action start
                    object = Factor( [TILDE119.text, factor3] ) 
                    #action end


                elif alt44 == 4:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:317:5: power
                    pass 
                    self._state.following.append(self.FOLLOW_power_in_factor2293)
                    power120 = self.power()

                    self._state.following.pop()
                    #action start
                    object = Factor( power120 ) 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "factor"


    # $ANTLR start "power"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:320:1: power returns [object] : atom ( trailer )* ( options {greedy=true; } : DOUBLESTAR factor )? ;
    def power(self, ):

        object = None

        DOUBLESTAR123 = None
        atom121 = None

        trailer122 = None

        factor124 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:321:3: ( atom ( trailer )* ( options {greedy=true; } : DOUBLESTAR factor )? )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:321:5: atom ( trailer )* ( options {greedy=true; } : DOUBLESTAR factor )?
                pass 
                self._state.following.append(self.FOLLOW_atom_in_power2313)
                atom121 = self.atom()

                self._state.following.pop()
                #action start
                object = Power( atom121 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:322:7: ( trailer )*
                while True: #loop45
                    alt45 = 2
                    LA45_0 = self.input.LA(1)

                    if (LA45_0 == LPAREN or LA45_0 == DOT) :
                        alt45 = 1


                    if alt45 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:322:9: trailer
                        pass 
                        self._state.following.append(self.FOLLOW_trailer_in_power2325)
                        trailer122 = self.trailer()

                        self._state.following.pop()
                        #action start
                        object.append_child( trailer122 ) 
                        #action end


                    else:
                        break #loop45
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:323:7: ( options {greedy=true; } : DOUBLESTAR factor )?
                alt46 = 2
                LA46_0 = self.input.LA(1)

                if (LA46_0 == DOUBLESTAR) :
                    alt46 = 1
                if alt46 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:323:31: DOUBLESTAR factor
                    pass 
                    DOUBLESTAR123=self.match(self.input, DOUBLESTAR, self.FOLLOW_DOUBLESTAR_in_power2346)
                    self._state.following.append(self.FOLLOW_factor_in_power2348)
                    factor124 = self.factor()

                    self._state.following.pop()
                    #action start
                    object.append_children( [DOUBLESTAR123.text, factor124] ) 
                    #action end







            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "power"


    # $ANTLR start "atom"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:326:1: atom returns [object] : ( LPAREN (comparisonList1= comparisonList )? RPAREN | LBRACK ( listmaker )? RBRACK | LCURLY ( dictmaker )? RCURLY | NAME | OBJECTBINDING | INT | LONGINT | FLOAT | COMPLEX | ( STRING )+ );
    def atom(self, ):

        object = None

        LPAREN125 = None
        RPAREN126 = None
        LBRACK127 = None
        RBRACK129 = None
        LCURLY130 = None
        RCURLY132 = None
        NAME133 = None
        OBJECTBINDING134 = None
        INT135 = None
        LONGINT136 = None
        FLOAT137 = None
        COMPLEX138 = None
        STRING139 = None
        comparisonList1 = None

        listmaker128 = None

        dictmaker131 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:327:3: ( LPAREN (comparisonList1= comparisonList )? RPAREN | LBRACK ( listmaker )? RBRACK | LCURLY ( dictmaker )? RCURLY | NAME | OBJECTBINDING | INT | LONGINT | FLOAT | COMPLEX | ( STRING )+ )
                alt51 = 10
                LA51 = self.input.LA(1)
                if LA51 == LPAREN:
                    alt51 = 1
                elif LA51 == LBRACK:
                    alt51 = 2
                elif LA51 == LCURLY:
                    alt51 = 3
                elif LA51 == NAME:
                    alt51 = 4
                elif LA51 == OBJECTBINDING:
                    alt51 = 5
                elif LA51 == INT:
                    alt51 = 6
                elif LA51 == LONGINT:
                    alt51 = 7
                elif LA51 == FLOAT:
                    alt51 = 8
                elif LA51 == COMPLEX:
                    alt51 = 9
                elif LA51 == STRING:
                    alt51 = 10
                else:
                    nvae = NoViableAltException("", 51, 0, self.input)

                    raise nvae

                if alt51 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:327:5: LPAREN (comparisonList1= comparisonList )? RPAREN
                    pass 
                    LPAREN125=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_atom2371)
                    #action start
                    object = Atom( LPAREN125.text ) 
                    #action end
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:328:23: (comparisonList1= comparisonList )?
                    alt47 = 2
                    LA47_0 = self.input.LA(1)

                    if ((NAME <= LA47_0 <= STRING) or LA47_0 == NOT or LA47_0 == OBJECTBINDING or LA47_0 == LPAREN or (PLUS <= LA47_0 <= MINUS) or LA47_0 == TILDE or LA47_0 == LBRACK or LA47_0 == LCURLY or (INT <= LA47_0 <= COMPLEX)) :
                        alt47 = 1
                    if alt47 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:328:25: comparisonList1= comparisonList
                        pass 
                        self._state.following.append(self.FOLLOW_comparisonList_in_atom2410)
                        comparisonList1 = self.comparisonList()

                        self._state.following.pop()
                        #action start
                        object.append_child( comparisonList1 ) 
                        #action end



                    RPAREN126=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_atom2439)
                    #action start
                    object.append_child( RPAREN126.text ) 
                    #action end


                elif alt51 == 2:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:330:5: LBRACK ( listmaker )? RBRACK
                    pass 
                    LBRACK127=self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_atom2447)
                    #action start
                    object = Atom( LBRACK127.text ) 
                    #action end
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:331:23: ( listmaker )?
                    alt48 = 2
                    LA48_0 = self.input.LA(1)

                    if ((NAME <= LA48_0 <= STRING) or LA48_0 == NOT or LA48_0 == OBJECTBINDING or LA48_0 == LPAREN or (PLUS <= LA48_0 <= MINUS) or LA48_0 == TILDE or LA48_0 == LBRACK or LA48_0 == LCURLY or (INT <= LA48_0 <= COMPLEX)) :
                        alt48 = 1
                    if alt48 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:331:25: listmaker
                        pass 
                        self._state.following.append(self.FOLLOW_listmaker_in_atom2484)
                        listmaker128 = self.listmaker()

                        self._state.following.pop()
                        #action start
                        object.append_child( listmaker128 ) 
                        #action end



                    RBRACK129=self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_atom2513)
                    #action start
                    object.append_child( RBRACK129.text ) 
                    #action end


                elif alt51 == 3:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:333:5: LCURLY ( dictmaker )? RCURLY
                    pass 
                    LCURLY130=self.match(self.input, LCURLY, self.FOLLOW_LCURLY_in_atom2521)
                    #action start
                    object = Atom( LCURLY130.text ) 
                    #action end
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:334:23: ( dictmaker )?
                    alt49 = 2
                    LA49_0 = self.input.LA(1)

                    if ((NAME <= LA49_0 <= STRING) or LA49_0 == NOT or LA49_0 == OBJECTBINDING or LA49_0 == LPAREN or (PLUS <= LA49_0 <= MINUS) or LA49_0 == TILDE or LA49_0 == LBRACK or LA49_0 == LCURLY or (INT <= LA49_0 <= COMPLEX)) :
                        alt49 = 1
                    if alt49 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:334:25: dictmaker
                        pass 
                        self._state.following.append(self.FOLLOW_dictmaker_in_atom2558)
                        dictmaker131 = self.dictmaker()

                        self._state.following.pop()
                        #action start
                        object.append_child( dictmaker131 ) 
                        #action end



                    RCURLY132=self.match(self.input, RCURLY, self.FOLLOW_RCURLY_in_atom2587)
                    #action start
                    object.append_child( RCURLY132.text ) 
                    #action end


                elif alt51 == 4:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:337:5: NAME
                    pass 
                    NAME133=self.match(self.input, NAME, self.FOLLOW_NAME_in_atom2596)
                    #action start
                    object = Atom( NAME133.text ) 
                    #action end


                elif alt51 == 5:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:338:5: OBJECTBINDING
                    pass 
                    OBJECTBINDING134=self.match(self.input, OBJECTBINDING, self.FOLLOW_OBJECTBINDING_in_atom2615)
                    #action start
                    object = Atom( OBJECTBINDING134.text ) 
                    #action end


                elif alt51 == 6:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:339:5: INT
                    pass 
                    INT135=self.match(self.input, INT, self.FOLLOW_INT_in_atom2625)
                    #action start
                    object = Atom( INT135.text ) 
                    #action end


                elif alt51 == 7:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:340:5: LONGINT
                    pass 
                    LONGINT136=self.match(self.input, LONGINT, self.FOLLOW_LONGINT_in_atom2645)
                    #action start
                    object = Atom( LONGINT136.text ) 
                    #action end


                elif alt51 == 8:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:341:5: FLOAT
                    pass 
                    FLOAT137=self.match(self.input, FLOAT, self.FOLLOW_FLOAT_in_atom2661)
                    #action start
                    object = Atom( FLOAT137.text ) 
                    #action end


                elif alt51 == 9:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:342:5: COMPLEX
                    pass 
                    COMPLEX138=self.match(self.input, COMPLEX, self.FOLLOW_COMPLEX_in_atom2679)
                    #action start
                    object = Atom( COMPLEX138.text ) 
                    #action end


                elif alt51 == 10:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:343:5: ( STRING )+
                    pass 
                    #action start
                    object = Atom() 
                    #action end
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:343:25: ( STRING )+
                    cnt50 = 0
                    while True: #loop50
                        alt50 = 2
                        LA50_0 = self.input.LA(1)

                        if (LA50_0 == STRING) :
                            alt50 = 1


                        if alt50 == 1:
                            # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:343:27: STRING
                            pass 
                            STRING139=self.match(self.input, STRING, self.FOLLOW_STRING_in_atom2699)
                            #action start
                            object.append_child( STRING139.text ) 
                            #action end


                        else:
                            if cnt50 >= 1:
                                break #loop50

                            eee = EarlyExitException(50, self.input)
                            raise eee

                        cnt50 += 1



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "atom"


    # $ANTLR start "listmaker"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:346:1: listmaker returns [object] : constraint1= constraint ( options {greedy=true; } : COMMA constraint2= constraint )* ( COMMA )? ;
    def listmaker(self, ):

        object = None

        constraint1 = None

        constraint2 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:347:3: (constraint1= constraint ( options {greedy=true; } : COMMA constraint2= constraint )* ( COMMA )? )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:347:5: constraint1= constraint ( options {greedy=true; } : COMMA constraint2= constraint )* ( COMMA )?
                pass 
                self._state.following.append(self.FOLLOW_constraint_in_listmaker2724)
                constraint1 = self.constraint()

                self._state.following.pop()
                #action start
                object = ListMaker( constraint1 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:348:7: ( options {greedy=true; } : COMMA constraint2= constraint )*
                while True: #loop52
                    alt52 = 2
                    LA52_0 = self.input.LA(1)

                    if (LA52_0 == COMMA) :
                        LA52_1 = self.input.LA(2)

                        if ((NAME <= LA52_1 <= STRING) or LA52_1 == NOT or LA52_1 == OBJECTBINDING or LA52_1 == LPAREN or (PLUS <= LA52_1 <= MINUS) or LA52_1 == TILDE or LA52_1 == LBRACK or LA52_1 == LCURLY or (INT <= LA52_1 <= COMPLEX)) :
                            alt52 = 1




                    if alt52 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:348:31: COMMA constraint2= constraint
                        pass 
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_listmaker2742)
                        self._state.following.append(self.FOLLOW_constraint_in_listmaker2746)
                        constraint2 = self.constraint()

                        self._state.following.pop()
                        #action start
                        object.append_children( [ ",", constraint2] ) 
                        #action end


                    else:
                        break #loop52
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:349:7: ( COMMA )?
                alt53 = 2
                LA53_0 = self.input.LA(1)

                if (LA53_0 == COMMA) :
                    alt53 = 1
                if alt53 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:349:9: COMMA
                    pass 
                    self.match(self.input, COMMA, self.FOLLOW_COMMA_in_listmaker2761)
                    #action start
                    object.append_child( "," ) 
                    #action end







            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "listmaker"


    # $ANTLR start "comparisonList"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:352:1: comparisonList returns [object] : constraint1= constraint ( options {k=2; } : COMMA constraint2= constraint )* ( COMMA )? ;
    def comparisonList(self, ):

        object = None

        constraint1 = None

        constraint2 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:353:3: (constraint1= constraint ( options {k=2; } : COMMA constraint2= constraint )* ( COMMA )? )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:353:5: constraint1= constraint ( options {k=2; } : COMMA constraint2= constraint )* ( COMMA )?
                pass 
                self._state.following.append(self.FOLLOW_constraint_in_comparisonList2786)
                constraint1 = self.constraint()

                self._state.following.pop()
                #action start
                object = ComparisonList( constraint1 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:354:7: ( options {k=2; } : COMMA constraint2= constraint )*
                while True: #loop54
                    alt54 = 2
                    alt54 = self.dfa54.predict(self.input)
                    if alt54 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:354:23: COMMA constraint2= constraint
                        pass 
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_comparisonList2804)
                        self._state.following.append(self.FOLLOW_constraint_in_comparisonList2808)
                        constraint2 = self.constraint()

                        self._state.following.pop()
                        #action start
                        object.append_children( [",", constraint2] ) 
                        #action end


                    else:
                        break #loop54
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:355:7: ( COMMA )?
                alt55 = 2
                LA55_0 = self.input.LA(1)

                if (LA55_0 == COMMA) :
                    alt55 = 1
                if alt55 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:355:9: COMMA
                    pass 
                    self.match(self.input, COMMA, self.FOLLOW_COMMA_in_comparisonList2823)
                    #action start
                    object.append_child( "," ) 
                    #action end







            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "comparisonList"


    # $ANTLR start "trailer"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:358:1: trailer returns [object] : ( LPAREN ( argumentList )? RPAREN | DOT NAME );
    def trailer(self, ):

        object = None

        LPAREN140 = None
        RPAREN142 = None
        DOT143 = None
        NAME144 = None
        argumentList141 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:359:3: ( LPAREN ( argumentList )? RPAREN | DOT NAME )
                alt57 = 2
                LA57_0 = self.input.LA(1)

                if (LA57_0 == LPAREN) :
                    alt57 = 1
                elif (LA57_0 == DOT) :
                    alt57 = 2
                else:
                    nvae = NoViableAltException("", 57, 0, self.input)

                    raise nvae

                if alt57 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:359:5: LPAREN ( argumentList )? RPAREN
                    pass 
                    LPAREN140=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_trailer2846)
                    #action start
                    object = Trailer( LPAREN140.text ) 
                    #action end
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:359:49: ( argumentList )?
                    alt56 = 2
                    LA56_0 = self.input.LA(1)

                    if ((NAME <= LA56_0 <= STRING) or LA56_0 == NOT or LA56_0 == OBJECTBINDING or LA56_0 == LPAREN or (PLUS <= LA56_0 <= MINUS) or LA56_0 == TILDE or LA56_0 == LBRACK or LA56_0 == LCURLY or (INT <= LA56_0 <= COMPLEX)) :
                        alt56 = 1
                    if alt56 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:359:50: argumentList
                        pass 
                        self._state.following.append(self.FOLLOW_argumentList_in_trailer2851)
                        argumentList141 = self.argumentList()

                        self._state.following.pop()
                        #action start
                        object.append_child( argumentList141 ) 
                        #action end



                    RPAREN142=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_trailer2858)
                    #action start
                    object.append_child( RPAREN142.text ) 
                    #action end


                elif alt57 == 2:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:360:5: DOT NAME
                    pass 
                    DOT143=self.match(self.input, DOT, self.FOLLOW_DOT_in_trailer2866)
                    NAME144=self.match(self.input, NAME, self.FOLLOW_NAME_in_trailer2868)
                    #action start
                    object = Trailer( [DOT143.text, NAME144.text] ) 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "trailer"


    # $ANTLR start "expressionList"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:363:1: expressionList returns [object] : expression1= expression ( options {k=2; } : COMMA expression2= expression )* ( COMMA )? ;
    def expressionList(self, ):

        object = None

        expression1 = None

        expression2 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:364:3: (expression1= expression ( options {k=2; } : COMMA expression2= expression )* ( COMMA )? )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:364:5: expression1= expression ( options {k=2; } : COMMA expression2= expression )* ( COMMA )?
                pass 
                self._state.following.append(self.FOLLOW_expression_in_expressionList2891)
                expression1 = self.expression()

                self._state.following.pop()
                #action start
                object = ExpressionList( expression1 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:365:7: ( options {k=2; } : COMMA expression2= expression )*
                while True: #loop58
                    alt58 = 2
                    alt58 = self.dfa58.predict(self.input)
                    if alt58 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:365:25: COMMA expression2= expression
                        pass 
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_expressionList2911)
                        self._state.following.append(self.FOLLOW_expression_in_expressionList2915)
                        expression2 = self.expression()

                        self._state.following.pop()
                        #action start
                        object.append_children( [ ",", expression2 ] ) 
                        #action end


                    else:
                        break #loop58
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:366:7: ( COMMA )?
                alt59 = 2
                LA59_0 = self.input.LA(1)

                if (LA59_0 == COMMA) :
                    alt59 = 1
                if alt59 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:366:9: COMMA
                    pass 
                    self.match(self.input, COMMA, self.FOLLOW_COMMA_in_expressionList2930)
                    #action start
                    object.append_child( "," ) 
                    #action end







            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "expressionList"


    # $ANTLR start "dictmaker"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:369:1: dictmaker returns [object] : constraint1= constraint COLON constraint2= constraint ( options {k=2; } : COMMA constraint3= constraint COLON constraint4= constraint )* ( COMMA )? ;
    def dictmaker(self, ):

        object = None

        constraint1 = None

        constraint2 = None

        constraint3 = None

        constraint4 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:370:3: (constraint1= constraint COLON constraint2= constraint ( options {k=2; } : COMMA constraint3= constraint COLON constraint4= constraint )* ( COMMA )? )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:370:5: constraint1= constraint COLON constraint2= constraint ( options {k=2; } : COMMA constraint3= constraint COLON constraint4= constraint )* ( COMMA )?
                pass 
                self._state.following.append(self.FOLLOW_constraint_in_dictmaker2955)
                constraint1 = self.constraint()

                self._state.following.pop()
                #action start
                object = DictMaker( constraint1 ) 
                #action end
                self.match(self.input, COLON, self.FOLLOW_COLON_in_dictmaker2965)
                self._state.following.append(self.FOLLOW_constraint_in_dictmaker2969)
                constraint2 = self.constraint()

                self._state.following.pop()
                #action start
                object.append_children( [":", constraint2] ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:372:9: ( options {k=2; } : COMMA constraint3= constraint COLON constraint4= constraint )*
                while True: #loop60
                    alt60 = 2
                    alt60 = self.dfa60.predict(self.input)
                    if alt60 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:372:26: COMMA constraint3= constraint COLON constraint4= constraint
                        pass 
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_dictmaker2990)
                        self._state.following.append(self.FOLLOW_constraint_in_dictmaker2994)
                        constraint3 = self.constraint()

                        self._state.following.pop()
                        self.match(self.input, COLON, self.FOLLOW_COLON_in_dictmaker2996)
                        self._state.following.append(self.FOLLOW_constraint_in_dictmaker3000)
                        constraint4 = self.constraint()

                        self._state.following.pop()
                        #action start
                        object.append_children( [",", constraint3, ":", constraint4] ) 
                        #action end


                    else:
                        break #loop60
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:373:9: ( COMMA )?
                alt61 = 2
                LA61_0 = self.input.LA(1)

                if (LA61_0 == COMMA) :
                    alt61 = 1
                if alt61 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:373:11: COMMA
                    pass 
                    self.match(self.input, COMMA, self.FOLLOW_COMMA_in_dictmaker3017)
                    #action start
                    object.append_child( "," ) 
                    #action end







            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "dictmaker"


    # $ANTLR start "argumentList"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:376:1: argumentList returns [object] : constraint1= constraint ( COMMA constraint2= constraint )* ( COMMA )? ;
    def argumentList(self, ):

        object = None

        constraint1 = None

        constraint2 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:377:3: (constraint1= constraint ( COMMA constraint2= constraint )* ( COMMA )? )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:377:5: constraint1= constraint ( COMMA constraint2= constraint )* ( COMMA )?
                pass 
                self._state.following.append(self.FOLLOW_constraint_in_argumentList3042)
                constraint1 = self.constraint()

                self._state.following.pop()
                #action start
                object = ArgumentList( constraint1 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:378:7: ( COMMA constraint2= constraint )*
                while True: #loop62
                    alt62 = 2
                    LA62_0 = self.input.LA(1)

                    if (LA62_0 == COMMA) :
                        LA62_1 = self.input.LA(2)

                        if ((NAME <= LA62_1 <= STRING) or LA62_1 == NOT or LA62_1 == OBJECTBINDING or LA62_1 == LPAREN or (PLUS <= LA62_1 <= MINUS) or LA62_1 == TILDE or LA62_1 == LBRACK or LA62_1 == LCURLY or (INT <= LA62_1 <= COMPLEX)) :
                            alt62 = 1




                    if alt62 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:378:9: COMMA constraint2= constraint
                        pass 
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_argumentList3054)
                        self._state.following.append(self.FOLLOW_constraint_in_argumentList3058)
                        constraint2 = self.constraint()

                        self._state.following.pop()
                        #action start
                        object.append_children( [",", constraint2] ) 
                        #action end


                    else:
                        break #loop62
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:379:7: ( COMMA )?
                alt63 = 2
                LA63_0 = self.input.LA(1)

                if (LA63_0 == COMMA) :
                    alt63 = 1
                if alt63 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:379:9: COMMA
                    pass 
                    self.match(self.input, COMMA, self.FOLLOW_COMMA_in_argumentList3073)
                    #action start
                    object.append_child( "," ) 
                    #action end







            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "argumentList"


    # Delegated rules


    # lookup tables for DFA #34

    DFA34_eot = DFA.unpack(
        u"\15\uffff"
        )

    DFA34_eof = DFA.unpack(
        u"\15\uffff"
        )

    DFA34_min = DFA.unpack(
        u"\1\16\11\uffff\1\11\2\uffff"
        )

    DFA34_max = DFA.unpack(
        u"\1\121\11\uffff\1\113\2\uffff"
        )

    DFA34_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\1\3\1\4\1\5\1\6\1\7\1\10\1\11\1\uffff\1\13\1\12"
        )

    DFA34_special = DFA.unpack(
        u"\15\uffff"
        )

            
    DFA34_transition = [
        DFA.unpack(u"\1\11\42\uffff\1\1\1\2\1\3\1\4\1\5\1\6\1\7\30\uffff"
        u"\1\10\1\12"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\2\14\3\uffff\1\13\1\uffff\1\14\1\uffff\1\14\51\uffff"
        u"\2\14\4\uffff\1\14\1\uffff\1\14\1\uffff\1\14\1\uffff\4\14"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #34

    class DFA34(DFA):
        pass


    # lookup tables for DFA #54

    DFA54_eot = DFA.unpack(
        u"\56\uffff"
        )

    DFA54_eof = DFA.unpack(
        u"\56\uffff"
        )

    DFA54_min = DFA.unpack(
        u"\2\6\54\uffff"
        )

    DFA54_max = DFA.unpack(
        u"\1\54\1\113\54\uffff"
        )

    DFA54_accept = DFA.unpack(
        u"\2\uffff\1\2\16\uffff\1\1\34\uffff"
        )

    DFA54_special = DFA.unpack(
        u"\56\uffff"
        )

            
    DFA54_transition = [
        DFA.unpack(u"\1\2\14\uffff\1\2\11\uffff\15\2\2\uffff\1\1"),
        DFA.unpack(u"\1\2\2\uffff\2\21\3\uffff\1\21\1\uffff\1\21\1\uffff"
        u"\1\21\1\2\11\uffff\15\2\22\uffff\2\21\4\uffff\1\21\1\uffff\1\21"
        u"\1\uffff\1\21\1\uffff\4\21"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #54

    class DFA54(DFA):
        pass


    # lookup tables for DFA #58

    DFA58_eot = DFA.unpack(
        u"\21\uffff"
        )

    DFA58_eof = DFA.unpack(
        u"\2\2\17\uffff"
        )

    DFA58_min = DFA.unpack(
        u"\1\54\1\11\17\uffff"
        )

    DFA58_max = DFA.unpack(
        u"\1\54\1\113\17\uffff"
        )

    DFA58_accept = DFA.unpack(
        u"\2\uffff\1\2\1\uffff\1\1\14\uffff"
        )

    DFA58_special = DFA.unpack(
        u"\21\uffff"
        )

            
    DFA58_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\2\4\5\uffff\1\4\1\uffff\1\4\51\uffff\2\4\4\uffff\1"
        u"\4\1\uffff\1\4\1\uffff\1\4\1\uffff\4\4"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #58

    class DFA58(DFA):
        pass


    # lookup tables for DFA #60

    DFA60_eot = DFA.unpack(
        u"\22\uffff"
        )

    DFA60_eof = DFA.unpack(
        u"\22\uffff"
        )

    DFA60_min = DFA.unpack(
        u"\1\54\1\11\20\uffff"
        )

    DFA60_max = DFA.unpack(
        u"\1\107\1\113\20\uffff"
        )

    DFA60_accept = DFA.unpack(
        u"\2\uffff\1\2\1\uffff\1\1\15\uffff"
        )

    DFA60_special = DFA.unpack(
        u"\22\uffff"
        )

            
    DFA60_transition = [
        DFA.unpack(u"\1\1\32\uffff\1\2"),
        DFA.unpack(u"\2\4\3\uffff\1\4\1\uffff\1\4\1\uffff\1\4\51\uffff\2"
        u"\4\4\uffff\1\4\1\uffff\1\4\1\uffff\1\4\1\2\4\4"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #60

    class DFA60(DFA):
        pass


 

    FOLLOW_NEWLINE_in_file78 = frozenset([1, 6, 7, 9, 10, 14, 16, 18, 42, 43, 60, 61, 66, 68, 70, 72, 73, 74, 75])
    FOLLOW_statement_in_file82 = frozenset([1, 6, 7, 9, 10, 14, 16, 18, 42, 43, 60, 61, 66, 68, 70, 72, 73, 74, 75])
    FOLLOW_EOF_in_file93 = frozenset([1])
    FOLLOW_importStmt_in_statement111 = frozenset([1])
    FOLLOW_attributeStmt_in_statement120 = frozenset([1])
    FOLLOW_ruleStmt_in_statement129 = frozenset([1])
    FOLLOW_expressionStmt_in_attributeStmt152 = frozenset([1])
    FOLLOW_RULE_in_ruleStmt172 = frozenset([9, 10])
    FOLLOW_id_in_ruleStmt174 = frozenset([8])
    FOLLOW_COLON_in_ruleStmt176 = frozenset([6])
    FOLLOW_NEWLINE_in_ruleStmt178 = frozenset([4])
    FOLLOW_INDENT_in_ruleStmt188 = frozenset([11, 12, 13])
    FOLLOW_ruleAttribute_in_ruleStmt192 = frozenset([11, 12, 13])
    FOLLOW_when_in_ruleStmt214 = frozenset([11, 12, 13])
    FOLLOW_then_in_ruleStmt234 = frozenset([5])
    FOLLOW_DEDENT_in_ruleStmt239 = frozenset([1])
    FOLLOW_NAME_in_id257 = frozenset([1])
    FOLLOW_STRING_in_id268 = frozenset([1])
    FOLLOW_agendaGroup_in_ruleAttribute289 = frozenset([1])
    FOLLOW_AGENDAGROUP_in_agendaGroup309 = frozenset([9, 10])
    FOLLOW_id_in_agendaGroup311 = frozenset([6])
    FOLLOW_NEWLINE_in_agendaGroup313 = frozenset([1])
    FOLLOW_WHEN_in_when333 = frozenset([8])
    FOLLOW_COLON_in_when335 = frozenset([6])
    FOLLOW_NEWLINE_in_when337 = frozenset([4])
    FOLLOW_INDENT_in_when347 = frozenset([5, 9, 14, 15, 16])
    FOLLOW_ruleCondition_in_when351 = frozenset([5])
    FOLLOW_DEDENT_in_when358 = frozenset([1])
    FOLLOW_THEN_in_then376 = frozenset([8])
    FOLLOW_COLON_in_then378 = frozenset([6])
    FOLLOW_NEWLINE_in_then380 = frozenset([4])
    FOLLOW_INDENT_in_then390 = frozenset([9, 10, 14, 16, 18, 20, 21, 23, 24, 25, 26, 27, 28, 60, 61, 66, 68, 70, 72, 73, 74, 75])
    FOLLOW_action_in_then394 = frozenset([5, 9, 10, 14, 16, 18, 20, 21, 23, 24, 25, 26, 27, 28, 60, 61, 66, 68, 70, 72, 73, 74, 75])
    FOLLOW_DEDENT_in_then401 = frozenset([1])
    FOLLOW_notCondition_in_ruleCondition419 = frozenset([6])
    FOLLOW_NEWLINE_in_ruleCondition421 = frozenset([1])
    FOLLOW_NOT_in_notCondition449 = frozenset([9, 14, 15, 16])
    FOLLOW_condition_in_notCondition456 = frozenset([1])
    FOLLOW_EXISTS_in_condition484 = frozenset([9, 14, 15, 16])
    FOLLOW_classConstraint_in_condition491 = frozenset([1])
    FOLLOW_OBJECTBINDING_in_classConstraint519 = frozenset([17])
    FOLLOW_ASSIGNEQUAL_in_classConstraint521 = frozenset([9])
    FOLLOW_NAME_in_classConstraint534 = frozenset([18])
    FOLLOW_LPAREN_in_classConstraint536 = frozenset([9, 10, 14, 16, 18, 19, 60, 61, 66, 68, 70, 72, 73, 74, 75])
    FOLLOW_constraint_in_classConstraint542 = frozenset([19])
    FOLLOW_RPAREN_in_classConstraint549 = frozenset([1])
    FOLLOW_simpleStmt_in_action569 = frozenset([1])
    FOLLOW_attributeAction_in_action583 = frozenset([1])
    FOLLOW_learnAction_in_action592 = frozenset([1])
    FOLLOW_forgetAction_in_action604 = frozenset([1])
    FOLLOW_modifyAction_in_action616 = frozenset([1])
    FOLLOW_haltAction_in_action628 = frozenset([1])
    FOLLOW_expressionStmt_in_simpleStmt654 = frozenset([1])
    FOLLOW_printStmt_in_simpleStmt668 = frozenset([1])
    FOLLOW_ATTRIBUTE_in_attributeAction699 = frozenset([9, 10, 14, 16, 18, 60, 61, 66, 68, 70, 72, 73, 74, 75])
    FOLLOW_expressionStmt_in_attributeAction701 = frozenset([1])
    FOLLOW_PRINT_in_printStmt721 = frozenset([6, 9, 10, 14, 16, 18, 22, 60, 61, 66, 68, 70, 72, 73, 74, 75])
    FOLLOW_comparisonList_in_printStmt735 = frozenset([6])
    FOLLOW_RIGHTSHIFT_in_printStmt747 = frozenset([9, 10, 14, 16, 18, 60, 61, 66, 68, 70, 72, 73, 74, 75])
    FOLLOW_comparisonList_in_printStmt751 = frozenset([6])
    FOLLOW_NEWLINE_in_printStmt758 = frozenset([1])
    FOLLOW_FORGET_in_forgetAction778 = frozenset([16])
    FOLLOW_DELETE_in_forgetAction790 = frozenset([16])
    FOLLOW_OBJECTBINDING_in_forgetAction803 = frozenset([6])
    FOLLOW_NEWLINE_in_forgetAction807 = frozenset([1])
    FOLLOW_LEARN_in_learnAction827 = frozenset([9])
    FOLLOW_INSERT_in_learnAction839 = frozenset([9])
    FOLLOW_NAME_in_learnAction854 = frozenset([18])
    FOLLOW_LPAREN_in_learnAction856 = frozenset([9, 10, 14, 16, 18, 19, 60, 61, 66, 68, 70, 72, 73, 74, 75])
    FOLLOW_argumentList_in_learnAction870 = frozenset([19])
    FOLLOW_RPAREN_in_learnAction877 = frozenset([6])
    FOLLOW_NEWLINE_in_learnAction881 = frozenset([1])
    FOLLOW_MODIFY_in_modifyAction899 = frozenset([16])
    FOLLOW_OBJECTBINDING_in_modifyAction901 = frozenset([8])
    FOLLOW_COLON_in_modifyAction903 = frozenset([6])
    FOLLOW_NEWLINE_in_modifyAction905 = frozenset([4])
    FOLLOW_INDENT_in_modifyAction915 = frozenset([9])
    FOLLOW_propertyAssignment_in_modifyAction919 = frozenset([5, 9])
    FOLLOW_DEDENT_in_modifyAction926 = frozenset([1])
    FOLLOW_HALT_in_haltAction944 = frozenset([6])
    FOLLOW_NEWLINE_in_haltAction948 = frozenset([1])
    FOLLOW_NAME_in_propertyAssignment966 = frozenset([29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41])
    FOLLOW_assignment_in_propertyAssignment968 = frozenset([9, 10, 14, 16, 18, 60, 61, 66, 68, 70, 72, 73, 74, 75])
    FOLLOW_constraint_in_propertyAssignment970 = frozenset([6])
    FOLLOW_NEWLINE_in_propertyAssignment974 = frozenset([1])
    FOLLOW_comparisonList_in_expressionStmt994 = frozenset([6, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41])
    FOLLOW_assignment_in_expressionStmt1006 = frozenset([9, 10, 14, 16, 18, 60, 61, 66, 68, 70, 72, 73, 74, 75])
    FOLLOW_comparisonList_in_expressionStmt1010 = frozenset([6])
    FOLLOW_NEWLINE_in_expressionStmt1017 = frozenset([1])
    FOLLOW_ASSIGN_in_assignment1035 = frozenset([1])
    FOLLOW_PLUSEQUAL_in_assignment1054 = frozenset([1])
    FOLLOW_MINUSEQUAL_in_assignment1070 = frozenset([1])
    FOLLOW_STAREQUAL_in_assignment1085 = frozenset([1])
    FOLLOW_SLASHEQUAL_in_assignment1101 = frozenset([1])
    FOLLOW_PERCENTEQUAL_in_assignment1116 = frozenset([1])
    FOLLOW_AMPEREQUAL_in_assignment1129 = frozenset([1])
    FOLLOW_VBAREQUAL_in_assignment1144 = frozenset([1])
    FOLLOW_CIRCUMFLEXEQUAL_in_assignment1160 = frozenset([1])
    FOLLOW_LEFTSHIFTEQUAL_in_assignment1170 = frozenset([1])
    FOLLOW_RIGHTSHIFTEQUAL_in_assignment1181 = frozenset([1])
    FOLLOW_DOUBLESTAREQUAL_in_assignment1191 = frozenset([1])
    FOLLOW_DOUBLESLASHEQUAL_in_assignment1201 = frozenset([1])
    FOLLOW_importName_in_importStmt1222 = frozenset([1])
    FOLLOW_importFrom_in_importStmt1230 = frozenset([1])
    FOLLOW_IMPORT_in_importName1250 = frozenset([9])
    FOLLOW_dottedAsNames_in_importName1252 = frozenset([6])
    FOLLOW_NEWLINE_in_importName1256 = frozenset([1])
    FOLLOW_FROM_in_importFrom1274 = frozenset([9])
    FOLLOW_dottedName_in_importFrom1278 = frozenset([42])
    FOLLOW_IMPORT_in_importFrom1282 = frozenset([9, 18])
    FOLLOW_importAsNames_in_importFrom1296 = frozenset([6])
    FOLLOW_LPAREN_in_importFrom1308 = frozenset([9])
    FOLLOW_importAsNames_in_importFrom1313 = frozenset([19])
    FOLLOW_RPAREN_in_importFrom1315 = frozenset([6])
    FOLLOW_NEWLINE_in_importFrom1327 = frozenset([1])
    FOLLOW_importAsName_in_importAsNames1346 = frozenset([1, 44])
    FOLLOW_COMMA_in_importAsNames1358 = frozenset([9])
    FOLLOW_importAsName_in_importAsNames1362 = frozenset([1, 44])
    FOLLOW_COMMA_in_importAsNames1371 = frozenset([1])
    FOLLOW_NAME_in_importAsName1395 = frozenset([1, 45])
    FOLLOW_AS_in_importAsName1400 = frozenset([9])
    FOLLOW_NAME_in_importAsName1404 = frozenset([1])
    FOLLOW_dottedAsName_in_dottedAsNames1428 = frozenset([1, 44])
    FOLLOW_COMMA_in_dottedAsNames1439 = frozenset([9])
    FOLLOW_dottedAsName_in_dottedAsNames1443 = frozenset([1, 44])
    FOLLOW_dottedName_in_dottedAsName1465 = frozenset([1, 45])
    FOLLOW_AS_in_dottedAsName1471 = frozenset([9])
    FOLLOW_NAME_in_dottedAsName1473 = frozenset([1])
    FOLLOW_NAME_in_dottedName1498 = frozenset([1, 46])
    FOLLOW_DOT_in_dottedName1510 = frozenset([9])
    FOLLOW_NAME_in_dottedName1514 = frozenset([1, 46])
    FOLLOW_orConstraint_in_constraint1537 = frozenset([1])
    FOLLOW_andConstraint_in_orConstraint1559 = frozenset([1, 47])
    FOLLOW_OR_in_orConstraint1571 = frozenset([9, 10, 14, 16, 18, 60, 61, 66, 68, 70, 72, 73, 74, 75])
    FOLLOW_andConstraint_in_orConstraint1575 = frozenset([1, 47])
    FOLLOW_notConstraint_in_andConstraint1600 = frozenset([1, 48])
    FOLLOW_AND_in_andConstraint1612 = frozenset([9, 10, 14, 16, 18, 60, 61, 66, 68, 70, 72, 73, 74, 75])
    FOLLOW_notConstraint_in_andConstraint1616 = frozenset([1, 48])
    FOLLOW_NOT_in_notConstraint1647 = frozenset([9, 10, 14, 16, 18, 60, 61, 66, 68, 70, 72, 73, 74, 75])
    FOLLOW_comparison_in_notConstraint1654 = frozenset([1])
    FOLLOW_expression_in_comparison1676 = frozenset([1, 14, 49, 50, 51, 52, 53, 54, 55, 80, 81])
    FOLLOW_comparisonOperation_in_comparison1686 = frozenset([9, 10, 14, 16, 18, 60, 61, 66, 68, 70, 72, 73, 74, 75])
    FOLLOW_expression_in_comparison1690 = frozenset([1, 14, 49, 50, 51, 52, 53, 54, 55, 80, 81])
    FOLLOW_LESS_in_comparisonOperation1715 = frozenset([1])
    FOLLOW_GREATER_in_comparisonOperation1734 = frozenset([1])
    FOLLOW_EQUAL_in_comparisonOperation1750 = frozenset([1])
    FOLLOW_GREATEREQUAL_in_comparisonOperation1768 = frozenset([1])
    FOLLOW_LESSEQUAL_in_comparisonOperation1779 = frozenset([1])
    FOLLOW_ALT_NOTEQUAL_in_comparisonOperation1793 = frozenset([1])
    FOLLOW_NOTEQUAL_in_comparisonOperation1804 = frozenset([1])
    FOLLOW_IN_in_comparisonOperation1819 = frozenset([1])
    FOLLOW_NOT_in_comparisonOperation1838 = frozenset([80])
    FOLLOW_IN_in_comparisonOperation1840 = frozenset([1])
    FOLLOW_IS_in_comparisonOperation1853 = frozenset([1])
    FOLLOW_IS_in_comparisonOperation1872 = frozenset([14])
    FOLLOW_NOT_in_comparisonOperation1874 = frozenset([1])
    FOLLOW_bitwiseOrExpr_in_expression1899 = frozenset([1])
    FOLLOW_bitwiseXorExpr_in_bitwiseOrExpr1921 = frozenset([1, 56])
    FOLLOW_VBAR_in_bitwiseOrExpr1933 = frozenset([9, 10, 14, 16, 18, 60, 61, 66, 68, 70, 72, 73, 74, 75])
    FOLLOW_bitwiseXorExpr_in_bitwiseOrExpr1937 = frozenset([1, 56])
    FOLLOW_bitwiseAndExpr_in_bitwiseXorExpr1962 = frozenset([1, 57])
    FOLLOW_CIRCUMFLEX_in_bitwiseXorExpr1974 = frozenset([9, 10, 14, 16, 18, 60, 61, 66, 68, 70, 72, 73, 74, 75])
    FOLLOW_bitwiseAndExpr_in_bitwiseXorExpr1978 = frozenset([1, 57])
    FOLLOW_shiftExpr_in_bitwiseAndExpr2003 = frozenset([1, 58])
    FOLLOW_AMPER_in_bitwiseAndExpr2015 = frozenset([9, 10, 14, 16, 18, 60, 61, 66, 68, 70, 72, 73, 74, 75])
    FOLLOW_shiftExpr_in_bitwiseAndExpr2019 = frozenset([1, 58])
    FOLLOW_arithExpr_in_shiftExpr2044 = frozenset([1, 22, 59])
    FOLLOW_LEFTSHIFT_in_shiftExpr2058 = frozenset([9, 10, 14, 16, 18, 60, 61, 66, 68, 70, 72, 73, 74, 75])
    FOLLOW_RIGHTSHIFT_in_shiftExpr2064 = frozenset([9, 10, 14, 16, 18, 60, 61, 66, 68, 70, 72, 73, 74, 75])
    FOLLOW_arithExpr_in_shiftExpr2082 = frozenset([1, 22, 59])
    FOLLOW_term_in_arithExpr2107 = frozenset([1, 60, 61])
    FOLLOW_PLUS_in_arithExpr2121 = frozenset([9, 10, 14, 16, 18, 60, 61, 66, 68, 70, 72, 73, 74, 75])
    FOLLOW_MINUS_in_arithExpr2127 = frozenset([9, 10, 14, 16, 18, 60, 61, 66, 68, 70, 72, 73, 74, 75])
    FOLLOW_term_in_arithExpr2145 = frozenset([1, 60, 61])
    FOLLOW_factor_in_term2170 = frozenset([1, 62, 63, 64, 65])
    FOLLOW_STAR_in_term2183 = frozenset([9, 10, 14, 16, 18, 60, 61, 66, 68, 70, 72, 73, 74, 75])
    FOLLOW_SLASH_in_term2189 = frozenset([9, 10, 14, 16, 18, 60, 61, 66, 68, 70, 72, 73, 74, 75])
    FOLLOW_PERCENT_in_term2205 = frozenset([9, 10, 14, 16, 18, 60, 61, 66, 68, 70, 72, 73, 74, 75])
    FOLLOW_DOUBLESLASH_in_term2211 = frozenset([9, 10, 14, 16, 18, 60, 61, 66, 68, 70, 72, 73, 74, 75])
    FOLLOW_factor_in_term2233 = frozenset([1, 62, 63, 64, 65])
    FOLLOW_PLUS_in_factor2256 = frozenset([9, 10, 14, 16, 18, 60, 61, 66, 68, 70, 72, 73, 74, 75])
    FOLLOW_factor_in_factor2261 = frozenset([1])
    FOLLOW_MINUS_in_factor2269 = frozenset([9, 10, 14, 16, 18, 60, 61, 66, 68, 70, 72, 73, 74, 75])
    FOLLOW_factor_in_factor2273 = frozenset([1])
    FOLLOW_TILDE_in_factor2281 = frozenset([9, 10, 14, 16, 18, 60, 61, 66, 68, 70, 72, 73, 74, 75])
    FOLLOW_factor_in_factor2285 = frozenset([1])
    FOLLOW_power_in_factor2293 = frozenset([1])
    FOLLOW_atom_in_power2313 = frozenset([1, 18, 46, 67])
    FOLLOW_trailer_in_power2325 = frozenset([1, 18, 46, 67])
    FOLLOW_DOUBLESTAR_in_power2346 = frozenset([9, 10, 14, 16, 18, 60, 61, 66, 68, 70, 72, 73, 74, 75])
    FOLLOW_factor_in_power2348 = frozenset([1])
    FOLLOW_LPAREN_in_atom2371 = frozenset([9, 10, 14, 16, 18, 19, 60, 61, 66, 68, 70, 72, 73, 74, 75])
    FOLLOW_comparisonList_in_atom2410 = frozenset([19])
    FOLLOW_RPAREN_in_atom2439 = frozenset([1])
    FOLLOW_LBRACK_in_atom2447 = frozenset([9, 10, 14, 16, 18, 60, 61, 66, 68, 69, 70, 72, 73, 74, 75])
    FOLLOW_listmaker_in_atom2484 = frozenset([69])
    FOLLOW_RBRACK_in_atom2513 = frozenset([1])
    FOLLOW_LCURLY_in_atom2521 = frozenset([9, 10, 14, 16, 18, 60, 61, 66, 68, 70, 71, 72, 73, 74, 75])
    FOLLOW_dictmaker_in_atom2558 = frozenset([71])
    FOLLOW_RCURLY_in_atom2587 = frozenset([1])
    FOLLOW_NAME_in_atom2596 = frozenset([1])
    FOLLOW_OBJECTBINDING_in_atom2615 = frozenset([1])
    FOLLOW_INT_in_atom2625 = frozenset([1])
    FOLLOW_LONGINT_in_atom2645 = frozenset([1])
    FOLLOW_FLOAT_in_atom2661 = frozenset([1])
    FOLLOW_COMPLEX_in_atom2679 = frozenset([1])
    FOLLOW_STRING_in_atom2699 = frozenset([1, 10])
    FOLLOW_constraint_in_listmaker2724 = frozenset([1, 44])
    FOLLOW_COMMA_in_listmaker2742 = frozenset([9, 10, 14, 16, 18, 60, 61, 66, 68, 70, 72, 73, 74, 75])
    FOLLOW_constraint_in_listmaker2746 = frozenset([1, 44])
    FOLLOW_COMMA_in_listmaker2761 = frozenset([1])
    FOLLOW_constraint_in_comparisonList2786 = frozenset([1, 44])
    FOLLOW_COMMA_in_comparisonList2804 = frozenset([9, 10, 14, 16, 18, 60, 61, 66, 68, 70, 72, 73, 74, 75])
    FOLLOW_constraint_in_comparisonList2808 = frozenset([1, 44])
    FOLLOW_COMMA_in_comparisonList2823 = frozenset([1])
    FOLLOW_LPAREN_in_trailer2846 = frozenset([9, 10, 14, 16, 18, 19, 60, 61, 66, 68, 70, 72, 73, 74, 75])
    FOLLOW_argumentList_in_trailer2851 = frozenset([19])
    FOLLOW_RPAREN_in_trailer2858 = frozenset([1])
    FOLLOW_DOT_in_trailer2866 = frozenset([9])
    FOLLOW_NAME_in_trailer2868 = frozenset([1])
    FOLLOW_expression_in_expressionList2891 = frozenset([1, 44])
    FOLLOW_COMMA_in_expressionList2911 = frozenset([9, 10, 14, 16, 18, 60, 61, 66, 68, 70, 72, 73, 74, 75])
    FOLLOW_expression_in_expressionList2915 = frozenset([1, 44])
    FOLLOW_COMMA_in_expressionList2930 = frozenset([1])
    FOLLOW_constraint_in_dictmaker2955 = frozenset([8])
    FOLLOW_COLON_in_dictmaker2965 = frozenset([9, 10, 14, 16, 18, 60, 61, 66, 68, 70, 72, 73, 74, 75])
    FOLLOW_constraint_in_dictmaker2969 = frozenset([1, 44])
    FOLLOW_COMMA_in_dictmaker2990 = frozenset([9, 10, 14, 16, 18, 60, 61, 66, 68, 70, 72, 73, 74, 75])
    FOLLOW_constraint_in_dictmaker2994 = frozenset([8])
    FOLLOW_COLON_in_dictmaker2996 = frozenset([9, 10, 14, 16, 18, 60, 61, 66, 68, 70, 72, 73, 74, 75])
    FOLLOW_constraint_in_dictmaker3000 = frozenset([1, 44])
    FOLLOW_COMMA_in_dictmaker3017 = frozenset([1])
    FOLLOW_constraint_in_argumentList3042 = frozenset([1, 44])
    FOLLOW_COMMA_in_argumentList3054 = frozenset([9, 10, 14, 16, 18, 60, 61, 66, 68, 70, 72, 73, 74, 75])
    FOLLOW_constraint_in_argumentList3058 = frozenset([1, 44])
    FOLLOW_COMMA_in_argumentList3073 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("PolicyLexer", PolicyParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
