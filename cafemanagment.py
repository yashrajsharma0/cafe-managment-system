print("welcome to our cafe sir/man ")

menu = {
    "pizza" : 200,
    "burger" : 150,
    "fries" : 100,
    "coke" : 50,
    "tea" : 30,
    "coffee" : 40,
    "juice" : 60,
    "sandwich" : 120,
    "chips" : 100,
    "salad" : 150,
    "cake" : 200,
    "icecream" : 100,
    "juice" : 60,
    "tea" : 30,
    "coffee" : 40,
}
print(menu)

total_order = 0

order_1 = input("what would you like to order sir? = ")


while order_1 in menu :
    print(f"your order {order_1} has been added ")
    total_order = total_order + menu[order_1]
    order = input("anything else you want to order sir?(yes/no) =")
    if "yes" in order:
        order_1 = input("what would you like to order sir? = ")
    if order_1 in menu:
            total_order = total_order + menu[order_1]
    if "no" in order:
        print(f"your total order is {total_order}")
        print("thanks for coming to our cafe sir/mam")
        break
   


 
