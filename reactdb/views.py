from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.sql.expression import func

import sphinxapi
from sphinxapi import SphinxClient

from models import (
    DBSession,
    Image,
    Keyword
    )

@view_config (route_name = 'home', renderer = 'reactdb:templates/home.mako')
def home (request):
    mysql = DBSession ()
    images = None
    sphinx = SphinxClient ()
    sphinx.SetServer ('127.0.0.1', 9312)
    sphinx.SetMatchMode (sphinxapi.SPH_MATCH_ANY)

    if 'query' in request.GET and len (request.GET['query']) > 0:
        # do search
        results = sphinx.Query (request.GET['query'])
        matches = []
        for match in results['matches']:
            matches.append (match['id'])

        if results['total'] > 0:
            images = mysql.query (Image.id.label ('id'), Image.filename.label ('filename'), func.count (Keyword.id).label ('match_count') ).join (Image.keywords).filter (Keyword.id.in_ (matches) ).group_by (Image).order_by ('match_count DESC').distinct ()
    else:
        # get some random images
        images = mysql.query (Image).order_by (func.rand () ).limit (30).all ()

    return {'images': images}

@view_config (route_name = 'keywords', renderer = 'reactdb:templates/keywords.mako')
def keywords (request):
    mysql = DBSession ()

    form = KeywordForm (request.POST)

    if form.submit.data:
        pass

    return {'form': form}
