/*
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
*/
/** 
 *  @author: Michael Joseph Walsh
 *
 *  A policy grammar derived from the ANTLR3 Python 2.3.3 Grammar authored by
 *  Terence Parr and Loring Craymer. 
 */

grammar Policy;

options {
  language = Python;
}

tokens {
  INDENT;
  DEDENT;
}

@header {
from intellect.Node import *
}

@lexer::init {
  self.implicitLineJoiningLevel = 0
  self.startPosition = -1
}

//
// P A R S E R  R U L E S
//

file returns [object] // returns a policy File object
  @init{ $object = File() }
  : ( NEWLINE | statement { $object.append_child( $statement.object ) } )+
  | EOF
  ;

statement returns [object] // returns a Statment object
  : importStmt  { $object = Statement( $importStmt.object, $importStmt.object.line, $importStmt.object.column ) }
  | attributeStmt  { $object = Statement( $attributeStmt.object ) }
  | ruleStmt    { $object = Statement( $ruleStmt.object, $ruleStmt.object.line, $ruleStmt.object.column ) }
  ;

importStmt returns [object] // returns a ImportStmt object
  : importName { $object = ImportStmt( children = $importName.object, line = $importName.object.line ) }
  | importFrom { $object = ImportStmt( children = $importFrom.object, line = $importFrom.object.line ) }
  ;

importName returns [object] // returns an ImportName object
  : IMPORT dottedAsNames { $object = ImportName( children = [$IMPORT.text, $dottedAsNames.object], line = $IMPORT.getLine() ) } NEWLINE
  ;

importFrom returns [object] // returns an ImportFrom object
  : FROM { $object = ImportFrom( children = $FROM.text, line = $FROM.getLine() ) } dottedName { $object.append_child( $dottedName.object ) } IMPORT { $object.append_child( $IMPORT.text ) }
      ( importAsNames1=importAsNames { object.append_child( $importAsNames1.object ) }
      | LPAREN  importAsNames2=importAsNames RPAREN { $object.append_children( [$LPAREN.text, $importAsNames2.object, $RPAREN.text] ) }
      ) NEWLINE
  ;

importAsNames returns [object]
  : importAsName1=importAsName { $object=ImportAsNames( $importAsName1.object ) }
      ( COMMA importAsName2=importAsName { $object.append_children( [",", $importAsName2.object] ) } )* ( COMMA { $object.append_child( "," ) } )?
  ;

importAsName returns [object]
  : name1=NAME { $object=ImportAsName( $name1.text ) } ( AS name2=NAME { $object.append_children( [$AS.text, $name2.text] ) } )?
  ;

dottedAsNames returns [object]
  : dottedAsName1=dottedAsName { $object = DottedAsNames( $dottedAsName1.object ) }
      ( COMMA dottedAsName2=dottedAsName { object.append_children( [$COMMA.text, $dottedAsName2.object] ) } )*
  ;

dottedAsName returns [object]
  : dottedName { $object = DottedAsName( $dottedName.object ) } ( AS NAME { $object.append_children( [$AS.text, $NAME.text] ) } )?
  ;

dottedName returns [object] // returns a DottedName object
  : name1=NAME { $object = DottedName( $name1.text ) }
      ( DOT name2=NAME { $object.append_children( [$DOT.text, $name2.text] ) } )*
  ;

attributeStmt returns [object] // returns an AttributeStmt object.
  : expressionStmt { $object = AttributeStmt( $expressionStmt.object ) }
  ;

ruleStmt returns [object] // returns a RuleStmt object.
  : RULE id COLON NEWLINE { $object = RuleStmt( [ $RULE.text, $id.object, $COLON.text ], $RULE.getLine(), $RULE.getCharPositionInLine() ) }
      INDENT ( ruleAttribute { $object.append_child( $ruleAttribute.object ) } )*
             ( when { $object.append_child( $when.object ) } )?
             then { $object.append_child( $then.object ) }  DEDENT
  ;

id returns [object] // returns an Id object
  : NAME    { $object = Id( $NAME.text ) }
  | STRING  { $object = Id( $STRING.text ) }
  ;

ruleAttribute returns [object] // returns a RuleAttribute object
  : agendaGroup { $object = RuleAttribute( $agendaGroup.object, $agendaGroup.object.line, $agendaGroup.object.column ) }
  ;

agendaGroup returns [object] // returns a RuleGroup
  : AGENDAGROUP id NEWLINE { $object = AgendaGroup( [ $AGENDAGROUP.text, $id.object ], $AGENDAGROUP.getLine(), $AGENDAGROUP.getCharPositionInLine() ) }
  ;

when returns [object] //returns a When object
  : WHEN COLON NEWLINE { $object = When( [$WHEN.text, $COLON.text], $WHEN.getLine(), $WHEN.getCharPositionInLine() ) }
      INDENT ( ruleCondition { $object.append_child( $ruleCondition.object ) } )? DEDENT
  ;

then returns [object] //return a Then object
  : THEN COLON NEWLINE { $object = Then( [$THEN.text, $COLON.text], $THEN.getLine(), $THEN.getCharPositionInLine() ) }
      INDENT ( action { $object.append_child( $action.object ) } )+ DEDENT
  ;

ruleCondition returns [object] // returns a NotCondition object
  : notCondition NEWLINE { $object = RuleCondition($notCondition.object) }
  ;

notCondition returns [object] // returns a NotCondition object
  @init{ $object = NotCondition() }
  : ( NOT { $object.append_child( $NOT.text ) } )* condition { $object.append_child( $condition.object ) }
  ;

condition returns [object] // returns a Condition object
  @init{ $object = Condition() }
  : ( EXISTS { $object.append_child( $EXISTS.text ) } )? classConstraint { $object.append_child( $classConstraint.object ) }
  ;

classConstraint returns [object] // returns ClassConstraint object
  @init{ $object = ClassConstraint() }
  : ( OBJECTBINDING ASSIGNEQUAL { $object.append_children( [ $OBJECTBINDING.text, $ASSIGNEQUAL.text] ) } )?
      NAME LPAREN { $object.append_children( [$NAME.text, $LPAREN.text] ); } ( constraint { $object.append_child( $constraint.object ) } )? RPAREN { $object.append_child( $RPAREN.text ) }
  ;

action returns [object] // returns an Action object
  : simpleStmt       { $object = Action( $simpleStmt.object, $simpleStmt.object.line, $simpleStmt.object.column ) }
  | attributeAction  { $object = Action( $attributeAction.object, $attributeAction.object.line, $attributeAction.object.column ) }
  | learnAction     { $object = Action( $learnAction.object, $learnAction.object.line, $learnAction.object.column ) }
  | forgetAction     { $object = Action( $forgetAction.object, $forgetAction.object.line, $forgetAction.object.column ) }
  | modifyAction     { $object = Action( $modifyAction.object, $modifyAction.object.line, $modifyAction.object.column ) }
  | haltAction       { $object = Action( $haltAction.object, $haltAction.object.line, $haltAction.object.column ) }
  ;

simpleStmt returns [object] // returns a SimpleStmt object
  : expressionStmt       { $object = SimpleStmt( $expressionStmt.object ) }
  | printStmt            { $object = SimpleStmt( $printStmt.object, $printStmt.object.line, $printStmt.object.column ) }
  ;

attributeAction returns [object] // returns a AttributeAction object
  : ATTRIBUTE expressionStmt { $object = AttributeAction( [ $ATTRIBUTE.text, $expressionStmt.object ] , $ATTRIBUTE.getLine(), $ATTRIBUTE.getCharPositionInLine() ) }
  ;

printStmt returns [object] // returns a PrintStmt object
  : PRINT { $object = PrintStmt( $PRINT.text, $PRINT.getLine(), $PRINT.getCharPositionInLine() ) }
      ( comparisonList1=comparisonList { $object.append_child( $comparisonList1.object ) }
      | RIGHTSHIFT comparisonList2=comparisonList { object.append_children( [$RIGHTSHIFT.text, $comparisonList2.object] ) } )? NEWLINE
  ;

forgetAction returns [object] // returns a ForgetAction object
  : ( FORGET { $object = ForgetAction( $FORGET.text, $FORGET.getLine(), $FORGET.getCharPositionInLine() ) }
      | DELETE { $object = ForgetAction( $DELETE.text, $DELETE.getLine(), $DELETE.getCharPositionInLine() ) } ) 
      OBJECTBINDING { $object.append_child( $OBJECTBINDING.text ) } NEWLINE
  ;

learnAction returns [object] // returns an LearnActions object
  : ( LEARN { $object = LearnAction( $LEARN.text, $LEARN.getLine(), $LEARN.getCharPositionInLine() ) }
      | INSERT { $object = LearnAction( $INSERT.text, $INSERT.getLine(), $INSERT.getCharPositionInLine() ) } ) 
        NAME LPAREN { $object.append_children( [$NAME.text, $LPAREN.text] ) }
        ( argumentList { $object.append_child( $argumentList.object ) } )? RPAREN { $object.append_child( $RPAREN.text ) } NEWLINE
  ;

modifyAction returns [object] // returns a ModifyAction object
  : MODIFY OBJECTBINDING COLON NEWLINE { $object = ModifyAction( [$MODIFY.text, $OBJECTBINDING.text, $COLON.text], $MODIFY.getLine(), $MODIFY.getCharPositionInLine() ) }
      INDENT ( propertyAssignment { $object.append_child( $propertyAssignment.object ) } )+ DEDENT
  ;

haltAction returns [object] // returns a HaltAction object
  : HALT { $object = HaltAction( $HALT.text, $HALT.getLine(), $HALT.getCharPositionInLine() ) } NEWLINE
  ;

propertyAssignment returns [object] // returns a PropertyAssignment object
  : NAME assignment constraint {$object = PropertyAssignment( [$NAME.text, $assignment.object, $constraint.object] ) } NEWLINE
  ;

expressionStmt returns [object] // returns a ExpressionStmt object
  : comparisonList1=comparisonList { $object = ExpressionStmt( $comparisonList1.object ) }
      ( assignment comparisonList2=comparisonList { $object.append_children( [$assignment.object, $comparisonList2.object] ) } )? NEWLINE
  ;

assignment returns [object] // returns a Assign object
  : ASSIGN            { $object = Assignment( $ASSIGN.text ) }
  | PLUSEQUAL         { $object = Assignment( $PLUSEQUAL.text ) }
  | MINUSEQUAL        { $object = Assignment( $MINUSEQUAL.text ) }
  | STAREQUAL         { $object = Assignment( $STAREQUAL.text ) }
  | SLASHEQUAL        { $object = Assignment( $SLASHEQUAL.text ) }
  | PERCENTEQUAL      { $object = Assignment( $PERCENTEQUAL.text ) }
  | AMPEREQUAL        { $object = Assignment( $AMPEREQUAL.text ) }
  | VBAREQUAL         { $object = Assignment( $VBAREQUAL.text ) }
  | CIRCUMFLEXEQUAL   { $object = Assignment( $CIRCUMFLEXEQUAL.text ) }
  | LEFTSHIFTEQUAL    { $object = Assignment( $LEFTSHIFTEQUAL.text ) }
  | RIGHTSHIFTEQUAL   { $object = Assignment( $RIGHTSHIFTEQUAL.text ) }
  | DOUBLESTAREQUAL   { $object = Assignment( $DOUBLESTAREQUAL.text ) }
  | DOUBLESLASHEQUAL  { $object = Assignment( $DOUBLESLASHEQUAL.text ) }
  ;

constraint returns [object] // returns a Contraint object
  : orConstraint { $object = Constraint( $orConstraint.object ) }
  ;

orConstraint returns [object] // returns an OrContraint object
  : constraint1=andConstraint { $object = OrConstraint( $constraint1.object ) }
      ( OR constraint2=andConstraint { $object.append_children( [$OR.text, $constraint2.object] ) } )*
  ;

andConstraint returns [object] // returns an AndConstraint object
  : constraint1=notConstraint {$object = AndConstraint( $constraint1.object )}
      ( AND constraint2=notConstraint { $object.append_children( [$AND.text, $constraint2.object] ) } )*
  ;

notConstraint returns [object] // returns a NotConstraint object
  @init{ $object = NotConstraint() }
  : ( NOT { $object.append_child( $NOT.text ) } )* comparison { $object.append_child( $comparison.object ) }
  ;

comparison returns [object] // returns a Comparison object
  : expression1=expression { $object = Comparison( $expression1.object ) }
    ( comparisonOperation expression2=expression { $object.append_children( [ $comparisonOperation.object, $expression2.object] ) } )*
  ;

comparisonOperation returns [object] // returns a ComparisonOperation object
  : ( LESS          { $object = ComparisonOperation( $LESS.text ) }
    | GREATER       { $object = ComparisonOperation( $GREATER.text ) }
    | EQUAL         { $object = ComparisonOperation( $EQUAL.text ) }
    | GREATEREQUAL  { $object = ComparisonOperation( $GREATEREQUAL.text ) }
    | LESSEQUAL     { $object = ComparisonOperation( $LESSEQUAL.text ) }
    | ALT_NOTEQUAL  { $object = ComparisonOperation( $ALT_NOTEQUAL.text ) }
    | NOTEQUAL      { $object = ComparisonOperation( $NOTEQUAL.text ) }
    | IN            { $object = ComparisonOperation( "in" ) }
    | NOT IN        { $object = ComparisonOperation( "not in" ) }
    | IS            { $object = ComparisonOperation( "is" ) }
    | IS NOT        { $object = ComparisonOperation( "is not" ) } )
  ;

expression returns [object] // returns Exrpession object
  : bitwiseOrExpr { $object = Expression( $bitwiseOrExpr.object ) }
  ;

bitwiseOrExpr returns [object] // returns a BitwiseOrExpr object
  : expr1=bitwiseXorExpr { $object = BitwiseOrExpr( $expr1.object ) }
      ( VBAR expr2=bitwiseXorExpr { $object.append_children( [$VBAR.text, $expr2.object] ) } )*
  ;

bitwiseXorExpr returns [object] // returns a BitwiseXorExpr object
  : expr1=bitwiseAndExpr { $object = BitwiseXorExpr( $expr1.object ) }
      ( CIRCUMFLEX expr2=bitwiseAndExpr { $object.append_children( [$CIRCUMFLEX.text, $expr2.object] ) } )*
  ;

bitwiseAndExpr returns [object] // returns a BitwiseAndExpr object
  : expr1=shiftExpr { $object = BitwiseAndExpr( $expr1.object ) }
      ( AMPER expr2=shiftExpr { $object.append_children( [$AMPER.text, $expr2.object] ) } )*
  ;

shiftExpr returns [object] // returns a ShiftExpr object
  : expr1=arithExpr { $object = ShiftExpr( $expr1.object ) }
      ( ( LEFTSHIFT { $object.append_child( $LEFTSHIFT.text ) } | RIGHTSHIFT { $object.append_child( $RIGHTSHIFT.text ) } )
          expr2=arithExpr { $object.append_child( $expr2.object ) } )*
  ;

arithExpr returns [object] // returns a ArithExpr object
  : term1=term { $object = ArithExpr( $term1.object ) }
      ( ( PLUS { $object.append_child( $PLUS.text ) } | MINUS { $object.append_child( $MINUS.text ) } )
          term2=term { $object.append_child( $term2.object ) } )*
  ;

term returns [object] // returns a Term object
  : factor1=factor {$object = Term( $factor1.object ) }
      ( (STAR { $object.append_child( $STAR.text ) } | SLASH { $object.append_child( $SLASH.text ) }
          | PERCENT { $object.append_child( $PERCENT.text ) } | DOUBLESLASH { $object.append_child( $DOUBLESLASH.text ) } )
              factor2=factor { $object.append_child( $factor2.object ) } )*
  ;

factor returns [object] // returns a Factor object
  : PLUS  factor1=factor { $object = Factor( [$PLUS.text, $factor1.object] ) }
  | MINUS factor2=factor { $object = Factor( [$MINUS.text, $factor2.object] ) }
  | TILDE factor3=factor { $object = Factor( [$TILDE.text, $factor3.object] ) }
  | power { $object = Factor( $power.object ) }
  ;

power returns [object] // returns a Power object
  : atom { $object = Power( $atom.object ) }
      ( trailer { $object.append_child( $trailer.object ) } )*
      (options {greedy=true;}:DOUBLESTAR factor { $object.append_children( [$DOUBLESTAR.text, $factor.object] ) } )?
  ;

atom returns [object] // returns a Atom object
  : LPAREN          {$object = Atom( $LPAREN.text ) }
                      ( comparisonList1=comparisonList { $object.append_child( $comparisonList1.object ) } )?
                      RPAREN { $object.append_child( $RPAREN.text ) }
  | LBRACK          {$object = Atom( $LBRACK.text ) }
                      ( listmaker { $object.append_child( $listmaker.object ) } )?
                      RBRACK { $object.append_child( $RBRACK.text ) }
  | LCURLY          {$object = Atom( $LCURLY.text ) }
                      ( dictmaker { $object.append_child( $dictmaker.object ) } )?
                      RCURLY { $object.append_child( $RCURLY.text ) }
//  | BACKQUOTE       comparisonList2=comparisonList BACKQUOTE { $object = Atom( ["`" , $comparisonList2.object, "`"] ) } Removed, used repr(contraint) instead
  | NAME            {$object = Atom( $NAME.text ) }
  | OBJECTBINDING   {$object = Atom( $OBJECTBINDING.text ) }
  | INT             {$object = Atom( $INT.text ) }
  | LONGINT         {$object = Atom( $LONGINT.text ) }
  | FLOAT           {$object = Atom( $FLOAT.text ) }
  | COMPLEX         {$object = Atom( $COMPLEX.text ) }
  | {$object = Atom() } ( STRING { $object.append_child( $STRING.text ) } )+
  ;

listmaker returns [object] // returns a ListMaker object
  : constraint1=constraint {$object = ListMaker( $constraint1.object ) }
      (options {greedy=true;}:COMMA constraint2=constraint { $object.append_children( [ ",", $constraint2.object] ) } )*
      ( COMMA { $object.append_child( "," ) } )?
  ;

comparisonList returns [object] // returns a ComparisonList object
  : constraint1=constraint { $object = ComparisonList( $constraint1.object ) }
      (options {k=2;}:COMMA constraint2=constraint { $object.append_children( [",", $constraint2.object] ) } )*
      ( COMMA { $object.append_child( "," ) } )?
  ;

trailer returns [object] // returns a Trailer object
  : LPAREN {$object = Trailer( $LPAREN.text ) } (argumentList { $object.append_child( $argumentList.object ) } )? RPAREN { $object.append_child( $RPAREN.text ) }
  | LBRACK {$object = Trailer( $LBRACK.text ) } (constraint { $object.append_child( $constraint.object ) } )? RBRACK { $object.append_child( $RBRACK.text ) }
  | DOT NAME { $object = Trailer( [$DOT.text, $NAME.text] ) }
  ;

expressionList  returns [object] // returns an ExpressionList object
  : expression1=expression { $object = ExpressionList( $expression1.object ) }
      ( options {k=2;}: COMMA expression2=expression { $object.append_children( [ ",", $expression2.object ] ) } )*
      ( COMMA { $object.append_child( "," ) } )?
  ;

dictmaker returns [object] // returns a DictMaker object
  : constraint1=constraint { $object = DictMaker( $constraint1.object ) }
      COLON constraint2=constraint { $object.append_children( [":", $constraint2.object] ) }
        (options {k=2;}: COMMA constraint3=constraint COLON constraint4=constraint { $object.append_children( [",", $constraint3.object, ":", $constraint4.object] ) } )*
        ( COMMA { $object.append_child( "," ) } )?
  ;

argumentList returns [object] // returns an ArgumentList object
  : constraint1=constraint { $object = ArgumentList( $constraint1.object ) }
      ( COMMA constraint2=constraint { $object.append_children( [",", $constraint2.object] ) } )*
      ( COMMA { $object.append_child( "," ) } )?
  ;

//
// L E X E R
//

LPAREN
  : '(' {self.implicitLineJoiningLevel += 1}
  ;

RPAREN
  : ')' {self.implicitLineJoiningLevel -= 1}
  ;

LBRACK
  : '[' {self.implicitLineJoiningLevel += 1}
  ;

RBRACK
  : ']' {self.implicitLineJoiningLevel -= 1}
  ;

LCURLY
  : '{' {self.implicitLineJoiningLevel += 1}
  ;

RCURLY
  : '}' {self.implicitLineJoiningLevel -= 1}
  ;

COLON
  : ':'
  ;

COMMA
  : ','
  ;

DOT
  : '.'
  ;

SEMI
  : ';'
  ;

PLUS
  : '+'
  ;

MINUS
  : '-'
  ;

STAR
  : '*'
  ;

DOLLAR
  : '$'
  ;

SLASH
  : '/'
  ;

VBAR
  : '|'
  ;

AMPER
  : '&'
  ;

LESS
  : '<'
  ;

GREATER
  : '>'
  ;

ASSIGN
  : '='
  ;

PERCENT
  : '%'
  ;

BACKQUOTE
  : '`'
  ;

CIRCUMFLEX
  : '^'
  ;

TILDE
  : '~'
  ;

EQUAL
  : '=='
  ;

ASSIGNEQUAL
  : ':='
  ;

NOTEQUAL
  : '!='
  ;

ALT_NOTEQUAL
  : '<>'
  ;

LESSEQUAL
  : '<='
  ;

LEFTSHIFT
  : '<<'
  ;

GREATEREQUAL
  : '>='
  ;

RIGHTSHIFT
  : '>>'
  ;

PLUSEQUAL
  : '+='
  ;

MINUSEQUAL
  : '-='
  ;

DOUBLESTAR
  : '**'
  ;

STAREQUAL
  : '*='
  ;

DOUBLESLASH
  : '//'
  ;

SLASHEQUAL
  : '/='
  ;

VBAREQUAL
  : '|='
  ;

PERCENTEQUAL
  : '%='
  ;

AMPEREQUAL
  : '&='
  ;

CIRCUMFLEXEQUAL
  : '^='
  ;

LEFTSHIFTEQUAL
  : '<<='
  ;

RIGHTSHIFTEQUAL
  : '>>='
  ;

DOUBLESTAREQUAL
  : '**='
  ;

DOUBLESLASHEQUAL
  : '//='
  ;

GLOBAL
  : 'global'
  ;

ATTRIBUTE
  : 'attribute'
  ;

RULE
  : 'rule'
  ;

AGENDAGROUP
  : 'agenda-group'
  ;

WHEN
  : 'when'
  ;

EXISTS
  : 'exists'
  ;

THEN
  : 'then'
  ;

MODIFY
  : 'modify'
  ;

INSERT
  : 'insert'
  ;

LEARN
  : 'learn'
  ;

DELETE
  : 'delete'
  ;

FORGET
  : 'forget'
  ;

HALT
  : 'halt'
  ;

PRINT
  : 'print'
  ;

IMPORT
  : 'import'
  ;

FROM
  : 'from'
  ;

AND
  : 'and'
  ;

OR
  : 'or'
  ;

IN
  : 'in'
  ;

IS
  : 'is'
  ;

AS
  : 'as'
  ;

NOT
  : 'not'
  ;

fragment
LETTER
  : ('a'..'z' | 'A'..'Z')
  ;

fragment
DIGIT
  : ('0'.. '9')
  ;

FLOAT
  : '.' DIGIT+ (EXPONENT)?
  | DIGIT+ '.' EXPONENT
  | DIGIT+ ('.' (DIGIT+ (EXPONENT)?)? | EXPONENT)
  ;

LONGINT
  : INT ('l'|'L')
  ;

fragment
EXPONENT
  : ('e' | 'E') ( '+' | '-' )? DIGIT+
  ;

INT
  : '0' ('x' | 'X') ( DIGIT | 'a' .. 'f' | 'A' .. 'F' )+
  | '0' DIGIT*
  | '1'..'9' DIGIT*
  ;

COMPLEX
  : INT ('j'|'J')
  | FLOAT ('j'|'J')
  ;

NAME
  : ( LETTER | '_') ( LETTER | '_' | DIGIT )*
  ;

OBJECTBINDING
  : DOLLAR NAME
  ;

STRING
  : ('r'|'u'|'ur')?
    (   '\'\'\'' (options {greedy=false;}:TRIAPOS)* '\'\'\''
    |   '"""' (options {greedy=false;}:TRIQUOTE)* '"""'
    |   '"' (ESC|~('\\'|'\n'|'"'))* '"'
    |   '\'' (ESC|~('\\'|'\n'|'\''))* '\''
    )
  ;

fragment
TRIQUOTE
	: '"'? '"'? (ESC|~('\\'|'"'))+
	;

fragment
TRIAPOS
  : '\''? '\''? (ESC|~('\\'|'\''))+
  ;

fragment
ESC
    :    '\\' .
    ;

CONTINUED_LINE
  : '\\' ( '\r' )? '\n' ( ' ' | '\t' )*  { $channel=HIDDEN }
      ( newline=NEWLINE { self.emit( ClassicToken( NEWLINE, newline.text ) ) }
        |
        )
  ;

NEWLINE
  : ( ( '\u000C' )? ( '\r' )? '\n' )+ {
    if self.startPosition == 0 or self.implicitLineJoiningLevel > 0:
        $channel=HIDDEN
    }
  ;

WS
  : { self.startPosition > 0 }? => ( ' ' | '\t' )+ { $channel=HIDDEN }
  ;

LEADING_WS
  @init { spaces = 0 }
  : { self.startPosition == 0 }? =>
      ( {self.implicitLineJoiningLevel > 0}? ( ' ' | '\t' )+ { $channel=HIDDEN }
        | (    ' ' { spaces += 1 }
            | '\t' {
                     spaces += 8
                     spaces -= (spaces \% 8)
                   }
            )+ { self.emit(ClassicToken(LEADING_WS, ' '*spaces)) }
               ( ('\r')? '\n' {
                 if self._state.token is not None:
                     self._state.token.setChannel(99)
                 else:
                     $channel=HIDDEN
	               }
                   )*
        )
  ;
 
COMMENT
  @init { $channel=HIDDEN }
  : { self.startPosition == 0 }? => (' '|'\t')* '#' (~'\n')* '\n'+
    | { self.startPosition > 0 }? => '#' (~'\n')*
  ;
