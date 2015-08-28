# -*- coding: utf-8 -*- 

from parameters import *
from SecretKey import *
#from PublicKey import *
from PublicKey_14 import *
from __builtin__ import max
from Function.operations import residue
from Encrypt import *
from Decrypt import *


for i in range(100):
    # 安全参数
    lbda = 3

    # 生成各个控制参数
    parameters = Par(lbda)

    # 生成私钥和公钥
    secret_key = Secret_Key(parameters.eta)
    # print bin(sk.sk)
    public_key = Public_Key(parameters, secret_key)

    m = 1

    cipher = encrypt(m, public_key, parameters, secret_key)
    m_d = decrypt(cipher, secret_key)
    if m_d == m:
        print "Right!\t", i

    parameters.clean()
    secret_key.clean()
    public_key.clean()
