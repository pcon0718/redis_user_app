import redis
import random

def get_list_of_words(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read().splitlines()

words = get_list_of_words('/home/pconway/python/redis_user_app/wordlist.10000')
loop_count = random.randrange(30)

## Select random word for key, value, and the key marked for deletion.
random_key = random.choice(words)
random_value = random.choice(words)
random_key_delete = random.choice(words)

## For debugging purposes only.
## Print the key, value, and the key marked for deletion.
# print(loop_count)
print('Key to be created: ', random_key)
print('Random Value: ', random_value)
print('Key to be Deleted: ', random_key_delete)

# i = 0
# while i < loop_count
#     print("hello")
#     i += 1

## Open up a connection to redis. Write a new key/value pair, and delete a random key.
r = redis.Redis(host='redis', port=6379)
r.set(random_key,random_value)
r.delete(random_key_delete)