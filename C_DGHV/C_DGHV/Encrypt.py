# coding = utf-8

import random
from Function.operations import *

def encrypt(m, public_key, Par, secret_key):
    pk = public_key.seq_pk
    p = secret_key.sk
    #Subset_norm = random.randrange(1, len(pk))
    #Subset = random.sample(pk, Subset_norm)
    Subset = public_key.seq_pk

    rho_ = Par.rho * 2
    noise = random.randrange(-(2 ** rho_), 2 ** rho_)

    x0 = public_key.max_of_seq_pk
    r0 = public_key.r0
    q0 = public_key.q0
    #cipher = ( m + 2 * noise + 2 * sum(Subset) ) % x0
    cipher = residue(( m + 2 * noise + 2 * sum(Subset) ), x0)

    print "\n******************* Encrypt ********************"
    print "noise = ", noise, 2*noise
    print "sum(Subset) = ", sum(Subset), 2*sum(Subset)
    print "x0 = ", x0
    #lr = [x- r0 for x in public_key.seq_r]
    #lq = [x - q0 for x in public_key.seq_q]
    #print "check r sum : ", 2*sum(lr)
    #print "check q sum : ", 2*sum(lq), 2*sum(lq)*p
    print "check c: ", m + 2*noise + residue( 2*( p * sum(public_key.seq_q) + sum(public_key.seq_r) ), x0)
    print "2*sum(Subset) % x0 = ", residue( 2 * sum(Subset),  x0)
    print "m + 2 * noise = ", m + 2 * noise
    print u"密文为：", cipher
    return cipher