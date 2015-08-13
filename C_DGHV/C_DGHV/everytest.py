# coding = utf-8


class C:
    a = 3

def fun(C):
    b = C.a
    print b

ss = C()
fun(ss)

li = []
li.insert(5,4)
print li
li.insert(3,7)
print li