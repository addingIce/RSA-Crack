'''
如果在两次公钥的加密过程中使用的n1和n2具有相同的素因子，那么可以利用欧几里得算法
直接将n1和n2分解。通过欧几里得算法可以直接求出n1和n2的最大公约数p:
(n1,n2)=p
可以得出：
n1=p*q1
n2=p*q2

解出Frame1明文为 m = '. Imagin'
    Frame18明文为 m = 'm A to B'
'''
#code = utf-8
import gmpy2
#---------------寻找含有含有相同因子p的N的Frame--------------------

N = []
for i in range(0,21):
     file = open('Frame'+str(i))
     try:
          frame = file.read( )
          N.append(gmpy2.mpz('0x'+frame[:256]))
     finally:
          file.close( )

for i  in range(0,21):
    for j in range(0,21):
        if not N[i] == N[j] and not gmpy2.gcd(N[i],N[j]) == 1:
            print i,'--',j,'\n'


#--------------Frame1,Frame18---------------------------------
N = []
E = []
C = []
f = [1,18]
for i in f:
     file = open('Frame'+str(i))
     try:
          frame = file.read( )
          N.append(gmpy2.mpz('0x'+frame[0:256]))
          E.append(gmpy2.mpz('0x'+frame[256:512]))
          C.append(gmpy2.mpz('0x'+frame[512:768]))
     finally:
          file.close( )

p = gmpy2.gcd(N[0],N[1])
print p
for i in range(0,2):
    q = N[i]/p
    print q
    s = gmpy2.gcdext(E[i],(p-1)*(q-1))
    d = s[1]
    print d
    m = pow(C[i],d,N[i])
    m = hex(m)
    m = m[-16:]
    print m.decode('hex')
    
