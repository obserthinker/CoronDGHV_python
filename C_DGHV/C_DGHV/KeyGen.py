# -*- coding: utf-8 -*- 

from parameters import *
from SecretKey import *
from PublicKey import *
from __builtin__ import max
from operations import residue

lbda = 3

par = Par(lbda)

# par.eta = 4 # test
sk = Secret_Key(par.eta)
# print bin(sk.sk)
pk = Public_Key(par, sk)
