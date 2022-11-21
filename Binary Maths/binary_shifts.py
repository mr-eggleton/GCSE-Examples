

def rightShift(binary, shiftbits=1):
    iLength = len(binary)
    binary = binary[0:(iLength - shiftbits)]
    binary = binary.rjust(iLength,"0")
    return binary


assert rightShift("00110011", 0) == "00110011"
assert rightShift("00110011", 1) == "00011001"
assert rightShift("00110011", 2) == "00001100"


def leftShift(binary, shiftbits=1):
    iLength = len(binary)
    binary = binary[shiftbits:iLength ]
    binary = binary.ljust(iLength,"0")
    
    return binary

assert leftShift("00110011", 0) == "00110011"
assert leftShift("00110011", 1) == "01100110"
assert leftShift("00110011", 2) == "11001100"


#ret = format(n, '08b')
#print(n, ret)