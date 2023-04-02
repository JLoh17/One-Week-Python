############ My Solution ############
todos = []
completed = []
command = input(f'''{"*"*10}
"Enter a command. Type 'h' for help: ''')

while command != 'q':
    if command == 'h':
        print("*"*10)
        print('To add a todo to the list, type it and hit enter')
        print('To complete a todo enter its number')

    elif command.isnumeric():
        # Identifies and removes list
        idx = int(command) - 1
        if idx >= len(todos):
            print('THERE IS NO TODO WITH THAT NUMBER')
        else:
            done_todo = todos.pop(idx)

            # Adds to completed list
            completed.append(done_todo)

            # Shows todo list
            for i in range(len(todos)):
                print(f'{i+1}) {todos[i]}')

    else:
        todos.append(command)
        for i in range(len(todos)):
            print(f'{i+1}) {todos[i]}')


    command = input(f'''{"*"*10}
"Enter a command. Type 'h' for help: ''')


print(f'Today you completed {len(completed)} todos')
for complete_item in completed:
  print(f'* {complete_item}')


############ Colt's Solution ############
# todos = []
# completed = []
# while True:
#     for i in range(len(todos)):
#         print(f"{i+1}) {todos[i]}")

#     print("***********************************")
#     print("Enter a command. Type 'h' for help:")
#     command = input("> ")
#     if command == "q":
#         break
#     elif command == "h":
#         print("TODO LIST HELP")
#         print("Type 'q' to quit")
#         print("To add a todo to the list, type it and hit enter")
#         print("To complete a todo enter its number")
#     elif command.isnumeric():
#         idx = int(command) - 1
#         if idx >= len(todos):
#             print("THERE IS NO TODO WITH THAT NUMBER!")
#         else:
#             done_todo = todos.pop(idx)
#             completed.append(done_todo)
#     else:
#         todos.append(command)
#     # Print todos from list
# if completed:
#     print(f"You completed {len(completed)} todos today: ")
#     for todo in completed:
#         print(f"* {todo}")
