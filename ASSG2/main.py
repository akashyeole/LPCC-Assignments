# Name: Akash Yeole
# Roll. No.: 321092
# Gr. No.: 22120281
# Batch: A3

from MacroProcessor import MacroProcessor
def main():
    mp = MacroProcessor("input.txt")
    try:
        mp.ProcessMacro()
    except Exception as e:
        print("Error occurred: ", e)

if __name__ == "__main__":
    main()