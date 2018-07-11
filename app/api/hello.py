from sanic.response import json
from sanic import Blueprint

blueprint = Blueprint('hello', url_prefix='/hello')

@blueprint.route('/')
async def index(request):
    return json({'key': 'value'})
