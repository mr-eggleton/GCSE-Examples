import re
import string

'''
Gets the list of inputs used in a logical expression
They are the uppercase letters used on their own
'''
def getInputs(sLogic):
    chunks = re.split(r"(\W)", sLogic) #split on all the gaps bewteen words
    #print("chunks", chunks)
    lInputs = []
    for chunk in chunks:
        if (chunk.strip() and chunk in string.ascii_uppercase):
            lInputs.append(chunk)
    #print("lInputs", lInputs)
    return lInputs

assert getInputs("A AND B") == ["A", "B"]
assert getInputs("A OR (B)") == ["A", "B"]
assert getInputs("not(A and (B))") == ["A", "B"]
assert getInputs("not A") == ["A"]
assert getInputs("A xor B") == ["A", "B"]

def getTruthTableRows(sLogic):
    lInputs = getInputs(sLogic)
    lRows = [] # new empty list
    for i in range(2 ** len(lInputs)):
        sBinary = "{0:b}".format(i).zfill(len(lInputs)) #get a binary string that has enough columns
        dValues = dict(zip(lInputs,map(int,list(sBinary)))) #join the input names and the binary numbers into a dictionary
        #print("dValues", dValues)
        lRows.append(dValues) # add the dictionary to the list
    #print("lRows", lRows)
    return lRows 

assert getTruthTableRows("A AND B") == [{'A': 0, 'B': 0}, {'A': 0, 'B': 1}, {'A': 1, 'B': 0},{'A': 1, 'B': 1}]
assert getTruthTableRows("A OR (B)") == [{'A': 0, 'B': 0}, {'A': 0, 'B': 1}, {'A': 1, 'B': 0},{'A': 1, 'B': 1}]
assert getTruthTableRows("not(A and (B))") == [{'A': 0, 'B': 0}, {'A': 0, 'B': 1}, {'A': 1, 'B': 0},{'A': 1, 'B': 1}]
assert getTruthTableRows("not A") == [{'A': 0}, {'A': 1}]
assert getTruthTableRows("A xor B") == [{'A': 0, 'B': 0}, {'A': 0, 'B': 1}, {'A': 1, 'B': 0},{'A': 1, 'B': 1}]

def getLogicString(sLogic):
    chunks = re.split(r"(\W)", sLogic)
    lInputs = getInputs(sLogic)
    #print(chunks)
    for i in range(len(chunks)):
        if chunks[i] in lInputs:
            chunks[i] = chunks[i]
        elif chunks[i] == "xor":
            chunks[i] = "!="
        else:
            chunks[i] = chunks[i].lower() #all the logic commands are lowercase

    sRow = "".join(chunks)
    #print("sRow", sRow)
    return sRow

assert getLogicString("A AND B") == "A and B"
assert getLogicString("A OR (B)") == "A or (B)"
assert getLogicString("not(A and (B))") == "not(A and (B))"
assert getLogicString("not A") == "not A"
#assert getLogicString("A xor B") == "A != B"

def getTruthTable(sLogic):
    lInputs = getInputs(sLogic)
    lRows = getTruthTableRows(sLogic)
    sLogic = getLogicString(sLogic)
    lTable = []
    for i in range(len(lRows)):
        newRow = lRows[i]
        data = dict(lRows[i])
        data['__builtins__']= {}
        newRow["out"] = int(eval(sLogic, data))
        lTable.append(newRow)
    return lTable

assert getTruthTable("A AND B") == [{'A': 0, 'B': 0, 'out':0}, {'A': 0, 'B': 1, 'out':0}, {'A': 1, 'B': 0, 'out':0},{'A': 1, 'B': 1, 'out':1}]
assert getTruthTable("A OR (B)") == [{'A': 0, 'B': 0, 'out':0}, {'A': 0, 'B': 1, 'out':1}, {'A': 1, 'B': 0, 'out':1},{'A': 1, 'B': 1, 'out':1}]
assert getTruthTable("not(A and (B))") == [{'A': 0, 'B': 0, 'out':1}, {'A': 0, 'B': 1, 'out':1}, {'A': 1, 'B': 0, 'out':1},{'A': 1, 'B': 1, 'out':0}]
assert getTruthTable("not A") == [{'A': 0, 'out':1}, {'A': 1, 'out':0}]
#assert getTruthTable("A xor B") == [{'A': 0, 'B': 0, 'out':0}, {'A': 0, 'B': 1, 'out':1}, {'A': 1, 'B': 0, 'out':1},{'A': 1, 'B': 1, 'out':0}]

def printTruthTable(sLogic):
    print(sLogic, ":")
    data = getTruthTable(sLogic)
    header = list(data[0].keys())
    print("\t".join(header))
    for line in data:
        print("\t".join(map(str, line.values())))
    print()

#Standard Ones
printTruthTable("A AND B")
printTruthTable("A OR B")
printTruthTable("NOT A")

#printTruthTable("A XOR B")

printTruthTable("not(A and (B)) or C")
printTruthTable("not A")