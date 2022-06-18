set1 = {1,2,'Hello',(7,9,5)}
print(set1)
#add a new value on set
set1.add(89)
print(set1)
#update
set1.update([1,2,15,7]) #duplicate value ignored
print(set1)
#update with list and set
set1.update([9,75],{1,2,5,6,9,85})
print(set1)
#union, intersect and differnce
A={1,2,3,4,5,6,7}
B={1,2,5,9,10,12,59}
print(A|B) #Union
print(A&B) #intersect
print(A-B) # difference
print(B-A) # difference
#dictionary
mydict = dict()
mydict["Name"] = "John"
mydict["Name2"] = "King"
print ("mydict: ", mydict)

myinfo = {"Name": "Tran", "Age": 37, "Address" : "Vietnam" }
print ("myinfo['Name'] = ", myinfo["Name"])
print ("myinfo['Age'] = ", myinfo["Age"])
print ("myinfo['Address'] = ", myinfo["Address"])

set2=set()
set2.add(int(input()))
set2.add(int(input()))
set2.add(int(input()))
print(set2)
