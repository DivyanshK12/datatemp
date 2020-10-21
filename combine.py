from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

from try4 import app as flask_app
from dash1 import app as app1
from dash3 import app as app3

application = DispatcherMiddleware(flask_app, {
    '/app1': app1.server,
    '/app3' : app3.server,
})

if __name__ == '__main__':
    run_simple('localhost', 8050, application)