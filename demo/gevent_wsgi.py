from promise import set_default_scheduler
from promise.schedulers.gevent import GeventScheduler

from gevent.pywsgi import WSGIServer

from gevent import monkey
monkey.patch_all()

# Change the default promise scheduler to use gevent
set_default_scheduler(GeventScheduler)


import application as app
application = app.application

http_server = WSGIServer(('', 8080), application)
http_server.serve_forever()
