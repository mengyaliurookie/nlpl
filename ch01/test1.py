import numpy as np

D,N=8,7
x=np.random.randn(1,N)
print(x)
print('-=-'*27)
y=np.repeat(x,D,axis=0)
print(y)
print('-=-'*27)
dy=np.random.randn(N,D)
dx=np.sum(dy,axis=0,keepdims=True)
print(dx)

