import PySimpleGUI as sg      
import searcher

def main():


    sg.theme('DarkAmber')    # Keep things interesting for your users

    layout = [[sg.Text('Welcome to wikipedia downloader!')],      
            [sg.Text('Search:', size=(15, 1)), sg.InputText()],      
            [sg.Submit(), sg.Cancel()],
            [sg.Output(size=(50,10), key='-Output-')]]      

    window = sg.Window('Wikipedia downloader', layout)      

    while True:                             # The Event Loop
        event, values = window.read() 
        print(event, values)       
        if event == sg.WIN_CLOSED or event == 'Exit':
            break      

    window.close()

if __name__ == "__main__":
    main()