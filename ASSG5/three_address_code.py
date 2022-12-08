# from prettytable import PrettyTable
from tabulate import tabulate

def process_expression(data, three_address_code):
    expressions = 0
    token_id_dict = dict()

    for i in range(data.__len__()):
        d = data[i]
        if token_id_dict.__contains__(d):
            data[i] = token_id_dict[d]
        elif d.__len__() > 1 and d[0] == '-':
            n = d[1:]
            three_address_code.append(["-", n, "", f"t{expressions}"])
            data[i] = f"t{expressions}"
            token_id_dict[d] = data[i]
            expressions += 1

    while (1):
        if data.__contains__("*") and data.__contains__("/"):
            multiplicationIndex = data.index("*")
            divisionIndex = data.index("/")
            if multiplicationIndex < divisionIndex:
                d = f"{data[multiplicationIndex]} {data[multiplicationIndex - 1]} {data[multiplicationIndex + 1]}"
                if token_id_dict.__contains__(d):
                    del data[multiplicationIndex - 1: multiplicationIndex + 2]
                    if data.__len__() <= multiplicationIndex - 1:
                        data.append(f"t{expressions}")
                    else:
                        data.insert(multiplicationIndex - 1, data[i])
                else:
                    three_address_code.append([data[multiplicationIndex], data[multiplicationIndex - 1], data[multiplicationIndex + 1], f"t{expressions}"])
                    del data[multiplicationIndex - 1: multiplicationIndex + 2]
                    if data.__len__() <= multiplicationIndex - 1:
                        data.append(f"t{expressions}")
                    else:
                        data.insert(multiplicationIndex - 1, f"t{expressions}")
                    token_id_dict[d] = f"t{expressions}"
                    expressions += 1
            else:
                d = f"{data[divisionIndex]} {data[divisionIndex - 1]} {data[divisionIndex + 1]}"
                if token_id_dict.__contains__(d):
                    del data[divisionIndex - 1: divisionIndex + 2]
                    if data.__len__() <= divisionIndex - 1:
                        data.append(f"t{expressions}")
                    else:
                        data.insert(divisionIndex - 1, data[i])
                else:
                    three_address_code.append([data[divisionIndex], data[divisionIndex - 1], data[divisionIndex + 1], f"t{expressions}"])
                    del data[divisionIndex - 1: divisionIndex + 2]
                    if data.__len__() <= divisionIndex - 1:
                        data.append(f"t{expressions}")
                    else:
                        data.insert(divisionIndex - 1, f"t{expressions}")
                    token_id_dict[d] = f"t{expressions}"
                    expressions += 1

        elif data.__contains__("*"):
            multiplicationIndex = data.index("*")
            d = f"{data[multiplicationIndex]} {data[multiplicationIndex - 1]} {data[multiplicationIndex + 1]}"
            if token_id_dict.__contains__(d):
                del data[multiplicationIndex - 1: multiplicationIndex + 2]
                if data.__len__() <= multiplicationIndex - 1:
                    data.append(f"t{expressions}")
                else:
                    data.insert(multiplicationIndex - 1, data[i])
            else:
                three_address_code.append([data[multiplicationIndex], data[multiplicationIndex - 1], data[multiplicationIndex + 1], f"t{expressions}"])
                del data[multiplicationIndex - 1: multiplicationIndex + 2]
                if data.__len__() <= multiplicationIndex - 1:
                    data.append(f"t{expressions}")
                else:
                    data.insert(multiplicationIndex - 1, f"t{expressions}")
                token_id_dict[d] = f"t{expressions}"
                expressions += 1

        elif data.__contains__("/"):
            divisionIndex = data.index("/")
            d = f"{data[divisionIndex]} {data[divisionIndex - 1]} {data[divisionIndex + 1]}"
            if token_id_dict.__contains__(d):
                del data[divisionIndex - 1: divisionIndex + 2]
                if data.__len__() <= divisionIndex - 1:
                    data.append(f"t{expressions}")
                else:
                    data.insert(divisionIndex - 1, data[i])
            else:
                three_address_code.append([data[divisionIndex], data[divisionIndex - 1], data[divisionIndex + 1], f"t{expressions}"])
                del data[divisionIndex - 1: divisionIndex + 2]
                if data.__len__() <= divisionIndex - 1:
                    data.append(f"t{expressions}")
                else:
                    data.insert(divisionIndex - 1, f"t{expressions}")
                token_id_dict[d] = f"t{expressions}"
                expressions += 1

        elif data.__contains__("+") and data.__contains__("-"):
            additionIndex = data.index("+")
            subtractionIndex = data.index("-")
            if additionIndex < subtractionIndex:
                d = f"{data[additionIndex]} {data[additionIndex - 1]} {data[additionIndex + 1]}"
                if token_id_dict.__contains__(d):
                    del data[additionIndex - 1: additionIndex + 2]
                    if data.__len__() <= additionIndex - 1:
                        data.append(f"t{expressions}")
                    else:
                        data.insert(additionIndex - 1, data[i])
                else:
                    three_address_code.append([data[additionIndex], data[additionIndex - 1], data[additionIndex + 1], f"t{expressions}"])
                    del data[additionIndex - 1: additionIndex + 2]
                    if data.__len__() <= additionIndex - 1:
                        data.append(f"t{expressions}")
                    else:
                        data.insert(additionIndex - 1, f"t{expressions}")
                    token_id_dict[d] = f"t{expressions}"
                    expressions += 1
            else:
                d = f"{data[subtractionIndex]} {data[subtractionIndex - 1]} {data[subtractionIndex + 1]}"
                if token_id_dict.__contains__(d):
                    del data[subtractionIndex - 1: subtractionIndex + 2]
                    if data.__len__() <= subtractionIndex - 1:
                        data.append(f"t{expressions}")
                    else:
                        data.insert(subtractionIndex - 1, data[i])
                else:
                    three_address_code.append([data[subtractionIndex], data[subtractionIndex - 1], data[subtractionIndex + 1], f"t{expressions}"])
                    del data[subtractionIndex - 1: subtractionIndex + 2]
                    if data.__len__() <= subtractionIndex - 1:
                        data.append(f"t{expressions}")
                    else:
                        data.insert(subtractionIndex - 1, f"t{expressions}")
                    token_id_dict[d] = f"t{expressions}"
                    expressions += 1

        elif data.__contains__("+"):
            additionIndex = data.index("+")
            d = f"{data[additionIndex]} {data[additionIndex - 1]} {data[additionIndex + 1]}"
            if token_id_dict.__contains__(d):
                del data[additionIndex - 1: additionIndex + 2]
                if data.__len__() <= additionIndex - 1:
                    data.append(f"t{expressions}")
                else:
                    data.insert(additionIndex - 1, data[i])
            else:
                three_address_code.append([data[additionIndex], data[additionIndex - 1], data[additionIndex + 1], f"t{expressions}"])
                del data[additionIndex - 1: additionIndex + 2]
                if data.__len__() <= additionIndex - 1:
                    data.append(f"t{expressions}")
                else:
                    data.insert(additionIndex - 1, f"t{expressions}")
                token_id_dict[d] = f"t{expressions}"
                expressions += 1

        elif data.__contains__("-"):
            subtractionIndex = data.index("-")
            d = f"{data[subtractionIndex]} {data[subtractionIndex - 1]} {data[subtractionIndex + 1]}"
            if token_id_dict.__contains__(d):
                del data[subtractionIndex - 1: subtractionIndex + 2]
                if data.__len__() <= subtractionIndex - 1:
                    data.append(f"t{expressions}")
                else:
                    data.insert(subtractionIndex - 1, data[i])
            else:
                three_address_code.append([data[subtractionIndex], data[subtractionIndex - 1], data[subtractionIndex + 1], f"t{expressions}"])
                del data[subtractionIndex - 1: subtractionIndex + 2]
                if data.__len__() <= subtractionIndex - 1:
                    data.append(f"t{expressions}")
                else:
                    data.insert(subtractionIndex - 1, f"t{expressions}")
                token_id_dict[d] = f"t{expressions}"
                expressions += 1
        
        else:
            three_address_code.append(["=", data[2], "", data[0]])
            break
    
def main():
    inputfile = open("input.txt", "r")
    outputfile = open("output.txt", "w")
    
    three_address_code = []

    for line in inputfile:
        if len(line.strip()) == 0:
            continue
        data = line.strip().split(' ')
        process_expression(data, three_address_code)

    outputfile.write(tabulate(three_address_code, headers=["Operator", "Operand1", "Operand2", "Output"]))

if __name__ == "__main__":
    main()
