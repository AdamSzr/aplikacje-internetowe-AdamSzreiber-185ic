from redis import Redis

print("ZAD_1 PING")
redis_connection = Redis()
print(redis_connection.ping())
