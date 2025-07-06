
n=input(("Enter the numbers:")).strip()
t=1
if n.isdigit():
    for i in n:
     t=t*int(i)
    print(f"The product is {t}")
else:
   print("Please enter only digits")


n=input("enter the number only:").strip()
t=0
if n.isdigit():
    for i in n:
        t=t+int(i)
    print(f"The sum is {t}")
else:
    print("u entered wrong numbers")
