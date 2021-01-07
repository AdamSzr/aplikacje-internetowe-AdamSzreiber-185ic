from redis import Redis

print("ZAD_2 RPUSH")

redis_connection = Redis(decode_responses=True)
list_key ="example-list"

redis_connection.rpush(list_key,1,2,3,4,5) #Push values onto the tail of the list name
print(redis_connection.lrange(list_key,0, -1)) #Return a slice of the list name between position start and end

