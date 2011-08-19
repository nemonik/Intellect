# $ANTLR 3.1.3 Mar 17, 2009 19:23:44 /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g 2011-08-18 14:48:17

import sys
from antlr3 import *
from antlr3.compat import set, frozenset
         
from intellect.Node import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
DOLLAR=75
DOUBLESLASH=63
MODIFY=24
EXPONENT=82
BACKQUOTE=76
SLASHEQUAL=31
CONTINUED_LINE=86
LBRACK=66
STAR=60
CIRCUMFLEXEQUAL=35
DOUBLESTAR=65
OBJECTBINDING=16
HALT=26
LETTER=80
ESC=85
TRIAPOS=83
ATTRIBUTE=25
GREATEREQUAL=50
COMPLEX=73
FLOAT=72
DEDENT=5
ASSIGNEQUAL=17
NOT=14
AND=46
RIGHTSHIFTEQUAL=37
EOF=-1
LPAREN=18
INDENT=4
PLUSEQUAL=28
LEADING_WS=88
NOTEQUAL=53
VBAR=54
MINUSEQUAL=29
AS=43
RPAREN=19
NAME=9
IMPORT=40
SLASH=61
GREATER=48
IN=78
THEN=13
INSERT=23
COMMA=42
IS=79
AMPER=56
EQUAL=49
DOUBLESTAREQUAL=38
TILDE=64
LESS=47
LEFTSHIFTEQUAL=36
PLUS=58
LEFTSHIFT=57
DIGIT=81
EXISTS=15
COMMENT=89
DOT=44
AGENDAGROUP=11
RBRACK=67
PERCENT=62
RULE=7
LCURLY=68
INT=70
DELETE=22
MINUS=59
RIGHTSHIFT=21
SEMI=74
PRINT=20
TRIQUOTE=84
COLON=8
DOUBLESLASHEQUAL=39
WS=87
NEWLINE=6
AMPEREQUAL=33
WHEN=12
VBAREQUAL=34
RCURLY=69
OR=45
ASSIGN=27
LONGINT=71
GLOBAL=77
FROM=41
LESSEQUAL=51
PERCENTEQUAL=32
STAREQUAL=30
CIRCUMFLEX=55
STRING=10
ALT_NOTEQUAL=52

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "INDENT", "DEDENT", "NEWLINE", "RULE", "COLON", "NAME", "STRING", "AGENDAGROUP", 
    "WHEN", "THEN", "NOT", "EXISTS", "OBJECTBINDING", "ASSIGNEQUAL", "LPAREN", 
    "RPAREN", "PRINT", "RIGHTSHIFT", "DELETE", "INSERT", "MODIFY", "ATTRIBUTE", 
    "HALT", "ASSIGN", "PLUSEQUAL", "MINUSEQUAL", "STAREQUAL", "SLASHEQUAL", 
    "PERCENTEQUAL", "AMPEREQUAL", "VBAREQUAL", "CIRCUMFLEXEQUAL", "LEFTSHIFTEQUAL", 
    "RIGHTSHIFTEQUAL", "DOUBLESTAREQUAL", "DOUBLESLASHEQUAL", "IMPORT", 
    "FROM", "COMMA", "AS", "DOT", "OR", "AND", "LESS", "GREATER", "EQUAL", 
    "GREATEREQUAL", "LESSEQUAL", "ALT_NOTEQUAL", "NOTEQUAL", "VBAR", "CIRCUMFLEX", 
    "AMPER", "LEFTSHIFT", "PLUS", "MINUS", "STAR", "SLASH", "PERCENT", "DOUBLESLASH", 
    "TILDE", "DOUBLESTAR", "LBRACK", "RBRACK", "LCURLY", "RCURLY", "INT", 
    "LONGINT", "FLOAT", "COMPLEX", "SEMI", "DOLLAR", "BACKQUOTE", "GLOBAL", 
    "IN", "IS", "LETTER", "DIGIT", "EXPONENT", "TRIAPOS", "TRIQUOTE", "ESC", 
    "CONTINUED_LINE", "WS", "LEADING_WS", "COMMENT"
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

        self.dfa32 = self.DFA32(
            self, 32,
            eot = self.DFA32_eot,
            eof = self.DFA32_eof,
            min = self.DFA32_min,
            max = self.DFA32_max,
            accept = self.DFA32_accept,
            special = self.DFA32_special,
            transition = self.DFA32_transition
            )

        self.dfa52 = self.DFA52(
            self, 52,
            eot = self.DFA52_eot,
            eof = self.DFA52_eof,
            min = self.DFA52_min,
            max = self.DFA52_max,
            accept = self.DFA52_accept,
            special = self.DFA52_special,
            transition = self.DFA52_transition
            )

        self.dfa56 = self.DFA56(
            self, 56,
            eot = self.DFA56_eot,
            eof = self.DFA56_eof,
            min = self.DFA56_min,
            max = self.DFA56_max,
            accept = self.DFA56_accept,
            special = self.DFA56_special,
            transition = self.DFA56_transition
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

                    if ((NAME <= LA8_0 <= STRING) or LA8_0 == NOT or LA8_0 == OBJECTBINDING or LA8_0 == LPAREN or LA8_0 == PRINT or (DELETE <= LA8_0 <= HALT) or (PLUS <= LA8_0 <= MINUS) or LA8_0 == TILDE or LA8_0 == LBRACK or LA8_0 == LCURLY or (INT <= LA8_0 <= COMPLEX)) :
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
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:127:1: action returns [object] : ( attributeAction | deleteAction | insertAction | modifyAction | haltAction | simpleStmt );
    def action(self, ):

        object = None

        attributeAction34 = None

        deleteAction35 = None

        insertAction36 = None

        modifyAction37 = None

        haltAction38 = None

        simpleStmt39 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:128:3: ( attributeAction | deleteAction | insertAction | modifyAction | haltAction | simpleStmt )
                alt13 = 6
                LA13 = self.input.LA(1)
                if LA13 == ATTRIBUTE:
                    alt13 = 1
                elif LA13 == DELETE:
                    alt13 = 2
                elif LA13 == INSERT:
                    alt13 = 3
                elif LA13 == MODIFY:
                    alt13 = 4
                elif LA13 == HALT:
                    alt13 = 5
                elif LA13 == NAME or LA13 == STRING or LA13 == NOT or LA13 == OBJECTBINDING or LA13 == LPAREN or LA13 == PRINT or LA13 == PLUS or LA13 == MINUS or LA13 == TILDE or LA13 == LBRACK or LA13 == LCURLY or LA13 == INT or LA13 == LONGINT or LA13 == FLOAT or LA13 == COMPLEX:
                    alt13 = 6
                else:
                    nvae = NoViableAltException("", 13, 0, self.input)

                    raise nvae

                if alt13 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:128:5: attributeAction
                    pass 
                    self._state.following.append(self.FOLLOW_attributeAction_in_action569)
                    attributeAction34 = self.attributeAction()

                    self._state.following.pop()
                    #action start
                    object = Action( attributeAction34, attributeAction34.line, attributeAction34.column ) 
                    #action end


                elif alt13 == 2:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:129:5: deleteAction
                    pass 
                    self._state.following.append(self.FOLLOW_deleteAction_in_action578)
                    deleteAction35 = self.deleteAction()

                    self._state.following.pop()
                    #action start
                    object = Action( deleteAction35, deleteAction35.line, deleteAction35.column ) 
                    #action end


                elif alt13 == 3:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:130:5: insertAction
                    pass 
                    self._state.following.append(self.FOLLOW_insertAction_in_action590)
                    insertAction36 = self.insertAction()

                    self._state.following.pop()
                    #action start
                    object = Action( insertAction36, insertAction36.line, insertAction36.column ) 
                    #action end


                elif alt13 == 4:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:131:5: modifyAction
                    pass 
                    self._state.following.append(self.FOLLOW_modifyAction_in_action602)
                    modifyAction37 = self.modifyAction()

                    self._state.following.pop()
                    #action start
                    object = Action( modifyAction37, modifyAction37.line, modifyAction37.column ) 
                    #action end


                elif alt13 == 5:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:132:5: haltAction
                    pass 
                    self._state.following.append(self.FOLLOW_haltAction_in_action614)
                    haltAction38 = self.haltAction()

                    self._state.following.pop()
                    #action start
                    object = Action( haltAction38, haltAction38.line, haltAction38.column ) 
                    #action end


                elif alt13 == 6:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:133:5: simpleStmt
                    pass 
                    self._state.following.append(self.FOLLOW_simpleStmt_in_action628)
                    simpleStmt39 = self.simpleStmt()

                    self._state.following.pop()
                    #action start
                    object = Action( simpleStmt39, simpleStmt39.line, simpleStmt39.column ) 
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


    # $ANTLR start "printStmt"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:141:1: printStmt returns [object] : PRINT (comparisonList1= comparisonList | RIGHTSHIFT comparisonList2= comparisonList )? NEWLINE ;
    def printStmt(self, ):

        object = None

        PRINT42 = None
        RIGHTSHIFT43 = None
        comparisonList1 = None

        comparisonList2 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:142:3: ( PRINT (comparisonList1= comparisonList | RIGHTSHIFT comparisonList2= comparisonList )? NEWLINE )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:142:5: PRINT (comparisonList1= comparisonList | RIGHTSHIFT comparisonList2= comparisonList )? NEWLINE
                pass 
                PRINT42=self.match(self.input, PRINT, self.FOLLOW_PRINT_in_printStmt699)
                #action start
                object = PrintStmt( PRINT42.text, PRINT42.getLine(), PRINT42.getCharPositionInLine() ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:143:7: (comparisonList1= comparisonList | RIGHTSHIFT comparisonList2= comparisonList )?
                alt15 = 3
                LA15_0 = self.input.LA(1)

                if ((NAME <= LA15_0 <= STRING) or LA15_0 == NOT or LA15_0 == OBJECTBINDING or LA15_0 == LPAREN or (PLUS <= LA15_0 <= MINUS) or LA15_0 == TILDE or LA15_0 == LBRACK or LA15_0 == LCURLY or (INT <= LA15_0 <= COMPLEX)) :
                    alt15 = 1
                elif (LA15_0 == RIGHTSHIFT) :
                    alt15 = 2
                if alt15 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:143:9: comparisonList1= comparisonList
                    pass 
                    self._state.following.append(self.FOLLOW_comparisonList_in_printStmt713)
                    comparisonList1 = self.comparisonList()

                    self._state.following.pop()
                    #action start
                    object.append_child( comparisonList1 ) 
                    #action end


                elif alt15 == 2:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:144:9: RIGHTSHIFT comparisonList2= comparisonList
                    pass 
                    RIGHTSHIFT43=self.match(self.input, RIGHTSHIFT, self.FOLLOW_RIGHTSHIFT_in_printStmt725)
                    self._state.following.append(self.FOLLOW_comparisonList_in_printStmt729)
                    comparisonList2 = self.comparisonList()

                    self._state.following.pop()
                    #action start
                    object.append_children( [RIGHTSHIFT43.text, comparisonList2] ) 
                    #action end



                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_printStmt736)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "printStmt"


    # $ANTLR start "deleteAction"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:147:1: deleteAction returns [object] : DELETE OBJECTBINDING NEWLINE ;
    def deleteAction(self, ):

        object = None

        DELETE44 = None
        OBJECTBINDING45 = None

        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:148:3: ( DELETE OBJECTBINDING NEWLINE )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:148:5: DELETE OBJECTBINDING NEWLINE
                pass 
                DELETE44=self.match(self.input, DELETE, self.FOLLOW_DELETE_in_deleteAction754)
                OBJECTBINDING45=self.match(self.input, OBJECTBINDING, self.FOLLOW_OBJECTBINDING_in_deleteAction756)
                #action start
                object = DeleteAction( [DELETE44.text, OBJECTBINDING45.text], DELETE44.getLine(), DELETE44.getCharPositionInLine() ) 
                #action end
                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_deleteAction760)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "deleteAction"


    # $ANTLR start "insertAction"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:151:1: insertAction returns [object] : INSERT NAME LPAREN ( argumentList )? RPAREN NEWLINE ;
    def insertAction(self, ):

        object = None

        INSERT46 = None
        NAME47 = None
        LPAREN48 = None
        RPAREN50 = None
        argumentList49 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:152:3: ( INSERT NAME LPAREN ( argumentList )? RPAREN NEWLINE )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:152:5: INSERT NAME LPAREN ( argumentList )? RPAREN NEWLINE
                pass 
                INSERT46=self.match(self.input, INSERT, self.FOLLOW_INSERT_in_insertAction778)
                NAME47=self.match(self.input, NAME, self.FOLLOW_NAME_in_insertAction780)
                LPAREN48=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_insertAction782)
                #action start
                object = InsertAction( [INSERT46.text, NAME47.text, LPAREN48.text], INSERT46.getLine(), INSERT46.getCharPositionInLine() ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:153:7: ( argumentList )?
                alt16 = 2
                LA16_0 = self.input.LA(1)

                if ((NAME <= LA16_0 <= STRING) or LA16_0 == NOT or LA16_0 == OBJECTBINDING or LA16_0 == LPAREN or (PLUS <= LA16_0 <= MINUS) or LA16_0 == TILDE or LA16_0 == LBRACK or LA16_0 == LCURLY or (INT <= LA16_0 <= COMPLEX)) :
                    alt16 = 1
                if alt16 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:153:9: argumentList
                    pass 
                    self._state.following.append(self.FOLLOW_argumentList_in_insertAction794)
                    argumentList49 = self.argumentList()

                    self._state.following.pop()
                    #action start
                    object.append_child( argumentList49 ) 
                    #action end



                RPAREN50=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_insertAction801)
                #action start
                object.append_child( RPAREN50.text ) 
                #action end
                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_insertAction805)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "insertAction"


    # $ANTLR start "modifyAction"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:156:1: modifyAction returns [object] : MODIFY OBJECTBINDING COLON NEWLINE INDENT ( propertyAssignment )+ DEDENT ;
    def modifyAction(self, ):

        object = None

        MODIFY51 = None
        OBJECTBINDING52 = None
        COLON53 = None
        propertyAssignment54 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:157:3: ( MODIFY OBJECTBINDING COLON NEWLINE INDENT ( propertyAssignment )+ DEDENT )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:157:5: MODIFY OBJECTBINDING COLON NEWLINE INDENT ( propertyAssignment )+ DEDENT
                pass 
                MODIFY51=self.match(self.input, MODIFY, self.FOLLOW_MODIFY_in_modifyAction823)
                OBJECTBINDING52=self.match(self.input, OBJECTBINDING, self.FOLLOW_OBJECTBINDING_in_modifyAction825)
                COLON53=self.match(self.input, COLON, self.FOLLOW_COLON_in_modifyAction827)
                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_modifyAction829)
                #action start
                object = ModifyAction( [MODIFY51.text, OBJECTBINDING52.text, COLON53.text], MODIFY51.getLine(), MODIFY51.getCharPositionInLine() ) 
                #action end
                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_modifyAction839)
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:158:14: ( propertyAssignment )+
                cnt17 = 0
                while True: #loop17
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if (LA17_0 == NAME) :
                        alt17 = 1


                    if alt17 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:158:16: propertyAssignment
                        pass 
                        self._state.following.append(self.FOLLOW_propertyAssignment_in_modifyAction843)
                        propertyAssignment54 = self.propertyAssignment()

                        self._state.following.pop()
                        #action start
                        object.append_child( propertyAssignment54 ) 
                        #action end


                    else:
                        if cnt17 >= 1:
                            break #loop17

                        eee = EarlyExitException(17, self.input)
                        raise eee

                    cnt17 += 1
                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_modifyAction850)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "modifyAction"


    # $ANTLR start "attributeAction"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:161:1: attributeAction returns [object] : ATTRIBUTE expressionStmt ;
    def attributeAction(self, ):

        object = None

        ATTRIBUTE55 = None
        expressionStmt56 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:162:3: ( ATTRIBUTE expressionStmt )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:162:5: ATTRIBUTE expressionStmt
                pass 
                ATTRIBUTE55=self.match(self.input, ATTRIBUTE, self.FOLLOW_ATTRIBUTE_in_attributeAction868)
                self._state.following.append(self.FOLLOW_expressionStmt_in_attributeAction870)
                expressionStmt56 = self.expressionStmt()

                self._state.following.pop()
                #action start
                object = AttributeAction( [ ATTRIBUTE55.text, expressionStmt56 ] , ATTRIBUTE55.getLine(), ATTRIBUTE55.getCharPositionInLine() ) 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "attributeAction"


    # $ANTLR start "haltAction"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:165:1: haltAction returns [object] : HALT NEWLINE ;
    def haltAction(self, ):

        object = None

        HALT57 = None

        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:166:3: ( HALT NEWLINE )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:166:5: HALT NEWLINE
                pass 
                HALT57=self.match(self.input, HALT, self.FOLLOW_HALT_in_haltAction890)
                #action start
                object = HaltAction( HALT57.text, HALT57.getLine(), HALT57.getCharPositionInLine() ) 
                #action end
                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_haltAction894)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "haltAction"


    # $ANTLR start "propertyAssignment"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:169:1: propertyAssignment returns [object] : NAME assignment constraint NEWLINE ;
    def propertyAssignment(self, ):

        object = None

        NAME58 = None
        assignment59 = None

        constraint60 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:170:3: ( NAME assignment constraint NEWLINE )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:170:5: NAME assignment constraint NEWLINE
                pass 
                NAME58=self.match(self.input, NAME, self.FOLLOW_NAME_in_propertyAssignment912)
                self._state.following.append(self.FOLLOW_assignment_in_propertyAssignment914)
                assignment59 = self.assignment()

                self._state.following.pop()
                self._state.following.append(self.FOLLOW_constraint_in_propertyAssignment916)
                constraint60 = self.constraint()

                self._state.following.pop()
                #action start
                object = PropertyAssignment( [NAME58.text, assignment59, constraint60] ) 
                #action end
                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_propertyAssignment920)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "propertyAssignment"


    # $ANTLR start "expressionStmt"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:173:1: expressionStmt returns [object] : comparisonList1= comparisonList ( assignment comparisonList2= comparisonList )? NEWLINE ;
    def expressionStmt(self, ):

        object = None

        comparisonList1 = None

        comparisonList2 = None

        assignment61 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:174:3: (comparisonList1= comparisonList ( assignment comparisonList2= comparisonList )? NEWLINE )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:174:5: comparisonList1= comparisonList ( assignment comparisonList2= comparisonList )? NEWLINE
                pass 
                self._state.following.append(self.FOLLOW_comparisonList_in_expressionStmt940)
                comparisonList1 = self.comparisonList()

                self._state.following.pop()
                #action start
                object = ExpressionStmt( comparisonList1 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:175:7: ( assignment comparisonList2= comparisonList )?
                alt18 = 2
                LA18_0 = self.input.LA(1)

                if ((ASSIGN <= LA18_0 <= DOUBLESLASHEQUAL)) :
                    alt18 = 1
                if alt18 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:175:9: assignment comparisonList2= comparisonList
                    pass 
                    self._state.following.append(self.FOLLOW_assignment_in_expressionStmt952)
                    assignment61 = self.assignment()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_comparisonList_in_expressionStmt956)
                    comparisonList2 = self.comparisonList()

                    self._state.following.pop()
                    #action start
                    object.append_children( [assignment61, comparisonList2] ) 
                    #action end



                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_expressionStmt963)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "expressionStmt"


    # $ANTLR start "assignment"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:178:1: assignment returns [object] : ( ASSIGN | PLUSEQUAL | MINUSEQUAL | STAREQUAL | SLASHEQUAL | PERCENTEQUAL | AMPEREQUAL | VBAREQUAL | CIRCUMFLEXEQUAL | LEFTSHIFTEQUAL | RIGHTSHIFTEQUAL | DOUBLESTAREQUAL | DOUBLESLASHEQUAL );
    def assignment(self, ):

        object = None

        ASSIGN62 = None
        PLUSEQUAL63 = None
        MINUSEQUAL64 = None
        STAREQUAL65 = None
        SLASHEQUAL66 = None
        PERCENTEQUAL67 = None
        AMPEREQUAL68 = None
        VBAREQUAL69 = None
        CIRCUMFLEXEQUAL70 = None
        LEFTSHIFTEQUAL71 = None
        RIGHTSHIFTEQUAL72 = None
        DOUBLESTAREQUAL73 = None
        DOUBLESLASHEQUAL74 = None

        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:179:3: ( ASSIGN | PLUSEQUAL | MINUSEQUAL | STAREQUAL | SLASHEQUAL | PERCENTEQUAL | AMPEREQUAL | VBAREQUAL | CIRCUMFLEXEQUAL | LEFTSHIFTEQUAL | RIGHTSHIFTEQUAL | DOUBLESTAREQUAL | DOUBLESLASHEQUAL )
                alt19 = 13
                LA19 = self.input.LA(1)
                if LA19 == ASSIGN:
                    alt19 = 1
                elif LA19 == PLUSEQUAL:
                    alt19 = 2
                elif LA19 == MINUSEQUAL:
                    alt19 = 3
                elif LA19 == STAREQUAL:
                    alt19 = 4
                elif LA19 == SLASHEQUAL:
                    alt19 = 5
                elif LA19 == PERCENTEQUAL:
                    alt19 = 6
                elif LA19 == AMPEREQUAL:
                    alt19 = 7
                elif LA19 == VBAREQUAL:
                    alt19 = 8
                elif LA19 == CIRCUMFLEXEQUAL:
                    alt19 = 9
                elif LA19 == LEFTSHIFTEQUAL:
                    alt19 = 10
                elif LA19 == RIGHTSHIFTEQUAL:
                    alt19 = 11
                elif LA19 == DOUBLESTAREQUAL:
                    alt19 = 12
                elif LA19 == DOUBLESLASHEQUAL:
                    alt19 = 13
                else:
                    nvae = NoViableAltException("", 19, 0, self.input)

                    raise nvae

                if alt19 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:179:5: ASSIGN
                    pass 
                    ASSIGN62=self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_assignment981)
                    #action start
                    object = Assignment( ASSIGN62.text ) 
                    #action end


                elif alt19 == 2:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:180:5: PLUSEQUAL
                    pass 
                    PLUSEQUAL63=self.match(self.input, PLUSEQUAL, self.FOLLOW_PLUSEQUAL_in_assignment1000)
                    #action start
                    object = Assignment( PLUSEQUAL63.text ) 
                    #action end


                elif alt19 == 3:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:181:5: MINUSEQUAL
                    pass 
                    MINUSEQUAL64=self.match(self.input, MINUSEQUAL, self.FOLLOW_MINUSEQUAL_in_assignment1016)
                    #action start
                    object = Assignment( MINUSEQUAL64.text ) 
                    #action end


                elif alt19 == 4:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:182:5: STAREQUAL
                    pass 
                    STAREQUAL65=self.match(self.input, STAREQUAL, self.FOLLOW_STAREQUAL_in_assignment1031)
                    #action start
                    object = Assignment( STAREQUAL65.text ) 
                    #action end


                elif alt19 == 5:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:183:5: SLASHEQUAL
                    pass 
                    SLASHEQUAL66=self.match(self.input, SLASHEQUAL, self.FOLLOW_SLASHEQUAL_in_assignment1047)
                    #action start
                    object = Assignment( SLASHEQUAL66.text ) 
                    #action end


                elif alt19 == 6:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:184:5: PERCENTEQUAL
                    pass 
                    PERCENTEQUAL67=self.match(self.input, PERCENTEQUAL, self.FOLLOW_PERCENTEQUAL_in_assignment1062)
                    #action start
                    object = Assignment( PERCENTEQUAL67.text ) 
                    #action end


                elif alt19 == 7:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:185:5: AMPEREQUAL
                    pass 
                    AMPEREQUAL68=self.match(self.input, AMPEREQUAL, self.FOLLOW_AMPEREQUAL_in_assignment1075)
                    #action start
                    object = Assignment( AMPEREQUAL68.text ) 
                    #action end


                elif alt19 == 8:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:186:5: VBAREQUAL
                    pass 
                    VBAREQUAL69=self.match(self.input, VBAREQUAL, self.FOLLOW_VBAREQUAL_in_assignment1090)
                    #action start
                    object = Assignment( VBAREQUAL69.text ) 
                    #action end


                elif alt19 == 9:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:187:5: CIRCUMFLEXEQUAL
                    pass 
                    CIRCUMFLEXEQUAL70=self.match(self.input, CIRCUMFLEXEQUAL, self.FOLLOW_CIRCUMFLEXEQUAL_in_assignment1106)
                    #action start
                    object = Assignment( CIRCUMFLEXEQUAL70.text ) 
                    #action end


                elif alt19 == 10:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:188:5: LEFTSHIFTEQUAL
                    pass 
                    LEFTSHIFTEQUAL71=self.match(self.input, LEFTSHIFTEQUAL, self.FOLLOW_LEFTSHIFTEQUAL_in_assignment1116)
                    #action start
                    object = Assignment( LEFTSHIFTEQUAL71.text ) 
                    #action end


                elif alt19 == 11:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:189:5: RIGHTSHIFTEQUAL
                    pass 
                    RIGHTSHIFTEQUAL72=self.match(self.input, RIGHTSHIFTEQUAL, self.FOLLOW_RIGHTSHIFTEQUAL_in_assignment1127)
                    #action start
                    object = Assignment( RIGHTSHIFTEQUAL72.text ) 
                    #action end


                elif alt19 == 12:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:190:5: DOUBLESTAREQUAL
                    pass 
                    DOUBLESTAREQUAL73=self.match(self.input, DOUBLESTAREQUAL, self.FOLLOW_DOUBLESTAREQUAL_in_assignment1137)
                    #action start
                    object = Assignment( DOUBLESTAREQUAL73.text ) 
                    #action end


                elif alt19 == 13:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:191:5: DOUBLESLASHEQUAL
                    pass 
                    DOUBLESLASHEQUAL74=self.match(self.input, DOUBLESLASHEQUAL, self.FOLLOW_DOUBLESLASHEQUAL_in_assignment1147)
                    #action start
                    object = Assignment( DOUBLESLASHEQUAL74.text ) 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "assignment"


    # $ANTLR start "importStmt"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:194:1: importStmt returns [object] : ( importName | importFrom );
    def importStmt(self, ):

        object = None

        importName75 = None

        importFrom76 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:195:3: ( importName | importFrom )
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if (LA20_0 == IMPORT) :
                    alt20 = 1
                elif (LA20_0 == FROM) :
                    alt20 = 2
                else:
                    nvae = NoViableAltException("", 20, 0, self.input)

                    raise nvae

                if alt20 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:195:5: importName
                    pass 
                    self._state.following.append(self.FOLLOW_importName_in_importStmt1168)
                    importName75 = self.importName()

                    self._state.following.pop()
                    #action start
                    object = ImportStmt( children = importName75, line = importName75.line ) 
                    #action end


                elif alt20 == 2:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:196:5: importFrom
                    pass 
                    self._state.following.append(self.FOLLOW_importFrom_in_importStmt1176)
                    importFrom76 = self.importFrom()

                    self._state.following.pop()
                    #action start
                    object = ImportStmt( children = importFrom76, line = importFrom76.line ) 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "importStmt"


    # $ANTLR start "importName"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:199:1: importName returns [object] : IMPORT dottedAsNames NEWLINE ;
    def importName(self, ):

        object = None

        IMPORT77 = None
        dottedAsNames78 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:200:3: ( IMPORT dottedAsNames NEWLINE )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:200:5: IMPORT dottedAsNames NEWLINE
                pass 
                IMPORT77=self.match(self.input, IMPORT, self.FOLLOW_IMPORT_in_importName1196)
                self._state.following.append(self.FOLLOW_dottedAsNames_in_importName1198)
                dottedAsNames78 = self.dottedAsNames()

                self._state.following.pop()
                #action start
                object = ImportName( children = [IMPORT77.text, dottedAsNames78], line = IMPORT77.getLine() ) 
                #action end
                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_importName1202)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "importName"


    # $ANTLR start "importFrom"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:203:1: importFrom returns [object] : FROM dottedName IMPORT (importAsNames1= importAsNames | LPAREN importAsNames2= importAsNames RPAREN ) NEWLINE ;
    def importFrom(self, ):

        object = None

        FROM79 = None
        IMPORT81 = None
        LPAREN82 = None
        RPAREN83 = None
        importAsNames1 = None

        importAsNames2 = None

        dottedName80 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:204:3: ( FROM dottedName IMPORT (importAsNames1= importAsNames | LPAREN importAsNames2= importAsNames RPAREN ) NEWLINE )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:204:5: FROM dottedName IMPORT (importAsNames1= importAsNames | LPAREN importAsNames2= importAsNames RPAREN ) NEWLINE
                pass 
                FROM79=self.match(self.input, FROM, self.FOLLOW_FROM_in_importFrom1220)
                #action start
                object = ImportFrom( children = FROM79.text, line = FROM79.getLine() ) 
                #action end
                self._state.following.append(self.FOLLOW_dottedName_in_importFrom1224)
                dottedName80 = self.dottedName()

                self._state.following.pop()
                #action start
                object.append_child( dottedName80 ) 
                #action end
                IMPORT81=self.match(self.input, IMPORT, self.FOLLOW_IMPORT_in_importFrom1228)
                #action start
                object.append_child( IMPORT81.text ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:205:7: (importAsNames1= importAsNames | LPAREN importAsNames2= importAsNames RPAREN )
                alt21 = 2
                LA21_0 = self.input.LA(1)

                if (LA21_0 == NAME) :
                    alt21 = 1
                elif (LA21_0 == LPAREN) :
                    alt21 = 2
                else:
                    nvae = NoViableAltException("", 21, 0, self.input)

                    raise nvae

                if alt21 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:205:9: importAsNames1= importAsNames
                    pass 
                    self._state.following.append(self.FOLLOW_importAsNames_in_importFrom1242)
                    importAsNames1 = self.importAsNames()

                    self._state.following.pop()
                    #action start
                    object.append_child( importAsNames1 ) 
                    #action end


                elif alt21 == 2:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:206:9: LPAREN importAsNames2= importAsNames RPAREN
                    pass 
                    LPAREN82=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_importFrom1254)
                    self._state.following.append(self.FOLLOW_importAsNames_in_importFrom1259)
                    importAsNames2 = self.importAsNames()

                    self._state.following.pop()
                    RPAREN83=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_importFrom1261)
                    #action start
                    object.append_children( [LPAREN82.text, importAsNames2, RPAREN83.text] ) 
                    #action end



                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_importFrom1273)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "importFrom"


    # $ANTLR start "importAsNames"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:210:1: importAsNames returns [object] : importAsName1= importAsName ( COMMA importAsName2= importAsName )* ( COMMA )? ;
    def importAsNames(self, ):

        object = None

        importAsName1 = None

        importAsName2 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:211:3: (importAsName1= importAsName ( COMMA importAsName2= importAsName )* ( COMMA )? )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:211:5: importAsName1= importAsName ( COMMA importAsName2= importAsName )* ( COMMA )?
                pass 
                self._state.following.append(self.FOLLOW_importAsName_in_importAsNames1292)
                importAsName1 = self.importAsName()

                self._state.following.pop()
                #action start
                object=ImportAsNames( importAsName1 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:212:7: ( COMMA importAsName2= importAsName )*
                while True: #loop22
                    alt22 = 2
                    LA22_0 = self.input.LA(1)

                    if (LA22_0 == COMMA) :
                        LA22_1 = self.input.LA(2)

                        if (LA22_1 == NAME) :
                            alt22 = 1




                    if alt22 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:212:9: COMMA importAsName2= importAsName
                        pass 
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_importAsNames1304)
                        self._state.following.append(self.FOLLOW_importAsName_in_importAsNames1308)
                        importAsName2 = self.importAsName()

                        self._state.following.pop()
                        #action start
                        object.append_children( [",", importAsName2] ) 
                        #action end


                    else:
                        break #loop22
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:212:105: ( COMMA )?
                alt23 = 2
                LA23_0 = self.input.LA(1)

                if (LA23_0 == COMMA) :
                    alt23 = 1
                if alt23 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:212:107: COMMA
                    pass 
                    self.match(self.input, COMMA, self.FOLLOW_COMMA_in_importAsNames1317)
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
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:215:1: importAsName returns [object] : name1= NAME ( AS name2= NAME )? ;
    def importAsName(self, ):

        object = None

        name1 = None
        name2 = None
        AS84 = None

        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:216:3: (name1= NAME ( AS name2= NAME )? )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:216:5: name1= NAME ( AS name2= NAME )?
                pass 
                name1=self.match(self.input, NAME, self.FOLLOW_NAME_in_importAsName1341)
                #action start
                object=ImportAsName( name1.text ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:216:56: ( AS name2= NAME )?
                alt24 = 2
                LA24_0 = self.input.LA(1)

                if (LA24_0 == AS) :
                    alt24 = 1
                if alt24 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:216:57: AS name2= NAME
                    pass 
                    AS84=self.match(self.input, AS, self.FOLLOW_AS_in_importAsName1346)
                    name2=self.match(self.input, NAME, self.FOLLOW_NAME_in_importAsName1350)
                    #action start
                    object.append_children( [AS84.text, name2.text] ) 
                    #action end







            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "importAsName"


    # $ANTLR start "dottedAsNames"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:219:1: dottedAsNames returns [object] : dottedAsName1= dottedAsName ( COMMA dottedAsName2= dottedAsName )* ;
    def dottedAsNames(self, ):

        object = None

        COMMA85 = None
        dottedAsName1 = None

        dottedAsName2 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:220:3: (dottedAsName1= dottedAsName ( COMMA dottedAsName2= dottedAsName )* )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:220:5: dottedAsName1= dottedAsName ( COMMA dottedAsName2= dottedAsName )*
                pass 
                self._state.following.append(self.FOLLOW_dottedAsName_in_dottedAsNames1374)
                dottedAsName1 = self.dottedAsName()

                self._state.following.pop()
                #action start
                object = DottedAsNames( dottedAsName1 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:221:7: ( COMMA dottedAsName2= dottedAsName )*
                while True: #loop25
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if (LA25_0 == COMMA) :
                        alt25 = 1


                    if alt25 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:221:8: COMMA dottedAsName2= dottedAsName
                        pass 
                        COMMA85=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_dottedAsNames1385)
                        self._state.following.append(self.FOLLOW_dottedAsName_in_dottedAsNames1389)
                        dottedAsName2 = self.dottedAsName()

                        self._state.following.pop()
                        #action start
                        object.append_children( [COMMA85.text, dottedAsName2] ) 
                        #action end


                    else:
                        break #loop25




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "dottedAsNames"


    # $ANTLR start "dottedAsName"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:224:1: dottedAsName returns [object] : dottedName ( AS NAME )? ;
    def dottedAsName(self, ):

        object = None

        AS87 = None
        NAME88 = None
        dottedName86 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:225:3: ( dottedName ( AS NAME )? )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:225:5: dottedName ( AS NAME )?
                pass 
                self._state.following.append(self.FOLLOW_dottedName_in_dottedAsName1411)
                dottedName86 = self.dottedName()

                self._state.following.pop()
                #action start
                object = DottedAsName( dottedName86 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:225:65: ( AS NAME )?
                alt26 = 2
                LA26_0 = self.input.LA(1)

                if (LA26_0 == AS) :
                    alt26 = 1
                if alt26 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:225:67: AS NAME
                    pass 
                    AS87=self.match(self.input, AS, self.FOLLOW_AS_in_dottedAsName1417)
                    NAME88=self.match(self.input, NAME, self.FOLLOW_NAME_in_dottedAsName1419)
                    #action start
                    object.append_children( [AS87.text, NAME88.text] ) 
                    #action end







            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "dottedAsName"


    # $ANTLR start "dottedName"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:228:1: dottedName returns [object] : name1= NAME ( DOT name2= NAME )* ;
    def dottedName(self, ):

        object = None

        name1 = None
        name2 = None
        DOT89 = None

        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:229:3: (name1= NAME ( DOT name2= NAME )* )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:229:5: name1= NAME ( DOT name2= NAME )*
                pass 
                name1=self.match(self.input, NAME, self.FOLLOW_NAME_in_dottedName1444)
                #action start
                object = DottedName( name1.text ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:230:7: ( DOT name2= NAME )*
                while True: #loop27
                    alt27 = 2
                    LA27_0 = self.input.LA(1)

                    if (LA27_0 == DOT) :
                        alt27 = 1


                    if alt27 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:230:9: DOT name2= NAME
                        pass 
                        DOT89=self.match(self.input, DOT, self.FOLLOW_DOT_in_dottedName1456)
                        name2=self.match(self.input, NAME, self.FOLLOW_NAME_in_dottedName1460)
                        #action start
                        object.append_children( [DOT89.text, name2.text] ) 
                        #action end


                    else:
                        break #loop27




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "dottedName"


    # $ANTLR start "constraint"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:233:1: constraint returns [object] : orConstraint ;
    def constraint(self, ):

        object = None

        orConstraint90 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:234:3: ( orConstraint )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:234:5: orConstraint
                pass 
                self._state.following.append(self.FOLLOW_orConstraint_in_constraint1483)
                orConstraint90 = self.orConstraint()

                self._state.following.pop()
                #action start
                object = Constraint( orConstraint90 ) 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "constraint"


    # $ANTLR start "orConstraint"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:237:1: orConstraint returns [object] : constraint1= andConstraint ( OR constraint2= andConstraint )* ;
    def orConstraint(self, ):

        object = None

        OR91 = None
        constraint1 = None

        constraint2 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:238:3: (constraint1= andConstraint ( OR constraint2= andConstraint )* )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:238:5: constraint1= andConstraint ( OR constraint2= andConstraint )*
                pass 
                self._state.following.append(self.FOLLOW_andConstraint_in_orConstraint1505)
                constraint1 = self.andConstraint()

                self._state.following.pop()
                #action start
                object = OrConstraint( constraint1 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:239:7: ( OR constraint2= andConstraint )*
                while True: #loop28
                    alt28 = 2
                    LA28_0 = self.input.LA(1)

                    if (LA28_0 == OR) :
                        alt28 = 1


                    if alt28 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:239:9: OR constraint2= andConstraint
                        pass 
                        OR91=self.match(self.input, OR, self.FOLLOW_OR_in_orConstraint1517)
                        self._state.following.append(self.FOLLOW_andConstraint_in_orConstraint1521)
                        constraint2 = self.andConstraint()

                        self._state.following.pop()
                        #action start
                        object.append_children( [OR91.text, constraint2] ) 
                        #action end


                    else:
                        break #loop28




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "orConstraint"


    # $ANTLR start "andConstraint"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:242:1: andConstraint returns [object] : constraint1= notConstraint ( AND constraint2= notConstraint )* ;
    def andConstraint(self, ):

        object = None

        AND92 = None
        constraint1 = None

        constraint2 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:243:3: (constraint1= notConstraint ( AND constraint2= notConstraint )* )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:243:5: constraint1= notConstraint ( AND constraint2= notConstraint )*
                pass 
                self._state.following.append(self.FOLLOW_notConstraint_in_andConstraint1546)
                constraint1 = self.notConstraint()

                self._state.following.pop()
                #action start
                object = AndConstraint( constraint1 )
                #action end
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:244:7: ( AND constraint2= notConstraint )*
                while True: #loop29
                    alt29 = 2
                    LA29_0 = self.input.LA(1)

                    if (LA29_0 == AND) :
                        alt29 = 1


                    if alt29 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:244:9: AND constraint2= notConstraint
                        pass 
                        AND92=self.match(self.input, AND, self.FOLLOW_AND_in_andConstraint1558)
                        self._state.following.append(self.FOLLOW_notConstraint_in_andConstraint1562)
                        constraint2 = self.notConstraint()

                        self._state.following.pop()
                        #action start
                        object.append_children( [AND92.text, constraint2] ) 
                        #action end


                    else:
                        break #loop29




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "andConstraint"


    # $ANTLR start "notConstraint"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:247:1: notConstraint returns [object] : ( NOT )* comparison ;
    def notConstraint(self, ):

        object = None

        NOT93 = None
        comparison94 = None


        object = NotConstraint() 
        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:249:3: ( ( NOT )* comparison )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:249:5: ( NOT )* comparison
                pass 
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:249:5: ( NOT )*
                while True: #loop30
                    alt30 = 2
                    LA30_0 = self.input.LA(1)

                    if (LA30_0 == NOT) :
                        alt30 = 1


                    if alt30 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:249:7: NOT
                        pass 
                        NOT93=self.match(self.input, NOT, self.FOLLOW_NOT_in_notConstraint1593)
                        #action start
                        object.append_child( NOT93.text ) 
                        #action end


                    else:
                        break #loop30
                self._state.following.append(self.FOLLOW_comparison_in_notConstraint1600)
                comparison94 = self.comparison()

                self._state.following.pop()
                #action start
                object.append_child( comparison94 ) 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "notConstraint"


    # $ANTLR start "comparison"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:252:1: comparison returns [object] : expression1= expression ( comparisonOperation expression2= expression )* ;
    def comparison(self, ):

        object = None

        expression1 = None

        expression2 = None

        comparisonOperation95 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:253:3: (expression1= expression ( comparisonOperation expression2= expression )* )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:253:5: expression1= expression ( comparisonOperation expression2= expression )*
                pass 
                self._state.following.append(self.FOLLOW_expression_in_comparison1622)
                expression1 = self.expression()

                self._state.following.pop()
                #action start
                object = Comparison( expression1 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:254:5: ( comparisonOperation expression2= expression )*
                while True: #loop31
                    alt31 = 2
                    LA31_0 = self.input.LA(1)

                    if (LA31_0 == NOT or (LESS <= LA31_0 <= NOTEQUAL) or (IN <= LA31_0 <= IS)) :
                        alt31 = 1


                    if alt31 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:254:7: comparisonOperation expression2= expression
                        pass 
                        self._state.following.append(self.FOLLOW_comparisonOperation_in_comparison1632)
                        comparisonOperation95 = self.comparisonOperation()

                        self._state.following.pop()
                        self._state.following.append(self.FOLLOW_expression_in_comparison1636)
                        expression2 = self.expression()

                        self._state.following.pop()
                        #action start
                        object.append_children( [ comparisonOperation95, expression2] ) 
                        #action end


                    else:
                        break #loop31




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "comparison"


    # $ANTLR start "comparisonOperation"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:257:1: comparisonOperation returns [object] : ( LESS | GREATER | EQUAL | GREATEREQUAL | LESSEQUAL | ALT_NOTEQUAL | NOTEQUAL | 'in' | 'not' 'in' | 'is' | 'is' 'not' ) ;
    def comparisonOperation(self, ):

        object = None

        LESS96 = None
        GREATER97 = None
        EQUAL98 = None
        GREATEREQUAL99 = None
        LESSEQUAL100 = None
        ALT_NOTEQUAL101 = None
        NOTEQUAL102 = None

        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:258:3: ( ( LESS | GREATER | EQUAL | GREATEREQUAL | LESSEQUAL | ALT_NOTEQUAL | NOTEQUAL | 'in' | 'not' 'in' | 'is' | 'is' 'not' ) )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:258:5: ( LESS | GREATER | EQUAL | GREATEREQUAL | LESSEQUAL | ALT_NOTEQUAL | NOTEQUAL | 'in' | 'not' 'in' | 'is' | 'is' 'not' )
                pass 
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:258:5: ( LESS | GREATER | EQUAL | GREATEREQUAL | LESSEQUAL | ALT_NOTEQUAL | NOTEQUAL | 'in' | 'not' 'in' | 'is' | 'is' 'not' )
                alt32 = 11
                alt32 = self.dfa32.predict(self.input)
                if alt32 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:258:7: LESS
                    pass 
                    LESS96=self.match(self.input, LESS, self.FOLLOW_LESS_in_comparisonOperation1661)
                    #action start
                    object = ComparisonOperation( LESS96.text ) 
                    #action end


                elif alt32 == 2:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:259:7: GREATER
                    pass 
                    GREATER97=self.match(self.input, GREATER, self.FOLLOW_GREATER_in_comparisonOperation1680)
                    #action start
                    object = ComparisonOperation( GREATER97.text ) 
                    #action end


                elif alt32 == 3:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:260:7: EQUAL
                    pass 
                    EQUAL98=self.match(self.input, EQUAL, self.FOLLOW_EQUAL_in_comparisonOperation1696)
                    #action start
                    object = ComparisonOperation( EQUAL98.text ) 
                    #action end


                elif alt32 == 4:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:261:7: GREATEREQUAL
                    pass 
                    GREATEREQUAL99=self.match(self.input, GREATEREQUAL, self.FOLLOW_GREATEREQUAL_in_comparisonOperation1714)
                    #action start
                    object = ComparisonOperation( GREATEREQUAL99.text ) 
                    #action end


                elif alt32 == 5:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:262:7: LESSEQUAL
                    pass 
                    LESSEQUAL100=self.match(self.input, LESSEQUAL, self.FOLLOW_LESSEQUAL_in_comparisonOperation1725)
                    #action start
                    object = ComparisonOperation( LESSEQUAL100.text ) 
                    #action end


                elif alt32 == 6:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:263:7: ALT_NOTEQUAL
                    pass 
                    ALT_NOTEQUAL101=self.match(self.input, ALT_NOTEQUAL, self.FOLLOW_ALT_NOTEQUAL_in_comparisonOperation1739)
                    #action start
                    object = ComparisonOperation( ALT_NOTEQUAL101.text ) 
                    #action end


                elif alt32 == 7:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:264:7: NOTEQUAL
                    pass 
                    NOTEQUAL102=self.match(self.input, NOTEQUAL, self.FOLLOW_NOTEQUAL_in_comparisonOperation1750)
                    #action start
                    object = ComparisonOperation( NOTEQUAL102.text ) 
                    #action end


                elif alt32 == 8:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:265:7: 'in'
                    pass 
                    self.match(self.input, IN, self.FOLLOW_IN_in_comparisonOperation1765)
                    #action start
                    object = ComparisonOperation( "in" ) 
                    #action end


                elif alt32 == 9:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:266:7: 'not' 'in'
                    pass 
                    self.match(self.input, NOT, self.FOLLOW_NOT_in_comparisonOperation1784)
                    self.match(self.input, IN, self.FOLLOW_IN_in_comparisonOperation1786)
                    #action start
                    object = ComparisonOperation( "not in" ) 
                    #action end


                elif alt32 == 10:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:267:7: 'is'
                    pass 
                    self.match(self.input, IS, self.FOLLOW_IS_in_comparisonOperation1799)
                    #action start
                    object = ComparisonOperation( "is" ) 
                    #action end


                elif alt32 == 11:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:268:7: 'is' 'not'
                    pass 
                    self.match(self.input, IS, self.FOLLOW_IS_in_comparisonOperation1818)
                    self.match(self.input, NOT, self.FOLLOW_NOT_in_comparisonOperation1820)
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
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:271:1: expression returns [object] : bitwiseOrExpr ;
    def expression(self, ):

        object = None

        bitwiseOrExpr103 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:272:3: ( bitwiseOrExpr )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:272:5: bitwiseOrExpr
                pass 
                self._state.following.append(self.FOLLOW_bitwiseOrExpr_in_expression1845)
                bitwiseOrExpr103 = self.bitwiseOrExpr()

                self._state.following.pop()
                #action start
                object = Expression( bitwiseOrExpr103 ) 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "expression"


    # $ANTLR start "bitwiseOrExpr"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:275:1: bitwiseOrExpr returns [object] : expr1= bitwiseXorExpr ( VBAR expr2= bitwiseXorExpr )* ;
    def bitwiseOrExpr(self, ):

        object = None

        VBAR104 = None
        expr1 = None

        expr2 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:276:3: (expr1= bitwiseXorExpr ( VBAR expr2= bitwiseXorExpr )* )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:276:5: expr1= bitwiseXorExpr ( VBAR expr2= bitwiseXorExpr )*
                pass 
                self._state.following.append(self.FOLLOW_bitwiseXorExpr_in_bitwiseOrExpr1867)
                expr1 = self.bitwiseXorExpr()

                self._state.following.pop()
                #action start
                object = BitwiseOrExpr( expr1 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:277:7: ( VBAR expr2= bitwiseXorExpr )*
                while True: #loop33
                    alt33 = 2
                    LA33_0 = self.input.LA(1)

                    if (LA33_0 == VBAR) :
                        alt33 = 1


                    if alt33 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:277:9: VBAR expr2= bitwiseXorExpr
                        pass 
                        VBAR104=self.match(self.input, VBAR, self.FOLLOW_VBAR_in_bitwiseOrExpr1879)
                        self._state.following.append(self.FOLLOW_bitwiseXorExpr_in_bitwiseOrExpr1883)
                        expr2 = self.bitwiseXorExpr()

                        self._state.following.pop()
                        #action start
                        object.append_children( [VBAR104.text, expr2] ) 
                        #action end


                    else:
                        break #loop33




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "bitwiseOrExpr"


    # $ANTLR start "bitwiseXorExpr"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:280:1: bitwiseXorExpr returns [object] : expr1= bitwiseAndExpr ( CIRCUMFLEX expr2= bitwiseAndExpr )* ;
    def bitwiseXorExpr(self, ):

        object = None

        CIRCUMFLEX105 = None
        expr1 = None

        expr2 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:281:3: (expr1= bitwiseAndExpr ( CIRCUMFLEX expr2= bitwiseAndExpr )* )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:281:5: expr1= bitwiseAndExpr ( CIRCUMFLEX expr2= bitwiseAndExpr )*
                pass 
                self._state.following.append(self.FOLLOW_bitwiseAndExpr_in_bitwiseXorExpr1908)
                expr1 = self.bitwiseAndExpr()

                self._state.following.pop()
                #action start
                object = BitwiseXorExpr( expr1 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:282:7: ( CIRCUMFLEX expr2= bitwiseAndExpr )*
                while True: #loop34
                    alt34 = 2
                    LA34_0 = self.input.LA(1)

                    if (LA34_0 == CIRCUMFLEX) :
                        alt34 = 1


                    if alt34 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:282:9: CIRCUMFLEX expr2= bitwiseAndExpr
                        pass 
                        CIRCUMFLEX105=self.match(self.input, CIRCUMFLEX, self.FOLLOW_CIRCUMFLEX_in_bitwiseXorExpr1920)
                        self._state.following.append(self.FOLLOW_bitwiseAndExpr_in_bitwiseXorExpr1924)
                        expr2 = self.bitwiseAndExpr()

                        self._state.following.pop()
                        #action start
                        object.append_children( [CIRCUMFLEX105.text, expr2] ) 
                        #action end


                    else:
                        break #loop34




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "bitwiseXorExpr"


    # $ANTLR start "bitwiseAndExpr"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:285:1: bitwiseAndExpr returns [object] : expr1= shiftExpr ( AMPER expr2= shiftExpr )* ;
    def bitwiseAndExpr(self, ):

        object = None

        AMPER106 = None
        expr1 = None

        expr2 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:286:3: (expr1= shiftExpr ( AMPER expr2= shiftExpr )* )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:286:5: expr1= shiftExpr ( AMPER expr2= shiftExpr )*
                pass 
                self._state.following.append(self.FOLLOW_shiftExpr_in_bitwiseAndExpr1949)
                expr1 = self.shiftExpr()

                self._state.following.pop()
                #action start
                object = BitwiseAndExpr( expr1 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:287:7: ( AMPER expr2= shiftExpr )*
                while True: #loop35
                    alt35 = 2
                    LA35_0 = self.input.LA(1)

                    if (LA35_0 == AMPER) :
                        alt35 = 1


                    if alt35 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:287:9: AMPER expr2= shiftExpr
                        pass 
                        AMPER106=self.match(self.input, AMPER, self.FOLLOW_AMPER_in_bitwiseAndExpr1961)
                        self._state.following.append(self.FOLLOW_shiftExpr_in_bitwiseAndExpr1965)
                        expr2 = self.shiftExpr()

                        self._state.following.pop()
                        #action start
                        object.append_children( [AMPER106.text, expr2] ) 
                        #action end


                    else:
                        break #loop35




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "bitwiseAndExpr"


    # $ANTLR start "shiftExpr"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:290:1: shiftExpr returns [object] : expr1= arithExpr ( ( LEFTSHIFT | RIGHTSHIFT ) expr2= arithExpr )* ;
    def shiftExpr(self, ):

        object = None

        LEFTSHIFT107 = None
        RIGHTSHIFT108 = None
        expr1 = None

        expr2 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:291:3: (expr1= arithExpr ( ( LEFTSHIFT | RIGHTSHIFT ) expr2= arithExpr )* )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:291:5: expr1= arithExpr ( ( LEFTSHIFT | RIGHTSHIFT ) expr2= arithExpr )*
                pass 
                self._state.following.append(self.FOLLOW_arithExpr_in_shiftExpr1990)
                expr1 = self.arithExpr()

                self._state.following.pop()
                #action start
                object = ShiftExpr( expr1 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:292:7: ( ( LEFTSHIFT | RIGHTSHIFT ) expr2= arithExpr )*
                while True: #loop37
                    alt37 = 2
                    LA37_0 = self.input.LA(1)

                    if (LA37_0 == RIGHTSHIFT or LA37_0 == LEFTSHIFT) :
                        alt37 = 1


                    if alt37 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:292:9: ( LEFTSHIFT | RIGHTSHIFT ) expr2= arithExpr
                        pass 
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:292:9: ( LEFTSHIFT | RIGHTSHIFT )
                        alt36 = 2
                        LA36_0 = self.input.LA(1)

                        if (LA36_0 == LEFTSHIFT) :
                            alt36 = 1
                        elif (LA36_0 == RIGHTSHIFT) :
                            alt36 = 2
                        else:
                            nvae = NoViableAltException("", 36, 0, self.input)

                            raise nvae

                        if alt36 == 1:
                            # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:292:11: LEFTSHIFT
                            pass 
                            LEFTSHIFT107=self.match(self.input, LEFTSHIFT, self.FOLLOW_LEFTSHIFT_in_shiftExpr2004)
                            #action start
                            object.append_child( LEFTSHIFT107.text ) 
                            #action end


                        elif alt36 == 2:
                            # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:292:67: RIGHTSHIFT
                            pass 
                            RIGHTSHIFT108=self.match(self.input, RIGHTSHIFT, self.FOLLOW_RIGHTSHIFT_in_shiftExpr2010)
                            #action start
                            object.append_child( RIGHTSHIFT108.text ) 
                            #action end



                        self._state.following.append(self.FOLLOW_arithExpr_in_shiftExpr2028)
                        expr2 = self.arithExpr()

                        self._state.following.pop()
                        #action start
                        object.append_child( expr2 ) 
                        #action end


                    else:
                        break #loop37




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "shiftExpr"


    # $ANTLR start "arithExpr"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:296:1: arithExpr returns [object] : term1= term ( ( PLUS | MINUS ) term2= term )* ;
    def arithExpr(self, ):

        object = None

        PLUS109 = None
        MINUS110 = None
        term1 = None

        term2 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:297:3: (term1= term ( ( PLUS | MINUS ) term2= term )* )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:297:5: term1= term ( ( PLUS | MINUS ) term2= term )*
                pass 
                self._state.following.append(self.FOLLOW_term_in_arithExpr2053)
                term1 = self.term()

                self._state.following.pop()
                #action start
                object = ArithExpr( term1 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:298:7: ( ( PLUS | MINUS ) term2= term )*
                while True: #loop39
                    alt39 = 2
                    LA39_0 = self.input.LA(1)

                    if ((PLUS <= LA39_0 <= MINUS)) :
                        alt39 = 1


                    if alt39 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:298:9: ( PLUS | MINUS ) term2= term
                        pass 
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:298:9: ( PLUS | MINUS )
                        alt38 = 2
                        LA38_0 = self.input.LA(1)

                        if (LA38_0 == PLUS) :
                            alt38 = 1
                        elif (LA38_0 == MINUS) :
                            alt38 = 2
                        else:
                            nvae = NoViableAltException("", 38, 0, self.input)

                            raise nvae

                        if alt38 == 1:
                            # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:298:11: PLUS
                            pass 
                            PLUS109=self.match(self.input, PLUS, self.FOLLOW_PLUS_in_arithExpr2067)
                            #action start
                            object.append_child( PLUS109.text ) 
                            #action end


                        elif alt38 == 2:
                            # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:298:57: MINUS
                            pass 
                            MINUS110=self.match(self.input, MINUS, self.FOLLOW_MINUS_in_arithExpr2073)
                            #action start
                            object.append_child( MINUS110.text ) 
                            #action end



                        self._state.following.append(self.FOLLOW_term_in_arithExpr2091)
                        term2 = self.term()

                        self._state.following.pop()
                        #action start
                        object.append_child( term2 ) 
                        #action end


                    else:
                        break #loop39




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "arithExpr"


    # $ANTLR start "term"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:302:1: term returns [object] : factor1= factor ( ( STAR | SLASH | PERCENT | DOUBLESLASH ) factor2= factor )* ;
    def term(self, ):

        object = None

        STAR111 = None
        SLASH112 = None
        PERCENT113 = None
        DOUBLESLASH114 = None
        factor1 = None

        factor2 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:303:3: (factor1= factor ( ( STAR | SLASH | PERCENT | DOUBLESLASH ) factor2= factor )* )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:303:5: factor1= factor ( ( STAR | SLASH | PERCENT | DOUBLESLASH ) factor2= factor )*
                pass 
                self._state.following.append(self.FOLLOW_factor_in_term2116)
                factor1 = self.factor()

                self._state.following.pop()
                #action start
                object = Term( factor1 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:304:7: ( ( STAR | SLASH | PERCENT | DOUBLESLASH ) factor2= factor )*
                while True: #loop41
                    alt41 = 2
                    LA41_0 = self.input.LA(1)

                    if ((STAR <= LA41_0 <= DOUBLESLASH)) :
                        alt41 = 1


                    if alt41 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:304:9: ( STAR | SLASH | PERCENT | DOUBLESLASH ) factor2= factor
                        pass 
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:304:9: ( STAR | SLASH | PERCENT | DOUBLESLASH )
                        alt40 = 4
                        LA40 = self.input.LA(1)
                        if LA40 == STAR:
                            alt40 = 1
                        elif LA40 == SLASH:
                            alt40 = 2
                        elif LA40 == PERCENT:
                            alt40 = 3
                        elif LA40 == DOUBLESLASH:
                            alt40 = 4
                        else:
                            nvae = NoViableAltException("", 40, 0, self.input)

                            raise nvae

                        if alt40 == 1:
                            # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:304:10: STAR
                            pass 
                            STAR111=self.match(self.input, STAR, self.FOLLOW_STAR_in_term2129)
                            #action start
                            object.append_child( STAR111.text ) 
                            #action end


                        elif alt40 == 2:
                            # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:304:56: SLASH
                            pass 
                            SLASH112=self.match(self.input, SLASH, self.FOLLOW_SLASH_in_term2135)
                            #action start
                            object.append_child( SLASH112.text ) 
                            #action end


                        elif alt40 == 3:
                            # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:305:13: PERCENT
                            pass 
                            PERCENT113=self.match(self.input, PERCENT, self.FOLLOW_PERCENT_in_term2151)
                            #action start
                            object.append_child( PERCENT113.text ) 
                            #action end


                        elif alt40 == 4:
                            # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:305:65: DOUBLESLASH
                            pass 
                            DOUBLESLASH114=self.match(self.input, DOUBLESLASH, self.FOLLOW_DOUBLESLASH_in_term2157)
                            #action start
                            object.append_child( DOUBLESLASH114.text ) 
                            #action end



                        self._state.following.append(self.FOLLOW_factor_in_term2179)
                        factor2 = self.factor()

                        self._state.following.pop()
                        #action start
                        object.append_child( factor2 ) 
                        #action end


                    else:
                        break #loop41




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "term"


    # $ANTLR start "factor"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:309:1: factor returns [object] : ( PLUS factor1= factor | MINUS factor2= factor | TILDE factor3= factor | power );
    def factor(self, ):

        object = None

        PLUS115 = None
        MINUS116 = None
        TILDE117 = None
        factor1 = None

        factor2 = None

        factor3 = None

        power118 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:310:3: ( PLUS factor1= factor | MINUS factor2= factor | TILDE factor3= factor | power )
                alt42 = 4
                LA42 = self.input.LA(1)
                if LA42 == PLUS:
                    alt42 = 1
                elif LA42 == MINUS:
                    alt42 = 2
                elif LA42 == TILDE:
                    alt42 = 3
                elif LA42 == NAME or LA42 == STRING or LA42 == OBJECTBINDING or LA42 == LPAREN or LA42 == LBRACK or LA42 == LCURLY or LA42 == INT or LA42 == LONGINT or LA42 == FLOAT or LA42 == COMPLEX:
                    alt42 = 4
                else:
                    nvae = NoViableAltException("", 42, 0, self.input)

                    raise nvae

                if alt42 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:310:5: PLUS factor1= factor
                    pass 
                    PLUS115=self.match(self.input, PLUS, self.FOLLOW_PLUS_in_factor2202)
                    self._state.following.append(self.FOLLOW_factor_in_factor2207)
                    factor1 = self.factor()

                    self._state.following.pop()
                    #action start
                    object = Factor( [PLUS115.text, factor1] ) 
                    #action end


                elif alt42 == 2:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:311:5: MINUS factor2= factor
                    pass 
                    MINUS116=self.match(self.input, MINUS, self.FOLLOW_MINUS_in_factor2215)
                    self._state.following.append(self.FOLLOW_factor_in_factor2219)
                    factor2 = self.factor()

                    self._state.following.pop()
                    #action start
                    object = Factor( [MINUS116.text, factor2] ) 
                    #action end


                elif alt42 == 3:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:312:5: TILDE factor3= factor
                    pass 
                    TILDE117=self.match(self.input, TILDE, self.FOLLOW_TILDE_in_factor2227)
                    self._state.following.append(self.FOLLOW_factor_in_factor2231)
                    factor3 = self.factor()

                    self._state.following.pop()
                    #action start
                    object = Factor( [TILDE117.text, factor3] ) 
                    #action end


                elif alt42 == 4:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:313:5: power
                    pass 
                    self._state.following.append(self.FOLLOW_power_in_factor2239)
                    power118 = self.power()

                    self._state.following.pop()
                    #action start
                    object = Factor( power118 ) 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "factor"


    # $ANTLR start "power"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:316:1: power returns [object] : atom ( trailer )* ( options {greedy=true; } : DOUBLESTAR factor )? ;
    def power(self, ):

        object = None

        DOUBLESTAR121 = None
        atom119 = None

        trailer120 = None

        factor122 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:317:3: ( atom ( trailer )* ( options {greedy=true; } : DOUBLESTAR factor )? )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:317:5: atom ( trailer )* ( options {greedy=true; } : DOUBLESTAR factor )?
                pass 
                self._state.following.append(self.FOLLOW_atom_in_power2259)
                atom119 = self.atom()

                self._state.following.pop()
                #action start
                object = Power( atom119 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:318:7: ( trailer )*
                while True: #loop43
                    alt43 = 2
                    LA43_0 = self.input.LA(1)

                    if (LA43_0 == LPAREN or LA43_0 == DOT) :
                        alt43 = 1


                    if alt43 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:318:9: trailer
                        pass 
                        self._state.following.append(self.FOLLOW_trailer_in_power2271)
                        trailer120 = self.trailer()

                        self._state.following.pop()
                        #action start
                        object.append_child( trailer120 ) 
                        #action end


                    else:
                        break #loop43
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:319:7: ( options {greedy=true; } : DOUBLESTAR factor )?
                alt44 = 2
                LA44_0 = self.input.LA(1)

                if (LA44_0 == DOUBLESTAR) :
                    alt44 = 1
                if alt44 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:319:31: DOUBLESTAR factor
                    pass 
                    DOUBLESTAR121=self.match(self.input, DOUBLESTAR, self.FOLLOW_DOUBLESTAR_in_power2292)
                    self._state.following.append(self.FOLLOW_factor_in_power2294)
                    factor122 = self.factor()

                    self._state.following.pop()
                    #action start
                    object.append_children( [DOUBLESTAR121.text, factor122] ) 
                    #action end







            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "power"


    # $ANTLR start "atom"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:322:1: atom returns [object] : ( LPAREN (comparisonList1= comparisonList )? RPAREN | LBRACK ( listmaker )? RBRACK | LCURLY ( dictmaker )? RCURLY | NAME | OBJECTBINDING | INT | LONGINT | FLOAT | COMPLEX | ( STRING )+ );
    def atom(self, ):

        object = None

        LPAREN123 = None
        RPAREN124 = None
        LBRACK125 = None
        RBRACK127 = None
        LCURLY128 = None
        RCURLY130 = None
        NAME131 = None
        OBJECTBINDING132 = None
        INT133 = None
        LONGINT134 = None
        FLOAT135 = None
        COMPLEX136 = None
        STRING137 = None
        comparisonList1 = None

        listmaker126 = None

        dictmaker129 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:323:3: ( LPAREN (comparisonList1= comparisonList )? RPAREN | LBRACK ( listmaker )? RBRACK | LCURLY ( dictmaker )? RCURLY | NAME | OBJECTBINDING | INT | LONGINT | FLOAT | COMPLEX | ( STRING )+ )
                alt49 = 10
                LA49 = self.input.LA(1)
                if LA49 == LPAREN:
                    alt49 = 1
                elif LA49 == LBRACK:
                    alt49 = 2
                elif LA49 == LCURLY:
                    alt49 = 3
                elif LA49 == NAME:
                    alt49 = 4
                elif LA49 == OBJECTBINDING:
                    alt49 = 5
                elif LA49 == INT:
                    alt49 = 6
                elif LA49 == LONGINT:
                    alt49 = 7
                elif LA49 == FLOAT:
                    alt49 = 8
                elif LA49 == COMPLEX:
                    alt49 = 9
                elif LA49 == STRING:
                    alt49 = 10
                else:
                    nvae = NoViableAltException("", 49, 0, self.input)

                    raise nvae

                if alt49 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:323:5: LPAREN (comparisonList1= comparisonList )? RPAREN
                    pass 
                    LPAREN123=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_atom2317)
                    #action start
                    object = Atom( LPAREN123.text ) 
                    #action end
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:324:23: (comparisonList1= comparisonList )?
                    alt45 = 2
                    LA45_0 = self.input.LA(1)

                    if ((NAME <= LA45_0 <= STRING) or LA45_0 == NOT or LA45_0 == OBJECTBINDING or LA45_0 == LPAREN or (PLUS <= LA45_0 <= MINUS) or LA45_0 == TILDE or LA45_0 == LBRACK or LA45_0 == LCURLY or (INT <= LA45_0 <= COMPLEX)) :
                        alt45 = 1
                    if alt45 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:324:25: comparisonList1= comparisonList
                        pass 
                        self._state.following.append(self.FOLLOW_comparisonList_in_atom2356)
                        comparisonList1 = self.comparisonList()

                        self._state.following.pop()
                        #action start
                        object.append_child( comparisonList1 ) 
                        #action end



                    RPAREN124=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_atom2385)
                    #action start
                    object.append_child( RPAREN124.text ) 
                    #action end


                elif alt49 == 2:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:326:5: LBRACK ( listmaker )? RBRACK
                    pass 
                    LBRACK125=self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_atom2393)
                    #action start
                    object = Atom( LBRACK125.text ) 
                    #action end
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:327:23: ( listmaker )?
                    alt46 = 2
                    LA46_0 = self.input.LA(1)

                    if ((NAME <= LA46_0 <= STRING) or LA46_0 == NOT or LA46_0 == OBJECTBINDING or LA46_0 == LPAREN or (PLUS <= LA46_0 <= MINUS) or LA46_0 == TILDE or LA46_0 == LBRACK or LA46_0 == LCURLY or (INT <= LA46_0 <= COMPLEX)) :
                        alt46 = 1
                    if alt46 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:327:25: listmaker
                        pass 
                        self._state.following.append(self.FOLLOW_listmaker_in_atom2430)
                        listmaker126 = self.listmaker()

                        self._state.following.pop()
                        #action start
                        object.append_child( listmaker126 ) 
                        #action end



                    RBRACK127=self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_atom2459)
                    #action start
                    object.append_child( RBRACK127.text ) 
                    #action end


                elif alt49 == 3:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:329:5: LCURLY ( dictmaker )? RCURLY
                    pass 
                    LCURLY128=self.match(self.input, LCURLY, self.FOLLOW_LCURLY_in_atom2467)
                    #action start
                    object = Atom( LCURLY128.text ) 
                    #action end
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:330:23: ( dictmaker )?
                    alt47 = 2
                    LA47_0 = self.input.LA(1)

                    if ((NAME <= LA47_0 <= STRING) or LA47_0 == NOT or LA47_0 == OBJECTBINDING or LA47_0 == LPAREN or (PLUS <= LA47_0 <= MINUS) or LA47_0 == TILDE or LA47_0 == LBRACK or LA47_0 == LCURLY or (INT <= LA47_0 <= COMPLEX)) :
                        alt47 = 1
                    if alt47 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:330:25: dictmaker
                        pass 
                        self._state.following.append(self.FOLLOW_dictmaker_in_atom2504)
                        dictmaker129 = self.dictmaker()

                        self._state.following.pop()
                        #action start
                        object.append_child( dictmaker129 ) 
                        #action end



                    RCURLY130=self.match(self.input, RCURLY, self.FOLLOW_RCURLY_in_atom2533)
                    #action start
                    object.append_child( RCURLY130.text ) 
                    #action end


                elif alt49 == 4:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:333:5: NAME
                    pass 
                    NAME131=self.match(self.input, NAME, self.FOLLOW_NAME_in_atom2542)
                    #action start
                    object = Atom( NAME131.text ) 
                    #action end


                elif alt49 == 5:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:334:5: OBJECTBINDING
                    pass 
                    OBJECTBINDING132=self.match(self.input, OBJECTBINDING, self.FOLLOW_OBJECTBINDING_in_atom2561)
                    #action start
                    object = Atom( OBJECTBINDING132.text ) 
                    #action end


                elif alt49 == 6:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:335:5: INT
                    pass 
                    INT133=self.match(self.input, INT, self.FOLLOW_INT_in_atom2571)
                    #action start
                    object = Atom( INT133.text ) 
                    #action end


                elif alt49 == 7:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:336:5: LONGINT
                    pass 
                    LONGINT134=self.match(self.input, LONGINT, self.FOLLOW_LONGINT_in_atom2591)
                    #action start
                    object = Atom( LONGINT134.text ) 
                    #action end


                elif alt49 == 8:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:337:5: FLOAT
                    pass 
                    FLOAT135=self.match(self.input, FLOAT, self.FOLLOW_FLOAT_in_atom2607)
                    #action start
                    object = Atom( FLOAT135.text ) 
                    #action end


                elif alt49 == 9:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:338:5: COMPLEX
                    pass 
                    COMPLEX136=self.match(self.input, COMPLEX, self.FOLLOW_COMPLEX_in_atom2625)
                    #action start
                    object = Atom( COMPLEX136.text ) 
                    #action end


                elif alt49 == 10:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:339:5: ( STRING )+
                    pass 
                    #action start
                    object = Atom() 
                    #action end
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:339:25: ( STRING )+
                    cnt48 = 0
                    while True: #loop48
                        alt48 = 2
                        LA48_0 = self.input.LA(1)

                        if (LA48_0 == STRING) :
                            alt48 = 1


                        if alt48 == 1:
                            # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:339:27: STRING
                            pass 
                            STRING137=self.match(self.input, STRING, self.FOLLOW_STRING_in_atom2645)
                            #action start
                            object.append_child( STRING137.text ) 
                            #action end


                        else:
                            if cnt48 >= 1:
                                break #loop48

                            eee = EarlyExitException(48, self.input)
                            raise eee

                        cnt48 += 1



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "atom"


    # $ANTLR start "listmaker"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:342:1: listmaker returns [object] : constraint1= constraint ( options {greedy=true; } : COMMA constraint2= constraint )* ( COMMA )? ;
    def listmaker(self, ):

        object = None

        constraint1 = None

        constraint2 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:343:3: (constraint1= constraint ( options {greedy=true; } : COMMA constraint2= constraint )* ( COMMA )? )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:343:5: constraint1= constraint ( options {greedy=true; } : COMMA constraint2= constraint )* ( COMMA )?
                pass 
                self._state.following.append(self.FOLLOW_constraint_in_listmaker2670)
                constraint1 = self.constraint()

                self._state.following.pop()
                #action start
                object = ListMaker( constraint1 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:344:7: ( options {greedy=true; } : COMMA constraint2= constraint )*
                while True: #loop50
                    alt50 = 2
                    LA50_0 = self.input.LA(1)

                    if (LA50_0 == COMMA) :
                        LA50_1 = self.input.LA(2)

                        if ((NAME <= LA50_1 <= STRING) or LA50_1 == NOT or LA50_1 == OBJECTBINDING or LA50_1 == LPAREN or (PLUS <= LA50_1 <= MINUS) or LA50_1 == TILDE or LA50_1 == LBRACK or LA50_1 == LCURLY or (INT <= LA50_1 <= COMPLEX)) :
                            alt50 = 1




                    if alt50 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:344:31: COMMA constraint2= constraint
                        pass 
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_listmaker2688)
                        self._state.following.append(self.FOLLOW_constraint_in_listmaker2692)
                        constraint2 = self.constraint()

                        self._state.following.pop()
                        #action start
                        object.append_children( [ ",", constraint2] ) 
                        #action end


                    else:
                        break #loop50
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:345:7: ( COMMA )?
                alt51 = 2
                LA51_0 = self.input.LA(1)

                if (LA51_0 == COMMA) :
                    alt51 = 1
                if alt51 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:345:9: COMMA
                    pass 
                    self.match(self.input, COMMA, self.FOLLOW_COMMA_in_listmaker2707)
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
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:348:1: comparisonList returns [object] : constraint1= constraint ( options {k=2; } : COMMA constraint2= constraint )* ( COMMA )? ;
    def comparisonList(self, ):

        object = None

        constraint1 = None

        constraint2 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:349:3: (constraint1= constraint ( options {k=2; } : COMMA constraint2= constraint )* ( COMMA )? )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:349:5: constraint1= constraint ( options {k=2; } : COMMA constraint2= constraint )* ( COMMA )?
                pass 
                self._state.following.append(self.FOLLOW_constraint_in_comparisonList2732)
                constraint1 = self.constraint()

                self._state.following.pop()
                #action start
                object = ComparisonList( constraint1 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:350:7: ( options {k=2; } : COMMA constraint2= constraint )*
                while True: #loop52
                    alt52 = 2
                    alt52 = self.dfa52.predict(self.input)
                    if alt52 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:350:23: COMMA constraint2= constraint
                        pass 
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_comparisonList2750)
                        self._state.following.append(self.FOLLOW_constraint_in_comparisonList2754)
                        constraint2 = self.constraint()

                        self._state.following.pop()
                        #action start
                        object.append_children( [",", constraint2] ) 
                        #action end


                    else:
                        break #loop52
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:351:7: ( COMMA )?
                alt53 = 2
                LA53_0 = self.input.LA(1)

                if (LA53_0 == COMMA) :
                    alt53 = 1
                if alt53 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:351:9: COMMA
                    pass 
                    self.match(self.input, COMMA, self.FOLLOW_COMMA_in_comparisonList2769)
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
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:354:1: trailer returns [object] : ( LPAREN ( argumentList )? RPAREN | DOT NAME );
    def trailer(self, ):

        object = None

        LPAREN138 = None
        RPAREN140 = None
        DOT141 = None
        NAME142 = None
        argumentList139 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:355:3: ( LPAREN ( argumentList )? RPAREN | DOT NAME )
                alt55 = 2
                LA55_0 = self.input.LA(1)

                if (LA55_0 == LPAREN) :
                    alt55 = 1
                elif (LA55_0 == DOT) :
                    alt55 = 2
                else:
                    nvae = NoViableAltException("", 55, 0, self.input)

                    raise nvae

                if alt55 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:355:5: LPAREN ( argumentList )? RPAREN
                    pass 
                    LPAREN138=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_trailer2792)
                    #action start
                    object = Trailer( LPAREN138.text ) 
                    #action end
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:355:49: ( argumentList )?
                    alt54 = 2
                    LA54_0 = self.input.LA(1)

                    if ((NAME <= LA54_0 <= STRING) or LA54_0 == NOT or LA54_0 == OBJECTBINDING or LA54_0 == LPAREN or (PLUS <= LA54_0 <= MINUS) or LA54_0 == TILDE or LA54_0 == LBRACK or LA54_0 == LCURLY or (INT <= LA54_0 <= COMPLEX)) :
                        alt54 = 1
                    if alt54 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:355:50: argumentList
                        pass 
                        self._state.following.append(self.FOLLOW_argumentList_in_trailer2797)
                        argumentList139 = self.argumentList()

                        self._state.following.pop()
                        #action start
                        object.append_child( argumentList139 ) 
                        #action end



                    RPAREN140=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_trailer2804)
                    #action start
                    object.append_child( RPAREN140.text ) 
                    #action end


                elif alt55 == 2:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:356:5: DOT NAME
                    pass 
                    DOT141=self.match(self.input, DOT, self.FOLLOW_DOT_in_trailer2812)
                    NAME142=self.match(self.input, NAME, self.FOLLOW_NAME_in_trailer2814)
                    #action start
                    object = Trailer( [DOT141.text, NAME142.text] ) 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "trailer"


    # $ANTLR start "expressionList"
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:359:1: expressionList returns [object] : expression1= expression ( options {k=2; } : COMMA expression2= expression )* ( COMMA )? ;
    def expressionList(self, ):

        object = None

        expression1 = None

        expression2 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:360:3: (expression1= expression ( options {k=2; } : COMMA expression2= expression )* ( COMMA )? )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:360:5: expression1= expression ( options {k=2; } : COMMA expression2= expression )* ( COMMA )?
                pass 
                self._state.following.append(self.FOLLOW_expression_in_expressionList2837)
                expression1 = self.expression()

                self._state.following.pop()
                #action start
                object = ExpressionList( expression1 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:361:7: ( options {k=2; } : COMMA expression2= expression )*
                while True: #loop56
                    alt56 = 2
                    alt56 = self.dfa56.predict(self.input)
                    if alt56 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:361:25: COMMA expression2= expression
                        pass 
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_expressionList2857)
                        self._state.following.append(self.FOLLOW_expression_in_expressionList2861)
                        expression2 = self.expression()

                        self._state.following.pop()
                        #action start
                        object.append_children( [ ",", expression2 ] ) 
                        #action end


                    else:
                        break #loop56
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:362:7: ( COMMA )?
                alt57 = 2
                LA57_0 = self.input.LA(1)

                if (LA57_0 == COMMA) :
                    alt57 = 1
                if alt57 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:362:9: COMMA
                    pass 
                    self.match(self.input, COMMA, self.FOLLOW_COMMA_in_expressionList2876)
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
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:365:1: dictmaker returns [object] : constraint1= constraint COLON constraint2= constraint ( options {k=2; } : COMMA constraint3= constraint COLON constraint4= constraint )* ( COMMA )? ;
    def dictmaker(self, ):

        object = None

        constraint1 = None

        constraint2 = None

        constraint3 = None

        constraint4 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:366:3: (constraint1= constraint COLON constraint2= constraint ( options {k=2; } : COMMA constraint3= constraint COLON constraint4= constraint )* ( COMMA )? )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:366:5: constraint1= constraint COLON constraint2= constraint ( options {k=2; } : COMMA constraint3= constraint COLON constraint4= constraint )* ( COMMA )?
                pass 
                self._state.following.append(self.FOLLOW_constraint_in_dictmaker2901)
                constraint1 = self.constraint()

                self._state.following.pop()
                #action start
                object = DictMaker( constraint1 ) 
                #action end
                self.match(self.input, COLON, self.FOLLOW_COLON_in_dictmaker2911)
                self._state.following.append(self.FOLLOW_constraint_in_dictmaker2915)
                constraint2 = self.constraint()

                self._state.following.pop()
                #action start
                object.append_children( [":", constraint2] ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:368:9: ( options {k=2; } : COMMA constraint3= constraint COLON constraint4= constraint )*
                while True: #loop58
                    alt58 = 2
                    alt58 = self.dfa58.predict(self.input)
                    if alt58 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:368:26: COMMA constraint3= constraint COLON constraint4= constraint
                        pass 
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_dictmaker2936)
                        self._state.following.append(self.FOLLOW_constraint_in_dictmaker2940)
                        constraint3 = self.constraint()

                        self._state.following.pop()
                        self.match(self.input, COLON, self.FOLLOW_COLON_in_dictmaker2942)
                        self._state.following.append(self.FOLLOW_constraint_in_dictmaker2946)
                        constraint4 = self.constraint()

                        self._state.following.pop()
                        #action start
                        object.append_children( [",", constraint3, ":", constraint4] ) 
                        #action end


                    else:
                        break #loop58
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:369:9: ( COMMA )?
                alt59 = 2
                LA59_0 = self.input.LA(1)

                if (LA59_0 == COMMA) :
                    alt59 = 1
                if alt59 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:369:11: COMMA
                    pass 
                    self.match(self.input, COMMA, self.FOLLOW_COMMA_in_dictmaker2963)
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
    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:372:1: argumentList returns [object] : constraint1= constraint ( COMMA constraint2= constraint )* ( COMMA )? ;
    def argumentList(self, ):

        object = None

        constraint1 = None

        constraint2 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:373:3: (constraint1= constraint ( COMMA constraint2= constraint )* ( COMMA )? )
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:373:5: constraint1= constraint ( COMMA constraint2= constraint )* ( COMMA )?
                pass 
                self._state.following.append(self.FOLLOW_constraint_in_argumentList2988)
                constraint1 = self.constraint()

                self._state.following.pop()
                #action start
                object = ArgumentList( constraint1 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:374:7: ( COMMA constraint2= constraint )*
                while True: #loop60
                    alt60 = 2
                    LA60_0 = self.input.LA(1)

                    if (LA60_0 == COMMA) :
                        LA60_1 = self.input.LA(2)

                        if ((NAME <= LA60_1 <= STRING) or LA60_1 == NOT or LA60_1 == OBJECTBINDING or LA60_1 == LPAREN or (PLUS <= LA60_1 <= MINUS) or LA60_1 == TILDE or LA60_1 == LBRACK or LA60_1 == LCURLY or (INT <= LA60_1 <= COMPLEX)) :
                            alt60 = 1




                    if alt60 == 1:
                        # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:374:9: COMMA constraint2= constraint
                        pass 
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_argumentList3000)
                        self._state.following.append(self.FOLLOW_constraint_in_argumentList3004)
                        constraint2 = self.constraint()

                        self._state.following.pop()
                        #action start
                        object.append_children( [",", constraint2] ) 
                        #action end


                    else:
                        break #loop60
                # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:375:7: ( COMMA )?
                alt61 = 2
                LA61_0 = self.input.LA(1)

                if (LA61_0 == COMMA) :
                    alt61 = 1
                if alt61 == 1:
                    # /Users/walsh/Development/workspace/Intellect/src/intellect/grammar/Policy.g:375:9: COMMA
                    pass 
                    self.match(self.input, COMMA, self.FOLLOW_COMMA_in_argumentList3019)
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


    # lookup tables for DFA #32

    DFA32_eot = DFA.unpack(
        u"\15\uffff"
        )

    DFA32_eof = DFA.unpack(
        u"\15\uffff"
        )

    DFA32_min = DFA.unpack(
        u"\1\16\11\uffff\1\11\2\uffff"
        )

    DFA32_max = DFA.unpack(
        u"\1\117\11\uffff\1\111\2\uffff"
        )

    DFA32_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\1\3\1\4\1\5\1\6\1\7\1\10\1\11\1\uffff\1\13\1\12"
        )

    DFA32_special = DFA.unpack(
        u"\15\uffff"
        )

            
    DFA32_transition = [
        DFA.unpack(u"\1\11\40\uffff\1\1\1\2\1\3\1\4\1\5\1\6\1\7\30\uffff"
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
        DFA.unpack(u"\2\14\3\uffff\1\13\1\uffff\1\14\1\uffff\1\14\47\uffff"
        u"\2\14\4\uffff\1\14\1\uffff\1\14\1\uffff\1\14\1\uffff\4\14"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #32

    class DFA32(DFA):
        pass


    # lookup tables for DFA #52

    DFA52_eot = DFA.unpack(
        u"\56\uffff"
        )

    DFA52_eof = DFA.unpack(
        u"\56\uffff"
        )

    DFA52_min = DFA.unpack(
        u"\2\6\54\uffff"
        )

    DFA52_max = DFA.unpack(
        u"\1\52\1\111\54\uffff"
        )

    DFA52_accept = DFA.unpack(
        u"\2\uffff\1\2\35\uffff\1\1\15\uffff"
        )

    DFA52_special = DFA.unpack(
        u"\56\uffff"
        )

            
    DFA52_transition = [
        DFA.unpack(u"\1\2\14\uffff\1\2\7\uffff\15\2\2\uffff\1\1"),
        DFA.unpack(u"\1\2\2\uffff\2\40\3\uffff\1\40\1\uffff\1\40\1\uffff"
        u"\1\40\1\2\7\uffff\15\2\22\uffff\2\40\4\uffff\1\40\1\uffff\1\40"
        u"\1\uffff\1\40\1\uffff\4\40"),
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

    # class definition for DFA #52

    class DFA52(DFA):
        pass


    # lookup tables for DFA #56

    DFA56_eot = DFA.unpack(
        u"\21\uffff"
        )

    DFA56_eof = DFA.unpack(
        u"\2\2\17\uffff"
        )

    DFA56_min = DFA.unpack(
        u"\1\52\1\11\17\uffff"
        )

    DFA56_max = DFA.unpack(
        u"\1\52\1\111\17\uffff"
        )

    DFA56_accept = DFA.unpack(
        u"\2\uffff\1\2\1\uffff\1\1\14\uffff"
        )

    DFA56_special = DFA.unpack(
        u"\21\uffff"
        )

            
    DFA56_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\2\4\5\uffff\1\4\1\uffff\1\4\47\uffff\2\4\4\uffff\1"
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

    # class definition for DFA #56

    class DFA56(DFA):
        pass


    # lookup tables for DFA #58

    DFA58_eot = DFA.unpack(
        u"\22\uffff"
        )

    DFA58_eof = DFA.unpack(
        u"\22\uffff"
        )

    DFA58_min = DFA.unpack(
        u"\1\52\1\11\20\uffff"
        )

    DFA58_max = DFA.unpack(
        u"\1\105\1\111\20\uffff"
        )

    DFA58_accept = DFA.unpack(
        u"\2\uffff\1\2\1\1\16\uffff"
        )

    DFA58_special = DFA.unpack(
        u"\22\uffff"
        )

            
    DFA58_transition = [
        DFA.unpack(u"\1\1\32\uffff\1\2"),
        DFA.unpack(u"\2\3\3\uffff\1\3\1\uffff\1\3\1\uffff\1\3\47\uffff\2"
        u"\3\4\uffff\1\3\1\uffff\1\3\1\uffff\1\3\1\2\4\3"),
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

    # class definition for DFA #58

    class DFA58(DFA):
        pass


 

    FOLLOW_NEWLINE_in_file78 = frozenset([1, 6, 7, 9, 10, 14, 16, 18, 40, 41, 58, 59, 64, 66, 68, 70, 71, 72, 73])
    FOLLOW_statement_in_file82 = frozenset([1, 6, 7, 9, 10, 14, 16, 18, 40, 41, 58, 59, 64, 66, 68, 70, 71, 72, 73])
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
    FOLLOW_INDENT_in_then390 = frozenset([9, 10, 14, 16, 18, 20, 22, 23, 24, 25, 26, 58, 59, 64, 66, 68, 70, 71, 72, 73])
    FOLLOW_action_in_then394 = frozenset([5, 9, 10, 14, 16, 18, 20, 22, 23, 24, 25, 26, 58, 59, 64, 66, 68, 70, 71, 72, 73])
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
    FOLLOW_LPAREN_in_classConstraint536 = frozenset([9, 10, 14, 16, 18, 19, 58, 59, 64, 66, 68, 70, 71, 72, 73])
    FOLLOW_constraint_in_classConstraint542 = frozenset([19])
    FOLLOW_RPAREN_in_classConstraint549 = frozenset([1])
    FOLLOW_attributeAction_in_action569 = frozenset([1])
    FOLLOW_deleteAction_in_action578 = frozenset([1])
    FOLLOW_insertAction_in_action590 = frozenset([1])
    FOLLOW_modifyAction_in_action602 = frozenset([1])
    FOLLOW_haltAction_in_action614 = frozenset([1])
    FOLLOW_simpleStmt_in_action628 = frozenset([1])
    FOLLOW_expressionStmt_in_simpleStmt654 = frozenset([1])
    FOLLOW_printStmt_in_simpleStmt668 = frozenset([1])
    FOLLOW_PRINT_in_printStmt699 = frozenset([6, 9, 10, 14, 16, 18, 21, 58, 59, 64, 66, 68, 70, 71, 72, 73])
    FOLLOW_comparisonList_in_printStmt713 = frozenset([6])
    FOLLOW_RIGHTSHIFT_in_printStmt725 = frozenset([9, 10, 14, 16, 18, 58, 59, 64, 66, 68, 70, 71, 72, 73])
    FOLLOW_comparisonList_in_printStmt729 = frozenset([6])
    FOLLOW_NEWLINE_in_printStmt736 = frozenset([1])
    FOLLOW_DELETE_in_deleteAction754 = frozenset([16])
    FOLLOW_OBJECTBINDING_in_deleteAction756 = frozenset([6])
    FOLLOW_NEWLINE_in_deleteAction760 = frozenset([1])
    FOLLOW_INSERT_in_insertAction778 = frozenset([9])
    FOLLOW_NAME_in_insertAction780 = frozenset([18])
    FOLLOW_LPAREN_in_insertAction782 = frozenset([9, 10, 14, 16, 18, 19, 58, 59, 64, 66, 68, 70, 71, 72, 73])
    FOLLOW_argumentList_in_insertAction794 = frozenset([19])
    FOLLOW_RPAREN_in_insertAction801 = frozenset([6])
    FOLLOW_NEWLINE_in_insertAction805 = frozenset([1])
    FOLLOW_MODIFY_in_modifyAction823 = frozenset([16])
    FOLLOW_OBJECTBINDING_in_modifyAction825 = frozenset([8])
    FOLLOW_COLON_in_modifyAction827 = frozenset([6])
    FOLLOW_NEWLINE_in_modifyAction829 = frozenset([4])
    FOLLOW_INDENT_in_modifyAction839 = frozenset([9])
    FOLLOW_propertyAssignment_in_modifyAction843 = frozenset([5, 9])
    FOLLOW_DEDENT_in_modifyAction850 = frozenset([1])
    FOLLOW_ATTRIBUTE_in_attributeAction868 = frozenset([9, 10, 14, 16, 18, 58, 59, 64, 66, 68, 70, 71, 72, 73])
    FOLLOW_expressionStmt_in_attributeAction870 = frozenset([1])
    FOLLOW_HALT_in_haltAction890 = frozenset([6])
    FOLLOW_NEWLINE_in_haltAction894 = frozenset([1])
    FOLLOW_NAME_in_propertyAssignment912 = frozenset([27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39])
    FOLLOW_assignment_in_propertyAssignment914 = frozenset([9, 10, 14, 16, 18, 58, 59, 64, 66, 68, 70, 71, 72, 73])
    FOLLOW_constraint_in_propertyAssignment916 = frozenset([6])
    FOLLOW_NEWLINE_in_propertyAssignment920 = frozenset([1])
    FOLLOW_comparisonList_in_expressionStmt940 = frozenset([6, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39])
    FOLLOW_assignment_in_expressionStmt952 = frozenset([9, 10, 14, 16, 18, 58, 59, 64, 66, 68, 70, 71, 72, 73])
    FOLLOW_comparisonList_in_expressionStmt956 = frozenset([6])
    FOLLOW_NEWLINE_in_expressionStmt963 = frozenset([1])
    FOLLOW_ASSIGN_in_assignment981 = frozenset([1])
    FOLLOW_PLUSEQUAL_in_assignment1000 = frozenset([1])
    FOLLOW_MINUSEQUAL_in_assignment1016 = frozenset([1])
    FOLLOW_STAREQUAL_in_assignment1031 = frozenset([1])
    FOLLOW_SLASHEQUAL_in_assignment1047 = frozenset([1])
    FOLLOW_PERCENTEQUAL_in_assignment1062 = frozenset([1])
    FOLLOW_AMPEREQUAL_in_assignment1075 = frozenset([1])
    FOLLOW_VBAREQUAL_in_assignment1090 = frozenset([1])
    FOLLOW_CIRCUMFLEXEQUAL_in_assignment1106 = frozenset([1])
    FOLLOW_LEFTSHIFTEQUAL_in_assignment1116 = frozenset([1])
    FOLLOW_RIGHTSHIFTEQUAL_in_assignment1127 = frozenset([1])
    FOLLOW_DOUBLESTAREQUAL_in_assignment1137 = frozenset([1])
    FOLLOW_DOUBLESLASHEQUAL_in_assignment1147 = frozenset([1])
    FOLLOW_importName_in_importStmt1168 = frozenset([1])
    FOLLOW_importFrom_in_importStmt1176 = frozenset([1])
    FOLLOW_IMPORT_in_importName1196 = frozenset([9])
    FOLLOW_dottedAsNames_in_importName1198 = frozenset([6])
    FOLLOW_NEWLINE_in_importName1202 = frozenset([1])
    FOLLOW_FROM_in_importFrom1220 = frozenset([9])
    FOLLOW_dottedName_in_importFrom1224 = frozenset([40])
    FOLLOW_IMPORT_in_importFrom1228 = frozenset([9, 18])
    FOLLOW_importAsNames_in_importFrom1242 = frozenset([6])
    FOLLOW_LPAREN_in_importFrom1254 = frozenset([9])
    FOLLOW_importAsNames_in_importFrom1259 = frozenset([19])
    FOLLOW_RPAREN_in_importFrom1261 = frozenset([6])
    FOLLOW_NEWLINE_in_importFrom1273 = frozenset([1])
    FOLLOW_importAsName_in_importAsNames1292 = frozenset([1, 42])
    FOLLOW_COMMA_in_importAsNames1304 = frozenset([9])
    FOLLOW_importAsName_in_importAsNames1308 = frozenset([1, 42])
    FOLLOW_COMMA_in_importAsNames1317 = frozenset([1])
    FOLLOW_NAME_in_importAsName1341 = frozenset([1, 43])
    FOLLOW_AS_in_importAsName1346 = frozenset([9])
    FOLLOW_NAME_in_importAsName1350 = frozenset([1])
    FOLLOW_dottedAsName_in_dottedAsNames1374 = frozenset([1, 42])
    FOLLOW_COMMA_in_dottedAsNames1385 = frozenset([9])
    FOLLOW_dottedAsName_in_dottedAsNames1389 = frozenset([1, 42])
    FOLLOW_dottedName_in_dottedAsName1411 = frozenset([1, 43])
    FOLLOW_AS_in_dottedAsName1417 = frozenset([9])
    FOLLOW_NAME_in_dottedAsName1419 = frozenset([1])
    FOLLOW_NAME_in_dottedName1444 = frozenset([1, 44])
    FOLLOW_DOT_in_dottedName1456 = frozenset([9])
    FOLLOW_NAME_in_dottedName1460 = frozenset([1, 44])
    FOLLOW_orConstraint_in_constraint1483 = frozenset([1])
    FOLLOW_andConstraint_in_orConstraint1505 = frozenset([1, 45])
    FOLLOW_OR_in_orConstraint1517 = frozenset([9, 10, 14, 16, 18, 58, 59, 64, 66, 68, 70, 71, 72, 73])
    FOLLOW_andConstraint_in_orConstraint1521 = frozenset([1, 45])
    FOLLOW_notConstraint_in_andConstraint1546 = frozenset([1, 46])
    FOLLOW_AND_in_andConstraint1558 = frozenset([9, 10, 14, 16, 18, 58, 59, 64, 66, 68, 70, 71, 72, 73])
    FOLLOW_notConstraint_in_andConstraint1562 = frozenset([1, 46])
    FOLLOW_NOT_in_notConstraint1593 = frozenset([9, 10, 14, 16, 18, 58, 59, 64, 66, 68, 70, 71, 72, 73])
    FOLLOW_comparison_in_notConstraint1600 = frozenset([1])
    FOLLOW_expression_in_comparison1622 = frozenset([1, 14, 47, 48, 49, 50, 51, 52, 53, 78, 79])
    FOLLOW_comparisonOperation_in_comparison1632 = frozenset([9, 10, 14, 16, 18, 58, 59, 64, 66, 68, 70, 71, 72, 73])
    FOLLOW_expression_in_comparison1636 = frozenset([1, 14, 47, 48, 49, 50, 51, 52, 53, 78, 79])
    FOLLOW_LESS_in_comparisonOperation1661 = frozenset([1])
    FOLLOW_GREATER_in_comparisonOperation1680 = frozenset([1])
    FOLLOW_EQUAL_in_comparisonOperation1696 = frozenset([1])
    FOLLOW_GREATEREQUAL_in_comparisonOperation1714 = frozenset([1])
    FOLLOW_LESSEQUAL_in_comparisonOperation1725 = frozenset([1])
    FOLLOW_ALT_NOTEQUAL_in_comparisonOperation1739 = frozenset([1])
    FOLLOW_NOTEQUAL_in_comparisonOperation1750 = frozenset([1])
    FOLLOW_IN_in_comparisonOperation1765 = frozenset([1])
    FOLLOW_NOT_in_comparisonOperation1784 = frozenset([78])
    FOLLOW_IN_in_comparisonOperation1786 = frozenset([1])
    FOLLOW_IS_in_comparisonOperation1799 = frozenset([1])
    FOLLOW_IS_in_comparisonOperation1818 = frozenset([14])
    FOLLOW_NOT_in_comparisonOperation1820 = frozenset([1])
    FOLLOW_bitwiseOrExpr_in_expression1845 = frozenset([1])
    FOLLOW_bitwiseXorExpr_in_bitwiseOrExpr1867 = frozenset([1, 54])
    FOLLOW_VBAR_in_bitwiseOrExpr1879 = frozenset([9, 10, 14, 16, 18, 58, 59, 64, 66, 68, 70, 71, 72, 73])
    FOLLOW_bitwiseXorExpr_in_bitwiseOrExpr1883 = frozenset([1, 54])
    FOLLOW_bitwiseAndExpr_in_bitwiseXorExpr1908 = frozenset([1, 55])
    FOLLOW_CIRCUMFLEX_in_bitwiseXorExpr1920 = frozenset([9, 10, 14, 16, 18, 58, 59, 64, 66, 68, 70, 71, 72, 73])
    FOLLOW_bitwiseAndExpr_in_bitwiseXorExpr1924 = frozenset([1, 55])
    FOLLOW_shiftExpr_in_bitwiseAndExpr1949 = frozenset([1, 56])
    FOLLOW_AMPER_in_bitwiseAndExpr1961 = frozenset([9, 10, 14, 16, 18, 58, 59, 64, 66, 68, 70, 71, 72, 73])
    FOLLOW_shiftExpr_in_bitwiseAndExpr1965 = frozenset([1, 56])
    FOLLOW_arithExpr_in_shiftExpr1990 = frozenset([1, 21, 57])
    FOLLOW_LEFTSHIFT_in_shiftExpr2004 = frozenset([9, 10, 14, 16, 18, 58, 59, 64, 66, 68, 70, 71, 72, 73])
    FOLLOW_RIGHTSHIFT_in_shiftExpr2010 = frozenset([9, 10, 14, 16, 18, 58, 59, 64, 66, 68, 70, 71, 72, 73])
    FOLLOW_arithExpr_in_shiftExpr2028 = frozenset([1, 21, 57])
    FOLLOW_term_in_arithExpr2053 = frozenset([1, 58, 59])
    FOLLOW_PLUS_in_arithExpr2067 = frozenset([9, 10, 14, 16, 18, 58, 59, 64, 66, 68, 70, 71, 72, 73])
    FOLLOW_MINUS_in_arithExpr2073 = frozenset([9, 10, 14, 16, 18, 58, 59, 64, 66, 68, 70, 71, 72, 73])
    FOLLOW_term_in_arithExpr2091 = frozenset([1, 58, 59])
    FOLLOW_factor_in_term2116 = frozenset([1, 60, 61, 62, 63])
    FOLLOW_STAR_in_term2129 = frozenset([9, 10, 14, 16, 18, 58, 59, 64, 66, 68, 70, 71, 72, 73])
    FOLLOW_SLASH_in_term2135 = frozenset([9, 10, 14, 16, 18, 58, 59, 64, 66, 68, 70, 71, 72, 73])
    FOLLOW_PERCENT_in_term2151 = frozenset([9, 10, 14, 16, 18, 58, 59, 64, 66, 68, 70, 71, 72, 73])
    FOLLOW_DOUBLESLASH_in_term2157 = frozenset([9, 10, 14, 16, 18, 58, 59, 64, 66, 68, 70, 71, 72, 73])
    FOLLOW_factor_in_term2179 = frozenset([1, 60, 61, 62, 63])
    FOLLOW_PLUS_in_factor2202 = frozenset([9, 10, 14, 16, 18, 58, 59, 64, 66, 68, 70, 71, 72, 73])
    FOLLOW_factor_in_factor2207 = frozenset([1])
    FOLLOW_MINUS_in_factor2215 = frozenset([9, 10, 14, 16, 18, 58, 59, 64, 66, 68, 70, 71, 72, 73])
    FOLLOW_factor_in_factor2219 = frozenset([1])
    FOLLOW_TILDE_in_factor2227 = frozenset([9, 10, 14, 16, 18, 58, 59, 64, 66, 68, 70, 71, 72, 73])
    FOLLOW_factor_in_factor2231 = frozenset([1])
    FOLLOW_power_in_factor2239 = frozenset([1])
    FOLLOW_atom_in_power2259 = frozenset([1, 18, 44, 65])
    FOLLOW_trailer_in_power2271 = frozenset([1, 18, 44, 65])
    FOLLOW_DOUBLESTAR_in_power2292 = frozenset([9, 10, 14, 16, 18, 58, 59, 64, 66, 68, 70, 71, 72, 73])
    FOLLOW_factor_in_power2294 = frozenset([1])
    FOLLOW_LPAREN_in_atom2317 = frozenset([9, 10, 14, 16, 18, 19, 58, 59, 64, 66, 68, 70, 71, 72, 73])
    FOLLOW_comparisonList_in_atom2356 = frozenset([19])
    FOLLOW_RPAREN_in_atom2385 = frozenset([1])
    FOLLOW_LBRACK_in_atom2393 = frozenset([9, 10, 14, 16, 18, 58, 59, 64, 66, 67, 68, 70, 71, 72, 73])
    FOLLOW_listmaker_in_atom2430 = frozenset([67])
    FOLLOW_RBRACK_in_atom2459 = frozenset([1])
    FOLLOW_LCURLY_in_atom2467 = frozenset([9, 10, 14, 16, 18, 58, 59, 64, 66, 68, 69, 70, 71, 72, 73])
    FOLLOW_dictmaker_in_atom2504 = frozenset([69])
    FOLLOW_RCURLY_in_atom2533 = frozenset([1])
    FOLLOW_NAME_in_atom2542 = frozenset([1])
    FOLLOW_OBJECTBINDING_in_atom2561 = frozenset([1])
    FOLLOW_INT_in_atom2571 = frozenset([1])
    FOLLOW_LONGINT_in_atom2591 = frozenset([1])
    FOLLOW_FLOAT_in_atom2607 = frozenset([1])
    FOLLOW_COMPLEX_in_atom2625 = frozenset([1])
    FOLLOW_STRING_in_atom2645 = frozenset([1, 10])
    FOLLOW_constraint_in_listmaker2670 = frozenset([1, 42])
    FOLLOW_COMMA_in_listmaker2688 = frozenset([9, 10, 14, 16, 18, 58, 59, 64, 66, 68, 70, 71, 72, 73])
    FOLLOW_constraint_in_listmaker2692 = frozenset([1, 42])
    FOLLOW_COMMA_in_listmaker2707 = frozenset([1])
    FOLLOW_constraint_in_comparisonList2732 = frozenset([1, 42])
    FOLLOW_COMMA_in_comparisonList2750 = frozenset([9, 10, 14, 16, 18, 58, 59, 64, 66, 68, 70, 71, 72, 73])
    FOLLOW_constraint_in_comparisonList2754 = frozenset([1, 42])
    FOLLOW_COMMA_in_comparisonList2769 = frozenset([1])
    FOLLOW_LPAREN_in_trailer2792 = frozenset([9, 10, 14, 16, 18, 19, 58, 59, 64, 66, 68, 70, 71, 72, 73])
    FOLLOW_argumentList_in_trailer2797 = frozenset([19])
    FOLLOW_RPAREN_in_trailer2804 = frozenset([1])
    FOLLOW_DOT_in_trailer2812 = frozenset([9])
    FOLLOW_NAME_in_trailer2814 = frozenset([1])
    FOLLOW_expression_in_expressionList2837 = frozenset([1, 42])
    FOLLOW_COMMA_in_expressionList2857 = frozenset([9, 10, 14, 16, 18, 58, 59, 64, 66, 68, 70, 71, 72, 73])
    FOLLOW_expression_in_expressionList2861 = frozenset([1, 42])
    FOLLOW_COMMA_in_expressionList2876 = frozenset([1])
    FOLLOW_constraint_in_dictmaker2901 = frozenset([8])
    FOLLOW_COLON_in_dictmaker2911 = frozenset([9, 10, 14, 16, 18, 58, 59, 64, 66, 68, 70, 71, 72, 73])
    FOLLOW_constraint_in_dictmaker2915 = frozenset([1, 42])
    FOLLOW_COMMA_in_dictmaker2936 = frozenset([9, 10, 14, 16, 18, 58, 59, 64, 66, 68, 70, 71, 72, 73])
    FOLLOW_constraint_in_dictmaker2940 = frozenset([8])
    FOLLOW_COLON_in_dictmaker2942 = frozenset([9, 10, 14, 16, 18, 58, 59, 64, 66, 68, 70, 71, 72, 73])
    FOLLOW_constraint_in_dictmaker2946 = frozenset([1, 42])
    FOLLOW_COMMA_in_dictmaker2963 = frozenset([1])
    FOLLOW_constraint_in_argumentList2988 = frozenset([1, 42])
    FOLLOW_COMMA_in_argumentList3000 = frozenset([9, 10, 14, 16, 18, 58, 59, 64, 66, 68, 70, 71, 72, 73])
    FOLLOW_constraint_in_argumentList3004 = frozenset([1, 42])
    FOLLOW_COMMA_in_argumentList3019 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("PolicyLexer", PolicyParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
