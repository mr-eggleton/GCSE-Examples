# ‘Hex’ to ‘Decimal’,
HEXCHARS = "0123456789ABCDEF"

def hexChar2Int(hexChar):
    dec = 0
    if hexChar == "1":
        dec = 1
    elif hexChar == "2":
        dec = 2
        
    elif False:
        for j in range(16):
            if hexChar == HEXCHARS[j]:
                dec = int(j)    
    elif False:
        dec = HEXCHARS.index(hexChar)
    else:
        try:
            dec = int(hexChar)
        except:
            dec = 10 + "ABCDEF".index(hexChar)
    
    return dec

assert hexChar2Int("0") == 0
assert hexChar2Int("1") == 1
assert hexChar2Int("9") == 9
assert hexChar2Int("A") == 10   
assert hexChar2Int("F") == 15

'''
def hex2dec(hex):
    den = 0
    for i in range(len(hex)):
        placeValue = (16 ** (len(hex) - i - 1))
        den = (hexChar2Int(hex[i]) * placeValue) + den

    dec = str(den) 
    
    return dec
'''
def hex2dec(hex):
    den = 0
    placeValue = 1
    lHex = list(hex)
    while len(lHex):
        digit = lHex.pop()
        den = (hexChar2Int(digit) * placeValue) + den
        placeValue *= 16
    return str(den)

assert hex2dec("0") == "0"
assert hex2dec("1") == "1"
assert hex2dec("A") == "10"
assert hex2dec("F") == "15"
assert hex2dec("10") == "16"
assert hex2dec("F0") == "240"
assert hex2dec("FF") == "255"


'''
def dec2bin(number):
    bin = ""
    # The algorithm goes here  
    return bin


def dec2bin(number):
    bin = ""
    # Divide number by 2
    # Add the remainder to the left of current bin string
    # Do it again until the number is 0
    print ("bin", bin)
    return bin


def dec2bin(number):
    bin = ""
    # while number >= 0
        # remainder = number % 2 
        # number = int(number / 2)
        # bin = str(remain)+bin        
        # if number is 0 stop looping
    print ("bin", bin)
    return bin

'''
from operator import xor


def dec2bin(number):
    bin = ""
    while number >= 0:
        remainder = number % 2 
        number = int(number / 2)
        bin = str(remainder)+bin        
        if number == 0:
            break
    #print ("bin", bin)
    return bin
'''
def dec2bin(number):
    bin = ""
    # while number >= 0
        # remainder = number % 2 
        # number = int(number / 2)
        # bin = str(remain)+bin        
        # if number is 0 stop looping
    print ("bin", bin)
    return bin
'''
assert dec2bin(0) == "0"
assert dec2bin(1) == "1"
assert dec2bin(2) == "10"
assert dec2bin(3) == "11"
assert dec2bin(128) == "10000000"


def number2HexDigit(n):
    if n<10:
        return str(n)
    string = "ABCDEF"
    return string[n-10]


assert number2HexDigit(0) == "0"
assert number2HexDigit(1) == "1"
assert number2HexDigit(10) == "A"
assert number2HexDigit(15) == "F"

def dec2hex(number):
    hex = ""
    while number >= 0:
        remainder = number % 16 
        number = int(number / 16)
        hexDigit = number2HexDigit(remainder)
        hex = hexDigit + hex
        if number == 0:
            break# stop looping
    #print ("hex", hex)
    return hex

assert dec2hex(0) == "0"
assert dec2hex(10) == "A"
assert dec2hex(31) == "1F"


def denary2binary(n):
    ret = format(n, '08b')
    #print(n, ret)
    return ret

assert denary2binary(0) == "00000000"
assert denary2binary(1) == "00000001"
assert denary2binary(2) == "00000010"
assert denary2binary(3) == "00000011"
assert denary2binary(128) == "10000000"


def denary2binary(n):
    binary = ""
    current = n
    while current >= 0:
        remain = current % 2
        current = int(current / 2)
        binary = str(remain)+binary
        #print(n, current, remain, binary)
        if(current == 0):
            break
        
    return binary

    '''
    ret = format(n, '08b')
    print(n, ret)
    return ret
    '''
'''
assert denary2hex(0) == "00"
assert denary2hex(1) == "01"
assert denary2hex(2) == "02"
assert denary2hex(10) == "0A"
'''
assert denary2binary(0) == "0"
assert denary2binary(1) == "1"
assert denary2binary(2) == "10"
assert denary2binary(10) == "1010"

assert denary2binary(31) == "11111"
assert denary2binary(128) == "10000000"

'''
def denary2hex(n):    
    ret = format(n, '02X')
    print(n, ret)
    return ret
'''

from math import ceil

bDebug = False

def _binaryAdd(a,b):
    iLength = max(len(a),len(b))
    #iLength = 8 * max(1,ceil(max(len(a),len(b))/ 8))
    
    a = a.rjust(iLength,"0")
    b = b.rjust(iLength,"0")
    if bDebug:
        print("a",a,"b",b)
    C = False
    sSum = ""

    for i in list(range(iLength-1, -1 , -1)):
        A = a[i] == "1"
        B = b[i] == "1"
        if bDebug:
            print("A",A,"B",B,"C",C)
        hS = A ^ B
        hC = A and B
        S = hS ^ C
        C = hC or (C and hS)

        if bDebug:
            print("S",S,"C",C)

        sS = "0"
        if S:
            sS = "1"
        sSum = sS+sSum

    if bDebug:
        print("sSum", sSum)
    return (sSum, C)

def bin2dec(a):
    return str(int(a,2))

assert bin2dec("0") == "0"
assert bin2dec("1") == "1"
assert bin2dec("1001") == "9"
assert bin2dec("1010") == "10"

def dec2hex(a):
    return f'{int(a):X}'

assert dec2hex("0") == "0"
assert dec2hex("1") == "1"
assert dec2hex("9") == "9"
assert dec2hex("10") == "A"
assert dec2hex("17") == "11"


def __binaryAdd(a,b):
    iLength = max(len(a),len(b))
    #iLength = 8 * max(1,ceil(max(len(a),len(b))/ 8))
    
    a = list(a.rjust(iLength,"0"))
    b = list(b.rjust(iLength,"0"))
    if bDebug:
        print("a",a,"b",b)
    C = False
    sSum = ""

    while len(a) or len(b):
    #for i in list(range(iLength-1, -1 , -1)):
        A = B = "0"
        if len(a):
            A = a.pop() == "1"
        if len(b):
            B = b.pop() == "1"
        if bDebug:
            print("A",A,"B",B,"C",C)
        hS = A ^ B
        hC = A and B
        S = hS ^ C
        C = hC or (C and hS)

        if bDebug:
            print("S",S,"C",C)

        sS = "0"
        if S:
            sS = "1"
        sSum = sS+sSum

    if bDebug:
        print("sSum", sSum)
    return (sSum, C)

def ___binaryAdd(a,b):
    #bDebug = True
    iLength = max(len(a),len(b))
    #iLength = 8 * max(1,ceil(max(len(a),len(b))/ 8))
    
    a = a.rjust(iLength,"0")
    b = b.rjust(iLength,"0")
    if bDebug:
        print("a",a,"b",b)
    C = 0
    sSum = ""

    for i in list(range(iLength-1, -1 , -1)):
        A = int(a[i])
        B = int(b[i])
        if bDebug:
            print("A",A,"B",B,"C",C)
        S = A + B + C
        if(S > 1):
            S = S - 2
            C = 1
        else : 
            C = 0

        if bDebug:
            print("S",S,"C",C)

        sSum = str(S)+sSum

    if bDebug:
        print("sSum", sSum)
    return (sSum, C)

def binaryAdd(a,b):
    return ___binaryAdd(a,b)
    iLength = 8 * max(1,ceil(max(len(a),len(b))/ 8))
    
    a1 = list(map(bool, map(int, list(a.rjust(iLength,"0")))))
    b1 = list(map(bool, map(int, list(b.rjust(iLength,"0")))))
    #print("a",a,"b",b,"a1",a1, "b1",b1)
    
    lSum = [False]*iLength
    lCarry = [False]*(iLength + 1)
    C = False
    
    for i in list(range(iLength-1, -1 , -1)):
        A = a1[i]
        B = b1[i]

        #print("A",A,"B",B,"C",C)

        # https://www.electronics-tutorials.ws/wp-content/uploads/2018/05/combination-comb49.gif
        hS = A ^ B
        hC = A and B
        S = hS ^ C
        C = hC or (C and hS)
        
        #print("S",S,"C",C)

        lSum[i] = S
    
    sSum = "".join(list(map(str, map(int, lSum))))
    #print("lSum",lSum,"sSum",sSum, "lCarry",lCarry)
    return (sSum, C)


assert binaryAdd("","")   == ("", False)
assert binaryAdd("0","0") == ("0", False)
assert binaryAdd("1","0") == ("1", False)
assert binaryAdd("0","1") == ("1", False)
assert binaryAdd("1","01") == ("10", False)
assert binaryAdd("1","1") == ("0", True)

'''
assert binaryAdd("","")   == ("00000000", False)
assert binaryAdd("0","0") == ("00000000", False)
assert binaryAdd("1","0") == ("00000001", False)
assert binaryAdd("0","1") == ("00000001", False)
assert binaryAdd("1","1") == ("00000010", False)
'''
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


if __name__ == "__main__":
    binary1 = getBinary("Please input first binary number")
    binary2 = getBinary("Please input second binary number")
    (sSum, C) = binaryAdd(binary1, binary2)

    #print("Result", sSum)
    if C:
        print("There was an overflow error")