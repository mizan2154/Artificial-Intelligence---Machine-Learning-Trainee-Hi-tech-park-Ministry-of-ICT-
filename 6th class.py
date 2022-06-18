#update value
years =[1998,1999,2021,2022,2025]
print("Years: ",years)
years[1]=2005
print("Years: ",years)
for i in years:
    print(('Year: ',i))
New_year=int( input('Enter a new year: '))
years.append(New_year)
print("Years: ",years)
#rang update
years[1:4]=2222,2563,999
print("Years: ",years)
#delete index and remove exact value

del years[1]
print(years)
years.remove(145)
print(years)
#innsert new value in list
years.insert(2,777)
print(years)
# concate by
name =['mizan','salam','mustafiz']
concate = name+years
print(concate)

#clone list/multiple time write
bookid =[1,2,3]*10
for j in bookid:
    print(j)

#in for search true or false

print (77 in years)