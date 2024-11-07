# todo = []
def write():
    todo = []
    while True:
        i = input()
        todo.append(i)
        if i == '':
            break
    return todo

def create(todo):
    with open("todo.txt",'w') as ToDo:
        for i in range(len(todo)):
            ToDo.write(f"{todo[i]}\n")
    ToDo.close()

def appendTask(Todo):
    todo = open("todo.txt", 'a')
    for i in range(len(Todo)):
        todo.write(f"{Todo[i]}\n")
    todo.close()

def show():
    f = open('todo.txt', 'r')
    contents = f.read()
    print(f"\n{contents}")
    f.close()

def main():
    while True:
        print("\nWelcome To My To-Do List project!")
        print('''1. Create A Task
2. Add New Task to Workspace
3. Display A Task ''')
        i = int(input())
        if i == 1:
            todo = write()
            create(todo)
        elif i == 2:
            newTask = write()
            appendTask(newTask)
        elif i == 3:
            show()
        
        e = input("Enter E to exit: ").lower()
        if e == 'e':
            print("Thank You!")
            break

if __name__ == '__main__':
    main()