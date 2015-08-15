# -*- coding: utf-8 -*-

from Function.operations import *

def decrypt(cipher, secret_key):
    p = secret_key.sk
    #m = (c % p) % 2
    
    print "************** Decrypt ***************"
    print "c = ", cipher.c, "\t p = ", p, "\tx0 = ", cipher.x0
    m = residue( cipher.c, p)
    #print "c % p = ", m
    print "c % p % 2 = ", residue(m, 2)

    print "\n**** check *******"
    print "m + 2r = ", cipher.m + 2*cipher.noise
    print ""
    r = residue( cipher.sum * 2, cipher.x0)
    print "% x0 = ",r
    r = residue(r, p)
    print "% p = ", r
    print residue(r, 2 )