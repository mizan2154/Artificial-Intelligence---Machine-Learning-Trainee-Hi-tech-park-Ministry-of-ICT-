politicleParties=['AAP','Elephent','Hand','Rest']
electionYear=['2014','2009','2005','2001']
countryStatus=['worst','developing','developed']
corruptionStatus=['Max','Normal','Min']

while True:
    year=input('Enter a year: ')
    if year=='0':
        break
    else:
        if year == "2014":
            print("AAp Wins!")
            print("Country status: "+countryStatus[2])
            print("Corruption Status: "+corruptionStatus[2])
        elif year == "2009":
            print("Hand Won !")
            print("Country status: "+countryStatus[0])
            print("Corruption Status: "+corruptionStatus[0])
        elif year == "2005":
            print("Hand won!")
            print("Country status: "+countryStatus[0])
            print("Corruption Status: "+corruptionStatus[0])
        elif year == "2001":
            print("Rest Won!")
        else:
            print('Wrong year of election!') 


print('Thank You!')