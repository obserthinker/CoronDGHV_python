# coding = utf-8

import random

def encrypt(m, public_key, Par):
    pk = public_key.seq_pk
    Subset_norm = random.randrange(1, len(pk))
    Subset = random.sample(pk, Subset_norm)

    rho_ = Par.rho * 2
    noise = random.randrange(-(2 ** rho_), 2 ** rho_)

    cipher = ( m + 2 * noise + 2 * sum(Subset) ) % pk[0]

    print pk[0]
    print cipher
    return cipher