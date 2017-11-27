
'''
令网中有3用户为加快加密速度，均选用e=3，而有不同的模m1、m2、m3，一般m1、m2、m3互素，
否则可求出其公因子，即求出构成m1、m2、mj的两个因子p和q中的1个，进而导致解密密钥被破解。
若有l用户要将明文m传给这3个用户，其密文分别为：
c1 = m^3 mod n1    m<n1
c2 = m^3 mod n2    m<n2
c3 = m^3 mod n3   m<n3
设 c = m^3 mod (n1*n2*n3)   利用中国剩余定理，可根据n1、n2、n3、c1、c2、c3求出c
由于m<n1、m<n2、m<n3，可得m^3<n1*n2*n3  因此c=m^3，即可求出m。 


e = 0x03 的有：7,11,15
e = 0x05 的有：3,8,12,16,20
经过尝试，3,8,12,16,20可解出明文 m = 't is a f'
'''

#code = utf-8
import gmpy2
#---------------寻找使用相同指数e的Frame--------------------
'''
E = []
N = []
for i in range(0,21):
     file = open('Frame'+str(i))
     try:
          frame = file.read( )
          N.append(frame[0:256])
          E.append(frame[256:512])
     finally:
          file.close( )

for i  in range(0,21):
    if(E.count(E[i]) > 1):
        if(not gmpy2.is_prime(gmpy2.mpz('0x'+N[i]))):
            print i,'   ',E[i]
'''


#------------------------------------------------------------
def CTR(a,m):
    result = 0
    M = 1
    for t in m:
        M = M*t
    for i in range(0,len(a)):
        s = gmpy2.gcdext(M/m[i],m[i])
        result = result + a[i]*(M/m[i])*s[1]
    return result%M

a = []
m = []
e = 0
I = [3,8,12,16,20]
for i in I:
     file = open('Frame'+str(i))
     try:
          frame = file.read( )
          e = gmpy2.mpz('0x'+frame[256:512])
          m.append(gmpy2.mpz('0x'+frame[0:256]))
          a.append(gmpy2.mpz('0x'+frame[512:768]))
     finally:
          file.close( )

result = CTR(a,m)
result = gmpy2.iroot(result,e)

result = hex(result[0])[-16:]
print result.decode('hex')

