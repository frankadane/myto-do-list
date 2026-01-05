import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a TodoList")
input_box = sg.InputText(tooltip="Enter TodoList",
                         key="todo")
add_button = sg.Button("Add")
print_button = sg.Button("Print")
window = sg.Window("TodoList", [[label],
                                [input_box,add_button]],
                   font=("Helvetica", 12))

while True:
    event, values = window.read()
    print(f"Event: {event} ,Values: {values}" )
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()