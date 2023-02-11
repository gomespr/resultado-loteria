import PySimpleGUI as sg
from resultados import resultado

def make_window():
    sg.theme('blue mono')
    
    layout =  [
                [sg.Text('Qual resultado você gostaria de saber?')],
                [sg.OptionMenu(values=('Mega', 'Quina', 'Dupla Sena', 'Loto Fácil', 'Loto Mania', 'Dia de Sorte', 'Time Mania', 'Federal', 'Super Sete'), default_value='Mega', k='-OPTION MENU-'), sg.Button('Ok')],
                [sg.Multiline(size=(45,5), expand_x=True, expand_y=True, k='-MLINE-')]]
    
    window = sg.Window('Resultados da Loteria', layout, right_click_menu_tearoff=True, grab_anywhere=True, resizable=True, margins=(0,0), use_custom_titlebar=True, finalize=True, keep_on_top=True)
    return window

def main():
    window = make_window()
    
    while True:                            
        event, values = window.read() 
        print(event, values)       
        if event == sg.WIN_CLOSED or event == 'Exit':
            break      
        if event == 'Ok':
            if values['-OPTION MENU-']:
                try:
                    window['-MLINE-'].update(resultado(values['-OPTION MENU-']))
                except:
                    sg.popup('Site fora do ar.')
    window.close()

main()