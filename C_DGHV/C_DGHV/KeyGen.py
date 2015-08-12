# -*- coding: utf-8 -*- 

from parameters import *
from SecretKey import *

lbda = 3

par = Par(lbda)

# par.eta = 4 # test
sk = Secret_Key(par.eta)
# print bin(sk.sk)