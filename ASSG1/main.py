# Name: Akash Yeole
# Roll. No.: 321092
# Gr. No.: 22120281
# Batch: A3

from Assembler import Assembler

def main():
    assembler = Assembler("ASSG1/input3.txt")
    try:
        assembler.assemble()
    except Exception as e:
        print("Exception: ", e)

# Execution of the program starts from here
if __name__ == "__main__":
    main()