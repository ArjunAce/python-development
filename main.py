from sanic import Sanic
from sanic.response import text
from views.add import AddView

app = Sanic("MyHelloWorldApp")

@app.get("/")
async def hello_world(request):
   return text("Hello, world.")

@app.route('/test')
async def test(request):
    return text(f"Test endpoint")

@app.route('/tags/<tag>')
async def tag_handler(request, tag):
    return text("Tag - {}".format(tag))

app.add_route(AddView.as_view(), "/add")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, dev=True)