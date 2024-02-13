import PySimpleGUI as sg
import functions


label = sg.Text("Type in a to-do")
input_box =  sg.InputText(tooltip = "enter todo", key='todo')
add_button = sg.Button("Add")


# enable events를 통해 누른 리스트박스의 요소를 todo__ key값에 담아 리턴해준다.
list_box = sg.Listbox(values= functions.get_todos(), key = 'todo__' ,
                      enable_events= True,
                      # enable_evnets를 true로 설정하면 listbox 내용 하나하나 클릭할 때 마다 while 문을 돈다.
                      size = [45, 10])
edit_button = sg.Button("Edit")
window = sg.Window("My to DO App",
                   layout= [[label],[input_box, add_button],[list_box, edit_button]],
                   font=('Helvetica', 20))


while True:
    # event는 트리거한 이벤트를 나타내고, values는 창에 있는 모든 입력 요소의 현재값
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todo__'])
    match (event):
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todo__'].update(values= todos)
        case "Edit":
            todo_to_edit = values['todo__'][0]
            new_todo = values["todo"]

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index]= new_todo
            functions.write_todos(todos)
            window['todo__'].update(values= todos)

        case 'todo__':
            window['todo'].update(value= values['todo__'][0])
        case sg.WIN_CLOSED:
            # gui끄면 break
            break

window.close()