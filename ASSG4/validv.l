%{
    #include<iostream>
    #include<bits/stdc++.h>
    #include"validv.tab.h"
    using namespace std;  
%}

%%

^[" "]+ ;
[a-zA-Z]+ return A;
[0-9]+ return N;
["_"]+ return U;
[" "]+ return S;
[\n] return 0;
. return yytext[0]; 

%%

int yywrap(){}