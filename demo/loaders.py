# %load /code/demo/loaders.py

from promise import Promise
from promise.dataloader import DataLoader
import redis

from promise.schedulers.gevent import GeventScheduler
from promise import set_default_scheduler

set_default_scheduler(GeventScheduler())

r = redis.StrictRedis(host='redis', port=6379, db=0)

# http://docs.graphene-python.org/en/latest/execution/dataloader/
class PlayerLoader(DataLoader):

    def batch_load_fn(self, keys):
        p = r.pipeline()
        for key in keys:
            p.hgetall(key)
        return Promise.resolve([obj for obj in p.execute()])

        # return Promise.resolve([self.get_player(key, obj) for obj in p.execute()])