#coding = utf-8
import gmpy2

N = []
E = []
C = []
for i in range(0,21):
     file = open('Frame'+str(i))
     try:
          frame = file.read( )
     finally:
          file.close( )

     N.append(gmpy2.mpz('0x'+frame[0:256]))
     E.append(gmpy2.mpz('0x'+frame[256:512]))
     C.append(gmpy2.mpz('0x'+frame[512:768]))

#---------------Pollard rho算法------------------
'''
for n in N:
     print 'Testing on Frame',N.index(n),'...'
     x = gmpy2.mpz(2)
     y = x**2 + 1
     for i in range(0x10000,0x100000):
          p = gmpy2.gcd(y-x,n)
          if p != 1:
               print(p)
               break
          else:
               y=(((y**2+1)%n)**2+1)%n
               x=(x**2+1)%n
'''
#------------得到Frame6和Frame19的N的因子p
N2 = [N[6],N[19]]
E2 = [E[6],E[19]]
C2 = [C[6],C[19]]
P = [920724637201,1085663496559]
m = gmpy2.mpz(0)
for i in range(0,2):
    q = N2[i]/P[i]
    print 'q',q
    s = gmpy2.gcdext(E2[i],(P[i]-1)*(q-1))
    d = s[1]
    print 'd',d
    m = pow(C2[i],d,N2[i])
    m = hex(m)
    m = m[-16:]
    print m.decode('hex')
