%{
#include<iostream>
#include<bits/stdc++.h>
using namespace std;
%}

DIGIT [0-9]
NUMBER {DIGIT}+
REAL {DIGIT}*[.]{NUMBER}
TEXT [a-zA-Z]+
KEYWORDS "return"|"break"|"enum"|"struct"|"typedef"|"return"
DATATYPE ("int"|"float"|"double"|"long"|"unsigned"|"void"|"char")+(["*"]*)
CONDITIONAL "if"|"else"|"else if"|"switch"|"case"
ITERATIVE "for"|"while"|"do"
SEMICOLON ";"
IDENTIFIER {TEXT}({NUMBER}|{TEXT}|"_")*
ARITHMETIC_OPERATOR "+"|"-"|"/"|"%"|"*";
BINARY_OPERATOR "&"|"|"|"^"|"<<"|">>"
LOGICAL_OPERATOR "&&"|"||"|"!"
RELATIONAL_OPERATOR "<"|">"|"<="|">="|"=="
UNARY "++"|"--"
FUNCTION {DATATYPE}[" "]+{IDENTIFIER}[" "]*"("({DATATYPE}[" "]+{IDENTIFIER})*")"

%%
[" "|.]+ ;
{CONDITIONAL} {
    cout << "'" << yytext << "': is a CONDITIONAL.\n";
}

{ITERATIVE} {
    cout << "'" << yytext << "': is a ITERATVIE.\n";
}

{FUNCTION} {
    cout << "'" << yytext << "': is a FUNCTION.\n";
}

{DATATYPE} {
    cout << "'" << yytext << "': is a DATATYPE.\n";
}

{KEYWORDS} {
    cout << "'" << yytext << "': is a KEYWORD.\n";
}

{IDENTIFIER} {
    cout << "'" << yytext << "': is a IDENTIFIER.\n";
}

{REAL} {
    cout << "'" << yytext << "': is a REAL.\n";
}

{NUMBER} {
    cout << "'" << yytext << "': is a NUMBER.\n";
}

{SEMICOLON} {
    cout << "'" << yytext << "': is a SEMICOLON.\n";
}

{UNARY} {
    cout << "'" << yytext << "': is a UNARY.\n";
}

{ARITHMETIC_OPERATOR} {
    cout << "'" << yytext << "': is a ARITHMETIC OPERATOR.\n";
}

{BINARY_OPERATOR} {
    cout << "'" << yytext << "': is a BINARY OPERATOR.\n";
}

{LOGICAL_OPERATOR} {
    cout << "'" << yytext << "': is a LOGICAL OPERATOR.\n";
}

{RELATIONAL_OPERATOR} {
    cout << "'" << yytext << "': is a RELATIONAL OPERATOR.\n";
}

"{" {
    cout << "'" << yytext << "': is an BLOCK BEGIN.\n";
}

"}" {
    cout << "'" << yytext << "': is an BLOCK END.\n";
}

"(" {
    cout << "'" << yytext << "': is an PARANTHESIS OPEN.\n";
}

")" {
    cout << "'" << yytext << "': is an PARANTHESIS CLOSE.\n";
}

.|\n {
    cout << "\nEnter any type of token in C: ";  
}
%%

int yywrap(void){}
int main(){
    cout << "Enter any type of token in C: "; 
    yylex();
    return 0;
}