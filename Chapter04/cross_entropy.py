from matplotlib import pyplot
from math import log2

events = ['A', 'B', 'C','D']
p = [0.70, 0.05,0.10,0.15] 
q = [0.45, 0.10, 0.20,0.25]
print(f'P = {sum(p):.3f}',f'Q = {sum(q):.3f}')

pyplot.subplot(2,1,1)
pyplot.bar(events, p)
pyplot.subplot(2,1,2)
pyplot.bar(events, q)
pyplot.show()

def cross_entropy(p, q):
    return -sum([p*log2(q) for p,q in zip(p,q)])

h_pq = cross_entropy(p, q)
print(f'H(P, Q) =  {h_pq:.3f} bits')



