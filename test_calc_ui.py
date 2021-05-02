import PySimpleGUI as sg

layout = [
    [sg.Text('Reihe'), sg.InputText('7',key='_reihe_')],
    [sg.Text('Aufgabe:'), sg.Output(size=(20, 1))],
    [sg.Text('Ergebnis:'), sg.InputText(key='_ergebnis_')],
    [sg.Submit(), sg.Cancel()]
]
window = sg.Window('Reihe üben', layout)
while True:                             # The Event Loop
    event, values = window.read()
    # print(event, values) #debug
    if event in (None, 'Exit', 'Cancel'):
        break
    elif event == 'Submit':
        # TODO hier 
        # 0 - Input validation
        # 1 - Prüfen, ob schon eine Aufgabe da war
        # 2 - ggf. das Ergebnis prüfen
        # 3 - richtig/falsch anzeigen (z.B. nur bei falsch ein Popup, oder bei falsch Ergebnis rot machen)
        # 4 - eine neue Aufgabe aktualisieren
