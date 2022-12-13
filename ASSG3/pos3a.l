%{

#include<iostream>
#include<bits/stdc++.h>
using namespace std;

%}

%%
[" "|.]+ ;

is |
am |
are |
were |
was |
be |
being |
been |
do |
does |
did |
should |
can |
could |
has |
have |
had |
go |
jump |
run |
fuck |
walk |
want {
    cout << "'" << yytext << "': is a VERB" << endl; 
};

to |
behind |
from |
above |
below | 
between {
    cout << "'" << yytext << "': is a PREPOSITION" << endl;
};

very |
simply |
carefully |
simply |
gently |
quietly |
calmly |
angrily {
    cout << "'" << yytext << "': is an ADVERB" << endl;
};

if |
then |
and |
or |
but {
    cout << "'" << yytext << "': is a CONJUNCTION" << endl;
};

good |
bad |
small |
beautiful |
ugly |
sad |
happy |
big |
large |
cute {
    cout << "'" << yytext << "': is an ADJECTIVE" << endl;
};

i |
you |
he |
she |
his |
her |
it |
its |
my |
their |
your |
we |
they {
    cout << "'" << yytext << "': is a PRONOUN" << endl;
};

[a-zA-Z]+ {
    cout << "'" << yytext << "': Could not recognize that, might be a NOUN" << endl;
};

.|\n { cout << "\nEnter any english sentence: "; };

%%
int yywrap(void){}
int main(){
    cout << "Enter any english sentence: ";
    yylex();
    return 0;
}