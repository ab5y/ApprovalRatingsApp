import os
import sys
from pyramid.config import Configurator
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from sqlalchemy import engine_from_config

from .models.meta import (
    DBSession,
    Base,
    user_pwd_context
    )

from .models import User
# from security import user_access_finder

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    basepath = os.path.dirname(__file__)
    filepath = os.path.abspath(os.path.join(basepath, "..", "development.ini"))
    user_pwd_context.load_path(filepath)

    authn_policy = AuthTktAuthenticationPolicy('tilop', hashalg='sha512') #callback=user_access_finder, 
    authz_policy = ACLAuthorizationPolicy()

    config = Configurator(settings=settings,
                            root_factory='approvalratingsapp.models.RootFactory')
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.add_route('register', '/register')
    config.add_route('post_rating', '/post_rating')
    config.add_route('create_ratee', '/create_ratee', factory='approvalratingsapp.security.UserFactory')
    config.scan()
    return config.make_wsgi_app()
