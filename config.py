# DO NOT EDIT

# Assignment for 18yw85

from lib204 import wff
P, Q, R, S, T = map(wff.Variable, 'PQRST')
s1 = (P|(R|S))
s2 = ((~R|~P)&(P|~R))
s3 = (~P|(~R|~S))
s4 = ((~S|~R)&(S|~R))

s5 = ((~S>>(R&~P))|~(P|~S))
s6 = ((P>>S)>>(R|(S&~P)))