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


n = gmpy2.mpz(90252653600964453524559669296618135272911289775949194922543520872164147768650421038176330053599968601135821750672685664360786595430028684419411893316074286312793730822963564220564616708573764764386830123818197183233443472506106828919670406785228124876225200632055727680225997407097843708009916059133498338129)
p = gmpy2.mpz(1719620105458406433483340568317543019584575635895742560438771105058321655238562613083979651479555788009994557822024565226932906295208262756822275663694111)
q = gmpy2.mpz(52484065122572767557293534477361686456679280880304125291106733197354892893647364164212186415880889674435558369420400890814461263958618375991691022752189839)


s = gmpy2.gcdext(E[2],(p-1)*(q-1))
d = s[1]
print 'd',d
m = pow(C[2],d,N[2])
m = hex(m)
m = m[-16:]
print m.decode('hex')


n = gmpy2.mpz(93836514358344173762895084384953633159699750987954044414830106276642828025218933012478990865656107605541657809389659063108620208004740646099662700112782252200834393363574089818787717951026690934986964275526538236750596344542450864284576226592039259070002692883820960186403938410354082341916474419847211138467)
p = gmpy2.mpz(9686924917554805418937638872796017160525664579857640590160320300805115443578184985934338583303180178582009591634321755204008394655858254980766008932978699)
q = gmpy2.mpz(9686924917554805418937638872796017160525664579857640590160320300805115443578184985934338583303180178582009591634321755204008394655858254980766008932978633)


s = gmpy2.gcdext(E[10],(p-1)*(q-1))
d = s[1]
print 'd',d
m = pow(C[10],d,N[10])
m = hex(m)
m = m[-16:]
print m.decode('hex')
