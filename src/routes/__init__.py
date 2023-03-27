from sanic.log import logger
from routes.todo_list import todo_blueprint

def init_routes(app):
    logger.info(f"Initializing routes")
    app.blueprint(todo_blueprint)
