#Define the menu

menu = {
    'Pizza':40,
    'Pasta':50,
    'Burger':70,
    'Salad':10,
    'Coffee':5
}

#Greet
print("Welcome to Shreya restro")
print("Pizza: Rs40\n Pasta : Rs50 \n Burger : Rs70\n Salad : Rs10\n Coffee : Rs5")


order_total = 0

item_1 = input("Enter the name of item you wan to order = ")

if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} is not available yet!")

while(True):
    another_order = input("Do You want to add another item ? (Yes/NO) ")

    if another_order == "Yes":
        item_2 =input("Enter the name of next item = ")
        if item_2 in menu:
            order_total += menu[item_2]
            print(f"Item {item_2} has been added to order")
        else:
             print(f"Ordered item {item_2} is not available!")
    else:
        break

print(f"the total amount of items to pay is {order_total}")