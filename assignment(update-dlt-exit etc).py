BookList=['Gitanjoli','NoukaDubi','Mrittukhuda','Rupoi ','feluda','Bomkeysh']
print("===================")
print('1. ADD a Book')
print('2. Display Book list')
print('3. Edit Book')
print('4.Search Book')
print('5. delete a book')
print('6. Sorting Book list')
print('7.Exit')
print("===================")

while True:
    n= int(input('Enter Your Choise: '))
    if n==1:
        Newbook=input('Enter your new book name in list: ')
        BookList.append(Newbook)
    elif n==2:
        print("Book list: ", BookList)
    elif n==3:
        updateIndex=int(input('Which indexes book you want update: '))
        Nbook=input("Enter update book name: ")
        BookList[updateIndex]=Nbook
    elif n==4:
        BookName=('Which book do you want to search: ')
        print(BookName in BookList)
    elif n==5:
        removes = int(input('Name of remove book index: '))
        del BookList[removes]
    elif n==6:
        BookList.sort()
        print('sortinf done.')
    elif n==7:
        break

