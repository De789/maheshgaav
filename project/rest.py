menu={
    "Pasta":100,
    "Pohe":20,
    "Pulaav":75,
    "VadaaPaav":25
}

print("The items in our hotel are:\n ")
for item,price in menu.items():
    print(f"{item}:{price}")

order_total=0
item_1=input("Enter the name of item please:")
if item_1 in menu:
    order_total+=menu[item_1]
    print(f"Ur order for {item_1} has been added do u want anything else:")
else:
    print("ur ordered item is not available ,sorry")

more=input("Do you more sir : (yes/no)").strip()
if more=="yes":
    item_2 = input("Please enter the next item name: ").strip()
    if item_2 in menu:
       order_total+=menu[item_2]
    print(f"Ur order for {item_2} has been added ")
else:
    print("ur ordered item is not available ,sorry")

print(f"Your total order cost is {order_total}")
print("Thank you,please visit again")

