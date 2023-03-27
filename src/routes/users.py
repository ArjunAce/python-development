from sanic import Blueprint, response
from sanic.log import logger
from models.users import Users

users_blueprint = Blueprint("users",  url_prefix='/api')

@users_blueprint.route("/get_users", methods=["GET"])
async def get_users(request):
    try:
        users = await Users.query.gino.all()
        return response.json([user.to_dict() for user in users])
    except Exception as e:
        logger.error(e)
        return response.json({"error": "Something went wrong"}, status=500)


@users_blueprint.route("/add_user", methods=["POST"])
async def add_user(request):
    try:
        user = await Users.create(
            name=request.json["name"],
            age=request.json["age"]
        )
        return response.json({"id": user.id})
    except KeyError:
        return response.json({"error": "Missing name or age"}, status=400)
    except Exception as e:
        logger.error(e)
        return response.json({"error": "Something went wrong"}, status=500)


@users_blueprint.route("/get_user_by_id", methods=["POST"])
async def get_user_by_id(request):
    try:
        user_id = request.json["user_id"]
        user = await Users.get(user_id)
        if user:
            return response.json(user.to_dict())
        return response.json({"error": "User not found"})
    except KeyError:
        logger.error(e)
        return response.json({"error": "Missing user_id"}, status=400)
    except Exception as e:
        logger.error(e)
        return response.json({"error": "Something went wrong"}, status=500)
    


@users_blueprint.route("/update_user", methods=["PUT"])
async def update_user(request):
    try:
        user_id = request.json["user_id"]
        name=request.json["name"]
        age=request.json["age"]
        user = await Users.get(user_id)
    except KeyError:
        logger.error(e)
        return response.json({"error": "Missing user_id"}, status=400)
    except Exception as e:
        logger.error(e)
        return response.json({"error": "Something went wrong"}, status=500)
    
    if user:
        try:
            await user.update(
                name=name,
                age=age
            ).apply()
        except Exception as e:
            logger.error(e)
            return response.json({"error": "Something went wrong"}, status=500)
        return response.json({"success": "User updated", **user.to_dict()})
    return response.json({"error": "User not found"})


@users_blueprint.route("/delete_user", methods=["DELETE"])
async def delete_user(request):
    try:
        user_id = request.json["user_id"]
        user = await Users.get(user_id)
    except KeyError:
        return response.json({"error": "Missing user_id"}, status=400)
    except Exception as e:
        return response.json({"error": "Something went wrong"}, status=500)
    
    if user:
        try:
            await user.delete()
        except Exception as e:
            return response.json({"error": "Something went wrong"}, status=500)
        return response.json({"success": "User deleted", **user.to_dict()})
    return response.json({"error": "User not found"})
