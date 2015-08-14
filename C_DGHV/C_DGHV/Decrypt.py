# -*- coding: utf-8 -*-

from Function.operations import *

def decrypt(c, secret_key):
    p = secret_key.sk
    #m = (c % p) % 2
    
    print "************** Decrypt ***************"
    print "c = ", c, "\t p = ", p
    m = residue(c, p)
    print "c % p = ", m
    m = residue(m,2)
    print "(c % p) % 2 = ", m