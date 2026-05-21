#Stack Implementation using Linkedlist
# class Node:
#     def __init__(self, value=None):
#         self.value = value
#         self.next = None


# class Linkedlist:
#     def __init__(self):
#         self.head = None

#     def __iter__(self):
#         curNode = self.head
#         while curNode:
#             yield curNode
#             curNode = curNode.next


# class Stack:
#     def __init__(self):
#         self.Linkedlist = Linkedlist()

#     # display stack
#     def __str__(self):
#         values = [str(x.value) for x in self.Linkedlist]
#         return '\n'.join(values)

#     def isEmpty(self):
#         return self.Linkedlist.head is None

#     def push(self, value):
#         node = Node(value)
#         node.next = self.Linkedlist.head
#         self.Linkedlist.head = node

#     def pop(self):
#         if self.isEmpty():
#             return "There is no element in the Stack"
#         else:
#             poppedNode = self.Linkedlist.head
#             self.Linkedlist.head = self.Linkedlist.head.next
#             return poppedNode.value

#     def peek(self):
#         if self.isEmpty():
#             return "Stack is empty"
#         else:
#             return self.Linkedlist.head.value

#     def delete(self):
#         self.Linkedlist.head = None



# c = Stack()

# c.push(1)
# print(c)

# c.push(2)
# print(c)

# c.push(3)
# print(c)

# print("Display top value:")
# print(c.peek())

# print("Pop top element:")
# print(c.pop())

# print("Stack after pop:")
# print(c)

# print("Linkedlist deleted")
# c.delete()
# print(c)



#queue implementation using linkedlist


# class Node:
#     def __init__(self, value=None):
#         self.value = value
#         self.next = None
#     def __str__(self):
#         return str(self.value)
    
         
    
    

# class Linkedlist:
#     def __init__(self):
#         self.head = None
#         self.tail=None

#     def __iter__(self):
#         curNode = self.head
#         while curNode:
#             yield curNode
#             curNode = curNode.next

# class Queue:
#     def __init__(self):
#         self.Linkedlist = Linkedlist()
    
#       #display stack
#     def __str__(self):
#         values = [str(x) for x in self.Linkedlist]
#         return '\n'.join(values)
    
#     def enqueue(self,value):
#         newNode=Node(value)
#         if self.Linkedlist.head==None:
#             self.Linkedlist.head=newNode
#             self.Linkedlist.tail=newNode
#         else:
#             self.Linkedlist.tail.next=newNode
#             self.Linkedlist.tail = newNode
            
#     def isEmpty(self):
#          if self.Linkedlist.head == None:
#              return True
#          else:
#              return False
        
#     def Delete(self):
#         self.Linkedlist.head = None
    
#     def dequeue(self):
#         if self.isEmpty():
#             return "There is no element in the queue"
#         else:

#             tempNode = self.Linkedlist.head
#             if self.Linkedlist.head == self.Linkedlist.tail:
#                 self.Linkedlist.head =None
#                 self.Linkedlist.tail = None
#             else:
#                 self.Linkedlist.head = self.Linkedlist.head.next
#             return tempNode
#     def peek(self):
#         if self.isEmpty():
#             return "Queue  is empty"
#         else:
#             return self.Linkedlist.head.value


# custQueue=Queue()
# custQueue.enqueue(10)
# custQueue.enqueue(20)
# custQueue.enqueue(30)
# print(custQueue)
# print("Deleting element from Queue:")
# print(custQueue.dequeue())
# print("QUEUE Element Left ")
# print(custQueue)
# print("Peek Element:  ")
# print(custQueue.peek())
# print("Deleting element from Queue:")
# print(custQueue.dequeue())
# print(custQueue.dequeue())
# print(custQueue.dequeue())




# Graph implementation using Adjacency List
# class Graph:
#     def __init__(self):
#         self.adjacency_list = {}

#     def add_vertex(self, vertex):
#         if vertex not in self.adjacency_list:
#             self.adjacency_list[vertex] = []
#             return True
#         return False

#     def print_graph(self):
#         for vertex in self.adjacency_list:
#             print(vertex, ":", self.adjacency_list[vertex])

#     def add_edge(self, vertex1, vertex2):
#         if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
#             self.adjacency_list[vertex1].append(vertex2)
#             return True
#         return False

#     def remove_edge(self, vertex1, vertex2):
#         if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
#             if vertex2 in self.adjacency_list[vertex1]:
#                 self.adjacency_list[vertex1].remove(vertex2)
#                 return True
#         return False

   
#     def remove_vertex(self, vertex):
#         if vertex in self.adjacency_list:

#             for other_vertex in self.adjacency_list:
#                 if vertex in self.adjacency_list[other_vertex]:
#                     self.adjacency_list[other_vertex].remove(vertex)

#             del self.adjacency_list[vertex]
#             return True
#         return False



# my_graph = Graph()

# my_graph.add_vertex("A")
# my_graph.add_vertex("B")
# my_graph.add_vertex("C")
# my_graph.add_vertex("D")
# my_graph.add_vertex("E")

# my_graph.add_edge("A", "B")
# my_graph.add_edge("A", "C")
# my_graph.add_edge("A", "D")
# my_graph.add_edge("B", "A")
# my_graph.add_edge("B", "E")
# my_graph.add_edge("C", "D")
# my_graph.add_edge("C", "A")
# my_graph.add_edge("D", "A")
# my_graph.add_edge("D", "C")
# my_graph.add_edge("D", "E")
# my_graph.add_edge("E", "B")
# my_graph.add_edge("E", "D")

# print("Original Graph:")
# my_graph.print_graph()
# my_graph.remove_edge("A", "B")
# print()
# print("After Removing Edge A-B:")
# my_graph.print_graph()
# print()
# my_graph.remove_vertex("E")
# print()
# print("After Removing Vertex E:")
# my_graph.print_graph()




        # Static Method
# class Student:
#      #by using class name we can access static method
#     @staticmethod
#     def get_personal_detail(firstname,lastname):
#         print("Your personal detail=",firstname,lastname)
        
#     @staticmethod
#     def contact_detail(mobileNo,rollNo):
#         print("Your contact details=",mobileNo,rollNo)
        
# Student.get_personal_detail(firstname="SEJAL",lastname="Kashyap")
# Student.contact_detail(mobileNo=8767343606,rollNo=32)


#Inheritance
# class College:
#     def college_name(self):
#         print("Modern College")
# class Student(College):
#     def student_info(self):
#         print("Name : Sejal Kashyap")
#         print("Branch: engeneering ")
# obj= Student()
# obj.college_name()
# obj.student_info()



# class College:
#     def college_name(self):
#         print("Modern College")
# class Student(College):
#     def student_info(self):
#         print("Name : Sejal Kashyap")
#         print("Branch: engeneering ")
# class Exam(Student):
#     def subject(self):
#         print("Subject1: Design Engeering")
#         print("Subject2 : Math")
#         print("Subject 3: C-Language ")
# obj=Exam()


# obj.college_name()
# obj.student_info()
# obj.subject()



# class SubjMarks:
#     math = int(input("Enter Paper marks of math: "))
#     DE=int(input("Enter the paper marks of designe engineering: "))
#     c=int(input("Enter the paper marks of C LAnguage : "))
#     english =int(input("Enter the paper marks of english : "))

# class PractMarks:
#     cpract=int(input("Enter practicals marks of C language : "))

# class Result(SubjMarks,PractMarks):

#     def total(self):
#         if self.math >=40 and self.DE>=40 and self.c>=40 and self.english>=40 and self.cpract>=20:
#             print("PAss")
#         else:
#             print("Fail")
# obj=Result()
# obj.total()


#Python only supports Operator Overloading
# '''Suppose child class is not happy with parent class properties then it defines the same property by itself'''
# class Rbi:
#     def homeloan(self):
#         print("Home loan ROI = 8%")

#     def eduloan(self):
#         print("Education loan ROI = 9%")

# class Sbi(Rbi):
#     def eduloan(self):
#         print("Education loan ROI = 10%")

# obj = Sbi()
# obj.eduloan()



# #to access parent class method as well
# class Rbi:
#     def homeloan(self):
#         print("Home loan ROI = 8%")

#     def eduloan(self):
#         print("Education loan ROI = 9%")

# class Sbi(Rbi):
#     def eduloan(self):
#         print("Education loan ROI = 10%")
#         super().eduloan()

# obj = Sbi()
# obj.eduloan()


class Rbi:
    def __init__(self):
        print("Parent class ")
class SBI(Rbi):
    def __init__(self):
        print("child class ")

obj=SBI()