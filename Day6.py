# #reverse each word in string
# name=input("Enter the string:").split()

# string=''
# for word in name:
#     string += word[ : :-1]+" "
# print(string)





# #check for valid Parenthesis using stack
# Check for Valid Parenthesis using Stack

# expression = input("Enter expression: ")
# stack = []
# valid = True

# for ch in expression:
#     if ch in "({[":
#         stack.append(ch)

#     elif ch in ")}]":

#         if len(stack) == 0:
#             valid = False
#             break

#         top = stack.pop()

#         if (ch == ')' and top != '(') or \
#            (ch == '}' and top != '{') or \
#            (ch == ']' and top != '['):
#             valid = False
#             break

# if len(stack) != 0:
#     valid = False

# if valid:
#     print("Valid Parenthesis")
# else:
#     print("Invalid Parenthesis")


#INSERSION SORT
# arr=[5,3,8,6,2]
# for i in range(1,len(arr)):
#     key=arr[i]
#     j=i-1
#     while j>=0 and arr[j]>key:
#         arr[j+1]=arr[j]
#         j=j-1
#     arr[j+1]=key
# print(arr)


#selection sort
# arr = [2,3,7,1,9,15]
# for i in range(0, len(arr)):
#     min = i   # store index

#     j = i + 1
#     while j < len(arr):
#         if arr[min] > arr[j]:
#             min = j
#         j += 1

#     arr[i], arr[min] = arr[min], arr[i]
# print(arr)


#sort Dictionary by key or value
#write a function to sort a dictionary by keys or values in ascending or descending order


# #instance variable
# class New:
#     def __init__(self):
#         self.a = 10
# Obj1 = New()
# Obj2 = New()
# Obj3 = New()
# Obj1.a = 20   # Only Obj1 is changed
# print(Obj1.a)  # 20
# print(Obj2.a)  # 10
# print(Obj3.a)  # 10

# #Static Variable
# class New:
#     a = 10
#     def __init__(self):
#         self.name = "Shreya"
# Obj1 = New()
# Obj2 = New()
# Obj3 = New()
# #New.a = 50
# print(Obj1.a)
# print(Obj2.a)
# print(Obj3.a)





# class College:
#     collegename="Modern College"
#     def __init__(self):
#         self.studentname="Sejal "

# principal=College() #object creation
# teacher=College()
# accountant=College()

# print("principal = ",principal.collegename,".....",principal.studentname)
# print("teacher = ",teacher.collegename,".....",teacher.studentname)
# print("accountant = ",accountant.collegename,".....",accountant.studentname)
# College.collegename="HBD"
# principal.studentname="Sejal Kashyap"
# print("principal = ",principal.collegename,"|",principal.studentname)
# print("teacher = ",teacher.collegename,"|",teacher.studentname)
# print("accountant = ",accountant.collegename,"|",accountant.studentname)




# class Node:
#     def __init__(self,data):
#         self.data= data
#         self.next=None

# class LinkedList:
#     def __init__(self):
#         self.head=None

# linkedlist=LinkedList()


# linkedlist.head=Node(5)
# second         =Node(10)
# third          =Node(15)
# fourth         =Node(20)
# #connecting nodes
# linkedlist.head.next=second
# second.next=third
# third.next=fourth

# #display a linkedlist
# while linkedlist.head != None:
#     print(linkedlist.head.data,"|","->")
#     linkedlist.head =linkedlist.head.next




class Node:
    def __init__(self,data):
        self.data=data #instance variable
        self.next= None

class Linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None

    def addNode(self,value):
        self.node=Node(value)
        if self.head is None:
            self.head=self.node
            self.tail=self.node 
        else:
            self.tail.next=self.node
            self.tail      =self.node
    
    def DisplayNode(self):

        while Linkedlist.head != None:
            print(Linkedlist.head.data,"|",self.head.next ,"->",end= '')
            self.head=self.head.next

    def AddNodeBeginning(self,value):
        print("add node beginning")
        self.node=Node(value)
        if self.head is None:
            self.head =self.node
            self.tail=self.node
        else:
            self.node.next=self.head
            self.head=self.node


if __name__ == '__main__':
    object=Linkedlist()#Linkedlist object created
    #MEnu driven options
    while True:
        print('1. Add Node LinkedList : ')
        print("2. Add Node in Beg :" )
        print("3. Add Node in Between :" )
        print("4. Add Node in End :" )
        print("5. Display  Linked List  :" )
        print("6. Exit:" )
        ch = int(input("Enter choice : "))
        if  ch == 1:
            value=int(input('Enter value for node: '))
            object.addNode(value)
            print('Node added successfully in single LinkedList: ')
        elif ch ==2:
            value=int(input("ENter value for node: "))
            object.AddNodeBeginning(value)
        elif ch == 5:
            object.DisplayNode()


# # Linked List with All Menu Operations

# class Node:

#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class LinkedList:

#     def __init__(self):
#         self.head = None

#     # Add node at end
#     def add_end(self, value):

#         newnode = Node(value)

#         if self.head is None:
#             self.head = newnode

#         else:
#             temp = self.head

#             while temp.next is not None:
#                 temp = temp.next

#             temp.next = newnode

#     # Add node at beginning
#     def add_begin(self, value):

#         newnode = Node(value)

#         newnode.next = self.head
#         self.head = newnode

#     # Add node at specific position
#     def add_between(self, pos, value):

#         newnode = Node(value)

#         temp = self.head
#         count = 1

#         while count < pos - 1 and temp is not None:
#             temp = temp.next
#             count += 1

#         if temp is None:
#             print("Position Invalid")
#             return

#         newnode.next = temp.next
#         temp.next = newnode

#     # Delete first node
#     def delete_begin(self):

#         if self.head is None:
#             print("Linked List Empty")

#         else:
#             self.head = self.head.next
#             print("First node deleted")

#     # Delete last node
#     def delete_end(self):

#         if self.head is None:
#             print("Linked List Empty")

#         elif self.head.next is None:
#             self.head = None

#         else:
#             temp = self.head

#             while temp.next.next is not None:
#                 temp = temp.next

#             temp.next = None

#             print("Last node deleted")

#     # Delete node at position
#     def delete_between(self, pos):

#         if self.head is None:
#             print("Linked List Empty")
#             return

#         temp = self.head
#         count = 1

#         while count < pos - 1 and temp.next is not None:
#             temp = temp.next
#             count += 1

#         if temp.next is None:
#             print("Invalid Position")
#             return

#         temp.next = temp.next.next

#         print("Node deleted")

#     # Search node
#     def search(self, value):

#         temp = self.head
#         pos = 1

#         while temp is not None:

#             if temp.data == value:
#                 print("Element found at position", pos)
#                 return

#             temp = temp.next
#             pos += 1

#         print("Element not found")

#     # Display linked list
#     def display(self):

#         if self.head is None:
#             print("Linked List Empty")

#         else:

#             temp = self.head

#             while temp is not None:
#                 print(temp.data, end=" -> ")
#                 temp = temp.next

#             print("None")


# # Main Program
# if __name__ == "__main__":

#     obj = LinkedList()

#     while True:

#         print("\n----- LINKED LIST MENU -----")
#         print("1. Add Node at End")
#         print("2. Add Node at Beginning")
#         print("3. Add Node at Position")
#         print("4. Delete First Node")
#         print("5. Delete Last Node")
#         print("6. Delete Node at Position")
#         print("7. Search Element")
#         print("8. Display Linked List")
#         print("9. Exit")

#         ch = int(input("Enter choice: "))

#         if ch == 1:

#             value = int(input("Enter value: "))
#             obj.add_end(value)

#         elif ch == 2:

#             value = int(input("Enter value: "))
#             obj.add_begin(value)

#         elif ch == 3:

#             pos = int(input("Enter position: "))
#             value = int(input("Enter value: "))

#             obj.add_between(pos, value)

#         elif ch == 4:

#             obj.delete_begin()

#         elif ch == 5:

#             obj.delete_end()

#         elif ch == 6:

#             pos = int(input("Enter position: "))

#             obj.delete_between(pos)

#         elif ch == 7:

#             value = int(input("Enter value to search: "))

#             obj.search(value)

#         elif ch == 8:

#             obj.display()

#         elif ch == 9:

#             print("Program Ended")
#             break

#         else:
#              print("Invalid Choice")