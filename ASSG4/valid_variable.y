%{
    #include<stdio.h>
    #include<stdlib.h>
    int yylex();
    void yyerror(const char *s);
%}
%token A N U
%%
a : 
A N
| a A
| U A
| U N
| U A N
| A U N
| A N U
| A U
| a N
| a U
| a U a
| A;
%%

int main() {
    printf("Enter the variable name: ");
    yyparse();
    printf("Variable name is valid.");
}

void yyerror(const char *s) {
    printf("Variable name is Invalid!\n");
    exit(0);
}