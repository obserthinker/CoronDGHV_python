# coding = utf-8

def round_near(x):
    if (x - int(x)) <= 0.5:
        x = int(x)
    else:
        x = int(x) + 1

    return x

def residue(z, p):
    res = z - round_near(z/p) * p
    return res