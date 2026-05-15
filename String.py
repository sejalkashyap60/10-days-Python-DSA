# name ="SejalKashyap"
#        #012345678910
# print(name[0])
# print(name[1])
# print(name[-1])
# #print(name[15])
# print(name[0:5])
# print(name[1:])
# print(name[:5])
# print(name[:])
# print(name[1:8:2])
# print(name[::-1])


# s="Python are High level programming Language"
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())


#Format function
# name="Sejal"
# sal=43545
# age=21
# print("{}sal is {} age is{}".format(name,sal,age))
# print("{0}sal is {1} age is{2}".format(name,sal,age))
# print("{x}sal is {y} age is{z}".format(x=name,y=sal,z=age))
# A=1
# print(f"{A} is a good boy")

#wap to remove duplicate character
# name="SejalKashyap"
# newname=""
# for i in name:
#    if i not in newname:
#       newname += i
# print(newname)


#print(name[::-1])

#reverse a String
# name="sejalkashyap"
# newname=""
# N=len(name)
# for i in range(N-1,-1,-1):
#     newname += name[i]

# print(newname)

#check Whether the String is Palindrone or not 

# name="racecar"
# newname=""
# N=len(name)

# for i in range(N-1,-1,-1):
#     newname += name[i]
# if newname == name:
#         print("Its is palindrone")
# else:
#         print("not a palindrone ")
# print(newname)

#check number of vowels ans consonant
# vowels=['a','e','i','o','u']
# input="hello"
# vow=0
# cons=0
# for  i in  input:
#     if i in vowels:
#         vow += 1
#     else:
#         cons +=1

# print("vowels: ",vow)
# print("Consonants: ",cons)

# Anagram Program
# input1 = "silent"
# input2 = "listen"
# # Convert both strings to lowercase and sort them
# if sorted(input1.lower()) == sorted(input2.lower()):
#     print("Strings are Anagrams")
# else:
#     print("Strings are Not Anagrams")



# Count words in a string
# String = "i am Sejal Kashyap"
# count = 0
# for i in String:
#     if i == " ":
#         count += 1
# # Number of words = spaces + 1
# if len(String) > 0:
#     count += 1
# print("Number of words =", count)


# Count special symbols in a string
# input_string = "gasgg54@#vscsd!s"
# count = 0
# for i in input_string:
#     z = ord(i)

#     # ASCII ranges for special symbols
#     if (32 <= z <= 47) or (58 <= z <= 64) or (91 <= z <= 96) or (123 <= z <= 126):
#         count += 1
# print("Special symbols count =", count)


# #title case
# input="this is a test"
# print(input.title())



# print('SejalKashyap2130'.isalnum()) #true
# print('SejalKashyap'.isalpha()) #true
# print('777f'.isdigit()) 
# print('SejalKashyap'.islower()) 
# print(''.islower()) 
# print('SEJALKASHYAP'.isupper())
# print('My name Is Sejal'.istitle())
# print(''.istitle())
# print(''.isspace())
# print('Hello'.startswith("He"))
# print('HEllo'.endswith("lo"))
# print("SejalKashyap".find("z"))
# print("Sejal".index("l"))
# print("Sejal".count("a"))


# 111
# 222
# 333
#nested loop
# for i in range(1,4): #rows
#     for j in range(1,4): #inner cols
#         print(i,end = " ")
#     print()

# n=int(input("enter rows"))
# for i in range(1,n+1): #rows
#     for j in range(1,n+1): #inner cols
#         print(chr(64+i),end = " ")
#     print()

# n=int(input("enter rows : "))
# for i in range(1,n+1): #rows
#     for j in range(1,1+i): #inner cols
#         print("*",end = " ")
#     print()

# n=int(input("enter rows : "))
# for i in range(1,n+1): #rows
#     for j in range(1,n+2-i): #inner cols
#         print(chr(64+j),end = " ")
#     print()


# import time
# n=int(input("Enter number of rows:"))
# for i in range(1,n+1):
#     print(" "*(n-1),end="")
#     for j in range(1, i+1):
#         time.sleep(1)
#         print("*",end=" ")
#     print()

input=[]
output=0
for i in range(0,4):
    for j in range(4,-1,-1):
        output=i*j