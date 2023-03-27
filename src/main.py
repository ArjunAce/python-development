from sanic import Sanic
from sanic.response import text
from routes import init_routes
from models.todo_list import init_db

app = Sanic("todo_app")

init_db(app)
init_routes(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, dev=True)
