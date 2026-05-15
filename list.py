#mylist=["Prashant","Ashish","Komal","ankush","Ashish",77,"sandip",60.52,"prashant"]

# print(mylist)
# print(type(mylist))
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[-1])
# print(mylist[2:5])
# print(mylist[:5])
# print(mylist[1:])
# print(mylist[1:8:2])


# mylist[2]="Akshay"
# print(mylist)

# if "ankush" in mylist:
#     print("Yes ankush is available")
# else:
#     print('not available')

#append function always add value right side

# mylist.append('Sejal')
# mylist.append('shreya')
# print(mylist)

# mylist.insert(3,"Tejaswini")
# print(mylist)
# mylist.remove("sandip")
# print(mylist)

# newlist=mylist.copy()
# print(newlist)

# mylist=[['prashant','jha'],['85.56'],[440022,"yyy"]]
# print("example of multidimensional list:")
# print(mylist)
# print(mylist[0][0])
# print(mylist[0][1])
# print(mylist[2][1])
# print(mylist[1][0])
# print(mylist[2][0])

# list2=[50,25.50,'Prashant']
# list2.clear()
# print(list2)

# name="prashant"
# print(name)
# myname=list(name)#typecasting
# print(myname)
#we have used list constructor


# #SORTING__-_
# mylist=[2,5,23,90,56,34]
# mylist.sort()
# print(mylist)
# mylist.sort(reverse=True)
# print(mylist)


# mylist=[2,5,23,90,56,34]
# newlist=mylist
# print(id(mylist))
# print(id(newlist))

# mylist=[2,5,23,90,56,34]
# for i in mylist:
#     print(i)


# mylist=[0,1,2,4,0,2,5]
# mylist.remove(0)
# mylist.remove(0)
# mylist.append(0)
# mylist.append(0)
# print(mylist)


# mylist=[7,3,9,2,8]
# mylist.sort()
# print(mylist[-2])

# a=[1,2,3,4,5,6,7,8,9]
# a[::2]=10,20,30,40,50,60 #starting and ending missing only increment is 2 
# print(a)

# a=[1,2,3,4,5]
# print(a[3:0:-1]) 

# arr=[[1,2,3,4],
#      [4,5,6,7]
#      [8,9,10,11]
#      [12,13,14,15]]
# for i in range(0,4):         #i=0
#     print(arr[i].pop())


# arr=[1,2,3,4,5,6]
# for i in range(1,6):
#     arr[i-1]=arr[i]

# for i in range(0,6):
#     print(arr[i],end ="")

# fruit_list1=['Apple',"Berry","Cherry","Papaya"]
# fruit_list2=fruit_list1
# fruit_list3=fruit_list1[:]
# fruit_list2[0]='Guava'
# fruit_list3[1]='Kiwi'
# sum=0
# for ls in(fruit_list1,fruit_list2,fruit_list3):
#      if ls[0]=='Guava':
#         sum+=1
#      if ls[1]=='Kiwi':
#         sum+=20
# print(sum)
        
# #find the common element in array
# A=[1,2,3]
# B=[2,3,4]
# C=[3,4,5]
# for i in A:
#     if i in B and i in C:
#            print(i)


mylist=[]
N=int(input("Enter the value of N:"))
for i in range(N):
    val=int(input("Enter the value: "))
    mylist.append(val)
#print(mylist)
sum=0
for i in range(len(mylist)-1):
     if i+1 in range(len(mylist)):
        sum+=abs(mylist[i]-mylist[i+1])
print(sum)