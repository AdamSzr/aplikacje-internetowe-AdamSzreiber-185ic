from redis import Redis

redis_connection = Redis(decode_responses=True)

hash_key ='test_hash'

print( redis_connection.hset(hash_key,'key1','value5'))
# Set key to value within hash name, mapping accepts a dict of key/value pairs that that will be added to hash name.
# Returns the number of fields that were added.