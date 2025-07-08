# def longest_word(word:str):
#     words=word.split()
#     return min(words,key=len)
# print(longest_word("Mahesh anant patil is a good "))


# l=[10,20]
# l.extend([2,3,4,1])
# l.append([12,32])
# print(l)

# l.insert(0,"Mahesh")
# print(l)

def hello(*args):
    return sum(args)

hello(1,2,3,4)
print(hello(1,2,3,4))

def apply(func,x):
    return func(x)

result=apply(lambda x:x*2,4)
print(result)


def args(**a):
    for item,price in a.items():
        print(f"{item}:{price}")
res=args(item="book",price=100)
print(res)