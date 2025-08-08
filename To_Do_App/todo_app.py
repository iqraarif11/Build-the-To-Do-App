task_list = []

def add_task(title):
    task = {"title":title, "status": "incomplete"}
    task_list.append("task")

def complete_task(index):
    if 0 <= index < len(task_list):
        task_list[index]["status"]="complete"
    else:
        print("invalid Task Index!")

        def view_task():
for i,task in enumerate(task_list):
    print(f"{i}. {task['title']} - {task['status']}")

    add_task("Learn Python")
    add_task("Write Notes")

    view_task()

    complete_task(0)

    view_task()            