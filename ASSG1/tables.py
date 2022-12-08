# Class EMOT: A structure to store mnemonic, classname and opcode of an EMOT entry.
class EMOT:
    mnemonic = ""
    classname = ""
    opcode = ""
    def __init__(self, mnemonic, classname, opcode):
        self.mnemonic = mnemonic
        self.classname = classname
        self.opcode = opcode

# Tuple which has every emot entry hardcoded in it.
EMOT_TABLE = (
    EMOT("STOP", "IS", "00"),
    EMOT("ADD", "IS", "01"),
    EMOT("SUB", "IS", "02"),
    EMOT("MULT", "IS", "03"),
    EMOT("MOVER", "IS", "04"),
    EMOT("MOVEM", "IS", "05"),
    EMOT("COMP", "IS", "06"),
    EMOT("BC", "IS", "07"),
    EMOT("DIV", "IS", "08"),
    EMOT("READ", "IS", "09"),
    EMOT("PRINT", "IS", "10"),
    EMOT("LOAD", "IS", "11"),
    EMOT("START", "AD", "01"),
    EMOT("END", "AD", "02"),
    EMOT("ORIGIN", "AD", "03"),
    EMOT("EQU", "AD", "04"),
    EMOT("LTORG", "AD", "05"),
    EMOT("DS", "DL", "01"),
    EMOT("DC", "DL", "02"),
    EMOT("AREG", "RG", "01"),
    EMOT("BREG", "RG", "02"),
    EMOT("CREG", "RG", "03"),
    EMOT("DREG", "RG", "04"),
    EMOT("EQ", "CC", "01"),
    EMOT("LT", "CC", "02"),
    EMOT("GT", "CC", "03"),
    EMOT("LE", "CC", "04"),
    EMOT("GE", "CC", "05"),
    EMOT("ANY", "CC", "06"),
)

# Class SYMBOL: A structure to store an indvidual symbol table entry
class SYMBOL:
    id = ""
    name = ""
    address = ""
    
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address

# Class LITERAL: A structure to store an indvidual literal table entry
class LITERAL:
    id = ""
    name = ""
    address = ""
    
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address

# POOL: TO store the pool record.
class POOL:
    id = ""
    pool = ""
    address = ""
    
    def __init__(self, id, pool, length):
        self.id = id
        self.pool = pool
        self.length = length
    
# Function which searches for specific token in an EMOT table and returns its details if found.
def GetIfEMOT(token):
    for emot in EMOT_TABLE:
        if emot.mnemonic == token:
            return [True, emot.mnemonic, emot.classname, emot.opcode]
    return [False, "", "", ""]

# Return an address and id of a symbol in an symbol table
def GetAddressOfSymbol(token, SYMBOL_TABLE):
    for symbol in SYMBOL_TABLE:
        if(symbol.name == token):
            return [symbol.address, symbol.id]