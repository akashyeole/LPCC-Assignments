%{
    #include<iostream>
    #include<bits/stdc++.h>
    #include "arithmetic.tab.h"
    using namespace std;
    extern int yylval;

%}

%%

[0-9]+ {
    yylval = atoi(yytext);
    return NUMBER;
}

[" "]+ ;
[\n] return 0;
. return yytext[0];

%%

int yywrap() {
    return 1;
}