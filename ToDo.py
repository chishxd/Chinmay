# todo = [access tasks via dates]
def write():
    todo = {}
    task = []
    date = input("Enter The Date:\n")
    while True:
        print("\nEnter The Tasks: ")
        i = input()
        task.append(i)
        if i == '':
            break
    todo[date] = task
    return todo

def create(todo,m):
    if m == 'a':
        with open("todo.txt",'a') as ToDo:
            for i in todo:
                ToDo.write(f"{i}\n")
                for j in range(len(todo[i])):
                    ToDo.write(f"   {todo[i][j]}\n")
            ToDo.close()
    elif m == 'w':
        with open("todo.txt",'w') as ToDo:
            for i in todo:
                ToDo.write(f"{i}\n")
                for j in range(len(todo[i])):
                    ToDo.write(f"   {todo[i][j]}\n")
            ToDo.close()


def show():
    f = open('todo.txt', 'r')
    contents = f.read()
    print(f"\n{contents}")
    f.close()

def main():
    while True:
        print("\nWelcome To My To-Do List project!")
        i = input('''1. Create A New Workspace
2. Add to current workspace
3. Display A Task\n''')
        if i in ('1','a'):
            todo = write()
            create(todo,'w')
        elif i in ('2','b'):
            todo = write()
            create(todo,'a')
        elif i in ('3','c'):
            show()
        
        e = input("Enter E to exit: ").lower()
        if e == 'e':
            print("Thank You!")
            break

if __name__ == '__main__':
    main()
