import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a TodoList")
input_box = sg.InputText(tooltip="Enter TodoList")
add_button = sg.Button("Add")
print_button = sg.Button("Print")
window = sg.Window("TodoList", [[label], [input_box,add_button]])
window.read()
window.close()