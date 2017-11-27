#coding = utf-8
import gmpy2
frame = [7]
for i in frame:
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
     j = 1
     while 1:
         if(gmpy2.iroot(c+j*n,e)[1]==1):
             print gmpy2.iroot(c+i*n,e)
             break
         j = j+1
