%{
    #include "valid_variable.tab.h"
    #include<stdio.h>
    #include<stdlib.h>
%}
%option noyywrap
%%
[a-zA-Z] return A;
[0-9] return N;
[_] return U;
\n return 0;
. return yytext[0];
%%