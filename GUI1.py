import PySimpleGUI as sg
from PIL import Image

def new_layout(i):
    return [[sg.T("Divisão: "), sg.InputText(key=("-q-", i))]]

PLUS_ICO = Image.open("plus.png")


column_layout = [
    [sg.T("Divisão: "), sg.InputText(key=("-q-", 0)),
    sg.Button(enable_events=True, image_data=PLUS_ICO, key="-plus-")]
]

layout = [
    [sg.Column(column_layout, key='-Column-')],
    [sg.Submit(button_text="Update/Insert"), sg.Cancel(button_text="Cancel")],
]

window = sg.Window("Adicionar organizadores", layout)
i = 1
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit', 'Cancel'):
        break
    elif event == '-plus-':
        if i<5:
            window.extend_layout(window['-Column-'], new_layout(i))
            i += 1
    print(event, values)

event, values = window.read()
window.close()
