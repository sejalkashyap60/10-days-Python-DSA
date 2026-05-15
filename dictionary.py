# mydict={
#     101:"Sejal",
#      102:"ashish",
#     "103":"mohini",
#     "104":"TRIVANI",
#     101:"aditya",
#      104:"ashish",
        
# }
# print(mydict)

# a=mydict[102]
# print(a) #ashish

#we will replace old value by new value
# mydict[102]="peter"
# print(mydict)

# #only print key x=0,1
# for x in mydict:
#     print(x) #DISPLAY KEYS

# for x in mydict.values():
#     print(x) #DISPLAY VALUES

# for x,y in mydict.items():
#     print(x,y) #DISPLAY VALUES and keys

#adding a new key:value pair
# mydict["mobile_no"]=86745864785
# print(mydict)

# mydict.pop(101)
# print(mydict)

# a={(1,2):1,
#    (2,3):2,
#    (4,5):3}
# print(a[4,5]) //3


# a={'a':1,'b':2,'c':3}
# print(a['a','b']) //key error

# arr={}
# arr[1]=1
# arr['1']=2
# arr[1]+=1
# sum=0
# for k in arr:
#     sum += arr[k]
# print(sum) //4

# my_dict={}
# my_dict[1]=1
# my_dict['1']=2
# my_dict[1.0]=4
# print(my_dict) #{1:4,'1':2}
# sum=0
# for k in my_dict:
#     sum+= my_dict[k]
# print(sum)


# my_dict={}
# my_dict[(1,2,4)]=8
# my_dict[(4,2,1)]=10
# my_dict[(1,2)]=12
# print(my_dict)
# sum=0
# for k in my_dict:
#     sum+= my_dict[k]
# print(sum)
# print(my_dict)


# box={}
# jars={}
# crates={}
# box['biscuits']=1
# box['cakes']=3
# jars['jam']=4
# crates['box']=box
# crates['jars']=jars
# print(len(crates[box]))   #type error


# dict={'c':97,'a':96,'b':98}
# for _ in sorted(dict):
#     print(dict[_]) #output : 96 98 97 

# rec={"Name": "Python","Age":"20"}
# r=rec.copy()
# print(id(r)==id(rec)) #false 
# print(id(r))    #2475040169152
# print(id(rec))  #2475039731328

# rec={"Name": "Python","Age":"20"}
# id1=id(rec)
# del rec
# rec={"Name": "Python","Age":"20"}
# id2=id(rec)
# print(id1==id2) //true

#find the maximum key 
# mydict = {"A":50, "B":30, "C":70}
# if mydict["A"] > mydict["B"] and mydict["A"] > mydict["C"]:
#     print("A is greater")
# elif mydict["B"] > mydict["A"] and mydict["B"] > mydict["C"]:
#     print("B is greater")
# else:
#     print("C is greater")


#count frequency of element in a list Using a Dictionary
# my_list = [1, 2, 2, 3, 4, 1, 2, 3, 5]

# frequency = {}

# for item in my_list:
#     if item in frequency:
#         frequency[item] += 1
#     else:
#         frequency[item] = 1

# print("Element Frequencies:")
# for key, value in frequency.items():
#     print(key, ":", value)

#reverse a number
# num =123456 
# a=num %10
# num =num // 10
# b=num %10
# num =num // 10

# c=num %10
# num =num // 10

# d=num %10
# num =num // 10

# e=num %10
# num =num // 10

# f=num %10
# num =num // 10

# rev=a*100000 +b * 10000+c*1000+d*100+e*10 +f*1
# print(rev)


# Amount=int(input("Please Enter Amount for Withdraw:")) 
# print("100 notes= ",Amount//100)
# print("50 notes= ",(Amount%100)//50)
# print("20 notes= ",((Amount%100)%50)//20)
# print("10 notes= ",(((Amount%100)%50)%20)//10)
# print("5 notes= ",((((Amount%100)%50)%20)%10)//5)



Amount = int(input("Please Enter Amount for Withdraw: "))
print("100 notes = ", Amount // 100)
print("50 notes = ", (Amount % 100) // 50)
print("20 notes = ", ((Amount % 100) % 50) // 20)
print("10 notes = ", (((Amount % 100) % 50) % 20) // 10)
print("5 notes = ", ((((Amount % 100) % 50) % 20) % 10) // 5)

# Adding 2 rupee and 1 rupee coins
print("2 rupee coins = ", (((((Amount % 100) % 50) % 20) % 10) % 5) // 2)
print("1 rupee coins = ", (((((Amount % 100) % 50) % 20) % 10) % 5) % 2)
