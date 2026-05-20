# Find the first Non-Repeating Character:



# ****************RECURSION****************8

# def factorial(num):
#     if num<=1:
#         return 1
#     return num*factorial(num-1)
# print(factorial(4))

#4*factorial(3)
#3*factorial(2)
#2*factorial(1)
# 4*3*2*1=24



# def capitalizeFirst(arr):
#     result=[]
#     if len(arr)==0:
#         return result
#     result.append(arr[0][0].upper()+arr[0][1:]) # T+aco=Taco
#     return result + capitalizeFirst(arr[1:])
# print(capitalizeFirst(['car','taco','banana']))
# #output : ['Car', 'Taco', 'Banana']


# def power(base,exponent):
#     if exponent == 0:
#         return 1
#     return base*power(base,exponent-1)

# print(power(2,0))
# print(power(2,2))
# print(power(2,4))
#output:
# 1
# 4
# 16


# def productOfArray(arr):#1,2,3
#     if len(arr)==0:
#         return 1
#     return arr[0]*productOfArray(arr[1:])
#             # 1*2*3*1
# print(productOfArray([1,2,3]))
# print(productOfArray([1,2,3,10]))


#reverse a string using recurssion

# def reverse(string): #python
#     if len(string) <= 1: #6>=1
#      return string
#     return string[len(string)-1]+reverse(string[0:len(string)-1])
#         #n                          #0:4
# print(reverse('python'))
# print(reverse('appmilalers'))


# def recursiveRange(num):
#     if num <=0:
#         return 0
#     return num + recursiveRange(num - 1)
# print(recursiveRange(6))#654321


# def isPalindrome(string): #awesome 
#     if len(string) == 0: #6==0
#         return True
#     if string[0] != string[len(string)-1]:
#         return False
#     return isPalindrome(string[1:-1])
# print(isPalindrome('lalal'))
# # print(isPalindrome('tacocat'))



#someRecursive Solution
# def someRecursive(arr, cb):
#     if len(arr) == 0:
#         return False
    
#     if not(cb(arr[0])):
#         return someRecursive(arr[1:], cb)
    
#     return True


# def isOdd(num):
#     if num % 2 == 0:
#         return False
#     else:
#         return True


# print(someRecursive([1,2,3,4], isOdd))
# print(someRecursive([4,6,8,9], isOdd))
# print(someRecursive([4,6,8], isOdd))




# input 7 9 8 6 8 10
# output 19
# n = int(input())

# arr = list(map(int, input().split()))

# max_product = arr[0] * arr[1]
# ans_sum = arr[0] + arr[1]

# for i in range(n):
#     for j in range(i + 1, n):
#         product = arr[i] * arr[j]

#         if product > max_product:
#             max_product = product
#             ans_sum = arr[i] + arr[j]

# print(ans_sum)



# class Tree:
#     def __init__(self,data):
#         self.data=data #data("Drinks")("Hot")
#         self.child=[]

#     def __str__(self,level=0):
#         ret=" "*level+str(self.data)+"\n"
#         for ch in self.child:
#             ret+=ch.__str__(level+1)
#         return ret
#     def addChild(self,object):
#         self.child.append(object)
#         print("Tree node added")
# rootNode = Tree("Drinks")
# Hot      =Tree("Hot")
# Cold     =Tree("Cold")
# Tea      =Tree("Tea")
# Coffee   =Tree("Coffee")
# NonAlcoholic  =Tree("NonAlcoholi")
# Alcoholic     =Tree("Alcoholic")

# rootNode.addChild(Hot)
# rootNode.addChild(Cold)
# Hot.addChild(Tea)
# Hot.addChild(Coffee)
# Cold.addChild(NonAlcoholic)
# Cold.addChild(Alcoholic)

# print(rootNode)




class Tree:
    def __init__(self,data):
        self.data=data #data("Drinks")("Hot")
        self.child=[]

    def __str__(self,level=0):
        ret=" "*level+str(self.data)+"\n"
        for ch in self.child:
            ret+=ch.__str__(level+1)
        return ret
    def addChild(self,object):
        self.child.append(object)
        print("Tree node added")
N1= Tree("N1")
N2      =Tree("N2")
N3     =Tree("N3")
N4     =Tree("N4")
N5      =Tree("N5")
N6      =Tree("N6")
N7     =Tree("N7")
N8      =Tree("N8")


N1.addChild(N2)
N1.addChild(N3)
N2.addChild(N4)
N2.addChild(N5)
N3.addChild(N6)
N4.addChild(N7)
N4.addChild(N8)

print(N1)
