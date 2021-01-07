from redis import Redis

redis_connection = Redis(decode_responses=True)

redis_connection.sadd("key","val1") # Add value(s) to set name
redis_connection.sadd("key","val2")
redis_connection.sadd("key","val3","valueMoje") # can be more then 1 value

print(redis_connection.smembers("key"))#Return all members of the set name