import falcon
from router import routes
from handler.Error import EngineError
from utils.logger import Log

# falcon.API instances are callable WSGI apps
app = falcon.API()

for route in routes:
    Log(f"Adding route: {route}")
    app.add_route(route, routes[route])

app.add_error_handler(EngineError, EngineError.handle)
