%{
// Recognizing subsets of c language (Without symbol tables)
// Name: Akash Yeole
// Roll. No.: 321092
// Gr. No.: 22120281
// Batch: A3
#include<stdio.h>

%}

DIGIT[0-9]
NUMBER {DIGIT}*
REAL {DIGIT}*[.]{NUMBER}
TEXT [A-Za-z]
KEYWORDS "auto"|"break"|"enum"|"struct"|"typedef"
DATATYPE "int"|"float"|"double"|"long"|"void"|"unsigned char"
CONDTIONAL "if"|"else"|"else if"|"switch"|"case"
ITERATIVE "for"|"while"|"do"
SEMICOLAN ";"
IDENTIFIER {TEXT}({DIGIT}|{TEXT}|"_")*
NONIDENTIFIER {DIGIT}({TEXT}|{DIGIT}|"_")*
ARITHMATIC_OP "+"|"-"|"/"|"%"|"*";
LOGICAL_OP "&&"|"||"|"!"|"!="
RELEATIONAL_OP "<"|">"|"<="|">="|"=="
UNARY "++"|"--"
FUNCTION {ACCESS}{DATATYPE}{IDENTIFER}"("({DATATYPE}{IDENTIFIER})*")"

%%

[  \n\t]+ ;
{CONDTIONAL} {printf("%s\tis a CONDITIONAL \n",yytext);}
{ITERATIVE} {printf("%s\tis an ITERATIVE \n",yytext);}
{DATATYPE} {printf("%s\tis a DATATYPE\n",yytext);}
{KEYWORDS} {printf("%s\tis a KEYWORDS \n",yytext);}
{IDENTIFIER} {printf("%s\tis an IDENTIFIER \n",yytext);}
{REAL} {printf("%s\tis a REAL \n",yytext);}
{NUMBER} {printf("%s\tis a NUMBER \n",yytext);}
{NONIDENTIFIER} {printf("%S\tis a NONIDENTIFIER \n",yytext);}
{SEMICOLAN} {printf("%s\tis a SEMICOLAN \n",yytext);}
{UNARY} {printf("%s\tis an UNARY \n",yytext);}
{ARITHMATIC_OP} {printf("%s\tis an ARITHMATIC_OP \n",yytext);}
{LOGICAL_OP} {printf("%s\tis a LOGICAL OP \n",yytext);}
{RELEATIONAL_OP} {printf("%s\tis a RELEATIONAL OP \n",yytext);}
"=" {printf("%s\tis an ASSIGNMENT OP \n",yytext);}
"{" {printf("%s\tis a BLOCK BEGIN \n",yytext);}
"}" {printf("%s\tis a BLOCK END \n",yytext);}
"(" {printf("%s\tis a PARATHRSIS BEGIN \n",yytext);}
")" {printf("%s\tis a PARATHRSIS END \n",yytext);}
. ;

%%
int yywrap(void){}
main ( )
{ 
 printf("Enter construct of C language below-\n");
 yylex();
 return 0;  
} 