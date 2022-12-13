%{
    #include<iostream>
    #include<bits/stdc++.h>
    #include"function.tab.h"
    extern int yylval;
%}

%%
[" "]+ ;

sqrt return SQRT;
log return LOG;
log10 return LOG10;
pow return POW;
[0-9]+ {
    yylval = atoi(yytext);
    return NUMBER;
}

\n return 0;
. return yytext[0];

%%

yywrap(){}