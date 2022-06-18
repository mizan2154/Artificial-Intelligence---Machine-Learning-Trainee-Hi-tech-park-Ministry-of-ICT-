"""file= open('E:/acheivment/demo.txt','w') #write
file.write('Hello world\n')
file.write('Hello Bangladesh\n')
file.write('Hello Evryone\n')
file.write('This for check only\n')
file.close()"""
#read
'''file= open('E:/acheivment/demo.txt','r')
l=file.read()
a=[l]
print(a )
file.close()'''

a= open('E:/acheivment/demo.txt','r')
d =a.read()
data=[d]
for line in data:
    words= line.split()
print(words)