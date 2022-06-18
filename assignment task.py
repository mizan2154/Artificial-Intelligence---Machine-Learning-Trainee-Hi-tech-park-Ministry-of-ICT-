BookName = ['Gitanjoli','AgniBina','Debdas','Meghnadh','Shawgat','Ruposhi Bangla']
Writter =['Rabindranath Tagor', 'Kazi Nazrul Islam','Shorat Chandra','Mickel Modu shudon datta','Begum Rokeya', 'Jibonanda das']
BookCode = ['R01','N01','S01','M01','BR01','J01']
BookType =['Novel','Poetry','Fiction','other']
Q= int(input('How many book you want to buy: '))
for i in range (Q):
    WB= input('Please Enter Your BookCode: ')
    print('Book Number: ',i)
    if WB == 'R01': 
        print('Book Name: '+BookName[0])
        print('Writter: ' +Writter[0])
        print('Type of Book' +BookType[1])
    elif WB == 'N01':
        print('Book Name: '+BookName[1])
        print('Writter: ' +Writter[1])
        print('Type of Book :' +BookType[1])
    elif WB == 'S01':
        print('Book Name: '+BookName[2])
        print('Writter: ' +Writter[2])
        print('Type of Book :' +BookType[2])
    elif WB == 'M01':
        print('Book Name: '+BookName[3])
        print('Writter: ' +Writter[3])
        print('Type of Book :' +BookType[2])
    elif WB == 'BR01':
        print('Book Name: '+BookName[4])
        print('Writter: ' +Writter[4])
        print('Type of Book :' +BookType[3])
    elif WB == 'J01':
        print('Book Name: '+BookName[5])
        print('Writter: ' +Writter[5])
        print('Type of Book :' +BookType[1])

    else:
        print('No Book Available On this Book')
print('Thanks For buying books.')
