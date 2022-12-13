%{
    #include<iostream>
    #include<bits/stdc++.h>
    using namespace std;
    int yylex();
    void yyerror(string s);
%}

%token NUMBER SQRT LOG POW LOG10

%%
START : E {
    cout << "Output: " << $$ << endl;
    return 0;
}

E : NUMBER |
SQRT'('E')' { $$ = sqrt($3); } |
LOG'('E')' { $$ = log($3); } |
LOG10'('E')' { $$ = log10($3); } |
POW'('E','E')' { $$ = pow($3, $5); } 

%%

int main() {
    cout << endl << "Enter any inbuilt function call: ";
    yyparse();
    cout << endl;
    return 0;
}

void yyerror(string s) {
    cout << "Invalid Input or Function might not be included in a program!" << endl;
    return;
}