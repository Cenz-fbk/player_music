#import_libs
import PySimpleGUI as Py
from PySimpleGUI.PySimpleGUI import WIN_CLOSED
from music import play_music


class execution:
    # set_theme
    Py.theme('black')
    # Desing
    layout = [
        [Py.Text('Sprotify')],
        [Py.Button('Play', size=(144, 0))],

        [Py.Text('Óla por favor espere a música acabar \n para fechar o programa')],
        [Py.Text('Por causa das limitações  da biblioteca \n temos algus bugs')]
    ]
    

    # create_windown
    window = Py.Window('Sprotify-0.1', layout, size=(300, 345))

    # receive_information

    while True:
        events, values = window.read()

        # set_buttons

        if events == WIN_CLOSED:
            break
        try:
            if events == 'Play':
                play_music()

        except:
            exit()
