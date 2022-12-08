%{
    #include<stdio.h>
    int flag=0;
    int yylex();
    void yyerror(const char *s);
   
%}
%token NUMBER

%left '+' '-'
%left '*' '/' '%'
%left '(' ')'
%%
ArithmeticExpression: E {
            printf("\nResult=: %d\n",$$);
            return 0;
}
E : 
E '+' E {$$=$1+$3;}
| E '-' E {$$=$1-$3;}
| E '*' E {$$=$1*$3;}
| E '/' E {$$=$1/$3;}
| E '%' E {$$=$1%$3;}
|'(' E ')' {$$=$2;}
| NUMBER {$$=$1;}
;
%%

int main() {
    printf("\nEnter Any Arithmetic Expression that includes (*, +, -, /, %): ");
    yyparse();
    if(flag==0)
        printf("\nEntered arithmetic expression was valid one\n");
    return 0;
 
}
void yyerror(const char *s) {
   printf("\nEntered arithmetic expression was Invalid\n");
   flag=1;
}