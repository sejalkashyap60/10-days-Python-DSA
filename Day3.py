#occurence of ab count Program 1
# input_str = "abababab"
# count = 0
# for i in range(len(input_str) - 1):
#     if input_str[i:i+2] == "ab":
#         count += 1
# print(count)

#while loop
# i=1
# while i<=5:
#     print(i)
#     i+=1

#function  Program 2
# def hello():
#     print("helloooooo guysss")

# hello()
# hello()

#defining function Program 3
# def arithemetic():
#     a=int(input("Enter value of a:"))
#     b=int(input("Enter value of b:"))
#     sum=a+b
#     sub=a-b
#     div=a/b
#     mul=a*b
#     return sum,sub,div,mul #return in tuple 
# result=arithemetic()
# print("Arithemetic:",result) 


#how many types of argument in function
#positional argument,keyword argument, default argument, variable length argument/variable number arguments
# def arithemetic(a,b):

#     sum=a+b
#     sub=a-b
#     div=a/b
#     mul=a*b
#     return sum,sub,div,mul #return in tuple 
# #positional arguments
# result=arithemetic(10,2)
# print("Arithemetic:",result) 

#keyword arguments
# def credential(Username,password):
#     if Username==password:
#         print("login succesfully")
#     else:
#         print("Invalid Credentials")
# credential(Username="admin",password="admin") #calling function

#default arguments
# def cityName(city="Pune"):#default arguments
#     print(city)
# cityName("nagpur")
# cityName("mumbai")
# cityName()


#variable length  or variabkle number of agrument
# def cityName(*name):
#     print(name)

# cityName("Nag","delhi","Mumbai","pune")


#modularity approach in function
import sys
def add():
    a=int(input("Enter the value of A:"))
    b=int(input("Enter the value of B:"))
    print("Result:",a+b)
def sub():
    a=int(input("Enter the value of A:"))
    b=int(input("Enter the value of B:"))
    print("Result: ",a-b)
def mul():
    a=int(input("Enter the value of A:"))
    b=int(input("Enter the value of B:"))
    print("Result: ",a*b)
def div():
    a=int(input("Enter the value of A:"))
    b=int(input("Enter the value of B:"))
    print("REsult:", a/b)

while True:
    print("1.Addition")
    print("2.Subtraction")
    print("3. Multiplication ")
    print("4. Division ")
    print("5.Exit")
    choice=int(input("Enter your choice: "))
    if choice ==1:
        add()#calling add
    elif choice==2:
        sub()  
    elif choice==3:
        mul()   
    elif choice==4:
        div()   
    elif choice ==5:
        sys.exit()        

