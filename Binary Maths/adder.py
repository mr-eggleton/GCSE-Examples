def binaryAdd(a,b, iLength=8):    
    a = a.rjust(iLength,"0")
    b = b.rjust(iLength,"0")
    C = 0
    sSum = ""

    for i in list(range(iLength-1, -1 , -1)):
        A = int(a[i])
        B = int(b[i])
        S = A + B + C
        if(S > 1):
            S = S - 2
            C = 1
        else : 
            C = 0

        sSum = str(S)+sSum

    return (sSum, C)

assert binaryAdd("","")   == ("00000000", False)
assert binaryAdd("0","0") == ("00000000", False)
assert binaryAdd("1","0") == ("00000001", False)
assert binaryAdd("0","1") == ("00000001", False)
assert binaryAdd("1","1") == ("00000010", False)

assert binaryAdd("11111111","00000001") == ("00000000", True)
assert binaryAdd("11111111","1") == ("00000000", True)
assert binaryAdd("11111111","10000000") == ("01111111", True)
assert binaryAdd("11111111","11111111") == ("11111110", True)

def getBinary(message):
    value = input (message + " : ")
    if value.replace("0","").replace("1","").strip() != "":
        print("Not a valid binary string.")
        return getBinary(message)
    return value

while True:
    binary1 = getBinary("Please input first binary number")
    binary2 = getBinary("Please input second binary number")
    (sSum, C) = binaryAdd(binary1, binary2)

    print("Result", sSum)
    if C:
        print("There was an overflow error")