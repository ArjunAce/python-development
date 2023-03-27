from gino.ext.sanic import Gino
from sanic.log import logger
from config import DB_DSN

db = Gino()


def init_db(app):
    logger.info(f"Initializing db")
    app.config.DB_DSN = DB_DSN
    db.init_app(app)

    @app.listener("before_server_start")
    async def create_db(app, loop):
        await db.set_bind(app.config.DB_DSN)
        await db.gino.create_all()
