import random
import hashlib
from collections import Counter

char_sets = [
    '01234567890',
    'abcdefghijklmnopqrstuvwxyz',
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    '!@#$%^&*()=+/?\|[]{}`~;:,<.>'
]


def generate(site, month_key, extra_secret, length, char_specs):

    #if length < sum(char_specs.values()):
    #    raise ValueError('Not enough length to fulfill character specs')

    # make a seed
    seed_str = site.lower() + month_key + extra_secret
    h = hashlib.sha256()
    h.update(seed_str.encode('ascii'))
    random.seed(h.digest())

    # decide password length if a range is provided
    pwd_length = random.choice(list(length)) if type(length) == range else length
    # decide the character set for every char of password
    charset_seq = []
    while not all(Counter(charset_seq)[i] > char_specs[i] for i in range(len(char_sets))):
        charset_seq = random.choices(range(len(char_sets)), k=pwd_length)

    # pick password chars from previously decided sets
    password = ''.join([random.choice(char_sets[s]) for s in charset_seq])

    return password
