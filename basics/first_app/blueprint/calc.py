from sanic import Blueprint, response

calc = Blueprint('calc', url_prefix='/calc')

@calc.route('/add', methods=['POST'])
async def add(request):
    data = request.json
    num1 = data.get('num1')
    num2 = data.get('num2')

    if num1 is None or num2 is None:
        return response.json({"error": "num1 and num2 are required"}, status=400)

    result = num1 + num2
    return response.json({"result": result})


@calc.route('/multiply', methods=['POST'])
async def multiply(request):
    data = request.json
    num1 = data.get('num1')
    num2 = data.get('num2')

    if num1 is None or num2 is None:
        return response.json({"error": "num1 and num2 are required"}, status=400)

    result = num1 * num2
    return response.json({"result": result})
