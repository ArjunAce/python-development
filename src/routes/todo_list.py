from sanic import response
from sanic.log import logger
from sanic.blueprints import Blueprint
from models.todo_list import TodoList
from models.users import Users
from datetime import datetime
from utils import todo_to_dict
from models import db

todo_blueprint = Blueprint("todos",  url_prefix='/api')


@todo_blueprint.route("/get_todos", methods=["GET"])
async def get_todos(request):
    logger.info("Fetching all todos")
    try:
        todos = await db.select([
            TodoList,
            Users.name,
            Users.age,
        ]).select_from(
            TodoList.join(Users)
        ).gino.load(( 
            TodoList,
            Users.name,
            Users.age
            )
        ).all()

        todo_list = []
        for todo, name, age in todos:
            todo_dict = todo_to_dict(todo)
            todo_dict.update({"name": name, "age": age})
            todo_list.append(todo_dict)

        return response.json(todo_list)
    except Exception as e:
        logger.error(e)
        return response.json({"error": "something went wrong"}, status=500)


@todo_blueprint.route("/get_todos_by_status", methods=["GET"])
async def get_todos_by_status(request):
    status = request.args.get("status", None)

    if status is None:
        return response.json({"error": "Missing status parameter"}, status=400)

    status = status.lower()
    status = True if status == "true" else False if status == "false" else None
    if status is None:
        return response.json({"error": "Invalid status parameter"}, status=400)

    try:
        todos = await TodoList.query.where(TodoList.status == status).gino.all()
        return response.json([todo_to_dict(todo) for todo in todos])
    except Exception as e:
        logger.error(e)
        return response.json({"error": "Something went wrong"}, status=500)


@todo_blueprint.route("/add_todo", methods=["POST"])
async def add_todo(request):
    logger.info("Adding a new todo")
    try:
        item = request.json["item"]
        status = request.json.get("status", False)
        created_at = datetime.now()

        todo = await TodoList.create(
            item=item,
            created_at=created_at,
            status=status
        )
        return response.json({"id": todo.id, "created_at": created_at.strftime("%Y-%m-%d %H:%M:%S")})
    except Exception as e:
        logger.error(e)
        return response.json({"error": "something went wrong"}, status=500)


@todo_blueprint.route("/get_todo_by_id", methods=["POST"])
async def get_todo_by_id(request):
    todo_id = request.json["id"]
    logger.info(f"Fetching todo with ID {todo_id}")
    try:
        todo = await TodoList.get(todo_id)
        if todo:
            return response.json(todo_to_dict(todo))
        return response.json({"error": "No todo found"}, status=200)
    except Exception as e:
        logger.error(e)
        return response.json({"error": "something went wrong"}, status=500)


@todo_blueprint.route("/update_todo", methods=["PUT"])
async def update_todo(request):
    try:
        todo_id = request.json["id"]
        item = request.json["item"]
        status = request.json["status"]
        logger.info(f"Updating todo with ID {todo_id}")
        todo = await TodoList.get(todo_id)
        if todo:
            await todo.update(
                item=item,
                status=status
            ).apply()
            return response.json({"success": "Todo updated", **todo_to_dict(todo)})
        return response.json({"error": "No todo found"}, status=200)
    except KeyError:
        return response.json({"error": "id, item and status are required"}, status=400)
    except Exception as e:
        logger.error(e)
        return response.json({"error": "something went wrong"}, status=500)


@todo_blueprint.route("/delete_todo", methods=["DELETE"])
async def delete_todo(request):
    try:
        todo_id = request.json["id"]
        logger.info(f"Deleting todo with ID {todo_id}")
        todo = await TodoList.get(todo_id)
        if todo:
            await todo.delete()
            return response.json({"success": "Todo deleted", **todo_to_dict(todo)})
        return response.json({"error": "No todo found"}, status=200)
    except KeyError:
        return response.json({"error": "id is required"}, status=400)
    except Exception as e:
        logger.error(e)
        return response.json({"error": "something went wrong"}, status=500)
