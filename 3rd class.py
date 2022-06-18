bike= 100
cng=200
truck = 500
miniBus= 1000
Bus = 1500
vehicle = input('Enter your vehicle name: ')
toolfee= int(input('Enter your amount: '))
if toolfee==100:
     print('Please take your ticket for bike')
elif toolfee==200:
    print('Please take your ticket for cng')
elif toolfee == 500:
    print('Please take your ticket for truck')
elif toolfee==1000:
    print('Please take your ticket for MiniBus')
elif toolfee==1500:
    print('Please take your ticket for Bus')
else:
    print('Back to counter')