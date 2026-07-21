import redis
from app.settings import settings

def get_cache():
    if settings.REDIS_ENABLED:
        return redis.Redis(host='redis', port=6379, db=0)
    return None
