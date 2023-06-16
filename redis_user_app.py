import redis
import string
import random

# initializing size of string
K = random.randrange(100)
V = random.randrange(100)

# using random.choices()
# generating random strings
key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=K))
value = ''.join(random.choices(string.ascii_uppercase + string.digits, k=V))
print(key)
print(value)

r = redis.Redis(host='redis', port=6379)
r.set(key,value)
# r.get('foo')