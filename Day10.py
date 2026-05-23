# import re
# count=0
# pattern= re.compile("function")

# matcher=pattern.finditer(" A function in python  is defined by function  a def statement.python the gerneral syntax looks like this: def function body.The parameter python list consists of none or more parameters. ")
# for i in matcher:
#     count+=1
#     print(i.start(),".....",i.end(),"......",i.group())
# print("The number of occurence : ",count)




# import re
# count=0
# matcher=re.finditer("Hi","HiHiHiHi")

# for i in matcher:
#     count+=1
#     print(i.start(),".....",i.end(),"......",i.group())
# print("The number of occurence : ",count)

# import re
# obj = input("enter any character ")
# objmatch=re.finditer(obj,"a7b @k9z")
# # print(objmatch)
# for match in objmatch:
   
#     print(match.start(),".....",match.end(),"......",match.group())


# import re
# a=input("enter string to perform match operation : ")
# mtch=re.match(a,"Python is very important language ")
# print(mtch)
# if mtch != None:
#     print("Match found at beginning level ")
#     print(mtch.start()," ",mtch.end())
# else:
#     print("There is no matching at beginning level")


#matches full and return 
# import re
# a=input("enter string to perform match operation : ")
# mtch=re.match(a,"pythonisvery ")
# print(mtch)
# if mtch != None:
#     print("Match found  ")
#     print(mtch.start()," ",mtch.end())
# else:
#     print("Full match not found ")


#valid email id or not 
# import re
# s=input("enter Email id  : ")
# m=re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com",s)

# if m != None:
#     print("valid email  ")
   
# else:
#     print(" Invalid Email ")






#WAp to check mobile number
# import re
# mo =input("Enter mobile number")
# obj = re.fullmatch("[6-9]\d{9}",mo)
# if obj!=None:
#     print("valid mobile number ")
# else:
#     print("Invalid mobile number ")



# import re
# a =input("Enter String to perform match  operation : ")
# mtch = re.search(a,"python sss dynamic lann ")
# print(mtch)
# if mtch!=None:
#     print(mtch.start()," ",mtch.end()," ",mtch.group())
# else:
#     print("there is no matching anywhere")




# import re
# mtch=re.findall('0-9',"abch3vhv475vv78596hbhjvjv")
# print(mtch)




# import re
# obj=re.sub('[a-z]','*','2345 ABCD habc deff ')
# print (obj)




# import re
# obj = re.subn('[0-7]','@','ab3gd6nk17')
# print(obj)
# print("the string is = ",obj[0])
# print("the number pf replacement is =",obj[1])



# finding word from file

# import re
# f = open("file1.txt", "r")
# data = f.read()
# f.close()

# word = input("Enter string to search: ")

# match = re.search(word, data)

# if match:
#     print("Match found")
#     print("Start Index:", match.start())
#     print("End Index:", match.end())
# else:
#     print("Match not found")

# import os, sys
# fname = input("Enter file name: ")
# if os.path.isfile(fname):
#     print("File exists: ", fname)
#     f = open(fname, "r")
# else:
#     print("file does not exists: ",fname)
#     sys.exit(0)
# lcount = wcount = ccount = 0
# for line in f:
#     lcount = lcount+1
#     ccount = ccount+len(line)
#     words = line.split()
#     wcount= wcount+ len(words)
# print("The number of line: ", lcount)
# print("The number of words: ",wcount)
# print("The number of characters: ",ccount)





# class Graph:
#     def __init__(self,vertices):
#         self.v = vertices

#         self.matrix=[[0 for _ in range(vertices)]
#                       for _ in range(vertices)]
    
#     def display(self):
#         for row in self.matrix:
#             print(row)
    
#     def add_edge(self, u,v):
#         self.matrix[u][v]=1
#         self.matrix[v][u]=1

#     def remove_edge(self, u,v):
#         self.matrix[u][v]=0
#         self.matrix[v][u]=0

        

# g=Graph(4)


# g.add_edge(0,1)
# g.add_edge(1,0)
# g.add_edge(0,2)
# g.add_edge(2,0)
# g.add_edge(1,3)
# g.add_edge(3,1)
# g.add_edge(2,3)
# g.add_edge(3,2)

# print("Adjacency Matrix")
# g.display()




class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):   # colon added here
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)
        self.table[index].append(key)

    def display(self):
        print(self.table)



ht = HashTable(5)

ht.insert(10)
ht.insert(15)
ht.insert(7)
ht.insert(22)

ht.display()