# sal=int(input("Enter your Salary: "))
# rating=int(input("Enter your performance apprasial rating : "))
# increment=0
# if rating>= 1 and rating <=3:
#     increment=sal*0.1
# elif rating>= 3.1 and rating <=4:
#     increment=sal*0.3
# elif rating>= 4.1 and rating <=5:
#     increment=sal*0.4
# else:
#     print("Invalid rating")
# print('Incremented Salary: ',increment+sal)


# calculate gross of basic sal
# basicSalary=20000
# HRA=20000*0.2
# TA=20000*0.3
# DA=20000*0.45

# gross=20000-(HRA+TA+DA)
# print(gross)



#Binary Search

# def binarySearch(array,target):
#     low=0
#     high=len(array)-1
#     while low<=high:
#         mid=(low+high)//2
#         if array[mid] == target:
#             return mid
#         elif array[mid] < target:
#             low=mid+1
#         else:
#             high=mid-1
#     return -1

# array=[1,2,4,6,8,9,10,17,15,19,20,25,28,39,30,32,35,37,39,40,50,54,56,62,64,69,70,72,74,76,83,85,88,90,92,94,96,99,100]
# target=72
# result=binarySearch(array,target)
# if result == -1:
#     print("Element not Found")
# else:
#     print("Element found at ",result)


#BUBBLE_SORT
# def bubbleSort(array):
#     for i in range(len(array)-1): #passes
#         for j in range(len(array)-i-1): #here i is used to reduce number of comparisions
#             if array[j]>array[j+1]:
#                 temp=array[j]
#                 array[j]=array[j+1]
#                 array[j+1]=temp
#             print(array)
#         print()
# array=[64,34,25,12,22,11,90]
# bubbleSort(array)


mylist=[2,3,5,6,7,2,4,5,8]
newlist=[]

for i in range(0,len(mylist)):
    count=0
    key=mylist[i]
    j=i+1
    while j < len(mylist):
        if key == mylist[j]:
              newlist.append(key)
        j=j+1
print(len(newlist))