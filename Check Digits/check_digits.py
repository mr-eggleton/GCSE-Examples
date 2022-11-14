# py -m pip install isbnlib
from isbnlib import meta


def getEANCheckDigit(digits):
    sum = 0
    for i in range(len(digits)):
        num = int(digits[i])
        if i % 2:
            num *= 3
        #print(digits[i],"num", num)
        
        sum += num
    #print ("sum", sum)        
    return str((10 - (sum % 10)) %10)

def isEAN13Valid(barcode):
    lastdigit = barcode[-1]
    digits = barcode[:-1]
    
    checkdigit = getEANCheckDigit(digits)
    
    #print("lastdigit", lastdigit, "digits", digits, "checkdigit", checkdigit)
    return lastdigit == checkdigit
    
    
assert isEAN13Valid("4006381333931")

assert isEAN13Valid("0123455432100")
assert isEAN13Valid("9780345391803")
assert isEAN13Valid("9780345391827")

while True:
    num = input("Input / Scan barcode: ")
    if isEAN13Valid(num):
        print("Barcode", num, "is valid")
        data = meta(num)
        #print(data)
        name = data['Title']
        print(num, " is ", name)
    else:
        print("Barcode invalid")