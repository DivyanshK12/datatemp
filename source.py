from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

from fileinput import app as flask_app
from dashapps.dash1 import app as app1
from dashapps.dash2 import app as app2
from dashapps.dash3 import app as app3
import sys

application = DispatcherMiddleware(flask_app, {
    '/app1': app1.server,
    '/app2': app2.server,
    '/app3': app3.server,
})

if __name__ == '__main__':
    port = int(sys.argv[1])
    run_simple('0.0.0.0', port, application)
    #use localhost for local running and port 8050