import random
import hashlib
from collections import Counter


def generate(site, month_key, extra_secret, length, char_sets):

    seed_str = site.lower() + month_key + extra_secret
    h = hashlib.sha256()
    h.update(seed_str.encode('ascii'))
    random.seed(h.digest())

    pwd_length = random.choice(list(length)) if type(length) == range else length
    charset_seq = []
    while not all(Counter(charset_seq)[i] > 0 for i in range(len(char_sets))):
        charset_seq = random.choices(list(range(len(char_sets))), k=pwd_length)

    password = ''
    for s in charset_seq:
        password += random.choice(char_sets[s])

    return password
