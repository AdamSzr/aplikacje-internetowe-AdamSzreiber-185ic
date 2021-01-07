from redis import Redis
from time import sleep
from datetime import datetime

redis_connection = Redis(decode_responses=True)
redis_connection.setex("key",30,"value")# Set the value of key name to value that expires in time seconds. 
# time can be represented by an integer

# jest to zlozenie 2 funkcji:
# redis_connection.set("key","value")
# redis_connection.expire("key",30)


print(datetime.now().time(), redis_connection.get("key"))
sleep(10)
print(datetime.now().time(), redis_connection.get("key"))
sleep(30)
print(datetime.now().time(), redis_connection.get("key"))