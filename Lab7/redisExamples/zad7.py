from redis import Redis

redis_connection = Redis(decode_responses=True)

redis_connection.zadd("sorted_set_key",{"key1": 1})#Set any number of element-name, score pairs to the key name.
# Pairs are specified as a dict of element-names keys to score values.
redis_connection.zadd("sorted_set_key",{"key44": 44})
redis_connection.zadd("sorted_set_key",{"key32": 32})
redis_connection.zadd("sorted_set_key",{"key4": 4})

print(redis_connection.zrange("sorted_set_key",0, -1))
#Return a range of values from sorted set name between start and end sorted in ascending order