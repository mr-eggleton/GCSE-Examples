import PySimpleGUI as sg
# python.exe -m pip install pysimplegui
# https://www.pysimplegui.org/en/latest/

#sg.theme('GreenTan') # give our window a spiffy set of colors

layout = [
        [sg.Text("Plain text", tooltip='Text to encrypt'), sg.Input(key="-PLAINTEXT-")],
        [sg.Text("Key"), sg.Input(1, key="-KEY-")],
        [sg.Button('ENCODE')],
        [sg.Text("Cypher text"), sg.Text("", key="-CYPHERTEXT-")],
        [sg.Button('EXIT')]]

window = sg.Window('ASCII Convertor', layout)

ALPHABET_STARTS_AT = ord("a")

def encodeChar(char, key):
    new = chr(((ord(char.lower())-ALPHABET_STARTS_AT)+key % 26) + ALPHABET_STARTS_AT)
    print ("new", new)
    return new

assert encodeChar("a",0) == "a"
assert encodeChar("a",1) == "b"
assert encodeChar("A",0) == "a"
assert encodeChar("A",1) == "b"
assert encodeChar("Z",1) == "a"



while True:     # The Event Loop
    event, values = window.read()
    if event in (None, 'EXIT'):            # quit if exit button or X
        break
    if event == 'ENCODE':
        plaintext = values['-PLAINTEXT-'].lower()
        key = values["-KEY-"]
        output = [encodeChar(c, key) for c in plaintext]
        print(output)
        #print(values['-PLAINTEXT-'])
        #for character in values['-PLAINTEXT-']:
        window['-CYPHERTEXT-'].update(output)
        