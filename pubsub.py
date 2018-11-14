import redis
rconn = redis.StrictRedis(host='localhost', port=6379)
pubsub = rconn.pubsub()

rconn.publish('python.org.pk', 'Msg1 from python.org.pk')


pubsub = rconn.pubsub()
pubsub.subscribe('python.org.pk')
pubsub.get_message()

