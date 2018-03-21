# %load /code/demo/loaders.py

from promise import Promise
from promise.dataloader import DataLoader
import redis

from promise.schedulers.gevent import GeventScheduler
from promise import set_default_scheduler
from schema import Player

set_default_scheduler(GeventScheduler())

r = redis.StrictRedis(host='redis', port=6379, db=0)

# http://docs.graphene-python.org/en/latest/execution/dataloader/
class PlayerLoader(DataLoader):

    def batch_load_fn(self, keys):
        pipe = r.pipeline()
        for key in keys:
            pipe.get(key)
        pipeline_resp = pipe.execute()
        return Promise.resolve([Player.from_redis_obj(key, obj) for key, obj in zip(keys, pipeline_resp)])