import PySimpleGUI as sg
# python.exe -m pip install pysimplegui
# https://www.pysimplegui.org/en/latest/
FIRST = ord("A")

#sg.theme('GreenTan') # give our window a spiffy set of colors

debug = False
        
def charAtPos(string="", pos=0, char=" "):
    temp = list(string)
    try:
        temp[pos] = char
    except :
        pass
    return "".join(temp)

def charAtPos1(string="", pos=0, char=" "):
    return string[:pos]+char+string[pos+1:]

assert charAtPos() == ""
assert charAtPos("A") == " "
assert charAtPos("AAAAAA", 1)  == "A AAAA"
assert charAtPos("AAAAAA", -1) == "AAAAA "
assert charAtPos("AAAAAA", -1, "Z") == "AAAAAZ"

def encode(plain_text, key, classical=True):
    return encodeV1(plain_text, key, classical)

def encodeV1(plain_text, key, classical=True):
    output = ""
    for c in plain_text.upper():
        new_c = c
        num = ord(c)
        if num >= ord("A") and num <= ord("Z"):
            new_num = num + key
            if new_num > ord("Z"):
                new_num = new_num - 26
            if new_num < ord("A"):
                new_num = new_num + 26
            new_c = chr(new_num)
        elif classical:
            new_c = ""
        output += new_c
    if debug :
        print("encodeV1 plain_text", plain_text, "output", output)
    return output

def encodeV2(plain_text, key, classical=True):
    output = ""
    for c in plain_text.upper():
        num = ord(c)-FIRST
        new_c = c
        if num>=0 and num < 26:
            new_num = ((num + key) % 26) + FIRST
            new_c = chr(new_num)
        elif classical:
            new_c = ""
        output += new_c
    if debug :
        print("encodeV2 plain_text", plain_text, "output", output)
    return output

    
def encodeV3(plain_text, key, classical=True):
    return "".join([chr(FIRST +(((ord(c)-FIRST)+key)%26)) if ord(c)>=FIRST and ord(c) < FIRST+26 else ("" if classical else c) for c in list(plain_text.upper())])

assert encode("A",1) == "B"
assert encode("a",1) == "B"
assert encode("B", -1) == "A"
assert encode("Z",1) == "A"
assert encode("A", -1) == "Z"

assert encode("A A",1) == "BB"
assert encode("A,A",1) == "BB"
assert encode("A A",1, False) == "B B"
assert encode("A,A",1, False) == "B,B"



start_text = "Veni, vidi, vici"
start_key = 1
start_classical = True
start_output =  encode(start_text, start_key, start_classical)

layout = [
            [sg.Text('Text to Caesar Cypher', size=20), sg.Input(start_text, key="-INPUT-",enable_events=True)],
            [
                sg.Text('Caesar Key', size=20), sg.Spin(key="-KEY-", values=list(range(-25,25)), initial_value=start_key, enable_events=True),
                sg.Checkbox('Classical Mode', default=True, key='-CLASSICAL-', enable_events=start_classical)
            ],
            [sg.Button('ENCODE', bind_return_key=True), sg.Button('EXIT')],
            [sg.Button("LOAD"), sg.Button("SAVE")],
            [sg.Text("Encoded Text:"), sg.Text(start_output, size=(110, 1), key="-OUTPUT-")]
        ]
window = sg.Window('Caesar Cypher', layout)


while True:     # The Event Loop
    event, values = window.read()
    if event in (None, 'EXIT'):            # quit if exit button or X
        break
    if event == "LOAD":
        filename = sg.popup_get_file('Please enter a file name')
        with open(filename) as file:
            text = file.read()
            window['-INPUT-'].update(text)
    if event == "SAVE":
        filename = sg.popup_get_file('Please enter a file name', default_extension = ".txt", save_as = True)
        with open(filename, 'w') as file:
            file.write(encode(values['-INPUT-'], values['-KEY-'],values['-CLASSICAL-']))
    #if event == 'CONVERT':)

    window['-OUTPUT-'].update(encode(values['-INPUT-'], values['-KEY-'],values['-CLASSICAL-']))
        