import os

def add_project(self, widget, data=None):
    pass

def get_projects():
    files = os.listdir("/home/wybe/prog/todo/")
    todos = []
    for entry in files:
        if entry[-5:] != ".todo":
            continue
        todos.append(entry[:-5])
    return todos

def open_project(self, widget):
    todos = []
    todo = []
    start = False
    detail = []
    fp = open(widget+".todo", "r")
    lines = fp.readlines()
    for line in lines:
        if not len(line):
            continue
        line = line.strip("\n")

        if line[0] == "[" and line[-1] == "]":
            if start:
                todo = {
                    "title": title,
                    "detail": detail,
                    }
                todos.append(todo)
                todo = []
            title = line[1:len(line)-1]
            start = True
        else:
            detail.append(line)
    todo = {
        "title": title,
        "detail": detail,
        }
    todos.append(todo)
    return todos
