#coding = utf-8
import gmpy2


for i in range(0,21):
     print 'Testing on Frame',i,'...'
     file = open('Frame'+str(i))
     try:
          frame = file.read( )
     finally:
          file.close( )

     n = gmpy2.mpz('0x'+frame[0:256])
     e = gmpy2.mpz('0x'+frame[256:512])
     c = gmpy2.mpz('0x'+frame[512:768])
     m = gmpy2.mpz(0)
     e = 3
     m = gmpy2.iroot(c,e)
     if(m[1]):
          print 'Frame',i,':',m[0]
