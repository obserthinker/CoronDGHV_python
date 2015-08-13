# -*- coding: utf-8 -*-

def decrypt(c, secret_key):
    p = secret_key.sk
    m = (c % p) % 2
    print m