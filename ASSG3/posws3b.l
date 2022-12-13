%{
    #include<iostream>
    #include<bits/stdc++.h>
    using namespace std;
    int state = 0;
    void addWord(int type, string &word);
    int searchWord(string &word);
    vector<set<string>> symbolTable(8);
%}

%%
[" "]+ ;

\n {
    state = 0;
    cout << "\nEnter a word to recognize or add it as a part of speech in a symbol table: ";
}

^verb {state = 1;}
^adjective {state = 2;}
^adverb {state = 3;}
^noun {state = 4;}
^preposition {state = 5;}
^pronoun {state = 6;}
^conjunction {state = 7;}

[a-zA-Z]+ {
    string word(yytext);
    if(state) {
        addWord(state, word);
        cout << "\t'" << word << "' added in a symbol table.\n";
    }
    else {
        switch(searchWord(word)) {
            case 1: cout << "\t'" << word << "' is a VERB." << endl;
                    break;
            case 2: cout << "\t'" << word << "' is a ADJECTIVE." << endl;
                    break;
            case 3: cout << "\t'" << word << "' is a ADVERB." << endl;
                    break;
            case 4: cout << "\t'" << word << "' is a NOUN." << endl;
                    break;
            case 5: cout << "\t'" << word << "' is a PREPOSITION." << endl;
                    break;
            case 6: cout << "\t'" << word << "' is a PRONOUN." << endl;
                    break;
            case 7: cout << "\t'" << word << "' is a CONJUNCTION." << endl;
                    break;
            default: cout << "\t'" << word <<"': Coudn't recognize that word! Please try to addd it in a symbol table(so called)." << endl;
                    break;
        }
    }
}

. ;
%%

int yywrap(void){}

int main(){
    cout << "Enter a word to recognize or add it as a part of speech in a symbol table (to add the words type its part of speech name and the word(s) itself[separated by sapce]): ";
    yylex();
    return 0;
}

void addWord(int type, string &word){
    symbolTable[type].insert(word);
    return;
}

int searchWord(string &word){
    for(int i = 0; i < 8; i++){
        if(symbolTable[i].find(word) != symbolTable[i].end()){
            return i;
        }
    }
    return -1;
}