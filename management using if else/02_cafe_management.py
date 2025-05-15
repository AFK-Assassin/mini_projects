# first i need to take a data type and function approriate for the project
# dictionary and conditionals statements used in this 

menu = {'coffee': 80,
        'latte' : 100,
        'tea': 50,
        'burger':110,
        'pizza':120,
        'sandwhich':90

}

# greet the customer
print ("welcome to btech panwari")
print("coffee 80\nlatte 100\ntea 50\nburger 110\npizza 120\nsandwhich 90")

order_total = 0

item_1= input(f"enter item from  you want to order = ")
if item_1 in menu :
    order_total += menu[item_1]
    print (item_1)
else:
    print(f"{item_1} is not available yet")

another_order = input(f"do you like to add another item? (Yes/No) " , )
if another_order == "yes":

    item_2 = input("enter the item you want to order : ")
    if item_2 in menu :
        order_total += menu[item_2]
        print(item_2)
    else :
        print("thank you")


print(f"your final bill is : inr {order_total}")


