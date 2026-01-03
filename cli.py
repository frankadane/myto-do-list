
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")

while True:
    user_action = input("Type add or new or more follow by todo, edit,complete, show or exit: ")
    user_action.strip()


    if user_action.startswith('add') or user_action.startswith('new') or user_action.startswith('more'):
        todo = user_action[4:] + '\n'
        todos = functions.get_todos()
        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()

        new_todos = [item.strip("\n") for item in todos]

        for idx,item in enumerate(new_todos):
            row = f"{idx + 1}-{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1
            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos( todos)

        except ValueError:
            print("Invalid input. Edit must be followed by a number.")
            continue
        except IndexError:
            print("Invalid input. Number out of range.")
            continue
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[8:])
            todos = functions.get_todos()
            index = number-1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(number-1)

            functions.write_todos( todos)

            message = f"Todo '{todo_to_remove}' has been completed and removed from todos."
            print(message)
        except ValueError:
            print("Invalid input. Complete must be followed by a number.")
            continue
        except IndexError:
            print("Invalid input. Number out of range.")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Invalid command. Type 'add', 'edit', 'complete' or 'show'")

print("Bye!")

