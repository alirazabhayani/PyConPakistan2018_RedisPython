import redis
rconn = redis.StrictRedis(host='localhost', port=6379)

pubsub = rconn.pubsub()
pubsub.subscribe('python.org.pk')
pubsub.get_message()