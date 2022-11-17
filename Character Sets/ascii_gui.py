import PySimpleGUI as sg
# https://www.pysimplegui.org/en/latest/

#sg.theme('GreenTan') # give our window a spiffy set of colors

layout = [
        [
            sg.Text('Text to convert to ASCII'), 
            sg.Input(key="-INPUT-"),
            sg.Button('CONVERT', bind_return_key=True)
        ],
        [sg.Text("", key="-OUTPUT-")],
        #[sg.Output(size=(110, 20), font=('Helvetica 10'))],
        [sg.Button('EXIT')]]

window = sg.Window('ASCII Convertor', layout)

while True:     # The Event Loop
    event, values = window.read()
    if event in (None, 'EXIT'):            # quit if exit button or X
        break
    if event == 'CONVERT':
        output = ""
        #print(values['-INPUT-'])
        for character in values['-INPUT-']:
            print(character, "=" , str(ord(character)))
            output += str(ord(character))+ ", "
        window['-OUTPUT-'].update(output)
        