#coding = utf-8
import gmpy2

N = []
for i in range(0,21):
     file = open('Frame'+str(i))
     try:
          frame = file.read( )
     finally:
          file.close( )

     N.append(gmpy2.mpz('0x'+frame[0:256]))
for n in N:
    print n
