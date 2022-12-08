from tables import *
import os
from copy import deepcopy

class MacroProcessor:
    RAW_FILE = ""
    CLEAN_FILE = "cleaned.txt"
    INTERMEDIATE_CODE = "output.txt"

    MNT = []
    MDT = []

    def __init__(self, file):
        self.RAW_FILE = file

    def __CleanFile(self):
        read_file = open(self.RAW_FILE, "r")
        write_file = open(self.CLEAN_FILE, "w")
        for line in read_file:
            if(line[0] != "\n" and line[0][0] != ";"):
                write_file.write(line)
        read_file.close()
        write_file.close()

    def __tokenize(self, line):
        tokens = []
        for space_separated_data in line.split():
            tokens.extend(deepcopy([comma_separated_data.strip().upper() for comma_separated_data in space_separated_data.strip().split(',') if comma_separated_data != '']))
        return tokens

    def __test(self):
        target_file = open(self.CLEAN_FILE, "r")
        output_file = open(self.INTERMEDIATE_CODE, "w")

        macro = False
        for line in target_file:
            tokens = self.__tokenize(line)
            if(tokens[0] == "MACRO"):
                macro = True
                self.MNT.append(MACRO(tokens[1], str(len(tokens[2:])), str(len(self.MDT) + 1)))
                ala = [(tokens[i+2], "#{}".format(i+1)) for i in range(len(tokens[2:]))]
                # ala = None
                self.MNT[-1].positional_arg = deepcopy(ala)
                continue
            elif (tokens[0] == "MEND"):
                macro = False
                self.MDT.append(line)
            if(macro):
                self.MDT.append(line)
            elif(tokens[0] != "MEND"):
                output_file.write(line)
        
        target_file.close()
        output_file.close()
    
    def __PrintTables(self):
        print("MNT:")
        for macro in self.MNT:
            print(macro.macro_name, macro.no_of_parameter, macro.starting_index)
        
        print("\nPositional arguements list:")
        for macro in self.MNT: 
            if(macro.no_of_parameter != "0"):
                print("Macro:", macro.macro_name)
                for arg in macro.positional_arg:
                    print("\t",arg)
                print()
        
        print("\nMDT:")
        print(*self.MDT)

    def ProcessMacro(self):
        self.__CleanFile()
        self.__test()
        self.__PrintTables()


        os.remove(self.CLEAN_FILE)
