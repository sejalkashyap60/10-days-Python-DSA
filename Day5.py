# def func(value,values):
#     var=1
#     values[0]=44
# t=3
# v=[1,2,3]
# func(t,v)
# print(t,v[0]) #output 3 44



# def f(i,values=[]):
#     values.append(i)
#     print(values)
#     #return values
# f(1)
# f(2)
# f(3) #output [1] [1,2] [1,2,3]



#QUEUE
# import sys
# class Queue:
#     def __init__(self,size):
#         self.myQueue = []#creating stack
#         self.queueSize= size #defining Size


        
#     def isFull(self):
#         if len(self.myQueue)==self.queueSize:
#             return True
#         else:
#             return False

#     def Enqueue(self, value):
#         if self.isFull():
#             print("Queue is Full")
#         else:
#             self.myQueue.append(value)
#             print("Element add")

#     def display(self):
#         print(self.myQueue)

#     def IsEmpty(self):
#         if self.myQueue ==[]:
#             return True
#         else:
#             return False
        
#     def Dequeue(self):
#         if self.IsEmpty():
#             print("Queue is Empty")
#         else:
#             print(self.myQueue.pop(0))

#     def peek(self):
#         if self.IsEmpty():
#             print("Queue is Empty ")
#         else:
#             print(self.myQueue[0])
#     def DeleteQ(self):
#             self.myQueue=None
#             print("Queue is deleted")
    
# size=int(input("Enter the size of queue:"))
# obj = Queue(size)

# print("Queue has created :")
# while True:
#     print("1. Enqueue Operation")
#     print("2. Display Queue")
#     print("3. Dequeue OPeration ")
#     print("4. Peek Operation :")
#     print("5. Delete Queue ")
#     print("7. Exit")
#     choice = int(input("Enter your choice :"))
#     if choice == 1:
#         value = int(input("Enter value to add in Queue :"))
#         obj.Enqueue(value)
#     elif choice == 2:
#         obj.display()
#     elif choice== 3:
#         obj.Dequeue()
#     elif choice == 4:
#         obj.peek()
#     elif choice == 5:
#         obj.DeleteQ()
#     else:
#         sys.exit()



# fruit={} #{'Apple':1,"Banana":2,"apple":3}
# def addone(index):
#     if index in fruit:
#         fruit[index]+=1
#     else:
#         fruit[index]=1
# addone('Apple')
# addone('banana')
# addone('apple')
# print(len(fruit)) #output: 3


# input=int(input("Enter the number of students : "))
# student={}

# for i in range(input):
#     name=input("Enter Student name: ")
#     marks=int(input("Enter Student Marks: "))
#     student[name]=marks
# while True:
#     name=input("Enter Student Name to get marks:")
#     marks=student.get(name,-1)
#     if marks== -1:
#         print("Student not found")
#     else:
#         print("The Marks of ",name , "are",marks )
#     option=input("Do you want to find another student marks[yes|no]")
#     if option =="no":
#         break
# print("Thanks for using our application ")







#***********************************************************************************
#********Part 2***********************************************************
#write A  program  to access each character of String in forward and backward direction by using while loop?

# input=" Learning python is very easy"
# i=0
# while i < len(input):
#     print(input[i],end='')
#     i+=1

# print()
# print("Backward direction ")
# i=len(input)-1
# while i>= 0:
#     print(input[i],end=' ')
#     i-=1





#data transfer input output error 
# input ="abcdfiger abcdfger"
# output="j"
# list= input.split(" ")
# print(list)

# first =list[0]
# second=list[1]
# print(first)
# print(second)

# i=0
# j=0
# islast=True
# while(i < len(first) and j < len(second)):
#     if(first[i] != second[j]):
#         print(first[i])
#         islast=False
#         break
#     i+=1
#     j+=1

# if(islast):
#     print(first[-1])


    

# v=['a','e','i','o','u']
# w=input("Enter the word where we will search the vowels:")
# #w=sejalkashyap
# found=[]
# for i in w:
#     if i in v:
#         if i not in found:
#             found.append(i)
# print('found vowels= ',found)
# print('unique vowels',len(found),'from the given word=',w)

#output :
# Enter the word where we will search the vowels:sejal kashyap
# found vowels=  ['e', 'a']
# unique vowels 2 from the given word= sejal kashyap



#three space seperated in first input 
# x,y,z=map(int,input().split()) #x=6 ,y=30,z=50
# mylist=[] #29 38 12 48 39 55 
# for i in range(x):
#     a=int(input())
#     mylist.append(a)

# for j in mylist:
#     if j>=y and j<=z:
#         print(j,end='')




# import datetime
# date=datetime.datetime.now()
# print(date)
# print("its's now: {:%d/%m/%Y %H:%M:%S}".format(date))



# #comparing Address
# x=['A','B','C']
# y=['A','B','C']
# z=[1,2,3,4]
# print(x==y) #true
# print(x==z) #false
# print(x!=z) #true



#list Compresison
# val=[2**i for i in range(1,6)]#i=1,2,3,4,5
# print(val) #output:[2, 4, 8, 16, 32]

# s=[2,4,6,8]
# val2=[i for i in s if i%2==0]#i=1
# print(val2)


#Dictionary Compression
# squares={x:x*x for x in range(1,6)}
# print(squares)
# doubles={x:2*x for x in range(1,6)}
# print(doubles)


#list compression  taking multiple values 
# a,b=[int(x) for x in input("Enter 2 numbers : ").split()]
# print("Product is : ",a*b)

#float number 
# a,b,c=[float(x) for x in input("Enter three number : ").split(',')]
# print("The sum is : ", a+b+c)



# for can be used with else
# mycart=[10,20,800,60,70]
# for item in mycart:
#     if item>400:
#         print("This is not in my budget")
#         continue
#     print(item)
# else:
#     print("You have purchased everything")




# while True:
#     user = input("Enter username : ")
#     password = input("Enter password : ")

#     if user == "admin" and password == "admin":
#         print("Successfully logged")
#         break
#     else:
#         print("Invalid")



#TOWER OF HANOI
import time
class Tower:
    def __init__(self):
        print("Welcome to Tower of Hanoi Game ")
        print()
        print("Given Problem A=[3,2,1]      B=[]           C=[]  ")
        print()
        print("Expected output A=[]         B=[]            C=[3,2,1] ")
        self.A=[]
        self.B=[]
        self.C=[]

    def tower(self,item):
        self.A.append(item)
        time.sleep(3)
        print("A=",self.A)
        print("Items in tower A\n")

    def pass1(self):
        self.temp=self.A.pop(2)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=",self.A   ,"  ","B=",self.B  ,"  ","C= ",self.C)

        print("PASS ONE COMPLETED  \n")
    def pass2(self):
        self.temp=self.A.pop(1)
        self.B.append(self.temp)
        time.sleep(3)
        print("A=",self.A   ,"  ","B=",self.B  ,"  ","C= ",self.C)

        print("PASS TWO COMPLETED  \n")
    def pass3(self):
        self.temp=self.C.pop(0)
        self.B.append(self.temp)
        time.sleep(3)
        print("A=",self.A   ,"  ","B=",self.B  ,"  ","C= ",self.C)

        print("PASS THREE COMPLETED  \n")
    def pass4(self):
        self.temp=self.A.pop(0)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=",self.A   ,"  ","B=",self.B  ,"  ","C= ",self.C)

        print("PASS FOUR COMPLETED  \n")
    def pass5(self):
        self.temp=self.B.pop(1)
        self.A.append(self.temp)
        time.sleep(3)
        print("A=",self.A   ,"  ","B=",self.B  ,"  ","C= ",self.C)

        print("PASS FIVE COMPLETED  \n")
    
    def pass6(self):
        self.temp=self.B.pop(0)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=",self.A   ,"  ","B=",self.B  ,"  ","C= ",self.C)

        print("PASS SIX COMPLETED  \n")
    def pass7(self):
        self.temp=self.A.pop(0)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=",self.A   ,"  ","B=",self.B  ,"  ","C= ",self.C)

        print("PASS SEVEN COMPLETED  \n")

obj=Tower()
obj.tower(3)
obj.tower(2)
obj.tower(1)
obj.pass1()
obj.pass2()
obj.pass3()
obj.pass4()
obj.pass5()
obj.pass6()
obj.pass7()









