from tables import EMOT_TABLE, SYMBOL, LITERAL, POOL, GetIfEMOT, GetAddressOfSymbol
import os
from copy import deepcopy

class Assembler:

    RAW_FILE = "input.txt"
    CLEAN_FILE = "clean.txt"
    INTERMEDIATE_CODE = "output.txt"

    LC = 0
    SYMBOL_COUNTER = 0
    LITERAL_COUNTER = 0
    LITERALS_IN_CURRENT_POOL = 0

    SYMBOL_TABLE = []
    LITERAL_TABLE = []
    POOL_TABLE = [POOL("1", "1", "")]

    # Constructor: intializes assembler with the file name that is to be assembled.
    def __init__(self, file_name):
        self.RAW_FILE = file_name

    # Cleaning the file; removing the comments and empty lines storing the cleaned program in the new file.
    def __CleanInput(self):
        read_file = open(self.RAW_FILE, "r")
        write_file = open(self.CLEAN_FILE, "w")
        for line in read_file:
            if(line[0] != "\n" and line[0][0] != ";"):
                write_file.write(line)
        read_file.close()
        write_file.close()

    # Converting each line to the tokens, first splitting by white space then by commas, and converting them to upper and stripped format then anf there.
    def __tokenize(self, line):
        tokens = []
        for space_separated_data in line.split():
            tokens.extend(deepcopy([comma_separated_data.strip().upper() for comma_separated_data in space_separated_data.strip().split(',') if comma_separated_data != '']))
        return tokens

    # Analyzes the the token makes the reuired entries in symbol and literal tables.
    def __SymbolAndLiteralAnalyzer(self, output_file, token):
        if(len(token) > 3 and token[:2] == "='" and token[-1] == "'"):
            for literal in self.LITERAL_TABLE[-self.LITERALS_IN_CURRENT_POOL:]:
                if(self.LITERALS_IN_CURRENT_POOL != 0 and literal.name == token):
                    output_file.write("(L, "+ literal.id +") ")
                    break
            else:
                self.LITERAL_COUNTER += 1
                self.LITERALS_IN_CURRENT_POOL += 1
                self.LITERAL_TABLE.append(LITERAL(str(self.LITERAL_COUNTER), token, ""))
                output_file.write("(L, "+ str(self.LITERAL_COUNTER) +") ")
        else:
            for symbol in self.SYMBOL_TABLE:
                if symbol.name == token:
                    output_file.write("(S, "+ symbol.id +") ")
                    break
            else:
                self.SYMBOL_COUNTER += 1
                self.SYMBOL_TABLE.append(SYMBOL(str(self.SYMBOL_COUNTER), token, ""))
                output_file.write("(S, "+ str(self.SYMBOL_COUNTER) +") ")

    # Processes the list of tokens 
    def __ProcessTokens(self, output_file, tokens):
        is_EMOT, mnemonic, classname, opcode = GetIfEMOT(tokens[0])
        
        if(is_EMOT): # If 1st token is present in EMOT
            output_file.write("("+classname+", "+opcode+") ")

            if(classname == "AD"): # Processing Assembler Directives
                # Processing START
                if(mnemonic == "START"):
                    self.LC = int(tokens[1])
                    output_file.write("(C, "+ tokens[1] +") ")
                # Processing ORIGIN
                elif(mnemonic == "ORIGIN"):
                    new_assign_address = 0
                    params = tokens[1].split('+')
                    for param in params:
                        for symbol in self.SYMBOL_TABLE:
                            if(symbol.name == param):
                                new_assign_address += int(symbol.address)
                                break
                        else:
                            new_assign_address += int(param)
                    self.LC = new_assign_address
                # Processing LTORG
                elif(mnemonic == "LTORG"):
                    if(self.LITERALS_IN_CURRENT_POOL != 0):
                        for literal in self.LITERAL_TABLE[-self.LITERALS_IN_CURRENT_POOL:]:
                            literal.address = str(self.LC)
                            self.LC += 1
                        self.POOL_TABLE[-1].length = str(self.LITERALS_IN_CURRENT_POOL)
                        self.POOL_TABLE.append(POOL(str(len(self.POOL_TABLE) + 1), str(len(self.LITERAL_TABLE) + 1), ""))
                        self.LITERALS_IN_CURRENT_POOL = 0
                # Processing END
                elif(mnemonic == "END"):
                    if(self.LITERALS_IN_CURRENT_POOL != 0):
                        for literal in self.LITERAL_TABLE[-self.LITERALS_IN_CURRENT_POOL:]:
                            literal.address = str(self.LC)
                            self.LC += 1
                        self.POOL_TABLE[-1].length = self.LITERALS_IN_CURRENT_POOL
                    else:
                        self.POOL_TABLE = self.POOL_TABLE[:-1]     
            
            elif(classname == "CC"): # Processing Conditional Codes
                pass

            elif(classname == "DL"): # Processing Declarative Statements
                if(mnemonic == "DS"):
                    self.LC += int(tokens[1])
                    output_file.write("(C, "+ tokens[1] +") ")
                else:
                    self.LC += int(tokens[1])
                    output_file.write("(C, 1) ")

            elif(classname == "IS"): # Processing Imperative Statements
                    for token in tokens[1:]:
                        is_EMOT, mnemonic, classname, opcode = GetIfEMOT(token)
                        if(is_EMOT):
                            output_file.write("("+classname+", "+ opcode +") ")
                        else:
                            self.__SymbolAndLiteralAnalyzer(output_file, token)

                    self.LC += 1

        else: # If 1st token is Symbol and not EMOT
            for symbol in self.SYMBOL_TABLE:
                if symbol.name == tokens[0]:
                    if(tokens[1] == "EQU"):
                        symbol.address, id = GetAddressOfSymbol(tokens[2], self.SYMBOL_TABLE)
                        output_file.write("(AD, 04) (S, "+ id +") ")
                        return
                    symbol.address = str(self.LC)
                    break
            else:
                if(tokens[1] == "EQU"):
                        address, id = GetAddressOfSymbol(tokens[2], self.SYMBOL_TABLE)
                        self.SYMBOL_COUNTER += 1
                        self.SYMBOL_TABLE.append(SYMBOL(str(self.SYMBOL_COUNTER), tokens[0], address))
                        output_file.write("(AD, 04) (S, "+ id +") ")
                        return
                self.SYMBOL_COUNTER += 1
                self.SYMBOL_TABLE.append(SYMBOL(str(self.SYMBOL_COUNTER), tokens[0], str(self.LC)))
            self.__ProcessTokens(output_file, tokens[1:])

    # Process the input cleaned input file line-by-line
    def __ProcessInput(self):
        target_file = open(self.CLEAN_FILE, "r")
        output_file = open(self.INTERMEDIATE_CODE, "w" )

        for line in target_file:
            tokens = self.__tokenize(line.strip())
            self.__ProcessTokens(output_file, tokens)
            output_file.write("\n")
        
        target_file.close()
        output_file.close()
    
    # Printing the tables finnaly on the console
    def __PrintTables(self):
        print("SYMBOL TABLE:")
        for symbol in self.SYMBOL_TABLE:
            print(symbol.id, symbol.name, symbol.address)
        
        print("\nLITERAL TABLE:")
        for literal in self.LITERAL_TABLE:
            print(literal.id, literal.name, literal.address)

        print("\nPOOL TABLE:")
        for pool in self.POOL_TABLE:
            print(pool.id, pool.pool, pool.length)

    def assemble(self):
        self.__CleanInput()
        self.__ProcessInput()
        self.__PrintTables()
        os.remove(self.CLEAN_FILE)
