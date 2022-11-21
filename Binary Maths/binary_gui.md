# Binary GUI Project

Turning your binary maths python into libraries and using them in a GUI.

- It's always good to separate you logic and your interface if you can
- It means you can test the logic on it's own

The GUI will work by :
- Turning 2 numbers into binary from whatever number format we select
- Doing an operation we select
- Converting the result into the selected format

---

## Task 1 : Make your own binary maths libraries

Make your old code only ask for input if you are running that file directly.

This mean the functions are still defined and tested but they wont ask for input as you use the defintion in other files

```python
if __name__ == "__main__":
    binary1 = getBinary("Please input first binary number")
```


---

## Task 2 : Imports

In your `binary_gui.py`. Import your library files instead of `binary_stuff`

```python
import py_compile
import PySimpleGUI as sg
# python.exe -m pip install pysimplegui
# https://www.pysimplegui.org/en/latest/

from binary_stuff import * 

```

---

## Lists we will need
```python

NUMBER_FORMATS = ['Binary', 'Hexadecimal', 'Denary', 'Decimal']
OPERATIONS = ['Number 1 only', 'Number 2 only', 'Binary Addition', 'Left Shift', 'Right Shift']
```

---

## Task 3 : toBinary() 

In your `binary_gui.py`. Make this call your convertors from your binary maths files

```python
def toBinary(num, format):
    print("toBinary", num, format)
    if format=="Binary":
        return num
    if format=="Denary" or format=="Decimal":
        return denary2binary(int(num))
    if format=="Hexadecimal":
        return hex2bin(num)
```
---


## Task 3 : fromBinary() 

In your `binary_gui.py`. Make this call your convertors from your binary maths files. 

The`try:` and `except NameError as err:` work together stop it crashing if you do not have a convertor set up


```python
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
```
---

## The layout

```python
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
```
---

## The event loop

```python
window = sg.Window('ASCII Convertor', layout)

while True:     # The Event Loop
    event, values = window.read()
    if event in (None, 'EXIT'):            # quit if exit button or X
        break
```
---

## Getting the inputs as binary

```python
    binary1 = toBinary(values["-NUM1-"], values["-FORMAT1-"])
    binary2 = toBinary(values["-NUM2-"], values["-FORMAT2-"])
```
---

## Task 4 : Do the Operations

Use your operation names from your library files

```python
    resultBinary = ""
    if values["-OPERATION-"] == 'Number 1 only':
        resultBinary = binary1
    if values["-OPERATION-"] == 'Number 2 only':
        resultBinary = binary2
    if values["-OPERATION-"] == 'Binary Addition':
        (resultBinary, overflowError) = binaryAdd(binary1, binary2)
        if(overflowError):
            print(binary1, "+", binary2, "produced an overflow error.")
```
---

## Display the result

```python

    window["-RESULT-"].update(fromBinary(resultBinary, values["-RESULT_FORMAT-"]))
```

## Tasks

- 1 : Make your own binary maths libraries
  - Make your old code only ask for input if you are running that file directly.
- 2 : Imports
  - In your `binary_gui.py`. Import your library files instead of `binary_stuff`
- 3 : fromBinary() 
  - Make this call your convertors from your binary maths files. 
- 4 : Do the Operations
  - Use your operation names from your library files
