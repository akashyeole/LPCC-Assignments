%{
    #include<iostream>
    #include<bits/stdc++.h>
    using namespace std;
    int f = 0;
    int yylex();
    void yyerror(string s);
%}

%token NUMBER
%left '+' '-'
%left '*' '/' '%'
%left '(' ')'

%%

AE : E {
    cout << "Result = " << $$  << endl;
    return 0;
}

E : 
E '+' E { $$ = $1 + $3; } |
E '-' E { $$ = $1 - $3; } |
E '*' E { $$ = $1 * $3; } |
E '/' E { 
   if($3 == 0) {
        yyerror("Cannot DIVIDE by 0!");
        return 0;
   }
   else{
        $$ = $1 / $3;
   }
} |
E '%' E { 
   if($3 == 0) {
        yyerror("Cannot MOD by 0!");
        return 0;
   }
   else{
        $$ = $1 % $3;
   }
} |
'(' E ')' { $$ = $2; }
| NUMBER { $$ = $1; } ;

%%

int main() {
    cout << "\nEnter arithmetic expression: ";
    yyparse();
    if(f == 0){
        cout << "Arithmetic expression is VALID." << endl;
    }
    cout << endl;
    return 0;
}

void yyerror(string s) {
    cout << "Arithemtic expression is INVALID.\n";
    cout << "ERROR: " << s << endl;
    f = 1;
    return;
}