from gevent import monkey
# from psycogreen.gevent import patch_psycopg


bind = '0.0.0.0:80'
backlog = 2048

workers = 1
worker_class = 'gevent'
worker_connections = 100
timeout = 60
keepalive = 2


def post_fork(server, worker):
    # Use gevent's monkey patching
    monkey.patch_all()
    # patch_psycopg()
    # worker.log.info("Made Psycopg2 Green")