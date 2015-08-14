import random
from parameters import *
from Function.operations import residue

class Public_Key:
    """Generate the public key"""

    max_of_seq_pk = 0
    q0 = 0
    r0 = 0
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
                self.max_of_seq_pk = max(self.seq_pk)
            if residue(self.max_of_seq_pk, p) % 2 == 0 and self.max_of_seq_pk % 2 == 1:
                index = self.seq_pk.index(self.max_of_seq_pk)
                self.q0 = self.seq_q[index]
                self.r0 = self.seq_r[index]
                #print "****** check x0 *******"
                #print "residul: ", residue(self.max_of_seq_pk, p) % 2
                running = False
            else:
                del self.seq_pk[:]
                del self.seq_q[:]
                del self.seq_r[:]
           
        print u"公钥：\n", self.seq_pk
        check = []
        for i in range(len(self.seq_pk)):
            check.append(self.seq_q[i] * p+self.seq_r[i])
        print "q[] = ", self.seq_q
        print "r[] = ", self.seq_r
        print "check pk: ", check