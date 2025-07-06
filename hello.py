
n=input(("Enter the numbers:")).strip()
t=1
if n.isdigit():
    for i in n:
     t=t*int(i)
    print(f"The product is {t}")
else:
   print("Please enter only digits")
