import PySimpleGUI as sg

layout = [[sg.Text('Example of modal window')],
          [sg.Button('Popup'), sg.Button('Non-Modal Popup')]]

window = sg.Window('Title', layout, relative_location=(0,-120))

while True:
  event, values = window.read()
  if event == sg.WIN_CLOSED:
    break
  
  if event == 'Popup':
    sg.popup('This is a normal, modal popup', 
             'You will not be able to interact with the main window while this popup is open', title='MODAL')
  elif event == 'Non-Modal Popup':
    sg.popup('This is a non-modal popup', 
             'Try mousing over the other window buttons.  They appear active', title='NON-MODAL', modal=False)
window.close()