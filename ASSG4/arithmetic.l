%{
    // To evaluate an arithmetic expression using YACC tool
    // Name: Akash Yeole
    // Roll. No.: 321092
    // Gr. No.: 22120281
    // Batch: A3
    #include<stdio.h>
    #include "arithmetic.tab.h"
    extern int yylval;
%}

%%
[0-9]+ {
          yylval = atoi(yytext);
          return NUMBER;
       }
[\t] ;
[\n] return 0;
. return yytext[0];
%%

int yywrap() {
    return 1;
}