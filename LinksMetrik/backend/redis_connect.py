from django.conf import settings
import redis


# Connect to our Redis instance
redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                   port=settings.REDIS_PORT, db=0,
                                   decode_responses=True)
