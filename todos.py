def gettodos(project):
    todos = []
    todo = {
        "title": "Todo number 1",
        "details": """- Write todo
- Test todo
- Publish todo""",
        }

    todos.append(todo)
    todo = {
        "title": "Todo number 2",
        "details": """- Write todo
- Test todo
- Publish todo""",
        }

    todos.append(todo)

    return todos
