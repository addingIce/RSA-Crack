'''
设n为信息明文，两个加密密钥分别为e1和e2，公共模数是n，则：
c1 = m^e1 mod n
c1 = m^e2 mod n
因为e1,e2互质，故用Euclideam算法能找到r和S， 满足：
r*e1 + s*e2 = 1
假设r为负数，需再用Euclideam算法计算c1^-1，则
(c1^-1)*(c2^s) = m mod n

解出明文 m = 'My secre'
'''

#coding = utf-8
import gmpy2
#---------------寻找使用相同模数N的Frame--------------------
'''
N = []
for i in range(0,21):
     file = open('Frame'+str(i))
     try:
          frame = file.read( )
          N.append(frame[:256])
     finally:
          file.close( )

for i  in range(0,21):
    if(N.count(N[i]) > 1):
        print i,'   ',N[i]
'''
#------------------Frame0 和 Frame4 使用相同模数N---------------------

file = open('Frame0')
try:
    frame = file.read( )
finally:
    file.close( )
n0 = gmpy2.mpz('0x'+frame[0:256])
e0 = gmpy2.mpz('0x'+frame[256:512])
c0 = gmpy2.mpz('0x'+frame[512:768])

file = open('Frame4')
try:
    frame = file.read( )
finally:
    file.close( )
n4 = gmpy2.mpz('0x'+frame[0:256])
e4 = gmpy2.mpz('0x'+frame[256:512])
c4 = gmpy2.mpz('0x'+frame[512:768])

s = gmpy2.gcdext(e0, e4)
s1 = s[1]
s2 = s[2]

if s1 < 0:
    s1 = -s1
    c0 = gmpy2.invert(c0, n0)
elif s2 < 0:
    s2 = -s2
    c4 = gmpy2.invert(c4, n0)
m = pow(c0, s1, n0) * pow(c4, s2, n0) % n0
m = hex(m)
m = m[-16:]
print m.decode('hex')
