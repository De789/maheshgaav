
# n=input(("Enter the numbers:")).strip()
# t=1
# if n.isdigit():
#     for i in n:
#      t=t*int(i)
#     print(f"The product is {t}")
# else:
#    print("Please enter only digits")


# n=input("enter the number only:").strip()
# t=0
# if n.isdigit():
#     for i in n:
#         t=t+int(i)
#     print(f"The sum is {t}")
# else:
#     print("u entered wrong numbers")

# class Dog():
#     legs="five"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def info(self):
#         print(f"This dog has {self.legs} legs name is {self.name} and age is {self.age}")
# class Animal(Dog):
#     def __init__(self,name,age,price):
#         self.price=price
#         super().__init__(name, age)
#     def price_animal(self):
#         print(f"Thye price is {self.price} and This dog has {self.legs} legs name is {self.name} and age is {self.age} ")
# x = Animal("sam", 25, 78)
# x.info()
# print(Animal.legs)
# Animal.legs="ten"
# print(Animal.legs)


x=[[1,2,3,4],[8],[4,5]]
# sum=0
# for i in x:
#     for j in i:
#         sum+=j
# print(sum)

# t=0
# for sublist in x:
#    t+=sum(sublist)
#    print(t)

# find only sum 
# s=0
# for i in x:
#     for j in i:
#         if j%2==0:
#             print(j)



 
# result=sum(num for sublist in x for num in sublist)
# print(result)

 
# def reverse_str(str:str):
#     if len(str)==0:
#         return ""
#     else:
#         return reverse_str(str[1:])+str[0]

# print(reverse_str("Shrikant"))
# s=input("Enter the string: ")
# reversed_str = ""
# for char in s:
#     reversed_str  = char +reversed_str 
# print(reversed_str)


# by using functools:
# from functools import reduce
# name="sachin"
# reverse_name=reduce(lambda x,y:y+x,name)
# print(reverse_name)



