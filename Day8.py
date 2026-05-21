#remove leading zeros from a list of integers
# element=[0,0,1,2,0,3,0,0,4]
# result=[]
# i=0
# while(i==0):
#     i+= 1
# result=element[2:]
# print(result)




# Find the first Missing Positive Integers
# input=[3,4,-1,1]
# positive=1
# while positive in input:
#     positive+=1
# print("Misiing postive is :",positive)




# Find the smallest missing positive 
# arr=[7,8,9,11,12]
# positive=1
# while positive in arr:
#     positive+=1
# print("Missing smallest positive: ",positive)


# class BSTNode:
#     def __init__(self,data): #constructor method
#         self.data=data
#         self.leftChild=None
#         self.rightChild=None

    
# def insertNode(rootNode ,nodeValue):
#     if rootNode.data==None:
#         rootNode.data= nodeValue
#     elif nodeValue <= rootNode.data:
#         if rootNode.leftChild is None:
#             rootNode.leftChild=BSTNode(nodeValue)
#         else:
#             insertNode(rootNode.leftChild,nodeValue)
#     else:
#         if rootNode.rightChild is None:
#             rootNode.rightChild=BSTNode(nodeValue)
#         else:
#             insertNode(rootNode.rightChild,nodeValue)

# def preOrderTraversal(rootNode):
#     if not rootNode:
#         return
#     print(rootNode.data,end=" ")
#     preOrderTraversal(rootNode.leftChild)
#     preOrderTraversal(rootNode.rightChild)

# def inOrderTraversal(rootNode):
#     if not rootNode:
#         return

#     inOrderTraversal(rootNode.leftChild)
#     print(rootNode.data,end=" ")
#     inOrderTraversal(rootNode.rightChild)


# def postOrderTraversal(rootNode):
#     if not rootNode:
#         return

#     postOrderTraversal(rootNode.leftChild)
#     postOrderTraversal(rootNode.rightChild)
#     print(rootNode.data,end=" ")

# def searchNode(rootNode,nodeValue):
    
#     if rootNode.data== nodeValue:
#         print("The value is found")
#     elif nodeValue<rootNode.data:
#         if rootNode.rightChild is None:
#             print("no node Exits")
#         elif rootNode.leftChild ==nodeValue:
#             print("The value is found ")
#         else:
#             searchNode(rootNode.leftChild,nodeValue)
#     else:
#         if rootNode.rightChild is None:
#             print("no node Exits")
#         elif rootNode.rightChild.data == nodeValue:
#             print("the value is found ")
#         else:
#          searchNode(rootNode.rightChild,nodeValue)
        

        
# newBST =BSTNode(None) #object creation with none parameter
# insertNode(newBST,70)
# insertNode(newBST,50)
# insertNode(newBST,90)
# insertNode(newBST,30)
# insertNode(newBST,60)
# insertNode(newBST,80)
# insertNode(newBST,100)
# insertNode(newBST,20)
# insertNode(newBST,40)
# insertNode(newBST,10)
# preOrderTraversal(newBST)
# print()
# inOrderTraversal(newBST)
# print()
# postOrderTraversal(newBST)
# searchNode(newBST,120 )



# a=int(input("Enter first Number : "))
# b=int(input("Enter second Number : "))

# try:
#     print(a/b)
# except ZeroDivisionError:
#     print("can't divide by zero")
# except ValueError:
#     print("Enter only integer value: ")
# else:
#     print("Everything is Okay")


# import logging
# logging.basicConfig(filename=" newfile.txt",level=logging.DEBUG)
# try:
#     a=int(input("enter first integer no : "))
#     b=int(input("Enter second integer no :"))
#     print(a/b)
# except(ZeroDivisionError,ValueError) as message:
#     print(message)
#     logging.exception(message)
# print("Logging level is set up.Check 'newfile.txt' for log details.")



# import csv
# f=open("employee.csv",'a')
# a= csv.writer(f)
# # a.writerow(["Emp Id","Emp NAme ","Emp AGe"])
# empid=int(input("Enter the Employee ID"))
# empName=input("Enter the Employee Name: ")
# age=int(input("Enter employee age: "))
# a.writerow([empid,empName,age])
# print("file has created ")


import csv
f=open("student.csv",'a')
a= csv.writer(f)
# a.writerow(["Emp Id","Emp NAme ","Emp AGe"])
empid=int(input("Enter the student ID"))
empName=input("Enter the Student Name: ")
phy=int(input("Enter phy marks : "))
chem=int(input("Enter chem marks : "))
math=int(input("Enter math marks : "))
tot=phy+chem+math
per=(tot)/0.3
if tot >=40:
    print("Result: Pass")
else:
    print("Result: fail")

a.writerow([empid,empName,phy,chem,math,tot,per])
print("file has created ")
