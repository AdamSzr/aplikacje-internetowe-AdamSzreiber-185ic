from redis import Redis

redis_connection = Redis(decode_responses=True)

redis_connection.set("key","value") # Set the value at key name to value

redis_connection_1 = Redis(decode_responses=True, db=1) # not available on db1, because default is db0
# and on db0 exists an value of 'key' 

print(redis_connection_1.get("key"))

print(redis_connection.get("key"))