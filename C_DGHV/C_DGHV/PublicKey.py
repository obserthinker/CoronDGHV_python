import random
from parameters import *
from operations import residue

class Public_Key:
    """Generate the public key"""

    seq_pk = []
    seq_q = []
    seq_r = []
    def __init__(self, Par, SK):
        tau = Par.tau
        gamma = Par.gamma
        rho = Par.rho
        eta = Par.eta
        p = SK.sk
        # seq_q = range( 0, int((2 ** gamma) / p) ) # 这是q取值的理论范围。但是该范围太大以至于程序不能生成该序列
        init_q = range( 2 ** eta, 2 ** (eta + 1)) # q取值的实际范围，比p大即可
        init_r = range( - 2 ** rho + 1, 2 ** rho )
        
        running = True
        while running:
            for i in range(0, tau):
                q = random.choice(init_q)
                r = random.choice(init_r)
                x = p * q + r
                self.seq_q.append(q)
                self.seq_r.append(r)
                self.seq_pk.append(x)
            if residue(max(self.seq_pk), p) % 2 == 0 and max(self.seq_pk) % 2 == 1:
                print residue(max(pk.seq_pk), sk.sk) % 2
                print  max(pk.seq_pk) % 2
                running = False
            else:
                del self.seq_pk[:]
           
        print u"公钥：\n", self.seq_pk