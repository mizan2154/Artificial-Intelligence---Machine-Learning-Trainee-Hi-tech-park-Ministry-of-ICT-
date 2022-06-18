# learning Numpy
import numpy as np
A=np.zeros(10, dtype='int')
print(A)

b=np.ones((3,5), dtype=float) #here(3,5)=row*column
print(b)
c=np.full((3,5),1.23)
print(c)
d=np.arange(0, 20, 2)
print(d)
e=np.linspace(0,1,5)
print(e)
f= np.random.normal(1, 5, (3,4))
print(f)
g=  np.eye(5)
print(g)
x1 = np.array([4, 3, 4, 4, 8, 4])
print(x1)
x2 = np.random.randint(5, size=(3, 4))
print(x2)
x= np.arange(15)
print(x)
s=x[:5]
print(s)
s1=x[5:]
print(s1)
grid = np.array([[1,2,3],[4,5,6]])
l=np.concatenate([grid,grid,grid])
print(l)
