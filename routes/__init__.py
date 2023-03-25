from sanic import response
from sanic.log import logger
from sanic.blueprints import Blueprint
from models.todo_list import TodoList

api_blueprint = Blueprint("api",  url_prefix='/api')


@api_blueprint.route("/get_todos", methods=["GET"])
async def get_todos(request):
    logger.info("Fetching all todos")
    try:
        todos = await TodoList.query.gino.all()
    except Exception as e:
        logger.error(e)
        return response.json({"error": "something went wrong"}, status=500)
    return response.json([dict(todo) for todo in todos])


@api_blueprint.route("/add_todo", methods=["POST"])
async def add_todo(request):
    logger.info("Adding a new todo")
    try:
        todo = await TodoList.create(
            item=request.json["item"],
            created_at=request.json["created_at"],
            status=request.json["status"]
        )
    except Exception as e:
        logger.error(e)
        return response.json({"error": "something went wrong"}, status=500)
    return response.json({"id": todo.id})


@api_blueprint.route("/get_todo_by_id", methods=["POST"])
async def get_todo_by_id(request):
    todo_id = request.json["id"]
    logger.info(f"Fetching todo with ID {todo_id}")
    try:
        todo = await TodoList.get(todo_id)
        if todo:
            return response.json(dict(todo))
        return response.json({"error": "No todo found"}, status=404)
    except Exception as e:
        logger.error(e)
        return response.json({"error": "something went wrong"}, status=500)


@api_blueprint.route("/update_todo", methods=["POST"])
async def update_todo(request):
    todo_id = request.json["id"]
    logger.info(f"Updating todo with ID {todo_id}")
    try:
        todo = await TodoList.get(todo_id)
        if todo:
            await todo.update(
                item=request.json["item"],
                created_at=request.json["created_at"],
                status=request.json["status"]
            ).apply()
            return response.json({"success": "Todo updated"})
        return response.json({"error": "No todo found"}, status=404)
    except Exception as e:
        logger.error(e)
        return response.json({"error": "something went wrong"}, status=500)


@api_blueprint.route("/delete_todo", methods=["POST"])
async def delete_todo(request):
    todo_id = request.json["id"]
    logger.info(f"Deleting todo with ID {todo_id}")
    try:
        todo = await TodoList.get(todo_id)
        if todo:
            await todo.delete()
            return response.json({"success": "Todo deleted"})
        return response.json({"error": "No todo found"}, status=404)
    except Exception as e:
        logger.error(e)
        return response.json({"error": "something went wrong"}, status=500)

def init_routes(app):
    logger.info(f"Initializing routes")
    app.blueprint(api_blueprint)
