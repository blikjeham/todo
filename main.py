#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
import todos
from projects import *

def addprojects():
    box = gtk.VBox(False, 0)
    button = gtk.Button("New project")
    box.pack_start(button, False, False, 0)
    button.connect("clicked", add_project, None)
    button.show()
    projects = get_projects()
    for project in projects:
        button = gtk.Button(project)
        box.pack_start(button, False, False, 0)
        button.show()
    return box

def addlist():
    box = gtk.VBox(False, 0)
    label = gtk.Label("Current ToDo")
    label.set_alignment(0, 0)
    box.pack_start(label)
    label.show()
    todolist = todos.gettodos(1)
    for todo in todolist:
        button = gtk.Button(todo["title"])
        box.pack_start(button, False, False, 1)
        button.show()
        text = gtk.TextView()
        buffer = text.get_buffer()
        buffer.set_text(todo["details"])
        box.pack_start(text, True, True, 1)
        text.show()
    return box

class ToDoWindow:

    def delete_event(self, wigdet, event, data=None):
        return False

    def destroy(self, wigdet, data=None):
        gtk.main_quit()

    def __init__(self):
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_title("ToDoS")
        window.connect("delete_event", self.delete_event)
        window.connect("destroy", self.destroy)

        box = gtk.HBox(False, 0)
        projpane = addprojects()
        box.pack_start(projpane, False, True, 0)
        projpane.show()

        list = addlist()
        box.pack_start(list, True, True, 0)
        list.show()
        
        window.add(box)
        box.show()
        window.show()
        
    def main(self):
        gtk.main()

if __name__ == "__main__":
    window = ToDoWindow()
    window.main()
