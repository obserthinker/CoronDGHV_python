# coding = utf-8


a = [3,5,6]
b = [7,8,9]
#c = a + b
c = [x*y for x in a for y in b if a.index(x) == b.index(y)]
print range(len(a))