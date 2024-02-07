import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box =  sg.InputText(tooltip = "enter todo")
add_button = sg.Button("Add")

window = sg.Window("My to DO App", layout= [[label],[input_box, add_button]])
window.read()
window.close()