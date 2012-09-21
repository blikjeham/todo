import os

def add_project(self, widget, data=None):
    pass

def get_projects():
    files = os.listdir("/home/wybe/.todo/")
    todos = []
    for entry in files:
        if entry[-5:] != ".todo":
            continue
        todos.append(entry[:-5])
    return todos
