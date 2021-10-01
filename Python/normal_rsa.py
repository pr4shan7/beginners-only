import gmpy2,binascii

#p*q = n 
#http://factordb.com/
n = input("n:")
e = input("e")
p = input("p:")
q = input("q:")
c = input("c:")

d = gmpy2.invert(e,(p-1)*(q-1))

m = pow(c,d,n)

flag = binascii.unhexlify(format(m, 'x')).decode()

print("FLAG: {}".format(flag))