def encode(plain_text, key, classical=True):
    output = ""
    for c in plain_text.upper():
        num = ord(c)
        if num >= ord("A") and num <= ord("Z"):
            new_num = num + key
            if new_num > ord("Z"):
                new_num = new_num - 26
            if new_num < ord("A"):
                new_num = new_num + 26
            
            output += chr(new_num)
    return output


assert encode("A",1) == "B"
assert encode("a",1) == "B"
assert encode("B", -1) == "A"
assert encode("A", -1) == "Z"
assert encode("Z",1) == "A"

