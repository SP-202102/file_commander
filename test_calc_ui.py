import PySimpleGUI as sg
import random

default_base = '7'
default_lower_boundary = '1'
default_upper_boundary = '12'
default_question = default_base + ' * ' + default_lower_boundary

layout = [
    [sg.Text('Reihe'), sg.InputText(default_base,key='_reihe_', size=(10,20), background_color='yellow'), 
    sg.Text('von:'), sg.InputText(default_lower_boundary,key='_von_', size=(10,30) ),
    sg.Text('bis:'), sg.InputText(default_upper_boundary,key='_bis_', s=(10,80))
    ],
    [sg.Text('Aufgabe:'), sg.Text(default_question, key='_aufgabe_')],
    [sg.Text('Ergebnis:'), sg.InputText(key='_ergebnis_')],
    [sg.Submit(), sg.Cancel()]
]

question = default_question

sg.popup( eval(question) )

window = sg.Window('Reihe üben', layout, finalize=True)

window.Element('_aufgabe_').Update(question)

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
        sg.popup( "Ergebnis SOLL: " + str(eval(question)) + " - Ergebnis IST " + str(values['_ergebnis_'] ) )
        if values['_ergebnis_'] != str(eval(question)):
            window.Element('_ergebnis_').Update(background_color='#880000')
        else:
            # TODO select entered value - maybe that does not work with SimpleUI -> fix that there?
            window.Element('_ergebnis_').Update(background_color='#008800', select=True)
            #window.Element('_ergebnis_').select()
            random.seed()
            question = values['_reihe_'] + ' * ' + str(random.randint(int(values['_von_']), int(values['_bis_'])))
            window.Element('_aufgabe_').Update(question)
    else:
        sg.popup("hallo 2")
