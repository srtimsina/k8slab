from redis import Redis
import time

redis_host = 'redis.pong.svc.cluster.local'
r = Redis(redis_host, socket_connect_timeout=1) # short timeout for the test
while True:
    redis_response=r.ping() 
    print(redis_response)
    print('response from host "{}"'.format(redis_host))
    time.sleep(5)