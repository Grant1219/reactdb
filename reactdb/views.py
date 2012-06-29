from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.sql.expression import func

from models import (
    DBSession,
    Image,
    Keyword
    )

@view_config (route_name = 'home', renderer = 'reactdb:templates/home.mako')
def my_view (request):
    mysql = DBSession ()
    images = None

    if 'query' in request.GET:
        # do search
        pass
    else:
        # get some random images
        images = mysql.query (Image).order_by (func.rand () ).limit (30).all ()

    return {'images': images}
