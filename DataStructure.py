# #find biggest number
# def findBiggestNumber(sampleArray): #================>O(1)
#     biggestNumber=sampleArray[0]
#     for index in range(1,len(sampleArray)):#================>O(n)
       
#         if sampleArray[index]>biggestNumber:#================>O(1)
#             biggestNumber = sampleArray[index]#================>O(1)
#     print(biggestNumber)#================>O(1)

# sampleArray=[5,7,9,2,3,4]
# findBiggestNumber(sampleArray)

#time complexity=> O(n)

#================>


# def linearSearch(array,target):
#     for i in range(0,len(array)):
#         if array[i]==target:
#             return i
#     return -1

# array=[1,2,3,4,8,7,9]
# target=6
# result=linearSearch(array,target)
# if result == -1:
#   print("target value not found")
# else:
#   print("Element not found")
# linearSearch(array,target)



#removing spaces from the string 
# rstrip() //remove spaces at right hand side 
# lstrip() //remove spaces at left hand side 
# strip()//remove spaces at both sides 

# city=input("Enter your city Name: ")
# scity=city.strip()
# if scity=='Hyderabad':
#    print("Hello hyderabad...adab")

# elif scity=='Chennai':
#    print("Hello Madrasi...vanakkam")

# elif scity=='Banglore':
#    print("Hello Kannadiga...Shubhodaya")

# else:
#    print("your entered city is invalid")



# mylist=[[100,198,333,323],[122,232,221,111],[223,565,245,764]]
# newlist=[]
# for i in range(3): #row
#     j=0 #col
#     max=mylist[i][j]
#     for j in range(4):
#         c_max=mylist[i][j]
#         if max_< c_max:
#             max = c_max
#    newlist.append(max)
# #error code 

# input="sejal*is*goood*programmer"
# name=""
# val=""
# for i in input:
#       if i != "*":
#          name+=i
#       else:
#           val+=i
# print(name)
# print(str(val+name))
     

input="aaabbbbccceeeee"
#output=a3b4c3e5


newname={}
for i in range(len(input)):
    key=input[i] #key=a
    count=0
    for j in range(len(input)):
        if key == input[j]: 
            count+=1 #key=a value=1
    newname[key]=count
for i,j in newname.items():
    print(i,j,sep="",end="")


    