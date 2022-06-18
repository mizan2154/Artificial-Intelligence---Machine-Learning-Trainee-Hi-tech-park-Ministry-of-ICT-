def add(x,y,*z):
    t=x+y
    for i in z:
        t+=i
    return t
print(add(5,3))   
print(add(5,3,7))
print(add(5,3,7,9))
print(add(5,3,7,9,10))