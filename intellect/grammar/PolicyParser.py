# $ANTLR 3.1.3 Mar 17, 2009 19:23:44 /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g 2012-04-10 15:14:34

import sys
from antlr3 import *
from antlr3.compat import set, frozenset
         
from intellect.Node import *



# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
SLASHEQUAL=38
BACKQUOTE=80
EXPONENT=84
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
IMPORT=7
NAME=12
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
PERCENTEQUAL=39
LESSEQUAL=53
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

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "INDENT", "DEDENT", "NEWLINE", "IMPORT", "FROM", "LPAREN", "RPAREN", 
    "COMMA", "NAME", "AS", "DOT", "RULE", "COLON", "STRING", "AGENDAGROUP", 
    "WHEN", "THEN", "NOT", "EXISTS", "OBJECTBINDING", "ASSIGNEQUAL", "ATTRIBUTE", 
    "PRINT", "RIGHTSHIFT", "FORGET", "DELETE", "LEARN", "INSERT", "MODIFY", 
    "HALT", "ASSIGN", "PLUSEQUAL", "MINUSEQUAL", "STAREQUAL", "SLASHEQUAL", 
    "PERCENTEQUAL", "AMPEREQUAL", "VBAREQUAL", "CIRCUMFLEXEQUAL", "LEFTSHIFTEQUAL", 
    "RIGHTSHIFTEQUAL", "DOUBLESTAREQUAL", "DOUBLESLASHEQUAL", "OR", "AND", 
    "LESS", "GREATER", "EQUAL", "GREATEREQUAL", "LESSEQUAL", "ALT_NOTEQUAL", 
    "NOTEQUAL", "IN", "IS", "VBAR", "CIRCUMFLEX", "AMPER", "LEFTSHIFT", 
    "PLUS", "MINUS", "STAR", "SLASH", "PERCENT", "DOUBLESLASH", "TILDE", 
    "DOUBLESTAR", "LBRACK", "RBRACK", "LCURLY", "RCURLY", "INT", "LONGINT", 
    "FLOAT", "COMPLEX", "SEMI", "DOLLAR", "BACKQUOTE", "GLOBAL", "LETTER", 
    "DIGIT", "EXPONENT", "TRIAPOS", "TRIQUOTE", "ESC", "CONTINUED_LINE", 
    "WS", "LEADING_WS", "COMMENT"
]




class PolicyParser(Parser):
    grammarFileName = "/Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g"
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
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:61:1: file returns [object] : ( ( NEWLINE | statement )+ | EOF );
    def file(self, ):

        object = None

        statement1 = None


        object = File() 
        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:63:3: ( ( NEWLINE | statement )+ | EOF )
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if ((NEWLINE <= LA2_0 <= LPAREN) or LA2_0 == NAME or LA2_0 == RULE or LA2_0 == STRING or LA2_0 == NOT or LA2_0 == OBJECTBINDING or (PLUS <= LA2_0 <= MINUS) or LA2_0 == TILDE or LA2_0 == LBRACK or LA2_0 == LCURLY or (INT <= LA2_0 <= COMPLEX)) :
                    alt2 = 1
                elif (LA2_0 == EOF) :
                    alt2 = 2
                else:
                    nvae = NoViableAltException("", 2, 0, self.input)

                    raise nvae

                if alt2 == 1:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:63:5: ( NEWLINE | statement )+
                    pass 
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:63:5: ( NEWLINE | statement )+
                    cnt1 = 0
                    while True: #loop1
                        alt1 = 3
                        LA1_0 = self.input.LA(1)

                        if (LA1_0 == NEWLINE) :
                            alt1 = 1
                        elif ((IMPORT <= LA1_0 <= LPAREN) or LA1_0 == NAME or LA1_0 == RULE or LA1_0 == STRING or LA1_0 == NOT or LA1_0 == OBJECTBINDING or (PLUS <= LA1_0 <= MINUS) or LA1_0 == TILDE or LA1_0 == LBRACK or LA1_0 == LCURLY or (INT <= LA1_0 <= COMPLEX)) :
                            alt1 = 2


                        if alt1 == 1:
                            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:63:7: NEWLINE
                            pass 
                            self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_file78)


                        elif alt1 == 2:
                            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:63:17: statement
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
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:64:5: EOF
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
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:67:1: statement returns [object] : ( importStmt | attributeStmt | ruleStmt );
    def statement(self, ):

        object = None

        importStmt2 = None

        attributeStmt3 = None

        ruleStmt4 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:68:3: ( importStmt | attributeStmt | ruleStmt )
                alt3 = 3
                LA3 = self.input.LA(1)
                if LA3 == IMPORT or LA3 == FROM:
                    alt3 = 1
                elif LA3 == LPAREN or LA3 == NAME or LA3 == STRING or LA3 == NOT or LA3 == OBJECTBINDING or LA3 == PLUS or LA3 == MINUS or LA3 == TILDE or LA3 == LBRACK or LA3 == LCURLY or LA3 == INT or LA3 == LONGINT or LA3 == FLOAT or LA3 == COMPLEX:
                    alt3 = 2
                elif LA3 == RULE:
                    alt3 = 3
                else:
                    nvae = NoViableAltException("", 3, 0, self.input)

                    raise nvae

                if alt3 == 1:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:68:5: importStmt
                    pass 
                    self._state.following.append(self.FOLLOW_importStmt_in_statement111)
                    importStmt2 = self.importStmt()

                    self._state.following.pop()
                    #action start
                    object = Statement( importStmt2, importStmt2.line, importStmt2.column ) 
                    #action end


                elif alt3 == 2:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:69:5: attributeStmt
                    pass 
                    self._state.following.append(self.FOLLOW_attributeStmt_in_statement120)
                    attributeStmt3 = self.attributeStmt()

                    self._state.following.pop()
                    #action start
                    object = Statement( attributeStmt3 ) 
                    #action end


                elif alt3 == 3:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:70:5: ruleStmt
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


    # $ANTLR start "importStmt"
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:73:1: importStmt returns [object] : ( importName | importFrom );
    def importStmt(self, ):

        object = None

        importName5 = None

        importFrom6 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:74:3: ( importName | importFrom )
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == IMPORT) :
                    alt4 = 1
                elif (LA4_0 == FROM) :
                    alt4 = 2
                else:
                    nvae = NoViableAltException("", 4, 0, self.input)

                    raise nvae

                if alt4 == 1:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:74:5: importName
                    pass 
                    self._state.following.append(self.FOLLOW_importName_in_importStmt152)
                    importName5 = self.importName()

                    self._state.following.pop()
                    #action start
                    object = ImportStmt( children = importName5, line = importName5.line ) 
                    #action end


                elif alt4 == 2:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:75:5: importFrom
                    pass 
                    self._state.following.append(self.FOLLOW_importFrom_in_importStmt160)
                    importFrom6 = self.importFrom()

                    self._state.following.pop()
                    #action start
                    object = ImportStmt( children = importFrom6, line = importFrom6.line ) 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "importStmt"


    # $ANTLR start "importName"
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:78:1: importName returns [object] : IMPORT dottedAsNames NEWLINE ;
    def importName(self, ):

        object = None

        IMPORT7 = None
        dottedAsNames8 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:79:3: ( IMPORT dottedAsNames NEWLINE )
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:79:5: IMPORT dottedAsNames NEWLINE
                pass 
                IMPORT7=self.match(self.input, IMPORT, self.FOLLOW_IMPORT_in_importName180)
                self._state.following.append(self.FOLLOW_dottedAsNames_in_importName182)
                dottedAsNames8 = self.dottedAsNames()

                self._state.following.pop()
                #action start
                object = ImportName( children = [IMPORT7.text, dottedAsNames8], line = IMPORT7.getLine() ) 
                #action end
                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_importName186)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "importName"


    # $ANTLR start "importFrom"
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:82:1: importFrom returns [object] : FROM dottedName IMPORT (importAsNames1= importAsNames | LPAREN importAsNames2= importAsNames RPAREN ) NEWLINE ;
    def importFrom(self, ):

        object = None

        FROM9 = None
        IMPORT11 = None
        LPAREN12 = None
        RPAREN13 = None
        importAsNames1 = None

        importAsNames2 = None

        dottedName10 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:83:3: ( FROM dottedName IMPORT (importAsNames1= importAsNames | LPAREN importAsNames2= importAsNames RPAREN ) NEWLINE )
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:83:5: FROM dottedName IMPORT (importAsNames1= importAsNames | LPAREN importAsNames2= importAsNames RPAREN ) NEWLINE
                pass 
                FROM9=self.match(self.input, FROM, self.FOLLOW_FROM_in_importFrom204)
                #action start
                object = ImportFrom( children = FROM9.text, line = FROM9.getLine() ) 
                #action end
                self._state.following.append(self.FOLLOW_dottedName_in_importFrom208)
                dottedName10 = self.dottedName()

                self._state.following.pop()
                #action start
                object.append_child( dottedName10 ) 
                #action end
                IMPORT11=self.match(self.input, IMPORT, self.FOLLOW_IMPORT_in_importFrom212)
                #action start
                object.append_child( IMPORT11.text ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:84:7: (importAsNames1= importAsNames | LPAREN importAsNames2= importAsNames RPAREN )
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == NAME) :
                    alt5 = 1
                elif (LA5_0 == LPAREN) :
                    alt5 = 2
                else:
                    nvae = NoViableAltException("", 5, 0, self.input)

                    raise nvae

                if alt5 == 1:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:84:9: importAsNames1= importAsNames
                    pass 
                    self._state.following.append(self.FOLLOW_importAsNames_in_importFrom226)
                    importAsNames1 = self.importAsNames()

                    self._state.following.pop()
                    #action start
                    object.append_child( importAsNames1 ) 
                    #action end


                elif alt5 == 2:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:85:9: LPAREN importAsNames2= importAsNames RPAREN
                    pass 
                    LPAREN12=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_importFrom238)
                    self._state.following.append(self.FOLLOW_importAsNames_in_importFrom243)
                    importAsNames2 = self.importAsNames()

                    self._state.following.pop()
                    RPAREN13=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_importFrom245)
                    #action start
                    object.append_children( [LPAREN12.text, importAsNames2, RPAREN13.text] ) 
                    #action end



                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_importFrom257)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "importFrom"


    # $ANTLR start "importAsNames"
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:89:1: importAsNames returns [object] : importAsName1= importAsName ( COMMA importAsName2= importAsName )* ( COMMA )? ;
    def importAsNames(self, ):

        object = None

        importAsName1 = None

        importAsName2 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:90:3: (importAsName1= importAsName ( COMMA importAsName2= importAsName )* ( COMMA )? )
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:90:5: importAsName1= importAsName ( COMMA importAsName2= importAsName )* ( COMMA )?
                pass 
                self._state.following.append(self.FOLLOW_importAsName_in_importAsNames276)
                importAsName1 = self.importAsName()

                self._state.following.pop()
                #action start
                object=ImportAsNames( importAsName1 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:91:7: ( COMMA importAsName2= importAsName )*
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == COMMA) :
                        LA6_1 = self.input.LA(2)

                        if (LA6_1 == NAME) :
                            alt6 = 1




                    if alt6 == 1:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:91:9: COMMA importAsName2= importAsName
                        pass 
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_importAsNames288)
                        self._state.following.append(self.FOLLOW_importAsName_in_importAsNames292)
                        importAsName2 = self.importAsName()

                        self._state.following.pop()
                        #action start
                        object.append_children( [",", importAsName2] ) 
                        #action end


                    else:
                        break #loop6
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:91:105: ( COMMA )?
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if (LA7_0 == COMMA) :
                    alt7 = 1
                if alt7 == 1:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:91:107: COMMA
                    pass 
                    self.match(self.input, COMMA, self.FOLLOW_COMMA_in_importAsNames301)
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
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:94:1: importAsName returns [object] : name1= NAME ( AS name2= NAME )? ;
    def importAsName(self, ):

        object = None

        name1 = None
        name2 = None
        AS14 = None

        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:95:3: (name1= NAME ( AS name2= NAME )? )
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:95:5: name1= NAME ( AS name2= NAME )?
                pass 
                name1=self.match(self.input, NAME, self.FOLLOW_NAME_in_importAsName325)
                #action start
                object=ImportAsName( name1.text ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:95:56: ( AS name2= NAME )?
                alt8 = 2
                LA8_0 = self.input.LA(1)

                if (LA8_0 == AS) :
                    alt8 = 1
                if alt8 == 1:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:95:58: AS name2= NAME
                    pass 
                    AS14=self.match(self.input, AS, self.FOLLOW_AS_in_importAsName331)
                    name2=self.match(self.input, NAME, self.FOLLOW_NAME_in_importAsName335)
                    #action start
                    object.append_children( [AS14.text, name2.text] ) 
                    #action end







            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "importAsName"


    # $ANTLR start "dottedAsNames"
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:98:1: dottedAsNames returns [object] : dottedAsName1= dottedAsName ( COMMA dottedAsName2= dottedAsName )* ;
    def dottedAsNames(self, ):

        object = None

        COMMA15 = None
        dottedAsName1 = None

        dottedAsName2 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:99:3: (dottedAsName1= dottedAsName ( COMMA dottedAsName2= dottedAsName )* )
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:99:5: dottedAsName1= dottedAsName ( COMMA dottedAsName2= dottedAsName )*
                pass 
                self._state.following.append(self.FOLLOW_dottedAsName_in_dottedAsNames359)
                dottedAsName1 = self.dottedAsName()

                self._state.following.pop()
                #action start
                object = DottedAsNames( dottedAsName1 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:100:7: ( COMMA dottedAsName2= dottedAsName )*
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == COMMA) :
                        alt9 = 1


                    if alt9 == 1:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:100:9: COMMA dottedAsName2= dottedAsName
                        pass 
                        COMMA15=self.match(self.input, COMMA, self.FOLLOW_COMMA_in_dottedAsNames371)
                        self._state.following.append(self.FOLLOW_dottedAsName_in_dottedAsNames375)
                        dottedAsName2 = self.dottedAsName()

                        self._state.following.pop()
                        #action start
                        object.append_children( [COMMA15.text, dottedAsName2] ) 
                        #action end


                    else:
                        break #loop9




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "dottedAsNames"


    # $ANTLR start "dottedAsName"
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:103:1: dottedAsName returns [object] : dottedName ( AS NAME )? ;
    def dottedAsName(self, ):

        object = None

        AS17 = None
        NAME18 = None
        dottedName16 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:104:3: ( dottedName ( AS NAME )? )
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:104:5: dottedName ( AS NAME )?
                pass 
                self._state.following.append(self.FOLLOW_dottedName_in_dottedAsName397)
                dottedName16 = self.dottedName()

                self._state.following.pop()
                #action start
                object = DottedAsName( dottedName16 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:104:65: ( AS NAME )?
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == AS) :
                    alt10 = 1
                if alt10 == 1:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:104:67: AS NAME
                    pass 
                    AS17=self.match(self.input, AS, self.FOLLOW_AS_in_dottedAsName403)
                    NAME18=self.match(self.input, NAME, self.FOLLOW_NAME_in_dottedAsName405)
                    #action start
                    object.append_children( [AS17.text, NAME18.text] ) 
                    #action end







            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "dottedAsName"


    # $ANTLR start "dottedName"
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:107:1: dottedName returns [object] : name1= NAME ( DOT name2= NAME )* ;
    def dottedName(self, ):

        object = None

        name1 = None
        name2 = None
        DOT19 = None

        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:108:3: (name1= NAME ( DOT name2= NAME )* )
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:108:5: name1= NAME ( DOT name2= NAME )*
                pass 
                name1=self.match(self.input, NAME, self.FOLLOW_NAME_in_dottedName430)
                #action start
                object = DottedName( name1.text ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:109:7: ( DOT name2= NAME )*
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == DOT) :
                        alt11 = 1


                    if alt11 == 1:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:109:9: DOT name2= NAME
                        pass 
                        DOT19=self.match(self.input, DOT, self.FOLLOW_DOT_in_dottedName442)
                        name2=self.match(self.input, NAME, self.FOLLOW_NAME_in_dottedName446)
                        #action start
                        object.append_children( [DOT19.text, name2.text] ) 
                        #action end


                    else:
                        break #loop11




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "dottedName"


    # $ANTLR start "attributeStmt"
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:112:1: attributeStmt returns [object] : expressionStmt ;
    def attributeStmt(self, ):

        object = None

        expressionStmt20 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:113:3: ( expressionStmt )
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:113:5: expressionStmt
                pass 
                self._state.following.append(self.FOLLOW_expressionStmt_in_attributeStmt469)
                expressionStmt20 = self.expressionStmt()

                self._state.following.pop()
                #action start
                object = AttributeStmt( expressionStmt20 ) 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "attributeStmt"


    # $ANTLR start "ruleStmt"
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:116:1: ruleStmt returns [object] : RULE id COLON NEWLINE INDENT ( ruleAttribute )* ( when )? then DEDENT ;
    def ruleStmt(self, ):

        object = None

        RULE21 = None
        COLON23 = None
        id22 = None

        ruleAttribute24 = None

        when25 = None

        then26 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:117:3: ( RULE id COLON NEWLINE INDENT ( ruleAttribute )* ( when )? then DEDENT )
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:117:5: RULE id COLON NEWLINE INDENT ( ruleAttribute )* ( when )? then DEDENT
                pass 
                RULE21=self.match(self.input, RULE, self.FOLLOW_RULE_in_ruleStmt489)
                self._state.following.append(self.FOLLOW_id_in_ruleStmt491)
                id22 = self.id()

                self._state.following.pop()
                COLON23=self.match(self.input, COLON, self.FOLLOW_COLON_in_ruleStmt493)
                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_ruleStmt495)
                #action start
                object = RuleStmt( [ RULE21.text, id22, COLON23.text ], RULE21.getLine(), RULE21.getCharPositionInLine() ) 
                #action end
                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_ruleStmt505)
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:118:14: ( ruleAttribute )*
                while True: #loop12
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 == AGENDAGROUP) :
                        alt12 = 1


                    if alt12 == 1:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:118:16: ruleAttribute
                        pass 
                        self._state.following.append(self.FOLLOW_ruleAttribute_in_ruleStmt509)
                        ruleAttribute24 = self.ruleAttribute()

                        self._state.following.pop()
                        #action start
                        object.append_child( ruleAttribute24 ) 
                        #action end


                    else:
                        break #loop12
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:119:14: ( when )?
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if (LA13_0 == WHEN) :
                    alt13 = 1
                if alt13 == 1:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:119:16: when
                    pass 
                    self._state.following.append(self.FOLLOW_when_in_ruleStmt531)
                    when25 = self.when()

                    self._state.following.pop()
                    #action start
                    object.append_child( when25 ) 
                    #action end



                self._state.following.append(self.FOLLOW_then_in_ruleStmt551)
                then26 = self.then()

                self._state.following.pop()
                #action start
                object.append_child( then26 ) 
                #action end
                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_ruleStmt556)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "ruleStmt"


    # $ANTLR start "id"
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:123:1: id returns [object] : ( NAME | STRING );
    def id(self, ):

        object = None

        NAME27 = None
        STRING28 = None

        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:124:3: ( NAME | STRING )
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if (LA14_0 == NAME) :
                    alt14 = 1
                elif (LA14_0 == STRING) :
                    alt14 = 2
                else:
                    nvae = NoViableAltException("", 14, 0, self.input)

                    raise nvae

                if alt14 == 1:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:124:5: NAME
                    pass 
                    NAME27=self.match(self.input, NAME, self.FOLLOW_NAME_in_id574)
                    #action start
                    object = Id( NAME27.text ) 
                    #action end


                elif alt14 == 2:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:125:5: STRING
                    pass 
                    STRING28=self.match(self.input, STRING, self.FOLLOW_STRING_in_id585)
                    #action start
                    object = Id( STRING28.text ) 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "id"


    # $ANTLR start "ruleAttribute"
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:128:1: ruleAttribute returns [object] : agendaGroup ;
    def ruleAttribute(self, ):

        object = None

        agendaGroup29 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:129:3: ( agendaGroup )
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:129:5: agendaGroup
                pass 
                self._state.following.append(self.FOLLOW_agendaGroup_in_ruleAttribute606)
                agendaGroup29 = self.agendaGroup()

                self._state.following.pop()
                #action start
                object = RuleAttribute( agendaGroup29, agendaGroup29.line, agendaGroup29.column ) 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "ruleAttribute"


    # $ANTLR start "agendaGroup"
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:132:1: agendaGroup returns [object] : AGENDAGROUP id NEWLINE ;
    def agendaGroup(self, ):

        object = None

        AGENDAGROUP30 = None
        id31 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:133:3: ( AGENDAGROUP id NEWLINE )
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:133:5: AGENDAGROUP id NEWLINE
                pass 
                AGENDAGROUP30=self.match(self.input, AGENDAGROUP, self.FOLLOW_AGENDAGROUP_in_agendaGroup626)
                self._state.following.append(self.FOLLOW_id_in_agendaGroup628)
                id31 = self.id()

                self._state.following.pop()
                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_agendaGroup630)
                #action start
                object = AgendaGroup( [ AGENDAGROUP30.text, id31 ], AGENDAGROUP30.getLine(), AGENDAGROUP30.getCharPositionInLine() ) 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "agendaGroup"


    # $ANTLR start "when"
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:136:1: when returns [object] : WHEN COLON NEWLINE INDENT ( ruleCondition )? DEDENT ;
    def when(self, ):

        object = None

        WHEN32 = None
        COLON33 = None
        ruleCondition34 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:137:3: ( WHEN COLON NEWLINE INDENT ( ruleCondition )? DEDENT )
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:137:5: WHEN COLON NEWLINE INDENT ( ruleCondition )? DEDENT
                pass 
                WHEN32=self.match(self.input, WHEN, self.FOLLOW_WHEN_in_when650)
                COLON33=self.match(self.input, COLON, self.FOLLOW_COLON_in_when652)
                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_when654)
                #action start
                object = When( [WHEN32.text, COLON33.text], WHEN32.getLine(), WHEN32.getCharPositionInLine() ) 
                #action end
                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_when664)
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:138:14: ( ruleCondition )?
                alt15 = 2
                LA15_0 = self.input.LA(1)

                if (LA15_0 == NAME or (NOT <= LA15_0 <= OBJECTBINDING)) :
                    alt15 = 1
                if alt15 == 1:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:138:16: ruleCondition
                    pass 
                    self._state.following.append(self.FOLLOW_ruleCondition_in_when668)
                    ruleCondition34 = self.ruleCondition()

                    self._state.following.pop()
                    #action start
                    object.append_child( ruleCondition34 ) 
                    #action end



                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_when675)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "when"


    # $ANTLR start "then"
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:141:1: then returns [object] : THEN COLON NEWLINE INDENT ( action )+ DEDENT ;
    def then(self, ):

        object = None

        THEN35 = None
        COLON36 = None
        action37 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:142:3: ( THEN COLON NEWLINE INDENT ( action )+ DEDENT )
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:142:5: THEN COLON NEWLINE INDENT ( action )+ DEDENT
                pass 
                THEN35=self.match(self.input, THEN, self.FOLLOW_THEN_in_then693)
                COLON36=self.match(self.input, COLON, self.FOLLOW_COLON_in_then695)
                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_then697)
                #action start
                object = Then( [THEN35.text, COLON36.text], THEN35.getLine(), THEN35.getCharPositionInLine() ) 
                #action end
                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_then707)
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:143:14: ( action )+
                cnt16 = 0
                while True: #loop16
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == LPAREN or LA16_0 == NAME or LA16_0 == STRING or LA16_0 == NOT or LA16_0 == OBJECTBINDING or (ATTRIBUTE <= LA16_0 <= PRINT) or (FORGET <= LA16_0 <= HALT) or (PLUS <= LA16_0 <= MINUS) or LA16_0 == TILDE or LA16_0 == LBRACK or LA16_0 == LCURLY or (INT <= LA16_0 <= COMPLEX)) :
                        alt16 = 1


                    if alt16 == 1:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:143:16: action
                        pass 
                        self._state.following.append(self.FOLLOW_action_in_then711)
                        action37 = self.action()

                        self._state.following.pop()
                        #action start
                        object.append_child( action37 ) 
                        #action end


                    else:
                        if cnt16 >= 1:
                            break #loop16

                        eee = EarlyExitException(16, self.input)
                        raise eee

                    cnt16 += 1
                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_then718)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "then"


    # $ANTLR start "ruleCondition"
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:146:1: ruleCondition returns [object] : notCondition NEWLINE ;
    def ruleCondition(self, ):

        object = None

        notCondition38 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:147:3: ( notCondition NEWLINE )
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:147:5: notCondition NEWLINE
                pass 
                self._state.following.append(self.FOLLOW_notCondition_in_ruleCondition736)
                notCondition38 = self.notCondition()

                self._state.following.pop()
                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_ruleCondition738)
                #action start
                object = RuleCondition(notCondition38) 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "ruleCondition"


    # $ANTLR start "notCondition"
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:150:1: notCondition returns [object] : ( NOT )* condition ;
    def notCondition(self, ):

        object = None

        NOT39 = None
        condition40 = None


        object = NotCondition() 
        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:152:3: ( ( NOT )* condition )
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:152:5: ( NOT )* condition
                pass 
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:152:5: ( NOT )*
                while True: #loop17
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if (LA17_0 == NOT) :
                        alt17 = 1


                    if alt17 == 1:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:152:7: NOT
                        pass 
                        NOT39=self.match(self.input, NOT, self.FOLLOW_NOT_in_notCondition766)
                        #action start
                        object.append_child( NOT39.text ) 
                        #action end


                    else:
                        break #loop17
                self._state.following.append(self.FOLLOW_condition_in_notCondition773)
                condition40 = self.condition()

                self._state.following.pop()
                #action start
                object.append_child( condition40 ) 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "notCondition"


    # $ANTLR start "condition"
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:155:1: condition returns [object] : ( EXISTS )? classConstraint ;
    def condition(self, ):

        object = None

        EXISTS41 = None
        classConstraint42 = None


        object = Condition() 
        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:157:3: ( ( EXISTS )? classConstraint )
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:157:5: ( EXISTS )? classConstraint
                pass 
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:157:5: ( EXISTS )?
                alt18 = 2
                LA18_0 = self.input.LA(1)

                if (LA18_0 == EXISTS) :
                    alt18 = 1
                if alt18 == 1:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:157:7: EXISTS
                    pass 
                    EXISTS41=self.match(self.input, EXISTS, self.FOLLOW_EXISTS_in_condition801)
                    #action start
                    object.append_child( EXISTS41.text ) 
                    #action end



                self._state.following.append(self.FOLLOW_classConstraint_in_condition808)
                classConstraint42 = self.classConstraint()

                self._state.following.pop()
                #action start
                object.append_child( classConstraint42 ) 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "condition"


    # $ANTLR start "classConstraint"
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:160:1: classConstraint returns [object] : ( OBJECTBINDING ASSIGNEQUAL )? NAME LPAREN ( constraint )? RPAREN ;
    def classConstraint(self, ):

        object = None

        OBJECTBINDING43 = None
        ASSIGNEQUAL44 = None
        NAME45 = None
        LPAREN46 = None
        RPAREN48 = None
        constraint47 = None


        object = ClassConstraint() 
        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:162:3: ( ( OBJECTBINDING ASSIGNEQUAL )? NAME LPAREN ( constraint )? RPAREN )
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:162:5: ( OBJECTBINDING ASSIGNEQUAL )? NAME LPAREN ( constraint )? RPAREN
                pass 
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:162:5: ( OBJECTBINDING ASSIGNEQUAL )?
                alt19 = 2
                LA19_0 = self.input.LA(1)

                if (LA19_0 == OBJECTBINDING) :
                    alt19 = 1
                if alt19 == 1:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:162:7: OBJECTBINDING ASSIGNEQUAL
                    pass 
                    OBJECTBINDING43=self.match(self.input, OBJECTBINDING, self.FOLLOW_OBJECTBINDING_in_classConstraint836)
                    ASSIGNEQUAL44=self.match(self.input, ASSIGNEQUAL, self.FOLLOW_ASSIGNEQUAL_in_classConstraint838)
                    #action start
                    object.append_children( [ OBJECTBINDING43.text, ASSIGNEQUAL44.text] ) 
                    #action end



                NAME45=self.match(self.input, NAME, self.FOLLOW_NAME_in_classConstraint851)
                LPAREN46=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_classConstraint853)
                #action start
                object.append_children( [NAME45.text, LPAREN46.text] ); 
                #action end
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:163:78: ( constraint )?
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if (LA20_0 == LPAREN or LA20_0 == NAME or LA20_0 == STRING or LA20_0 == NOT or LA20_0 == OBJECTBINDING or (PLUS <= LA20_0 <= MINUS) or LA20_0 == TILDE or LA20_0 == LBRACK or LA20_0 == LCURLY or (INT <= LA20_0 <= COMPLEX)) :
                    alt20 = 1
                if alt20 == 1:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:163:80: constraint
                    pass 
                    self._state.following.append(self.FOLLOW_constraint_in_classConstraint859)
                    constraint47 = self.constraint()

                    self._state.following.pop()
                    #action start
                    object.append_child( constraint47 ) 
                    #action end



                RPAREN48=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_classConstraint866)
                #action start
                object.append_child( RPAREN48.text ) 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "classConstraint"


    # $ANTLR start "action"
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:166:1: action returns [object] : ( simpleStmt | attributeAction | learnAction | forgetAction | modifyAction | haltAction );
    def action(self, ):

        object = None

        simpleStmt49 = None

        attributeAction50 = None

        learnAction51 = None

        forgetAction52 = None

        modifyAction53 = None

        haltAction54 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:167:3: ( simpleStmt | attributeAction | learnAction | forgetAction | modifyAction | haltAction )
                alt21 = 6
                LA21 = self.input.LA(1)
                if LA21 == LPAREN or LA21 == NAME or LA21 == STRING or LA21 == NOT or LA21 == OBJECTBINDING or LA21 == PRINT or LA21 == PLUS or LA21 == MINUS or LA21 == TILDE or LA21 == LBRACK or LA21 == LCURLY or LA21 == INT or LA21 == LONGINT or LA21 == FLOAT or LA21 == COMPLEX:
                    alt21 = 1
                elif LA21 == ATTRIBUTE:
                    alt21 = 2
                elif LA21 == LEARN or LA21 == INSERT:
                    alt21 = 3
                elif LA21 == FORGET or LA21 == DELETE:
                    alt21 = 4
                elif LA21 == MODIFY:
                    alt21 = 5
                elif LA21 == HALT:
                    alt21 = 6
                else:
                    nvae = NoViableAltException("", 21, 0, self.input)

                    raise nvae

                if alt21 == 1:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:167:5: simpleStmt
                    pass 
                    self._state.following.append(self.FOLLOW_simpleStmt_in_action886)
                    simpleStmt49 = self.simpleStmt()

                    self._state.following.pop()
                    #action start
                    object = Action( simpleStmt49, simpleStmt49.line, simpleStmt49.column ) 
                    #action end


                elif alt21 == 2:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:168:5: attributeAction
                    pass 
                    self._state.following.append(self.FOLLOW_attributeAction_in_action900)
                    attributeAction50 = self.attributeAction()

                    self._state.following.pop()
                    #action start
                    object = Action( attributeAction50, attributeAction50.line, attributeAction50.column ) 
                    #action end


                elif alt21 == 3:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:169:5: learnAction
                    pass 
                    self._state.following.append(self.FOLLOW_learnAction_in_action909)
                    learnAction51 = self.learnAction()

                    self._state.following.pop()
                    #action start
                    object = Action( learnAction51, learnAction51.line, learnAction51.column ) 
                    #action end


                elif alt21 == 4:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:170:5: forgetAction
                    pass 
                    self._state.following.append(self.FOLLOW_forgetAction_in_action921)
                    forgetAction52 = self.forgetAction()

                    self._state.following.pop()
                    #action start
                    object = Action( forgetAction52, forgetAction52.line, forgetAction52.column ) 
                    #action end


                elif alt21 == 5:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:171:5: modifyAction
                    pass 
                    self._state.following.append(self.FOLLOW_modifyAction_in_action933)
                    modifyAction53 = self.modifyAction()

                    self._state.following.pop()
                    #action start
                    object = Action( modifyAction53, modifyAction53.line, modifyAction53.column ) 
                    #action end


                elif alt21 == 6:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:172:5: haltAction
                    pass 
                    self._state.following.append(self.FOLLOW_haltAction_in_action945)
                    haltAction54 = self.haltAction()

                    self._state.following.pop()
                    #action start
                    object = Action( haltAction54, haltAction54.line, haltAction54.column ) 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "action"


    # $ANTLR start "simpleStmt"
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:175:1: simpleStmt returns [object] : ( expressionStmt | printStmt );
    def simpleStmt(self, ):

        object = None

        expressionStmt55 = None

        printStmt56 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:176:3: ( expressionStmt | printStmt )
                alt22 = 2
                LA22_0 = self.input.LA(1)

                if (LA22_0 == LPAREN or LA22_0 == NAME or LA22_0 == STRING or LA22_0 == NOT or LA22_0 == OBJECTBINDING or (PLUS <= LA22_0 <= MINUS) or LA22_0 == TILDE or LA22_0 == LBRACK or LA22_0 == LCURLY or (INT <= LA22_0 <= COMPLEX)) :
                    alt22 = 1
                elif (LA22_0 == PRINT) :
                    alt22 = 2
                else:
                    nvae = NoViableAltException("", 22, 0, self.input)

                    raise nvae

                if alt22 == 1:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:176:5: expressionStmt
                    pass 
                    self._state.following.append(self.FOLLOW_expressionStmt_in_simpleStmt971)
                    expressionStmt55 = self.expressionStmt()

                    self._state.following.pop()
                    #action start
                    object = SimpleStmt( expressionStmt55 ) 
                    #action end


                elif alt22 == 2:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:177:5: printStmt
                    pass 
                    self._state.following.append(self.FOLLOW_printStmt_in_simpleStmt985)
                    printStmt56 = self.printStmt()

                    self._state.following.pop()
                    #action start
                    object = SimpleStmt( printStmt56, printStmt56.line, printStmt56.column ) 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "simpleStmt"


    # $ANTLR start "attributeAction"
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:180:1: attributeAction returns [object] : ATTRIBUTE expressionStmt ;
    def attributeAction(self, ):

        object = None

        ATTRIBUTE57 = None
        expressionStmt58 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:181:3: ( ATTRIBUTE expressionStmt )
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:181:5: ATTRIBUTE expressionStmt
                pass 
                ATTRIBUTE57=self.match(self.input, ATTRIBUTE, self.FOLLOW_ATTRIBUTE_in_attributeAction1016)
                self._state.following.append(self.FOLLOW_expressionStmt_in_attributeAction1018)
                expressionStmt58 = self.expressionStmt()

                self._state.following.pop()
                #action start
                object = AttributeAction( [ ATTRIBUTE57.text, expressionStmt58 ] , ATTRIBUTE57.getLine(), ATTRIBUTE57.getCharPositionInLine() ) 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "attributeAction"


    # $ANTLR start "printStmt"
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:184:1: printStmt returns [object] : PRINT (comparisonList1= comparisonList | RIGHTSHIFT comparisonList2= comparisonList )? NEWLINE ;
    def printStmt(self, ):

        object = None

        PRINT59 = None
        RIGHTSHIFT60 = None
        comparisonList1 = None

        comparisonList2 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:185:3: ( PRINT (comparisonList1= comparisonList | RIGHTSHIFT comparisonList2= comparisonList )? NEWLINE )
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:185:5: PRINT (comparisonList1= comparisonList | RIGHTSHIFT comparisonList2= comparisonList )? NEWLINE
                pass 
                PRINT59=self.match(self.input, PRINT, self.FOLLOW_PRINT_in_printStmt1038)
                #action start
                object = PrintStmt( PRINT59.text, PRINT59.getLine(), PRINT59.getCharPositionInLine() ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:186:7: (comparisonList1= comparisonList | RIGHTSHIFT comparisonList2= comparisonList )?
                alt23 = 3
                LA23_0 = self.input.LA(1)

                if (LA23_0 == LPAREN or LA23_0 == NAME or LA23_0 == STRING or LA23_0 == NOT or LA23_0 == OBJECTBINDING or (PLUS <= LA23_0 <= MINUS) or LA23_0 == TILDE or LA23_0 == LBRACK or LA23_0 == LCURLY or (INT <= LA23_0 <= COMPLEX)) :
                    alt23 = 1
                elif (LA23_0 == RIGHTSHIFT) :
                    alt23 = 2
                if alt23 == 1:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:186:9: comparisonList1= comparisonList
                    pass 
                    self._state.following.append(self.FOLLOW_comparisonList_in_printStmt1052)
                    comparisonList1 = self.comparisonList()

                    self._state.following.pop()
                    #action start
                    object.append_child( comparisonList1 ) 
                    #action end


                elif alt23 == 2:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:187:9: RIGHTSHIFT comparisonList2= comparisonList
                    pass 
                    RIGHTSHIFT60=self.match(self.input, RIGHTSHIFT, self.FOLLOW_RIGHTSHIFT_in_printStmt1064)
                    self._state.following.append(self.FOLLOW_comparisonList_in_printStmt1068)
                    comparisonList2 = self.comparisonList()

                    self._state.following.pop()
                    #action start
                    object.append_children( [RIGHTSHIFT60.text, comparisonList2] ) 
                    #action end



                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_printStmt1075)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "printStmt"


    # $ANTLR start "forgetAction"
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:190:1: forgetAction returns [object] : ( FORGET | DELETE ) OBJECTBINDING NEWLINE ;
    def forgetAction(self, ):

        object = None

        FORGET61 = None
        DELETE62 = None
        OBJECTBINDING63 = None

        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:191:3: ( ( FORGET | DELETE ) OBJECTBINDING NEWLINE )
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:191:5: ( FORGET | DELETE ) OBJECTBINDING NEWLINE
                pass 
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:191:5: ( FORGET | DELETE )
                alt24 = 2
                LA24_0 = self.input.LA(1)

                if (LA24_0 == FORGET) :
                    alt24 = 1
                elif (LA24_0 == DELETE) :
                    alt24 = 2
                else:
                    nvae = NoViableAltException("", 24, 0, self.input)

                    raise nvae

                if alt24 == 1:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:191:7: FORGET
                    pass 
                    FORGET61=self.match(self.input, FORGET, self.FOLLOW_FORGET_in_forgetAction1095)
                    #action start
                    object = ForgetAction( FORGET61.text, FORGET61.getLine(), FORGET61.getCharPositionInLine() ) 
                    #action end


                elif alt24 == 2:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:192:9: DELETE
                    pass 
                    DELETE62=self.match(self.input, DELETE, self.FOLLOW_DELETE_in_forgetAction1107)
                    #action start
                    object = ForgetAction( DELETE62.text, DELETE62.getLine(), DELETE62.getCharPositionInLine() ) 
                    #action end



                OBJECTBINDING63=self.match(self.input, OBJECTBINDING, self.FOLLOW_OBJECTBINDING_in_forgetAction1120)
                #action start
                object.append_child( OBJECTBINDING63.text ) 
                #action end
                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_forgetAction1124)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "forgetAction"


    # $ANTLR start "learnAction"
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:196:1: learnAction returns [object] : ( LEARN | INSERT ) NAME LPAREN ( argumentList )? RPAREN NEWLINE ;
    def learnAction(self, ):

        object = None

        LEARN64 = None
        INSERT65 = None
        NAME66 = None
        LPAREN67 = None
        RPAREN69 = None
        argumentList68 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:197:3: ( ( LEARN | INSERT ) NAME LPAREN ( argumentList )? RPAREN NEWLINE )
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:197:5: ( LEARN | INSERT ) NAME LPAREN ( argumentList )? RPAREN NEWLINE
                pass 
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:197:5: ( LEARN | INSERT )
                alt25 = 2
                LA25_0 = self.input.LA(1)

                if (LA25_0 == LEARN) :
                    alt25 = 1
                elif (LA25_0 == INSERT) :
                    alt25 = 2
                else:
                    nvae = NoViableAltException("", 25, 0, self.input)

                    raise nvae

                if alt25 == 1:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:197:7: LEARN
                    pass 
                    LEARN64=self.match(self.input, LEARN, self.FOLLOW_LEARN_in_learnAction1144)
                    #action start
                    object = LearnAction( LEARN64.text, LEARN64.getLine(), LEARN64.getCharPositionInLine() ) 
                    #action end


                elif alt25 == 2:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:198:9: INSERT
                    pass 
                    INSERT65=self.match(self.input, INSERT, self.FOLLOW_INSERT_in_learnAction1156)
                    #action start
                    object = LearnAction( INSERT65.text, INSERT65.getLine(), INSERT65.getCharPositionInLine() ) 
                    #action end



                NAME66=self.match(self.input, NAME, self.FOLLOW_NAME_in_learnAction1171)
                LPAREN67=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_learnAction1173)
                #action start
                object.append_children( [NAME66.text, LPAREN67.text] ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:200:9: ( argumentList )?
                alt26 = 2
                LA26_0 = self.input.LA(1)

                if (LA26_0 == LPAREN or LA26_0 == NAME or LA26_0 == STRING or LA26_0 == NOT or LA26_0 == OBJECTBINDING or (PLUS <= LA26_0 <= MINUS) or LA26_0 == TILDE or LA26_0 == LBRACK or LA26_0 == LCURLY or (INT <= LA26_0 <= COMPLEX)) :
                    alt26 = 1
                if alt26 == 1:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:200:11: argumentList
                    pass 
                    self._state.following.append(self.FOLLOW_argumentList_in_learnAction1187)
                    argumentList68 = self.argumentList()

                    self._state.following.pop()
                    #action start
                    object.append_child( argumentList68 ) 
                    #action end



                RPAREN69=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_learnAction1194)
                #action start
                object.append_child( RPAREN69.text ) 
                #action end
                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_learnAction1198)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "learnAction"


    # $ANTLR start "modifyAction"
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:203:1: modifyAction returns [object] : MODIFY OBJECTBINDING COLON NEWLINE INDENT ( propertyAssignment )+ DEDENT ;
    def modifyAction(self, ):

        object = None

        MODIFY70 = None
        OBJECTBINDING71 = None
        COLON72 = None
        propertyAssignment73 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:204:3: ( MODIFY OBJECTBINDING COLON NEWLINE INDENT ( propertyAssignment )+ DEDENT )
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:204:5: MODIFY OBJECTBINDING COLON NEWLINE INDENT ( propertyAssignment )+ DEDENT
                pass 
                MODIFY70=self.match(self.input, MODIFY, self.FOLLOW_MODIFY_in_modifyAction1216)
                OBJECTBINDING71=self.match(self.input, OBJECTBINDING, self.FOLLOW_OBJECTBINDING_in_modifyAction1218)
                COLON72=self.match(self.input, COLON, self.FOLLOW_COLON_in_modifyAction1220)
                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_modifyAction1222)
                #action start
                object = ModifyAction( [MODIFY70.text, OBJECTBINDING71.text, COLON72.text], MODIFY70.getLine(), MODIFY70.getCharPositionInLine() ) 
                #action end
                self.match(self.input, INDENT, self.FOLLOW_INDENT_in_modifyAction1232)
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:205:14: ( propertyAssignment )+
                cnt27 = 0
                while True: #loop27
                    alt27 = 2
                    LA27_0 = self.input.LA(1)

                    if (LA27_0 == NAME) :
                        alt27 = 1


                    if alt27 == 1:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:205:16: propertyAssignment
                        pass 
                        self._state.following.append(self.FOLLOW_propertyAssignment_in_modifyAction1236)
                        propertyAssignment73 = self.propertyAssignment()

                        self._state.following.pop()
                        #action start
                        object.append_child( propertyAssignment73 ) 
                        #action end


                    else:
                        if cnt27 >= 1:
                            break #loop27

                        eee = EarlyExitException(27, self.input)
                        raise eee

                    cnt27 += 1
                self.match(self.input, DEDENT, self.FOLLOW_DEDENT_in_modifyAction1243)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "modifyAction"


    # $ANTLR start "haltAction"
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:208:1: haltAction returns [object] : HALT NEWLINE ;
    def haltAction(self, ):

        object = None

        HALT74 = None

        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:209:3: ( HALT NEWLINE )
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:209:5: HALT NEWLINE
                pass 
                HALT74=self.match(self.input, HALT, self.FOLLOW_HALT_in_haltAction1261)
                #action start
                object = HaltAction( HALT74.text, HALT74.getLine(), HALT74.getCharPositionInLine() ) 
                #action end
                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_haltAction1265)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "haltAction"


    # $ANTLR start "propertyAssignment"
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:212:1: propertyAssignment returns [object] : NAME assignment constraint NEWLINE ;
    def propertyAssignment(self, ):

        object = None

        NAME75 = None
        assignment76 = None

        constraint77 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:213:3: ( NAME assignment constraint NEWLINE )
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:213:5: NAME assignment constraint NEWLINE
                pass 
                NAME75=self.match(self.input, NAME, self.FOLLOW_NAME_in_propertyAssignment1283)
                self._state.following.append(self.FOLLOW_assignment_in_propertyAssignment1285)
                assignment76 = self.assignment()

                self._state.following.pop()
                self._state.following.append(self.FOLLOW_constraint_in_propertyAssignment1287)
                constraint77 = self.constraint()

                self._state.following.pop()
                #action start
                object = PropertyAssignment( [NAME75.text, assignment76, constraint77] ) 
                #action end
                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_propertyAssignment1291)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "propertyAssignment"


    # $ANTLR start "expressionStmt"
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:216:1: expressionStmt returns [object] : comparisonList1= comparisonList ( assignment comparisonList2= comparisonList )? NEWLINE ;
    def expressionStmt(self, ):

        object = None

        comparisonList1 = None

        comparisonList2 = None

        assignment78 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:217:3: (comparisonList1= comparisonList ( assignment comparisonList2= comparisonList )? NEWLINE )
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:217:5: comparisonList1= comparisonList ( assignment comparisonList2= comparisonList )? NEWLINE
                pass 
                self._state.following.append(self.FOLLOW_comparisonList_in_expressionStmt1311)
                comparisonList1 = self.comparisonList()

                self._state.following.pop()
                #action start
                object = ExpressionStmt( comparisonList1 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:218:7: ( assignment comparisonList2= comparisonList )?
                alt28 = 2
                LA28_0 = self.input.LA(1)

                if ((ASSIGN <= LA28_0 <= DOUBLESLASHEQUAL)) :
                    alt28 = 1
                if alt28 == 1:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:218:9: assignment comparisonList2= comparisonList
                    pass 
                    self._state.following.append(self.FOLLOW_assignment_in_expressionStmt1323)
                    assignment78 = self.assignment()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_comparisonList_in_expressionStmt1327)
                    comparisonList2 = self.comparisonList()

                    self._state.following.pop()
                    #action start
                    object.append_children( [assignment78, comparisonList2] ) 
                    #action end



                self.match(self.input, NEWLINE, self.FOLLOW_NEWLINE_in_expressionStmt1334)




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "expressionStmt"


    # $ANTLR start "assignment"
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:221:1: assignment returns [object] : ( ASSIGN | PLUSEQUAL | MINUSEQUAL | STAREQUAL | SLASHEQUAL | PERCENTEQUAL | AMPEREQUAL | VBAREQUAL | CIRCUMFLEXEQUAL | LEFTSHIFTEQUAL | RIGHTSHIFTEQUAL | DOUBLESTAREQUAL | DOUBLESLASHEQUAL );
    def assignment(self, ):

        object = None

        ASSIGN79 = None
        PLUSEQUAL80 = None
        MINUSEQUAL81 = None
        STAREQUAL82 = None
        SLASHEQUAL83 = None
        PERCENTEQUAL84 = None
        AMPEREQUAL85 = None
        VBAREQUAL86 = None
        CIRCUMFLEXEQUAL87 = None
        LEFTSHIFTEQUAL88 = None
        RIGHTSHIFTEQUAL89 = None
        DOUBLESTAREQUAL90 = None
        DOUBLESLASHEQUAL91 = None

        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:222:3: ( ASSIGN | PLUSEQUAL | MINUSEQUAL | STAREQUAL | SLASHEQUAL | PERCENTEQUAL | AMPEREQUAL | VBAREQUAL | CIRCUMFLEXEQUAL | LEFTSHIFTEQUAL | RIGHTSHIFTEQUAL | DOUBLESTAREQUAL | DOUBLESLASHEQUAL )
                alt29 = 13
                LA29 = self.input.LA(1)
                if LA29 == ASSIGN:
                    alt29 = 1
                elif LA29 == PLUSEQUAL:
                    alt29 = 2
                elif LA29 == MINUSEQUAL:
                    alt29 = 3
                elif LA29 == STAREQUAL:
                    alt29 = 4
                elif LA29 == SLASHEQUAL:
                    alt29 = 5
                elif LA29 == PERCENTEQUAL:
                    alt29 = 6
                elif LA29 == AMPEREQUAL:
                    alt29 = 7
                elif LA29 == VBAREQUAL:
                    alt29 = 8
                elif LA29 == CIRCUMFLEXEQUAL:
                    alt29 = 9
                elif LA29 == LEFTSHIFTEQUAL:
                    alt29 = 10
                elif LA29 == RIGHTSHIFTEQUAL:
                    alt29 = 11
                elif LA29 == DOUBLESTAREQUAL:
                    alt29 = 12
                elif LA29 == DOUBLESLASHEQUAL:
                    alt29 = 13
                else:
                    nvae = NoViableAltException("", 29, 0, self.input)

                    raise nvae

                if alt29 == 1:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:222:5: ASSIGN
                    pass 
                    ASSIGN79=self.match(self.input, ASSIGN, self.FOLLOW_ASSIGN_in_assignment1352)
                    #action start
                    object = Assignment( ASSIGN79.text ) 
                    #action end


                elif alt29 == 2:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:223:5: PLUSEQUAL
                    pass 
                    PLUSEQUAL80=self.match(self.input, PLUSEQUAL, self.FOLLOW_PLUSEQUAL_in_assignment1371)
                    #action start
                    object = Assignment( PLUSEQUAL80.text ) 
                    #action end


                elif alt29 == 3:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:224:5: MINUSEQUAL
                    pass 
                    MINUSEQUAL81=self.match(self.input, MINUSEQUAL, self.FOLLOW_MINUSEQUAL_in_assignment1387)
                    #action start
                    object = Assignment( MINUSEQUAL81.text ) 
                    #action end


                elif alt29 == 4:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:225:5: STAREQUAL
                    pass 
                    STAREQUAL82=self.match(self.input, STAREQUAL, self.FOLLOW_STAREQUAL_in_assignment1402)
                    #action start
                    object = Assignment( STAREQUAL82.text ) 
                    #action end


                elif alt29 == 5:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:226:5: SLASHEQUAL
                    pass 
                    SLASHEQUAL83=self.match(self.input, SLASHEQUAL, self.FOLLOW_SLASHEQUAL_in_assignment1418)
                    #action start
                    object = Assignment( SLASHEQUAL83.text ) 
                    #action end


                elif alt29 == 6:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:227:5: PERCENTEQUAL
                    pass 
                    PERCENTEQUAL84=self.match(self.input, PERCENTEQUAL, self.FOLLOW_PERCENTEQUAL_in_assignment1433)
                    #action start
                    object = Assignment( PERCENTEQUAL84.text ) 
                    #action end


                elif alt29 == 7:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:228:5: AMPEREQUAL
                    pass 
                    AMPEREQUAL85=self.match(self.input, AMPEREQUAL, self.FOLLOW_AMPEREQUAL_in_assignment1446)
                    #action start
                    object = Assignment( AMPEREQUAL85.text ) 
                    #action end


                elif alt29 == 8:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:229:5: VBAREQUAL
                    pass 
                    VBAREQUAL86=self.match(self.input, VBAREQUAL, self.FOLLOW_VBAREQUAL_in_assignment1461)
                    #action start
                    object = Assignment( VBAREQUAL86.text ) 
                    #action end


                elif alt29 == 9:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:230:5: CIRCUMFLEXEQUAL
                    pass 
                    CIRCUMFLEXEQUAL87=self.match(self.input, CIRCUMFLEXEQUAL, self.FOLLOW_CIRCUMFLEXEQUAL_in_assignment1477)
                    #action start
                    object = Assignment( CIRCUMFLEXEQUAL87.text ) 
                    #action end


                elif alt29 == 10:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:231:5: LEFTSHIFTEQUAL
                    pass 
                    LEFTSHIFTEQUAL88=self.match(self.input, LEFTSHIFTEQUAL, self.FOLLOW_LEFTSHIFTEQUAL_in_assignment1487)
                    #action start
                    object = Assignment( LEFTSHIFTEQUAL88.text ) 
                    #action end


                elif alt29 == 11:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:232:5: RIGHTSHIFTEQUAL
                    pass 
                    RIGHTSHIFTEQUAL89=self.match(self.input, RIGHTSHIFTEQUAL, self.FOLLOW_RIGHTSHIFTEQUAL_in_assignment1498)
                    #action start
                    object = Assignment( RIGHTSHIFTEQUAL89.text ) 
                    #action end


                elif alt29 == 12:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:233:5: DOUBLESTAREQUAL
                    pass 
                    DOUBLESTAREQUAL90=self.match(self.input, DOUBLESTAREQUAL, self.FOLLOW_DOUBLESTAREQUAL_in_assignment1508)
                    #action start
                    object = Assignment( DOUBLESTAREQUAL90.text ) 
                    #action end


                elif alt29 == 13:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:234:5: DOUBLESLASHEQUAL
                    pass 
                    DOUBLESLASHEQUAL91=self.match(self.input, DOUBLESLASHEQUAL, self.FOLLOW_DOUBLESLASHEQUAL_in_assignment1518)
                    #action start
                    object = Assignment( DOUBLESLASHEQUAL91.text ) 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return object

    # $ANTLR end "assignment"


    # $ANTLR start "constraint"
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:237:1: constraint returns [object] : orConstraint ;
    def constraint(self, ):

        object = None

        orConstraint92 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:238:3: ( orConstraint )
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:238:5: orConstraint
                pass 
                self._state.following.append(self.FOLLOW_orConstraint_in_constraint1539)
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
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:241:1: orConstraint returns [object] : constraint1= andConstraint ( OR constraint2= andConstraint )* ;
    def orConstraint(self, ):

        object = None

        OR93 = None
        constraint1 = None

        constraint2 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:242:3: (constraint1= andConstraint ( OR constraint2= andConstraint )* )
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:242:5: constraint1= andConstraint ( OR constraint2= andConstraint )*
                pass 
                self._state.following.append(self.FOLLOW_andConstraint_in_orConstraint1561)
                constraint1 = self.andConstraint()

                self._state.following.pop()
                #action start
                object = OrConstraint( constraint1 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:243:7: ( OR constraint2= andConstraint )*
                while True: #loop30
                    alt30 = 2
                    LA30_0 = self.input.LA(1)

                    if (LA30_0 == OR) :
                        alt30 = 1


                    if alt30 == 1:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:243:9: OR constraint2= andConstraint
                        pass 
                        OR93=self.match(self.input, OR, self.FOLLOW_OR_in_orConstraint1573)
                        self._state.following.append(self.FOLLOW_andConstraint_in_orConstraint1577)
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
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:246:1: andConstraint returns [object] : constraint1= notConstraint ( AND constraint2= notConstraint )* ;
    def andConstraint(self, ):

        object = None

        AND94 = None
        constraint1 = None

        constraint2 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:247:3: (constraint1= notConstraint ( AND constraint2= notConstraint )* )
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:247:5: constraint1= notConstraint ( AND constraint2= notConstraint )*
                pass 
                self._state.following.append(self.FOLLOW_notConstraint_in_andConstraint1602)
                constraint1 = self.notConstraint()

                self._state.following.pop()
                #action start
                object = AndConstraint( constraint1 )
                #action end
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:248:7: ( AND constraint2= notConstraint )*
                while True: #loop31
                    alt31 = 2
                    LA31_0 = self.input.LA(1)

                    if (LA31_0 == AND) :
                        alt31 = 1


                    if alt31 == 1:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:248:9: AND constraint2= notConstraint
                        pass 
                        AND94=self.match(self.input, AND, self.FOLLOW_AND_in_andConstraint1614)
                        self._state.following.append(self.FOLLOW_notConstraint_in_andConstraint1618)
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
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:251:1: notConstraint returns [object] : ( NOT )* comparison ;
    def notConstraint(self, ):

        object = None

        NOT95 = None
        comparison96 = None


        object = NotConstraint() 
        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:253:3: ( ( NOT )* comparison )
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:253:5: ( NOT )* comparison
                pass 
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:253:5: ( NOT )*
                while True: #loop32
                    alt32 = 2
                    LA32_0 = self.input.LA(1)

                    if (LA32_0 == NOT) :
                        alt32 = 1


                    if alt32 == 1:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:253:7: NOT
                        pass 
                        NOT95=self.match(self.input, NOT, self.FOLLOW_NOT_in_notConstraint1649)
                        #action start
                        object.append_child( NOT95.text ) 
                        #action end


                    else:
                        break #loop32
                self._state.following.append(self.FOLLOW_comparison_in_notConstraint1656)
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
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:256:1: comparison returns [object] : expression1= expression ( comparisonOperation expression2= expression )* ;
    def comparison(self, ):

        object = None

        expression1 = None

        expression2 = None

        comparisonOperation97 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:257:3: (expression1= expression ( comparisonOperation expression2= expression )* )
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:257:5: expression1= expression ( comparisonOperation expression2= expression )*
                pass 
                self._state.following.append(self.FOLLOW_expression_in_comparison1678)
                expression1 = self.expression()

                self._state.following.pop()
                #action start
                object = Comparison( expression1 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:258:5: ( comparisonOperation expression2= expression )*
                while True: #loop33
                    alt33 = 2
                    LA33_0 = self.input.LA(1)

                    if (LA33_0 == NOT or (LESS <= LA33_0 <= IS)) :
                        alt33 = 1


                    if alt33 == 1:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:258:7: comparisonOperation expression2= expression
                        pass 
                        self._state.following.append(self.FOLLOW_comparisonOperation_in_comparison1688)
                        comparisonOperation97 = self.comparisonOperation()

                        self._state.following.pop()
                        self._state.following.append(self.FOLLOW_expression_in_comparison1692)
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
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:261:1: comparisonOperation returns [object] : ( LESS | GREATER | EQUAL | GREATEREQUAL | LESSEQUAL | ALT_NOTEQUAL | NOTEQUAL | IN | NOT IN | IS | IS NOT ) ;
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
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:262:3: ( ( LESS | GREATER | EQUAL | GREATEREQUAL | LESSEQUAL | ALT_NOTEQUAL | NOTEQUAL | IN | NOT IN | IS | IS NOT ) )
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:262:5: ( LESS | GREATER | EQUAL | GREATEREQUAL | LESSEQUAL | ALT_NOTEQUAL | NOTEQUAL | IN | NOT IN | IS | IS NOT )
                pass 
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:262:5: ( LESS | GREATER | EQUAL | GREATEREQUAL | LESSEQUAL | ALT_NOTEQUAL | NOTEQUAL | IN | NOT IN | IS | IS NOT )
                alt34 = 11
                alt34 = self.dfa34.predict(self.input)
                if alt34 == 1:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:262:7: LESS
                    pass 
                    LESS98=self.match(self.input, LESS, self.FOLLOW_LESS_in_comparisonOperation1717)
                    #action start
                    object = ComparisonOperation( LESS98.text ) 
                    #action end


                elif alt34 == 2:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:263:7: GREATER
                    pass 
                    GREATER99=self.match(self.input, GREATER, self.FOLLOW_GREATER_in_comparisonOperation1736)
                    #action start
                    object = ComparisonOperation( GREATER99.text ) 
                    #action end


                elif alt34 == 3:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:264:7: EQUAL
                    pass 
                    EQUAL100=self.match(self.input, EQUAL, self.FOLLOW_EQUAL_in_comparisonOperation1752)
                    #action start
                    object = ComparisonOperation( EQUAL100.text ) 
                    #action end


                elif alt34 == 4:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:265:7: GREATEREQUAL
                    pass 
                    GREATEREQUAL101=self.match(self.input, GREATEREQUAL, self.FOLLOW_GREATEREQUAL_in_comparisonOperation1770)
                    #action start
                    object = ComparisonOperation( GREATEREQUAL101.text ) 
                    #action end


                elif alt34 == 5:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:266:7: LESSEQUAL
                    pass 
                    LESSEQUAL102=self.match(self.input, LESSEQUAL, self.FOLLOW_LESSEQUAL_in_comparisonOperation1781)
                    #action start
                    object = ComparisonOperation( LESSEQUAL102.text ) 
                    #action end


                elif alt34 == 6:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:267:7: ALT_NOTEQUAL
                    pass 
                    ALT_NOTEQUAL103=self.match(self.input, ALT_NOTEQUAL, self.FOLLOW_ALT_NOTEQUAL_in_comparisonOperation1795)
                    #action start
                    object = ComparisonOperation( ALT_NOTEQUAL103.text ) 
                    #action end


                elif alt34 == 7:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:268:7: NOTEQUAL
                    pass 
                    NOTEQUAL104=self.match(self.input, NOTEQUAL, self.FOLLOW_NOTEQUAL_in_comparisonOperation1806)
                    #action start
                    object = ComparisonOperation( NOTEQUAL104.text ) 
                    #action end


                elif alt34 == 8:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:269:7: IN
                    pass 
                    self.match(self.input, IN, self.FOLLOW_IN_in_comparisonOperation1821)
                    #action start
                    object = ComparisonOperation( "in" ) 
                    #action end


                elif alt34 == 9:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:270:7: NOT IN
                    pass 
                    self.match(self.input, NOT, self.FOLLOW_NOT_in_comparisonOperation1842)
                    self.match(self.input, IN, self.FOLLOW_IN_in_comparisonOperation1844)
                    #action start
                    object = ComparisonOperation( "not in" ) 
                    #action end


                elif alt34 == 10:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:271:7: IS
                    pass 
                    self.match(self.input, IS, self.FOLLOW_IS_in_comparisonOperation1861)
                    #action start
                    object = ComparisonOperation( "is" ) 
                    #action end


                elif alt34 == 11:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:272:7: IS NOT
                    pass 
                    self.match(self.input, IS, self.FOLLOW_IS_in_comparisonOperation1882)
                    self.match(self.input, NOT, self.FOLLOW_NOT_in_comparisonOperation1884)
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
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:275:1: expression returns [object] : bitwiseOrExpr ;
    def expression(self, ):

        object = None

        bitwiseOrExpr105 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:276:3: ( bitwiseOrExpr )
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:276:5: bitwiseOrExpr
                pass 
                self._state.following.append(self.FOLLOW_bitwiseOrExpr_in_expression1913)
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
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:279:1: bitwiseOrExpr returns [object] : expr1= bitwiseXorExpr ( VBAR expr2= bitwiseXorExpr )* ;
    def bitwiseOrExpr(self, ):

        object = None

        VBAR106 = None
        expr1 = None

        expr2 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:280:3: (expr1= bitwiseXorExpr ( VBAR expr2= bitwiseXorExpr )* )
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:280:5: expr1= bitwiseXorExpr ( VBAR expr2= bitwiseXorExpr )*
                pass 
                self._state.following.append(self.FOLLOW_bitwiseXorExpr_in_bitwiseOrExpr1935)
                expr1 = self.bitwiseXorExpr()

                self._state.following.pop()
                #action start
                object = BitwiseOrExpr( expr1 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:281:7: ( VBAR expr2= bitwiseXorExpr )*
                while True: #loop35
                    alt35 = 2
                    LA35_0 = self.input.LA(1)

                    if (LA35_0 == VBAR) :
                        alt35 = 1


                    if alt35 == 1:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:281:9: VBAR expr2= bitwiseXorExpr
                        pass 
                        VBAR106=self.match(self.input, VBAR, self.FOLLOW_VBAR_in_bitwiseOrExpr1947)
                        self._state.following.append(self.FOLLOW_bitwiseXorExpr_in_bitwiseOrExpr1951)
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
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:284:1: bitwiseXorExpr returns [object] : expr1= bitwiseAndExpr ( CIRCUMFLEX expr2= bitwiseAndExpr )* ;
    def bitwiseXorExpr(self, ):

        object = None

        CIRCUMFLEX107 = None
        expr1 = None

        expr2 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:285:3: (expr1= bitwiseAndExpr ( CIRCUMFLEX expr2= bitwiseAndExpr )* )
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:285:5: expr1= bitwiseAndExpr ( CIRCUMFLEX expr2= bitwiseAndExpr )*
                pass 
                self._state.following.append(self.FOLLOW_bitwiseAndExpr_in_bitwiseXorExpr1976)
                expr1 = self.bitwiseAndExpr()

                self._state.following.pop()
                #action start
                object = BitwiseXorExpr( expr1 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:286:7: ( CIRCUMFLEX expr2= bitwiseAndExpr )*
                while True: #loop36
                    alt36 = 2
                    LA36_0 = self.input.LA(1)

                    if (LA36_0 == CIRCUMFLEX) :
                        alt36 = 1


                    if alt36 == 1:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:286:9: CIRCUMFLEX expr2= bitwiseAndExpr
                        pass 
                        CIRCUMFLEX107=self.match(self.input, CIRCUMFLEX, self.FOLLOW_CIRCUMFLEX_in_bitwiseXorExpr1988)
                        self._state.following.append(self.FOLLOW_bitwiseAndExpr_in_bitwiseXorExpr1992)
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
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:289:1: bitwiseAndExpr returns [object] : expr1= shiftExpr ( AMPER expr2= shiftExpr )* ;
    def bitwiseAndExpr(self, ):

        object = None

        AMPER108 = None
        expr1 = None

        expr2 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:290:3: (expr1= shiftExpr ( AMPER expr2= shiftExpr )* )
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:290:5: expr1= shiftExpr ( AMPER expr2= shiftExpr )*
                pass 
                self._state.following.append(self.FOLLOW_shiftExpr_in_bitwiseAndExpr2017)
                expr1 = self.shiftExpr()

                self._state.following.pop()
                #action start
                object = BitwiseAndExpr( expr1 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:291:7: ( AMPER expr2= shiftExpr )*
                while True: #loop37
                    alt37 = 2
                    LA37_0 = self.input.LA(1)

                    if (LA37_0 == AMPER) :
                        alt37 = 1


                    if alt37 == 1:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:291:9: AMPER expr2= shiftExpr
                        pass 
                        AMPER108=self.match(self.input, AMPER, self.FOLLOW_AMPER_in_bitwiseAndExpr2029)
                        self._state.following.append(self.FOLLOW_shiftExpr_in_bitwiseAndExpr2033)
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
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:294:1: shiftExpr returns [object] : expr1= arithExpr ( ( LEFTSHIFT | RIGHTSHIFT ) expr2= arithExpr )* ;
    def shiftExpr(self, ):

        object = None

        LEFTSHIFT109 = None
        RIGHTSHIFT110 = None
        expr1 = None

        expr2 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:295:3: (expr1= arithExpr ( ( LEFTSHIFT | RIGHTSHIFT ) expr2= arithExpr )* )
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:295:5: expr1= arithExpr ( ( LEFTSHIFT | RIGHTSHIFT ) expr2= arithExpr )*
                pass 
                self._state.following.append(self.FOLLOW_arithExpr_in_shiftExpr2058)
                expr1 = self.arithExpr()

                self._state.following.pop()
                #action start
                object = ShiftExpr( expr1 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:296:7: ( ( LEFTSHIFT | RIGHTSHIFT ) expr2= arithExpr )*
                while True: #loop39
                    alt39 = 2
                    LA39_0 = self.input.LA(1)

                    if (LA39_0 == RIGHTSHIFT or LA39_0 == LEFTSHIFT) :
                        alt39 = 1


                    if alt39 == 1:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:296:9: ( LEFTSHIFT | RIGHTSHIFT ) expr2= arithExpr
                        pass 
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:296:9: ( LEFTSHIFT | RIGHTSHIFT )
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
                            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:296:11: LEFTSHIFT
                            pass 
                            LEFTSHIFT109=self.match(self.input, LEFTSHIFT, self.FOLLOW_LEFTSHIFT_in_shiftExpr2072)
                            #action start
                            object.append_child( LEFTSHIFT109.text ) 
                            #action end


                        elif alt38 == 2:
                            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:296:67: RIGHTSHIFT
                            pass 
                            RIGHTSHIFT110=self.match(self.input, RIGHTSHIFT, self.FOLLOW_RIGHTSHIFT_in_shiftExpr2078)
                            #action start
                            object.append_child( RIGHTSHIFT110.text ) 
                            #action end



                        self._state.following.append(self.FOLLOW_arithExpr_in_shiftExpr2096)
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
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:300:1: arithExpr returns [object] : term1= term ( ( PLUS | MINUS ) term2= term )* ;
    def arithExpr(self, ):

        object = None

        PLUS111 = None
        MINUS112 = None
        term1 = None

        term2 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:301:3: (term1= term ( ( PLUS | MINUS ) term2= term )* )
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:301:5: term1= term ( ( PLUS | MINUS ) term2= term )*
                pass 
                self._state.following.append(self.FOLLOW_term_in_arithExpr2121)
                term1 = self.term()

                self._state.following.pop()
                #action start
                object = ArithExpr( term1 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:302:7: ( ( PLUS | MINUS ) term2= term )*
                while True: #loop41
                    alt41 = 2
                    LA41_0 = self.input.LA(1)

                    if ((PLUS <= LA41_0 <= MINUS)) :
                        alt41 = 1


                    if alt41 == 1:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:302:9: ( PLUS | MINUS ) term2= term
                        pass 
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:302:9: ( PLUS | MINUS )
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
                            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:302:11: PLUS
                            pass 
                            PLUS111=self.match(self.input, PLUS, self.FOLLOW_PLUS_in_arithExpr2135)
                            #action start
                            object.append_child( PLUS111.text ) 
                            #action end


                        elif alt40 == 2:
                            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:302:57: MINUS
                            pass 
                            MINUS112=self.match(self.input, MINUS, self.FOLLOW_MINUS_in_arithExpr2141)
                            #action start
                            object.append_child( MINUS112.text ) 
                            #action end



                        self._state.following.append(self.FOLLOW_term_in_arithExpr2159)
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
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:306:1: term returns [object] : factor1= factor ( ( STAR | SLASH | PERCENT | DOUBLESLASH ) factor2= factor )* ;
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
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:307:3: (factor1= factor ( ( STAR | SLASH | PERCENT | DOUBLESLASH ) factor2= factor )* )
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:307:5: factor1= factor ( ( STAR | SLASH | PERCENT | DOUBLESLASH ) factor2= factor )*
                pass 
                self._state.following.append(self.FOLLOW_factor_in_term2184)
                factor1 = self.factor()

                self._state.following.pop()
                #action start
                object = Term( factor1 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:308:7: ( ( STAR | SLASH | PERCENT | DOUBLESLASH ) factor2= factor )*
                while True: #loop43
                    alt43 = 2
                    LA43_0 = self.input.LA(1)

                    if ((STAR <= LA43_0 <= DOUBLESLASH)) :
                        alt43 = 1


                    if alt43 == 1:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:308:9: ( STAR | SLASH | PERCENT | DOUBLESLASH ) factor2= factor
                        pass 
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:308:9: ( STAR | SLASH | PERCENT | DOUBLESLASH )
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
                            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:308:10: STAR
                            pass 
                            STAR113=self.match(self.input, STAR, self.FOLLOW_STAR_in_term2197)
                            #action start
                            object.append_child( STAR113.text ) 
                            #action end


                        elif alt42 == 2:
                            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:308:56: SLASH
                            pass 
                            SLASH114=self.match(self.input, SLASH, self.FOLLOW_SLASH_in_term2203)
                            #action start
                            object.append_child( SLASH114.text ) 
                            #action end


                        elif alt42 == 3:
                            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:309:13: PERCENT
                            pass 
                            PERCENT115=self.match(self.input, PERCENT, self.FOLLOW_PERCENT_in_term2219)
                            #action start
                            object.append_child( PERCENT115.text ) 
                            #action end


                        elif alt42 == 4:
                            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:309:65: DOUBLESLASH
                            pass 
                            DOUBLESLASH116=self.match(self.input, DOUBLESLASH, self.FOLLOW_DOUBLESLASH_in_term2225)
                            #action start
                            object.append_child( DOUBLESLASH116.text ) 
                            #action end



                        self._state.following.append(self.FOLLOW_factor_in_term2247)
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
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:313:1: factor returns [object] : ( PLUS factor1= factor | MINUS factor2= factor | TILDE factor3= factor | power );
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
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:314:3: ( PLUS factor1= factor | MINUS factor2= factor | TILDE factor3= factor | power )
                alt44 = 4
                LA44 = self.input.LA(1)
                if LA44 == PLUS:
                    alt44 = 1
                elif LA44 == MINUS:
                    alt44 = 2
                elif LA44 == TILDE:
                    alt44 = 3
                elif LA44 == LPAREN or LA44 == NAME or LA44 == STRING or LA44 == OBJECTBINDING or LA44 == LBRACK or LA44 == LCURLY or LA44 == INT or LA44 == LONGINT or LA44 == FLOAT or LA44 == COMPLEX:
                    alt44 = 4
                else:
                    nvae = NoViableAltException("", 44, 0, self.input)

                    raise nvae

                if alt44 == 1:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:314:5: PLUS factor1= factor
                    pass 
                    PLUS117=self.match(self.input, PLUS, self.FOLLOW_PLUS_in_factor2270)
                    self._state.following.append(self.FOLLOW_factor_in_factor2275)
                    factor1 = self.factor()

                    self._state.following.pop()
                    #action start
                    object = Factor( [PLUS117.text, factor1] ) 
                    #action end


                elif alt44 == 2:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:315:5: MINUS factor2= factor
                    pass 
                    MINUS118=self.match(self.input, MINUS, self.FOLLOW_MINUS_in_factor2283)
                    self._state.following.append(self.FOLLOW_factor_in_factor2287)
                    factor2 = self.factor()

                    self._state.following.pop()
                    #action start
                    object = Factor( [MINUS118.text, factor2] ) 
                    #action end


                elif alt44 == 3:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:316:5: TILDE factor3= factor
                    pass 
                    TILDE119=self.match(self.input, TILDE, self.FOLLOW_TILDE_in_factor2295)
                    self._state.following.append(self.FOLLOW_factor_in_factor2299)
                    factor3 = self.factor()

                    self._state.following.pop()
                    #action start
                    object = Factor( [TILDE119.text, factor3] ) 
                    #action end


                elif alt44 == 4:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:317:5: power
                    pass 
                    self._state.following.append(self.FOLLOW_power_in_factor2307)
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
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:320:1: power returns [object] : atom ( trailer )* ( options {greedy=true; } : DOUBLESTAR factor )? ;
    def power(self, ):

        object = None

        DOUBLESTAR123 = None
        atom121 = None

        trailer122 = None

        factor124 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:321:3: ( atom ( trailer )* ( options {greedy=true; } : DOUBLESTAR factor )? )
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:321:5: atom ( trailer )* ( options {greedy=true; } : DOUBLESTAR factor )?
                pass 
                self._state.following.append(self.FOLLOW_atom_in_power2327)
                atom121 = self.atom()

                self._state.following.pop()
                #action start
                object = Power( atom121 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:322:7: ( trailer )*
                while True: #loop45
                    alt45 = 2
                    LA45_0 = self.input.LA(1)

                    if (LA45_0 == LPAREN or LA45_0 == DOT) :
                        alt45 = 1


                    if alt45 == 1:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:322:9: trailer
                        pass 
                        self._state.following.append(self.FOLLOW_trailer_in_power2339)
                        trailer122 = self.trailer()

                        self._state.following.pop()
                        #action start
                        object.append_child( trailer122 ) 
                        #action end


                    else:
                        break #loop45
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:323:7: ( options {greedy=true; } : DOUBLESTAR factor )?
                alt46 = 2
                LA46_0 = self.input.LA(1)

                if (LA46_0 == DOUBLESTAR) :
                    alt46 = 1
                if alt46 == 1:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:323:31: DOUBLESTAR factor
                    pass 
                    DOUBLESTAR123=self.match(self.input, DOUBLESTAR, self.FOLLOW_DOUBLESTAR_in_power2360)
                    self._state.following.append(self.FOLLOW_factor_in_power2362)
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
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:326:1: atom returns [object] : ( LPAREN (comparisonList1= comparisonList )? RPAREN | LBRACK ( listmaker )? RBRACK | LCURLY ( dictmaker )? RCURLY | NAME | OBJECTBINDING | INT | LONGINT | FLOAT | COMPLEX | ( STRING )+ );
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
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:327:3: ( LPAREN (comparisonList1= comparisonList )? RPAREN | LBRACK ( listmaker )? RBRACK | LCURLY ( dictmaker )? RCURLY | NAME | OBJECTBINDING | INT | LONGINT | FLOAT | COMPLEX | ( STRING )+ )
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
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:327:5: LPAREN (comparisonList1= comparisonList )? RPAREN
                    pass 
                    LPAREN125=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_atom2385)
                    #action start
                    object = Atom( LPAREN125.text ) 
                    #action end
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:328:23: (comparisonList1= comparisonList )?
                    alt47 = 2
                    LA47_0 = self.input.LA(1)

                    if (LA47_0 == LPAREN or LA47_0 == NAME or LA47_0 == STRING or LA47_0 == NOT or LA47_0 == OBJECTBINDING or (PLUS <= LA47_0 <= MINUS) or LA47_0 == TILDE or LA47_0 == LBRACK or LA47_0 == LCURLY or (INT <= LA47_0 <= COMPLEX)) :
                        alt47 = 1
                    if alt47 == 1:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:328:25: comparisonList1= comparisonList
                        pass 
                        self._state.following.append(self.FOLLOW_comparisonList_in_atom2424)
                        comparisonList1 = self.comparisonList()

                        self._state.following.pop()
                        #action start
                        object.append_child( comparisonList1 ) 
                        #action end



                    RPAREN126=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_atom2453)
                    #action start
                    object.append_child( RPAREN126.text ) 
                    #action end


                elif alt51 == 2:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:330:5: LBRACK ( listmaker )? RBRACK
                    pass 
                    LBRACK127=self.match(self.input, LBRACK, self.FOLLOW_LBRACK_in_atom2461)
                    #action start
                    object = Atom( LBRACK127.text ) 
                    #action end
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:331:23: ( listmaker )?
                    alt48 = 2
                    LA48_0 = self.input.LA(1)

                    if (LA48_0 == LPAREN or LA48_0 == NAME or LA48_0 == STRING or LA48_0 == NOT or LA48_0 == OBJECTBINDING or (PLUS <= LA48_0 <= MINUS) or LA48_0 == TILDE or LA48_0 == LBRACK or LA48_0 == LCURLY or (INT <= LA48_0 <= COMPLEX)) :
                        alt48 = 1
                    if alt48 == 1:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:331:25: listmaker
                        pass 
                        self._state.following.append(self.FOLLOW_listmaker_in_atom2498)
                        listmaker128 = self.listmaker()

                        self._state.following.pop()
                        #action start
                        object.append_child( listmaker128 ) 
                        #action end



                    RBRACK129=self.match(self.input, RBRACK, self.FOLLOW_RBRACK_in_atom2527)
                    #action start
                    object.append_child( RBRACK129.text ) 
                    #action end


                elif alt51 == 3:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:333:5: LCURLY ( dictmaker )? RCURLY
                    pass 
                    LCURLY130=self.match(self.input, LCURLY, self.FOLLOW_LCURLY_in_atom2535)
                    #action start
                    object = Atom( LCURLY130.text ) 
                    #action end
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:334:23: ( dictmaker )?
                    alt49 = 2
                    LA49_0 = self.input.LA(1)

                    if (LA49_0 == LPAREN or LA49_0 == NAME or LA49_0 == STRING or LA49_0 == NOT or LA49_0 == OBJECTBINDING or (PLUS <= LA49_0 <= MINUS) or LA49_0 == TILDE or LA49_0 == LBRACK or LA49_0 == LCURLY or (INT <= LA49_0 <= COMPLEX)) :
                        alt49 = 1
                    if alt49 == 1:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:334:25: dictmaker
                        pass 
                        self._state.following.append(self.FOLLOW_dictmaker_in_atom2572)
                        dictmaker131 = self.dictmaker()

                        self._state.following.pop()
                        #action start
                        object.append_child( dictmaker131 ) 
                        #action end



                    RCURLY132=self.match(self.input, RCURLY, self.FOLLOW_RCURLY_in_atom2601)
                    #action start
                    object.append_child( RCURLY132.text ) 
                    #action end


                elif alt51 == 4:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:337:5: NAME
                    pass 
                    NAME133=self.match(self.input, NAME, self.FOLLOW_NAME_in_atom2610)
                    #action start
                    object = Atom( NAME133.text ) 
                    #action end


                elif alt51 == 5:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:338:5: OBJECTBINDING
                    pass 
                    OBJECTBINDING134=self.match(self.input, OBJECTBINDING, self.FOLLOW_OBJECTBINDING_in_atom2629)
                    #action start
                    object = Atom( OBJECTBINDING134.text ) 
                    #action end


                elif alt51 == 6:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:339:5: INT
                    pass 
                    INT135=self.match(self.input, INT, self.FOLLOW_INT_in_atom2639)
                    #action start
                    object = Atom( INT135.text ) 
                    #action end


                elif alt51 == 7:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:340:5: LONGINT
                    pass 
                    LONGINT136=self.match(self.input, LONGINT, self.FOLLOW_LONGINT_in_atom2659)
                    #action start
                    object = Atom( LONGINT136.text ) 
                    #action end


                elif alt51 == 8:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:341:5: FLOAT
                    pass 
                    FLOAT137=self.match(self.input, FLOAT, self.FOLLOW_FLOAT_in_atom2675)
                    #action start
                    object = Atom( FLOAT137.text ) 
                    #action end


                elif alt51 == 9:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:342:5: COMPLEX
                    pass 
                    COMPLEX138=self.match(self.input, COMPLEX, self.FOLLOW_COMPLEX_in_atom2693)
                    #action start
                    object = Atom( COMPLEX138.text ) 
                    #action end


                elif alt51 == 10:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:343:5: ( STRING )+
                    pass 
                    #action start
                    object = Atom() 
                    #action end
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:343:25: ( STRING )+
                    cnt50 = 0
                    while True: #loop50
                        alt50 = 2
                        LA50_0 = self.input.LA(1)

                        if (LA50_0 == STRING) :
                            alt50 = 1


                        if alt50 == 1:
                            # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:343:27: STRING
                            pass 
                            STRING139=self.match(self.input, STRING, self.FOLLOW_STRING_in_atom2713)
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
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:346:1: listmaker returns [object] : constraint1= constraint ( options {greedy=true; } : COMMA constraint2= constraint )* ( COMMA )? ;
    def listmaker(self, ):

        object = None

        constraint1 = None

        constraint2 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:347:3: (constraint1= constraint ( options {greedy=true; } : COMMA constraint2= constraint )* ( COMMA )? )
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:347:5: constraint1= constraint ( options {greedy=true; } : COMMA constraint2= constraint )* ( COMMA )?
                pass 
                self._state.following.append(self.FOLLOW_constraint_in_listmaker2738)
                constraint1 = self.constraint()

                self._state.following.pop()
                #action start
                object = ListMaker( constraint1 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:348:7: ( options {greedy=true; } : COMMA constraint2= constraint )*
                while True: #loop52
                    alt52 = 2
                    LA52_0 = self.input.LA(1)

                    if (LA52_0 == COMMA) :
                        LA52_1 = self.input.LA(2)

                        if (LA52_1 == LPAREN or LA52_1 == NAME or LA52_1 == STRING or LA52_1 == NOT or LA52_1 == OBJECTBINDING or (PLUS <= LA52_1 <= MINUS) or LA52_1 == TILDE or LA52_1 == LBRACK or LA52_1 == LCURLY or (INT <= LA52_1 <= COMPLEX)) :
                            alt52 = 1




                    if alt52 == 1:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:348:31: COMMA constraint2= constraint
                        pass 
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_listmaker2756)
                        self._state.following.append(self.FOLLOW_constraint_in_listmaker2760)
                        constraint2 = self.constraint()

                        self._state.following.pop()
                        #action start
                        object.append_children( [ ",", constraint2] ) 
                        #action end


                    else:
                        break #loop52
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:349:7: ( COMMA )?
                alt53 = 2
                LA53_0 = self.input.LA(1)

                if (LA53_0 == COMMA) :
                    alt53 = 1
                if alt53 == 1:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:349:9: COMMA
                    pass 
                    self.match(self.input, COMMA, self.FOLLOW_COMMA_in_listmaker2775)
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
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:352:1: comparisonList returns [object] : constraint1= constraint ( options {k=2; } : COMMA constraint2= constraint )* ( COMMA )? ;
    def comparisonList(self, ):

        object = None

        constraint1 = None

        constraint2 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:353:3: (constraint1= constraint ( options {k=2; } : COMMA constraint2= constraint )* ( COMMA )? )
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:353:5: constraint1= constraint ( options {k=2; } : COMMA constraint2= constraint )* ( COMMA )?
                pass 
                self._state.following.append(self.FOLLOW_constraint_in_comparisonList2800)
                constraint1 = self.constraint()

                self._state.following.pop()
                #action start
                object = ComparisonList( constraint1 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:354:7: ( options {k=2; } : COMMA constraint2= constraint )*
                while True: #loop54
                    alt54 = 2
                    alt54 = self.dfa54.predict(self.input)
                    if alt54 == 1:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:354:23: COMMA constraint2= constraint
                        pass 
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_comparisonList2818)
                        self._state.following.append(self.FOLLOW_constraint_in_comparisonList2822)
                        constraint2 = self.constraint()

                        self._state.following.pop()
                        #action start
                        object.append_children( [",", constraint2] ) 
                        #action end


                    else:
                        break #loop54
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:355:7: ( COMMA )?
                alt55 = 2
                LA55_0 = self.input.LA(1)

                if (LA55_0 == COMMA) :
                    alt55 = 1
                if alt55 == 1:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:355:9: COMMA
                    pass 
                    self.match(self.input, COMMA, self.FOLLOW_COMMA_in_comparisonList2837)
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
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:358:1: trailer returns [object] : ( LPAREN ( argumentList )? RPAREN | DOT NAME );
    def trailer(self, ):

        object = None

        LPAREN140 = None
        RPAREN142 = None
        DOT143 = None
        NAME144 = None
        argumentList141 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:359:3: ( LPAREN ( argumentList )? RPAREN | DOT NAME )
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
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:359:5: LPAREN ( argumentList )? RPAREN
                    pass 
                    LPAREN140=self.match(self.input, LPAREN, self.FOLLOW_LPAREN_in_trailer2860)
                    #action start
                    object = Trailer( LPAREN140.text ) 
                    #action end
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:359:49: ( argumentList )?
                    alt56 = 2
                    LA56_0 = self.input.LA(1)

                    if (LA56_0 == LPAREN or LA56_0 == NAME or LA56_0 == STRING or LA56_0 == NOT or LA56_0 == OBJECTBINDING or (PLUS <= LA56_0 <= MINUS) or LA56_0 == TILDE or LA56_0 == LBRACK or LA56_0 == LCURLY or (INT <= LA56_0 <= COMPLEX)) :
                        alt56 = 1
                    if alt56 == 1:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:359:50: argumentList
                        pass 
                        self._state.following.append(self.FOLLOW_argumentList_in_trailer2865)
                        argumentList141 = self.argumentList()

                        self._state.following.pop()
                        #action start
                        object.append_child( argumentList141 ) 
                        #action end



                    RPAREN142=self.match(self.input, RPAREN, self.FOLLOW_RPAREN_in_trailer2872)
                    #action start
                    object.append_child( RPAREN142.text ) 
                    #action end


                elif alt57 == 2:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:360:5: DOT NAME
                    pass 
                    DOT143=self.match(self.input, DOT, self.FOLLOW_DOT_in_trailer2880)
                    NAME144=self.match(self.input, NAME, self.FOLLOW_NAME_in_trailer2882)
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
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:363:1: expressionList returns [object] : expression1= expression ( options {k=2; } : COMMA expression2= expression )* ( COMMA )? ;
    def expressionList(self, ):

        object = None

        expression1 = None

        expression2 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:364:3: (expression1= expression ( options {k=2; } : COMMA expression2= expression )* ( COMMA )? )
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:364:5: expression1= expression ( options {k=2; } : COMMA expression2= expression )* ( COMMA )?
                pass 
                self._state.following.append(self.FOLLOW_expression_in_expressionList2905)
                expression1 = self.expression()

                self._state.following.pop()
                #action start
                object = ExpressionList( expression1 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:365:7: ( options {k=2; } : COMMA expression2= expression )*
                while True: #loop58
                    alt58 = 2
                    alt58 = self.dfa58.predict(self.input)
                    if alt58 == 1:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:365:25: COMMA expression2= expression
                        pass 
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_expressionList2925)
                        self._state.following.append(self.FOLLOW_expression_in_expressionList2929)
                        expression2 = self.expression()

                        self._state.following.pop()
                        #action start
                        object.append_children( [ ",", expression2 ] ) 
                        #action end


                    else:
                        break #loop58
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:366:7: ( COMMA )?
                alt59 = 2
                LA59_0 = self.input.LA(1)

                if (LA59_0 == COMMA) :
                    alt59 = 1
                if alt59 == 1:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:366:9: COMMA
                    pass 
                    self.match(self.input, COMMA, self.FOLLOW_COMMA_in_expressionList2944)
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
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:369:1: dictmaker returns [object] : constraint1= constraint COLON constraint2= constraint ( options {k=2; } : COMMA constraint3= constraint COLON constraint4= constraint )* ( COMMA )? ;
    def dictmaker(self, ):

        object = None

        constraint1 = None

        constraint2 = None

        constraint3 = None

        constraint4 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:370:3: (constraint1= constraint COLON constraint2= constraint ( options {k=2; } : COMMA constraint3= constraint COLON constraint4= constraint )* ( COMMA )? )
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:370:5: constraint1= constraint COLON constraint2= constraint ( options {k=2; } : COMMA constraint3= constraint COLON constraint4= constraint )* ( COMMA )?
                pass 
                self._state.following.append(self.FOLLOW_constraint_in_dictmaker2969)
                constraint1 = self.constraint()

                self._state.following.pop()
                #action start
                object = DictMaker( constraint1 ) 
                #action end
                self.match(self.input, COLON, self.FOLLOW_COLON_in_dictmaker2979)
                self._state.following.append(self.FOLLOW_constraint_in_dictmaker2983)
                constraint2 = self.constraint()

                self._state.following.pop()
                #action start
                object.append_children( [":", constraint2] ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:372:9: ( options {k=2; } : COMMA constraint3= constraint COLON constraint4= constraint )*
                while True: #loop60
                    alt60 = 2
                    alt60 = self.dfa60.predict(self.input)
                    if alt60 == 1:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:372:26: COMMA constraint3= constraint COLON constraint4= constraint
                        pass 
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_dictmaker3004)
                        self._state.following.append(self.FOLLOW_constraint_in_dictmaker3008)
                        constraint3 = self.constraint()

                        self._state.following.pop()
                        self.match(self.input, COLON, self.FOLLOW_COLON_in_dictmaker3010)
                        self._state.following.append(self.FOLLOW_constraint_in_dictmaker3014)
                        constraint4 = self.constraint()

                        self._state.following.pop()
                        #action start
                        object.append_children( [",", constraint3, ":", constraint4] ) 
                        #action end


                    else:
                        break #loop60
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:373:9: ( COMMA )?
                alt61 = 2
                LA61_0 = self.input.LA(1)

                if (LA61_0 == COMMA) :
                    alt61 = 1
                if alt61 == 1:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:373:11: COMMA
                    pass 
                    self.match(self.input, COMMA, self.FOLLOW_COMMA_in_dictmaker3031)
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
    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:376:1: argumentList returns [object] : constraint1= constraint ( COMMA constraint2= constraint )* ( COMMA )? ;
    def argumentList(self, ):

        object = None

        constraint1 = None

        constraint2 = None


        try:
            try:
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:377:3: (constraint1= constraint ( COMMA constraint2= constraint )* ( COMMA )? )
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:377:5: constraint1= constraint ( COMMA constraint2= constraint )* ( COMMA )?
                pass 
                self._state.following.append(self.FOLLOW_constraint_in_argumentList3056)
                constraint1 = self.constraint()

                self._state.following.pop()
                #action start
                object = ArgumentList( constraint1 ) 
                #action end
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:378:7: ( COMMA constraint2= constraint )*
                while True: #loop62
                    alt62 = 2
                    LA62_0 = self.input.LA(1)

                    if (LA62_0 == COMMA) :
                        LA62_1 = self.input.LA(2)

                        if (LA62_1 == LPAREN or LA62_1 == NAME or LA62_1 == STRING or LA62_1 == NOT or LA62_1 == OBJECTBINDING or (PLUS <= LA62_1 <= MINUS) or LA62_1 == TILDE or LA62_1 == LBRACK or LA62_1 == LCURLY or (INT <= LA62_1 <= COMPLEX)) :
                            alt62 = 1




                    if alt62 == 1:
                        # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:378:9: COMMA constraint2= constraint
                        pass 
                        self.match(self.input, COMMA, self.FOLLOW_COMMA_in_argumentList3068)
                        self._state.following.append(self.FOLLOW_constraint_in_argumentList3072)
                        constraint2 = self.constraint()

                        self._state.following.pop()
                        #action start
                        object.append_children( [",", constraint2] ) 
                        #action end


                    else:
                        break #loop62
                # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:379:7: ( COMMA )?
                alt63 = 2
                LA63_0 = self.input.LA(1)

                if (LA63_0 == COMMA) :
                    alt63 = 1
                if alt63 == 1:
                    # /Users/walsh/Development/workspace/Intellect/intellect/grammar/Policy.g:379:9: COMMA
                    pass 
                    self.match(self.input, COMMA, self.FOLLOW_COMMA_in_argumentList3087)
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
        u"\1\25\11\uffff\1\11\2\uffff"
        )

    DFA34_max = DFA.unpack(
        u"\1\71\11\uffff\1\115\2\uffff"
        )

    DFA34_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\1\3\1\4\1\5\1\6\1\7\1\10\1\11\1\uffff\1\13\1\12"
        )

    DFA34_special = DFA.unpack(
        u"\15\uffff"
        )

            
    DFA34_transition = [
        DFA.unpack(u"\1\11\33\uffff\1\1\1\2\1\3\1\4\1\5\1\6\1\7\1\10\1\12"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\14\2\uffff\1\14\4\uffff\1\14\3\uffff\1\13\1\uffff"
        u"\1\14\46\uffff\2\14\4\uffff\1\14\1\uffff\1\14\1\uffff\1\14\1\uffff"
        u"\4\14"),
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
        u"\1\56\1\115\54\uffff"
        )

    DFA54_accept = DFA.unpack(
        u"\2\uffff\1\2\16\uffff\1\1\34\uffff"
        )

    DFA54_special = DFA.unpack(
        u"\56\uffff"
        )

            
    DFA54_transition = [
        DFA.unpack(u"\1\2\3\uffff\1\2\1\1\26\uffff\15\2"),
        DFA.unpack(u"\1\2\2\uffff\1\21\1\2\1\uffff\1\21\4\uffff\1\21\3\uffff"
        u"\1\21\1\uffff\1\21\12\uffff\15\2\17\uffff\2\21\4\uffff\1\21\1\uffff"
        u"\1\21\1\uffff\1\21\1\uffff\4\21"),
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
        u"\1\13\1\11\17\uffff"
        )

    DFA58_max = DFA.unpack(
        u"\1\13\1\115\17\uffff"
        )

    DFA58_accept = DFA.unpack(
        u"\2\uffff\1\2\1\uffff\1\1\14\uffff"
        )

    DFA58_special = DFA.unpack(
        u"\21\uffff"
        )

            
    DFA58_transition = [
        DFA.unpack(u"\1\1"),
        DFA.unpack(u"\1\4\2\uffff\1\4\4\uffff\1\4\5\uffff\1\4\46\uffff\2"
        u"\4\4\uffff\1\4\1\uffff\1\4\1\uffff\1\4\1\uffff\4\4"),
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
        u"\1\13\1\11\20\uffff"
        )

    DFA60_max = DFA.unpack(
        u"\1\111\1\115\20\uffff"
        )

    DFA60_accept = DFA.unpack(
        u"\2\uffff\1\2\1\uffff\1\1\15\uffff"
        )

    DFA60_special = DFA.unpack(
        u"\22\uffff"
        )

            
    DFA60_transition = [
        DFA.unpack(u"\1\1\75\uffff\1\2"),
        DFA.unpack(u"\1\4\2\uffff\1\4\4\uffff\1\4\3\uffff\1\4\1\uffff\1"
        u"\4\46\uffff\2\4\4\uffff\1\4\1\uffff\1\4\1\uffff\1\4\1\2\4\4"),
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


 

    FOLLOW_NEWLINE_in_file78 = frozenset([1, 6, 7, 8, 9, 12, 15, 17, 21, 23, 62, 63, 68, 70, 72, 74, 75, 76, 77])
    FOLLOW_statement_in_file82 = frozenset([1, 6, 7, 8, 9, 12, 15, 17, 21, 23, 62, 63, 68, 70, 72, 74, 75, 76, 77])
    FOLLOW_EOF_in_file93 = frozenset([1])
    FOLLOW_importStmt_in_statement111 = frozenset([1])
    FOLLOW_attributeStmt_in_statement120 = frozenset([1])
    FOLLOW_ruleStmt_in_statement129 = frozenset([1])
    FOLLOW_importName_in_importStmt152 = frozenset([1])
    FOLLOW_importFrom_in_importStmt160 = frozenset([1])
    FOLLOW_IMPORT_in_importName180 = frozenset([12])
    FOLLOW_dottedAsNames_in_importName182 = frozenset([6])
    FOLLOW_NEWLINE_in_importName186 = frozenset([1])
    FOLLOW_FROM_in_importFrom204 = frozenset([12])
    FOLLOW_dottedName_in_importFrom208 = frozenset([7])
    FOLLOW_IMPORT_in_importFrom212 = frozenset([9, 12])
    FOLLOW_importAsNames_in_importFrom226 = frozenset([6])
    FOLLOW_LPAREN_in_importFrom238 = frozenset([12])
    FOLLOW_importAsNames_in_importFrom243 = frozenset([10])
    FOLLOW_RPAREN_in_importFrom245 = frozenset([6])
    FOLLOW_NEWLINE_in_importFrom257 = frozenset([1])
    FOLLOW_importAsName_in_importAsNames276 = frozenset([1, 11])
    FOLLOW_COMMA_in_importAsNames288 = frozenset([12])
    FOLLOW_importAsName_in_importAsNames292 = frozenset([1, 11])
    FOLLOW_COMMA_in_importAsNames301 = frozenset([1])
    FOLLOW_NAME_in_importAsName325 = frozenset([1, 13])
    FOLLOW_AS_in_importAsName331 = frozenset([12])
    FOLLOW_NAME_in_importAsName335 = frozenset([1])
    FOLLOW_dottedAsName_in_dottedAsNames359 = frozenset([1, 11])
    FOLLOW_COMMA_in_dottedAsNames371 = frozenset([12])
    FOLLOW_dottedAsName_in_dottedAsNames375 = frozenset([1, 11])
    FOLLOW_dottedName_in_dottedAsName397 = frozenset([1, 13])
    FOLLOW_AS_in_dottedAsName403 = frozenset([12])
    FOLLOW_NAME_in_dottedAsName405 = frozenset([1])
    FOLLOW_NAME_in_dottedName430 = frozenset([1, 14])
    FOLLOW_DOT_in_dottedName442 = frozenset([12])
    FOLLOW_NAME_in_dottedName446 = frozenset([1, 14])
    FOLLOW_expressionStmt_in_attributeStmt469 = frozenset([1])
    FOLLOW_RULE_in_ruleStmt489 = frozenset([12, 17])
    FOLLOW_id_in_ruleStmt491 = frozenset([16])
    FOLLOW_COLON_in_ruleStmt493 = frozenset([6])
    FOLLOW_NEWLINE_in_ruleStmt495 = frozenset([4])
    FOLLOW_INDENT_in_ruleStmt505 = frozenset([18, 19, 20])
    FOLLOW_ruleAttribute_in_ruleStmt509 = frozenset([18, 19, 20])
    FOLLOW_when_in_ruleStmt531 = frozenset([18, 19, 20])
    FOLLOW_then_in_ruleStmt551 = frozenset([5])
    FOLLOW_DEDENT_in_ruleStmt556 = frozenset([1])
    FOLLOW_NAME_in_id574 = frozenset([1])
    FOLLOW_STRING_in_id585 = frozenset([1])
    FOLLOW_agendaGroup_in_ruleAttribute606 = frozenset([1])
    FOLLOW_AGENDAGROUP_in_agendaGroup626 = frozenset([12, 17])
    FOLLOW_id_in_agendaGroup628 = frozenset([6])
    FOLLOW_NEWLINE_in_agendaGroup630 = frozenset([1])
    FOLLOW_WHEN_in_when650 = frozenset([16])
    FOLLOW_COLON_in_when652 = frozenset([6])
    FOLLOW_NEWLINE_in_when654 = frozenset([4])
    FOLLOW_INDENT_in_when664 = frozenset([5, 12, 21, 22, 23])
    FOLLOW_ruleCondition_in_when668 = frozenset([5])
    FOLLOW_DEDENT_in_when675 = frozenset([1])
    FOLLOW_THEN_in_then693 = frozenset([16])
    FOLLOW_COLON_in_then695 = frozenset([6])
    FOLLOW_NEWLINE_in_then697 = frozenset([4])
    FOLLOW_INDENT_in_then707 = frozenset([9, 12, 17, 21, 23, 25, 26, 28, 29, 30, 31, 32, 33, 62, 63, 68, 70, 72, 74, 75, 76, 77])
    FOLLOW_action_in_then711 = frozenset([5, 9, 12, 17, 21, 23, 25, 26, 28, 29, 30, 31, 32, 33, 62, 63, 68, 70, 72, 74, 75, 76, 77])
    FOLLOW_DEDENT_in_then718 = frozenset([1])
    FOLLOW_notCondition_in_ruleCondition736 = frozenset([6])
    FOLLOW_NEWLINE_in_ruleCondition738 = frozenset([1])
    FOLLOW_NOT_in_notCondition766 = frozenset([12, 21, 22, 23])
    FOLLOW_condition_in_notCondition773 = frozenset([1])
    FOLLOW_EXISTS_in_condition801 = frozenset([12, 21, 22, 23])
    FOLLOW_classConstraint_in_condition808 = frozenset([1])
    FOLLOW_OBJECTBINDING_in_classConstraint836 = frozenset([24])
    FOLLOW_ASSIGNEQUAL_in_classConstraint838 = frozenset([12])
    FOLLOW_NAME_in_classConstraint851 = frozenset([9])
    FOLLOW_LPAREN_in_classConstraint853 = frozenset([9, 10, 12, 17, 21, 23, 62, 63, 68, 70, 72, 74, 75, 76, 77])
    FOLLOW_constraint_in_classConstraint859 = frozenset([10])
    FOLLOW_RPAREN_in_classConstraint866 = frozenset([1])
    FOLLOW_simpleStmt_in_action886 = frozenset([1])
    FOLLOW_attributeAction_in_action900 = frozenset([1])
    FOLLOW_learnAction_in_action909 = frozenset([1])
    FOLLOW_forgetAction_in_action921 = frozenset([1])
    FOLLOW_modifyAction_in_action933 = frozenset([1])
    FOLLOW_haltAction_in_action945 = frozenset([1])
    FOLLOW_expressionStmt_in_simpleStmt971 = frozenset([1])
    FOLLOW_printStmt_in_simpleStmt985 = frozenset([1])
    FOLLOW_ATTRIBUTE_in_attributeAction1016 = frozenset([9, 12, 17, 21, 23, 62, 63, 68, 70, 72, 74, 75, 76, 77])
    FOLLOW_expressionStmt_in_attributeAction1018 = frozenset([1])
    FOLLOW_PRINT_in_printStmt1038 = frozenset([6, 9, 12, 17, 21, 23, 27, 62, 63, 68, 70, 72, 74, 75, 76, 77])
    FOLLOW_comparisonList_in_printStmt1052 = frozenset([6])
    FOLLOW_RIGHTSHIFT_in_printStmt1064 = frozenset([9, 12, 17, 21, 23, 62, 63, 68, 70, 72, 74, 75, 76, 77])
    FOLLOW_comparisonList_in_printStmt1068 = frozenset([6])
    FOLLOW_NEWLINE_in_printStmt1075 = frozenset([1])
    FOLLOW_FORGET_in_forgetAction1095 = frozenset([23])
    FOLLOW_DELETE_in_forgetAction1107 = frozenset([23])
    FOLLOW_OBJECTBINDING_in_forgetAction1120 = frozenset([6])
    FOLLOW_NEWLINE_in_forgetAction1124 = frozenset([1])
    FOLLOW_LEARN_in_learnAction1144 = frozenset([12])
    FOLLOW_INSERT_in_learnAction1156 = frozenset([12])
    FOLLOW_NAME_in_learnAction1171 = frozenset([9])
    FOLLOW_LPAREN_in_learnAction1173 = frozenset([9, 10, 12, 17, 21, 23, 62, 63, 68, 70, 72, 74, 75, 76, 77])
    FOLLOW_argumentList_in_learnAction1187 = frozenset([10])
    FOLLOW_RPAREN_in_learnAction1194 = frozenset([6])
    FOLLOW_NEWLINE_in_learnAction1198 = frozenset([1])
    FOLLOW_MODIFY_in_modifyAction1216 = frozenset([23])
    FOLLOW_OBJECTBINDING_in_modifyAction1218 = frozenset([16])
    FOLLOW_COLON_in_modifyAction1220 = frozenset([6])
    FOLLOW_NEWLINE_in_modifyAction1222 = frozenset([4])
    FOLLOW_INDENT_in_modifyAction1232 = frozenset([12])
    FOLLOW_propertyAssignment_in_modifyAction1236 = frozenset([5, 12])
    FOLLOW_DEDENT_in_modifyAction1243 = frozenset([1])
    FOLLOW_HALT_in_haltAction1261 = frozenset([6])
    FOLLOW_NEWLINE_in_haltAction1265 = frozenset([1])
    FOLLOW_NAME_in_propertyAssignment1283 = frozenset([34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46])
    FOLLOW_assignment_in_propertyAssignment1285 = frozenset([9, 12, 17, 21, 23, 62, 63, 68, 70, 72, 74, 75, 76, 77])
    FOLLOW_constraint_in_propertyAssignment1287 = frozenset([6])
    FOLLOW_NEWLINE_in_propertyAssignment1291 = frozenset([1])
    FOLLOW_comparisonList_in_expressionStmt1311 = frozenset([6, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46])
    FOLLOW_assignment_in_expressionStmt1323 = frozenset([9, 12, 17, 21, 23, 62, 63, 68, 70, 72, 74, 75, 76, 77])
    FOLLOW_comparisonList_in_expressionStmt1327 = frozenset([6])
    FOLLOW_NEWLINE_in_expressionStmt1334 = frozenset([1])
    FOLLOW_ASSIGN_in_assignment1352 = frozenset([1])
    FOLLOW_PLUSEQUAL_in_assignment1371 = frozenset([1])
    FOLLOW_MINUSEQUAL_in_assignment1387 = frozenset([1])
    FOLLOW_STAREQUAL_in_assignment1402 = frozenset([1])
    FOLLOW_SLASHEQUAL_in_assignment1418 = frozenset([1])
    FOLLOW_PERCENTEQUAL_in_assignment1433 = frozenset([1])
    FOLLOW_AMPEREQUAL_in_assignment1446 = frozenset([1])
    FOLLOW_VBAREQUAL_in_assignment1461 = frozenset([1])
    FOLLOW_CIRCUMFLEXEQUAL_in_assignment1477 = frozenset([1])
    FOLLOW_LEFTSHIFTEQUAL_in_assignment1487 = frozenset([1])
    FOLLOW_RIGHTSHIFTEQUAL_in_assignment1498 = frozenset([1])
    FOLLOW_DOUBLESTAREQUAL_in_assignment1508 = frozenset([1])
    FOLLOW_DOUBLESLASHEQUAL_in_assignment1518 = frozenset([1])
    FOLLOW_orConstraint_in_constraint1539 = frozenset([1])
    FOLLOW_andConstraint_in_orConstraint1561 = frozenset([1, 47])
    FOLLOW_OR_in_orConstraint1573 = frozenset([9, 12, 17, 21, 23, 62, 63, 68, 70, 72, 74, 75, 76, 77])
    FOLLOW_andConstraint_in_orConstraint1577 = frozenset([1, 47])
    FOLLOW_notConstraint_in_andConstraint1602 = frozenset([1, 48])
    FOLLOW_AND_in_andConstraint1614 = frozenset([9, 12, 17, 21, 23, 62, 63, 68, 70, 72, 74, 75, 76, 77])
    FOLLOW_notConstraint_in_andConstraint1618 = frozenset([1, 48])
    FOLLOW_NOT_in_notConstraint1649 = frozenset([9, 12, 17, 21, 23, 62, 63, 68, 70, 72, 74, 75, 76, 77])
    FOLLOW_comparison_in_notConstraint1656 = frozenset([1])
    FOLLOW_expression_in_comparison1678 = frozenset([1, 21, 49, 50, 51, 52, 53, 54, 55, 56, 57])
    FOLLOW_comparisonOperation_in_comparison1688 = frozenset([9, 12, 17, 21, 23, 62, 63, 68, 70, 72, 74, 75, 76, 77])
    FOLLOW_expression_in_comparison1692 = frozenset([1, 21, 49, 50, 51, 52, 53, 54, 55, 56, 57])
    FOLLOW_LESS_in_comparisonOperation1717 = frozenset([1])
    FOLLOW_GREATER_in_comparisonOperation1736 = frozenset([1])
    FOLLOW_EQUAL_in_comparisonOperation1752 = frozenset([1])
    FOLLOW_GREATEREQUAL_in_comparisonOperation1770 = frozenset([1])
    FOLLOW_LESSEQUAL_in_comparisonOperation1781 = frozenset([1])
    FOLLOW_ALT_NOTEQUAL_in_comparisonOperation1795 = frozenset([1])
    FOLLOW_NOTEQUAL_in_comparisonOperation1806 = frozenset([1])
    FOLLOW_IN_in_comparisonOperation1821 = frozenset([1])
    FOLLOW_NOT_in_comparisonOperation1842 = frozenset([56])
    FOLLOW_IN_in_comparisonOperation1844 = frozenset([1])
    FOLLOW_IS_in_comparisonOperation1861 = frozenset([1])
    FOLLOW_IS_in_comparisonOperation1882 = frozenset([21])
    FOLLOW_NOT_in_comparisonOperation1884 = frozenset([1])
    FOLLOW_bitwiseOrExpr_in_expression1913 = frozenset([1])
    FOLLOW_bitwiseXorExpr_in_bitwiseOrExpr1935 = frozenset([1, 58])
    FOLLOW_VBAR_in_bitwiseOrExpr1947 = frozenset([9, 12, 17, 21, 23, 62, 63, 68, 70, 72, 74, 75, 76, 77])
    FOLLOW_bitwiseXorExpr_in_bitwiseOrExpr1951 = frozenset([1, 58])
    FOLLOW_bitwiseAndExpr_in_bitwiseXorExpr1976 = frozenset([1, 59])
    FOLLOW_CIRCUMFLEX_in_bitwiseXorExpr1988 = frozenset([9, 12, 17, 21, 23, 62, 63, 68, 70, 72, 74, 75, 76, 77])
    FOLLOW_bitwiseAndExpr_in_bitwiseXorExpr1992 = frozenset([1, 59])
    FOLLOW_shiftExpr_in_bitwiseAndExpr2017 = frozenset([1, 60])
    FOLLOW_AMPER_in_bitwiseAndExpr2029 = frozenset([9, 12, 17, 21, 23, 62, 63, 68, 70, 72, 74, 75, 76, 77])
    FOLLOW_shiftExpr_in_bitwiseAndExpr2033 = frozenset([1, 60])
    FOLLOW_arithExpr_in_shiftExpr2058 = frozenset([1, 27, 61])
    FOLLOW_LEFTSHIFT_in_shiftExpr2072 = frozenset([9, 12, 17, 21, 23, 62, 63, 68, 70, 72, 74, 75, 76, 77])
    FOLLOW_RIGHTSHIFT_in_shiftExpr2078 = frozenset([9, 12, 17, 21, 23, 62, 63, 68, 70, 72, 74, 75, 76, 77])
    FOLLOW_arithExpr_in_shiftExpr2096 = frozenset([1, 27, 61])
    FOLLOW_term_in_arithExpr2121 = frozenset([1, 62, 63])
    FOLLOW_PLUS_in_arithExpr2135 = frozenset([9, 12, 17, 21, 23, 62, 63, 68, 70, 72, 74, 75, 76, 77])
    FOLLOW_MINUS_in_arithExpr2141 = frozenset([9, 12, 17, 21, 23, 62, 63, 68, 70, 72, 74, 75, 76, 77])
    FOLLOW_term_in_arithExpr2159 = frozenset([1, 62, 63])
    FOLLOW_factor_in_term2184 = frozenset([1, 64, 65, 66, 67])
    FOLLOW_STAR_in_term2197 = frozenset([9, 12, 17, 21, 23, 62, 63, 68, 70, 72, 74, 75, 76, 77])
    FOLLOW_SLASH_in_term2203 = frozenset([9, 12, 17, 21, 23, 62, 63, 68, 70, 72, 74, 75, 76, 77])
    FOLLOW_PERCENT_in_term2219 = frozenset([9, 12, 17, 21, 23, 62, 63, 68, 70, 72, 74, 75, 76, 77])
    FOLLOW_DOUBLESLASH_in_term2225 = frozenset([9, 12, 17, 21, 23, 62, 63, 68, 70, 72, 74, 75, 76, 77])
    FOLLOW_factor_in_term2247 = frozenset([1, 64, 65, 66, 67])
    FOLLOW_PLUS_in_factor2270 = frozenset([9, 12, 17, 21, 23, 62, 63, 68, 70, 72, 74, 75, 76, 77])
    FOLLOW_factor_in_factor2275 = frozenset([1])
    FOLLOW_MINUS_in_factor2283 = frozenset([9, 12, 17, 21, 23, 62, 63, 68, 70, 72, 74, 75, 76, 77])
    FOLLOW_factor_in_factor2287 = frozenset([1])
    FOLLOW_TILDE_in_factor2295 = frozenset([9, 12, 17, 21, 23, 62, 63, 68, 70, 72, 74, 75, 76, 77])
    FOLLOW_factor_in_factor2299 = frozenset([1])
    FOLLOW_power_in_factor2307 = frozenset([1])
    FOLLOW_atom_in_power2327 = frozenset([1, 9, 14, 69])
    FOLLOW_trailer_in_power2339 = frozenset([1, 9, 14, 69])
    FOLLOW_DOUBLESTAR_in_power2360 = frozenset([9, 12, 17, 21, 23, 62, 63, 68, 70, 72, 74, 75, 76, 77])
    FOLLOW_factor_in_power2362 = frozenset([1])
    FOLLOW_LPAREN_in_atom2385 = frozenset([9, 10, 12, 17, 21, 23, 62, 63, 68, 70, 72, 74, 75, 76, 77])
    FOLLOW_comparisonList_in_atom2424 = frozenset([10])
    FOLLOW_RPAREN_in_atom2453 = frozenset([1])
    FOLLOW_LBRACK_in_atom2461 = frozenset([9, 12, 17, 21, 23, 62, 63, 68, 70, 71, 72, 74, 75, 76, 77])
    FOLLOW_listmaker_in_atom2498 = frozenset([71])
    FOLLOW_RBRACK_in_atom2527 = frozenset([1])
    FOLLOW_LCURLY_in_atom2535 = frozenset([9, 12, 17, 21, 23, 62, 63, 68, 70, 72, 73, 74, 75, 76, 77])
    FOLLOW_dictmaker_in_atom2572 = frozenset([73])
    FOLLOW_RCURLY_in_atom2601 = frozenset([1])
    FOLLOW_NAME_in_atom2610 = frozenset([1])
    FOLLOW_OBJECTBINDING_in_atom2629 = frozenset([1])
    FOLLOW_INT_in_atom2639 = frozenset([1])
    FOLLOW_LONGINT_in_atom2659 = frozenset([1])
    FOLLOW_FLOAT_in_atom2675 = frozenset([1])
    FOLLOW_COMPLEX_in_atom2693 = frozenset([1])
    FOLLOW_STRING_in_atom2713 = frozenset([1, 17])
    FOLLOW_constraint_in_listmaker2738 = frozenset([1, 11])
    FOLLOW_COMMA_in_listmaker2756 = frozenset([9, 12, 17, 21, 23, 62, 63, 68, 70, 72, 74, 75, 76, 77])
    FOLLOW_constraint_in_listmaker2760 = frozenset([1, 11])
    FOLLOW_COMMA_in_listmaker2775 = frozenset([1])
    FOLLOW_constraint_in_comparisonList2800 = frozenset([1, 11])
    FOLLOW_COMMA_in_comparisonList2818 = frozenset([9, 12, 17, 21, 23, 62, 63, 68, 70, 72, 74, 75, 76, 77])
    FOLLOW_constraint_in_comparisonList2822 = frozenset([1, 11])
    FOLLOW_COMMA_in_comparisonList2837 = frozenset([1])
    FOLLOW_LPAREN_in_trailer2860 = frozenset([9, 10, 12, 17, 21, 23, 62, 63, 68, 70, 72, 74, 75, 76, 77])
    FOLLOW_argumentList_in_trailer2865 = frozenset([10])
    FOLLOW_RPAREN_in_trailer2872 = frozenset([1])
    FOLLOW_DOT_in_trailer2880 = frozenset([12])
    FOLLOW_NAME_in_trailer2882 = frozenset([1])
    FOLLOW_expression_in_expressionList2905 = frozenset([1, 11])
    FOLLOW_COMMA_in_expressionList2925 = frozenset([9, 12, 17, 21, 23, 62, 63, 68, 70, 72, 74, 75, 76, 77])
    FOLLOW_expression_in_expressionList2929 = frozenset([1, 11])
    FOLLOW_COMMA_in_expressionList2944 = frozenset([1])
    FOLLOW_constraint_in_dictmaker2969 = frozenset([16])
    FOLLOW_COLON_in_dictmaker2979 = frozenset([9, 12, 17, 21, 23, 62, 63, 68, 70, 72, 74, 75, 76, 77])
    FOLLOW_constraint_in_dictmaker2983 = frozenset([1, 11])
    FOLLOW_COMMA_in_dictmaker3004 = frozenset([9, 12, 17, 21, 23, 62, 63, 68, 70, 72, 74, 75, 76, 77])
    FOLLOW_constraint_in_dictmaker3008 = frozenset([16])
    FOLLOW_COLON_in_dictmaker3010 = frozenset([9, 12, 17, 21, 23, 62, 63, 68, 70, 72, 74, 75, 76, 77])
    FOLLOW_constraint_in_dictmaker3014 = frozenset([1, 11])
    FOLLOW_COMMA_in_dictmaker3031 = frozenset([1])
    FOLLOW_constraint_in_argumentList3056 = frozenset([1, 11])
    FOLLOW_COMMA_in_argumentList3068 = frozenset([9, 12, 17, 21, 23, 62, 63, 68, 70, 72, 74, 75, 76, 77])
    FOLLOW_constraint_in_argumentList3072 = frozenset([1, 11])
    FOLLOW_COMMA_in_argumentList3087 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("PolicyLexer", PolicyParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
