#class object
# class Name:
#     age=30 #data member
#     def display(self):#method
#         print("HEllo WORLD")
# obj=Name()#create oobject
# print(obj.age)#aceessing  variable
# obj.display()


# class Student:
#     def __init__(self):
#         self.name="Sejal"
#         self.age=30

#     def display(self):
#         print("Name= ",self.name)
#         print("age= ",self.age)
# studentobj=Student()
# print(studentobj)


# class Message:
#     def __init__(self):
#         print("i am constructor")
#     def shows(self):
#         print("Class PRogram ")

# obj= Message()
# obj.shows()
# obj2=Message()
# obj2.shows()



#parameterized constructor
# class StudentInfo:
#     def __init__(self,name,age,roll_no):
#         self.Name=name
#         self.Age=age
#         self.RollNo=roll_no
#     def displayStudentInfo(self):
#         print("Name: ",self.Name)
#         print("Age: ",self.Age)
#         print("Rollno: ",self.RollNo)

# stuentObj=StudentInfo("Sejal",21,101)
# stuentObj.displayStudentInfo()


#STACK IMPLEMENTATION
# import sys
# class Stack:
#     def __init__(self,size):
#         self.myStack = []#creating stack
#         self.stackSize= size #defining Size
        
#     def isFull(self):
#         if len(self.myStack)==self.stackSize:
#             return True
#         else:
#             return False

#     def push(self, value):
#         if self.isFull():
#             print("Stack is Full")
#         else:
#             self.myStack.append(value)
#             print("Element push")

#     def display(self):
#         print(self.myStack)

#     def IsEmpty(self):
#         if self.myStack ==[]:
#             return True
#         else:
#             return False
        
#     def pop(self):
#         if self.IsEmpty():
#             print("stack is Empty")
#         else:
#             print(self.myStack.pop())
#     def peek(self):
#         if self.IsEmpty():
#             print("Stack is Empty ")
#         else:
#             print(self.myStack[-1])
#     def Delete(self):
#             self.myStack=None
#             print("Stack is deleted")
    
# size=int(input("Enter the size of stack:"))
# obj = Stack(size)

# print("Stack has created :")
# while True:
#     print("1. Push Operation")
#     print("2. Display Stack")
#     print("3. Pop OPeration ")
#     print("4. Peek Operation :")
#     print("5. Delete ")
#     print("7. Exit")
#     choice = int(input("Enter your choice :"))
#     if choice == 1:
#         value = int(input("Enter value to push in stack :"))
#         obj.push(value)
#     elif choice == 2:
#         obj.display()
#     elif choice== 3:
#         obj.pop()
#     elif choice == 4:
#         obj.peek()
#     elif choice == 5:
#         obj.Delete()
#     else:
#         sys.exit()



# input
class stack:
    def __init__(self):
        self.myStack=[]

