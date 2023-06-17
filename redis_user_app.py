import redis
import string
import random

def get_list_of_words(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read().splitlines()


words = get_list_of_words('./wordlist.10000')

random_key = random.choice(words)
random_value = random.choice(words)

print(random_key)
print(random_value)

r = redis.Redis(host='redis', port=6379)
r.set(random_key,random_value)