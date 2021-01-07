from redis import Redis

redis_connection = Redis(decode_responses=True)

pubsub = redis_connection.pubsub() #Return a Publish/Subscribe object.
# With this object, you can subscribe to channels and listen for messages that get published to them.
pubsub.subscribe("testowa_kanal_komunikacyjny")
# Channels supplied as keyword arguments expect a channel name as the key and a callable as the value.
# A channel's callable will be invoked automatically when a message is received on that channel rather than producing a message via listen() or get_message()
for message in pubsub.listen():
    print(message)