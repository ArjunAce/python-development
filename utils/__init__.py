def todo_to_dict(todo):
    todo_dict = todo.to_dict()
    todo_dict["created_at"] = todo_dict["created_at"].strftime(
        "%Y-%m-%d %H:%M:%S")
    return todo_dict
