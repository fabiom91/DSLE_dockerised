import cherrypy as cherrypy
from paste.translogger import TransLogger
from main import app as flask_app


app_logged = TransLogger(flask_app)

# Mount the WSGI callable object (app) on the root directory
cherrypy.tree.graft(app_logged, '/')

# Set the configuration of the web server
cherrypy.config.update({
    'engine.autoreload.on': False,
    'log.screen': True,
    'server.socket_port': 8080,
    'server.socket_host': '0.0.0.0'
})

# Start the CherryPy WSGI web server
cherrypy.engine.start()
cherrypy.engine.block()
