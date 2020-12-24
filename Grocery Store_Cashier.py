# grocery shopping cashier program

# Atia Najafi: atia.nadjafi@usask.ca, December 24 2020.
# tnq from PyGorm and useful tutorial video https://www.youtube.com/watch?v=gFURWvmUbSU, for cashier store
# my contribution to this code is to add the payment method and payment options

inventory = {"milk": 5, "bread": 2, "cola": 3, "pharmacy": 7}

basket = []
total = []

# if you like to add more rewards card, you have to create an inventory for phone number, address and name
# this function do not need any variable
def cashier():
    user_answer = input("Hello sir/madam! What do you need to purchase today?").lower()
    while user_answer != "quit":
        if user_answer in inventory:
            basket.append(user_answer)
            user_answer = input("perfect! you add that to your basket, anything else you wish to purchase?" 
                                "Type 'quit' to end").lower()
        else:
            user_answer = input("Sorry! we are run out of that item in our store! anything else you want?"
                                "type 'quit to end").lower()
# now we can call our cashier function
cashier()

print("Here is all of the items in your shopping cart", basket)

answer = input("do you wish to add anything else? Type yes/no").lower()

if answer == "yes":
    cashier()
    print("Here is all the items that you ordered", basket)
    for items in basket:
        total.append(inventory[items])
    amount_to_pay = sum(total)
else:
    for items in basket:
        total.append(inventory[items])
    amount_to_pay = sum(total)

print("your total is ", amount_to_pay)
print("how would like to pay?"
      "cash or debit or credit")
payment_method = input("for cash press 1"
                       "for credit or debit press 2")
if payment_method == 1:
    print("please scan your cash")
elif payment_method == 2:
    print("please insert or swipe your cart")

print()
customer_answer = input("do you need a copy of your receive?").lower()
if customer_answer == "yes":
    print("please take your receive, and have a great day")
elif customer_answer == "no":
    print("Thank you for shopping with us and have a great day")



