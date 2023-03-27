from sanic import Sanic
from routes import init_routes
from models import init_db

app = Sanic("todo_app")

init_db(app)
init_routes(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, dev=True)
