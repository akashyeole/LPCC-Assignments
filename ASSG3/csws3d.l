%{
    #include<iostream>
    #include<bits/stdc++.h>
    using namespace std;
    int state = 0;
    void addToken(int type, string &token);
    int searchToken(string &token);
    vector<set<string>> symbolTable(14);
%}

%%

[" "]+ ;

\n {
    state = 0;
    cout << "\nEnter a token to recognize or add its type in a symbol table: ";
}

^datatype {
    state = 1;
}

^number {
    state = 2;
}

^conditional {
    state = 3;
}

^iterative {
    state = 4;
}

^keyword {
    state = 5;
}

^identifier {
    state = 6;
}

^semicolon {
    state = 7;
}

^(arithmetic[" "]operator) {
    state = 8;
}

^(binary[" "]operator) {
    state = 9;
}

^(logical[" "]operator) {
    state = 10;
}

^(relational[" "]operator) {
    state = 11;
}

^(unary[" "]operator) {
    state = 12;
}

^function {
    state = 13;
}

[\+-\|!&=<>;a-zA-Z0-9]+ {
    string token(yytext);
    if(state) {
        addToken(state, token);
        cout << "\t'" << token << "' added in a symbol table." << endl;
    }
    else {
        switch (searchToken(token)) {
            case 1: cout << "\t'" << token << "' is a DATATYPE." << endl;
                    break;
            case 2: cout << "\t'" << token << "' is a NUMBER." << endl;
                    break;
            case 3: cout << "\t'" << token << "' is a CONDITIONAL." << endl;
                    break;
            case 4: cout << "\t'" << token << "' is an ITERATIVE." << endl;
                    break;
            case 5: cout << "\t'" << token << "' is a KEYWORD." << endl;
                    break;
            case 6: cout << "\t'" << token << "' is an IDENTIFIER." << endl;
                    break;
            case 7: cout << "\t'" << token << "' is a SEMICOLON." << endl;
                    break;
            case 8: cout << "\t'" << token << "' is an ARITHMETIC OPERATOR." << endl;
                    break;
            case 9: cout << "\t'" << token << "' is a BINARY OPERATOR." << endl;
                    break;
            case 10: cout << "\t'" << token << "' is a LOGICAL OPERATOR." << endl;
                    break;
            case 11: cout << "\t'" << token << "' is a RELATIONAL OPERATOR." << endl;
                    break;
            case 12: cout << "\t'" << token << "' is an UNARY OPERTOR." << endl;
                    break;
            case 13: cout << "\t'" << token << "' is a FUNCTION." << endl;
                    break;
            default: cout << "\t'" << token << "': couldn't recognize that token, try to add it in symbol table!" << endl;
                    break;
        }
    }
}

. /**/;

%%

int yywrap(void){}

int main(){
    cout << "Enter a token to recognize or add its type in a symbol table (to add the token type its token type and the token(s) itself[separated by sapce]): ";
    yylex();
    return 0;
}

void addToken(int type, string &token){
    symbolTable[type].insert(token);
    return;
}

int searchToken(string &token){
    for(int i = 1; i < 14; i++){
        if(symbolTable[i].find(token) != symbolTable[i].end()) return i;
    }
    return -1;
}