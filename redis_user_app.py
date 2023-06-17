import redis
import random

def get_list_of_words(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read().splitlines()

words = get_list_of_words('./wordlist.10000')

## Select random word for key, value, and the key marked for deletion.
random_key = random.choice(words)
random_value = random.choice(words)
random_key_delete = random.choice(words)

## For debugging purposes only.
## Print the key, value, and the key marked for deletion.
# print(random_key)
# print(random_value)
# print(random_key_delete)

## Open up a connection to redis. Write a new key/value pair, and delete a random key.
r = redis.Redis(host='redis', port=6379)
r.set(random_key,random_value)
r.delete(random_key)