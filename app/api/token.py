from sanic.response import json
from sanic import Blueprint

blueprint = Blueprint('token', url_prefix='/tokens')

@blueprint.route('/')
async def index(request):
    return json({'key': 'value'})
