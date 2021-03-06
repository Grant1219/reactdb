from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from models import initialize_db

def main (global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config (settings, 'sqlalchemy.')
    initialize_db (engine)

    config = Configurator (settings = settings)

    config.add_static_view ('static', 'static', cache_max_age = 3600)

    config.add_route ('home', '/')

    config.scan ()

    return config.make_wsgi_app ()

