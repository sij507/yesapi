import random
import string
from data import constants
import hashlib


def random_string(string_length=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))


def generate_sign(params):
    sign = ""
    for key in params:
        sign = sign + params[key]
    sign += constants.APP_SECRECT
    sign = hashlib.md5(sign.encode()).hexdigest().upper()
    return sign

