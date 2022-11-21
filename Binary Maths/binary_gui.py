import py_compile
import PySimpleGUI as sg
# python.exe -m pip install pysimplegui
# https://www.pysimplegui.org/en/latest/

from binary_stuff import * 

#sg.theme('GreenTan') # give our window a spiffy set of colors

NUMBER_FORMATS = ['Binary', 'Hexadecimal', 'Denary', 'Decimal']
OPERATIONS = ['Number 1 only', 'Number 2 only', 'Binary Addition', 'Left Shift', 'Right Shift']

def toBinary(num, format):
    print("toBinary", num, format)
    if format=="Binary":
        return num
    if format=="Denary" or format=="Decimal":
        return denary2binary(int(num))
        return denary2binary(int(num))
    if format=="Hexadecimal":
        return hex2bin(num)

def fromBinary(num, format):
    print("fromBinary", num, format)
    try :
        if format=="Binary":
            return num
        if format=="Denary" or format=="Decimal":
            return bin2dec(num)
        if format=="Hexadecimal":
            return bin2hex(num)
    except NameError as err:
        print("function or variable with ", err)


layout = [
        [   
            sg.T('No. 1'), sg.I(0, key="-NUM1-"), sg.T('as'),
            sg.Drop(NUMBER_FORMATS, key="-FORMAT1-", default_value="Binary"),
        ],
        [
            sg.T('No. 2'), sg.Input(0, key="-NUM2-"), sg.T('as'),
            sg.Drop(NUMBER_FORMATS, key="-FORMAT2-", default_value="Binary"),
        ],
        [
            sg.T('Operation'), 
            sg.Drop(OPERATIONS, key="-OPERATION-", default_value=OPERATIONS[0]),
            sg.T('as'),
            sg.Drop(NUMBER_FORMATS, key="-RESULT_FORMAT-", default_value="Binary"),
        ],
        [sg.B('GO', bind_return_key=True)],
        [
            sg.T("Result"),
            sg.T("", key="-RESULT-"),

        ],
        [sg.Output(size=(110, 5), font=('Helvetica 10'))],
        [sg.Exit()]
    ]

window = sg.Window('ASCII Convertor', layout)

while True:     # The Event Loop
    event, values = window.read()
    if event in (None, 'EXIT'):            # quit if exit button or X
        break
    
    binary1 = toBinary(values["-NUM1-"], values["-FORMAT1-"])
    binary2 = toBinary(values["-NUM2-"], values["-FORMAT2-"])
    
    resultBinary = ""
    if values["-OPERATION-"] == 'Number 1 only':
        resultBinary = binary1
    if values["-OPERATION-"] == 'Number 2 only':
        resultBinary = binary2
    if values["-OPERATION-"] == 'Binary Addition':
        (resultBinary, overflowError) = binaryAdd(binary1, binary2)
        if(overflowError):
            print(binary1, "+", binary2, "produced an overflow error.")
    
    window["-RESULT-"].update(fromBinary(resultBinary, values["-RESULT_FORMAT-"]))