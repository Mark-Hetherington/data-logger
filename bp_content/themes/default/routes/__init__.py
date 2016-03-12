"""
Using redirect route instead of simple routes since it supports strict_slash
Simple route: http://webapp-improved.appspot.com/guide/routing.html#simple-routes
RedirectRoute: http://webapp-improved.appspot.com/api/webapp2_extras/routes.html#webapp2_extras.routes.RedirectRoute
"""
from webapp2_extras.routes import RedirectRoute
from bp_content.themes.default.handlers import handlers

secure_scheme = 'https'

# Here go your routes, you can overwrite boilerplate routes (bp_includes/routes)

_routes = [
    #RedirectRoute('/secure/', handlers.SecureRequestHandler, name='secure', strict_slash=True),
    #RedirectRoute('/settings/delete_account', handlers.DeleteAccountHandler, name='delete-account', strict_slash=True),
    RedirectRoute('/contact/', handlers.ContactHandler, name='contact', strict_slash=True),
    RedirectRoute('/post-data/', handlers.DataSubmitHandler, name='data-submit', strict_slash=True),
    RedirectRoute('/taskqueue-process-data/', handlers.DataProcessHandler, name='taskqueue-process-data', strict_slash=True),
    RedirectRoute('/data-paths/', handlers.DataPathListHandler, name='data-path-index', strict_slash=True),
    RedirectRoute('/data-path/<path_id:.*>', handlers.DataPathDisplayHandler, name='data-path-view', strict_slash=True),
]

def get_routes():
    return _routes

def add_routes(app):
    if app.debug:
        secure_scheme = 'http'
    for r in _routes:
        app.router.add(r)
