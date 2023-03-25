from sanic import response
from sanic.views import HTTPMethodView

class AddView(HTTPMethodView):
   async def get(self, request):
    try:
        num1 = int(request.args.get('num1'))
        num2 = int(request.args.get('num2'))
        sum = num1 + num2
        return response.json({'sum': sum })
    except:
        return response.json({'response': 'some error occurred' })
    
   
   async def post(self, request):
    try:
        data = request.json
        num1 = int(data.get('num1'))
        num2 = int(data.get('num2'))
        sum = num1 + num2
        return response.json({'result': sum})
    except:
        return response.json({'response': 'some error occurred' })
       