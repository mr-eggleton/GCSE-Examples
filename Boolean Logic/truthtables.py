import re
import string


inputs = "AB"
cols = len(inputs)

logic = "A and B"

def getInputs(sLogic):
    chunks = re.split(r"(\W)", sLogic)
    #print(chunks)
    lInputs = []
    for chunk in chunks:
        #print(chunk, string.ascii_uppercase)
        if (chunk.strip() != "" and chunk in string.ascii_uppercase):
            lInputs.append(chunk)
    #print("lInputs", lInputs)
    return lInputs

assert getInputs("A AND B") == ["A", "B"]
assert getInputs("A OR (B)") == ["A", "B"]
assert getInputs("not(A and (B))") == ["A", "B"]
assert getInputs("not A") == ["A"]

def getTruthTableRows(sLogic):
    lInputs = getInputs(sLogic)
    lRows = []
    for i in range(2 ** len(lInputs)):
        sBinary = "{0:b}".format(i).zfill(len(lInputs))
        dValues = dict(zip(list(inputs),list(sBinary)))
        #print("dValues", dValues)
        lRows.append(dValues)
    #print("lRows", lRows)
    return lRows
    

assert getTruthTableRows("A AND B") == [{'A': '0', 'B': '0'}, {'A': '0', 'B': '1'}, {'A': '1', 'B': '0'},{'A': '1', 'B': '1'}]
assert getTruthTableRows("A OR (B)") == [{'A': '0', 'B': '0'}, {'A': '0', 'B': '1'}, {'A': '1', 'B': '0'},{'A': '1', 'B': '1'}]
assert getTruthTableRows("not(A and (B))") == [{'A': '0', 'B': '0'}, {'A': '0', 'B': '1'}, {'A': '1', 'B': '0'},{'A': '1', 'B': '1'}]
assert getTruthTableRows("not A") == [{'A': '0'}, {'A': '1'}]

def getRowString(sLogic, dRow):
    chunks = re.split(r"(\W)", sLogic)
    #print(chunks)
    for i in range(len(chunks)):
        if chunks[i] in dRow:
            chunks[i] = dRow[chunks[i]]
        else:
            chunks[i] = chunks[i].lower()
    sRow = "".join(chunks)
    #print("sRow", sRow)
    return sRow

assert getRowString("A AND B",{'A': '0', 'B': '1'}) == "0 and 1"
assert getRowString("A OR (B)",{'A': '0', 'B': '1'}) == "0 or (1)"
assert getRowString("not(A and (B))", {'A': '0', 'B': '1'}) == "not(0 and (1))"
assert getRowString("not A", {'A': '1'}) == "not 1"


def getLogicString(sLogic):
    chunks = re.split(r"(\W)", sLogic)
    lInputs = getInputs(sLogic)
    #print(chunks)
    for i in range(len(chunks)):
        if chunks[i] in lInputs:
            chunks[i] = chunks[i]
        else:
            chunks[i] = chunks[i].lower()
    sRow = "".join(chunks)
    #print("sRow", sRow)
    return sRow

assert getLogicString("A AND B") == "A and B"
assert getLogicString("A OR (B)") == "A or (B)"
assert getLogicString("not(A and (B))") == "not(A and (B))"
assert getLogicString("not A") == "not A"


def getTruthTable(sLogic):
    lInputs = getInputs(sLogic)
    lRows = getTruthTableRows(sLogic)
    sLogic = getLogicString(sLogic)
    lTable = []
    for i in range(len(lRows)):
        newRow = lRows[i]
        print("(sLogic, lRows[i]", sLogic, lRows[i])
        #newRow["out"] = eval(sLogic, lRows[i])
        print ("newRow", newRow)
        lTable.append(newRow)
    print("lTable", lTable)
    return lTable

assert getTruthTable("A AND B") == [{'A': '0', 'B': '0', 'out':'0'}, {'A': '0', 'B': '1', 'out':'0'}, {'A': '1', 'B': '0', 'out':'0'},{'A': '1', 'B': '1', 'out':'1'}]
assert getTruthTable("A OR (B)") == [{'A': '0', 'B': '0', 'out':'0'}, {'A': '0', 'B': '1', 'out':'1'}, {'A': '1', 'B': '0', 'out':'1'},{'A': '1', 'B': '1', 'out':'1'}]
assert getTruthTable("not(A and (B))") == [{'A': '0', 'B': '0', 'out':'1'}, {'A': '0', 'B': '1', 'out':'1'}, {'A': '1', 'B': '0', 'out':'1'},{'A': '1', 'B': '1', 'out':'1'}]
assert getTruthTable("not A") == [{'A': '0', 'out':'1'}, {'A': '1', 'out':'0'}]

        #thisLogic = logic.replace("A", str(test["A"]))

        #chunks = re.split(r"\W", logic) 
        
        #print("thisLogic", thisLogic, "chunks", chunks)
