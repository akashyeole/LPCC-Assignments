%{
    #include<iostream>
    #include<bits/stdc++.h>
    using namespace std;
    int f = 0;
    int yylex();
    void yyerror(string s);
%}

%token A N U S
%%

a : A |
A N |
a A |
U A |
U N |
U A N |
A U N |
A N U |
A U |
a N |
a U |
a U a;

%%

int main() {
    cout << endl << "Enter variable name to validate: ";
    yyparse();
    if(f == 0){
        cout << "Variable name is VALID." << endl;
    }
    cout << endl;
    return 0;
}

void yyerror(string s) {
    f = 1;
    cout << "Variable name is INVALID!" << endl;
    return;
}