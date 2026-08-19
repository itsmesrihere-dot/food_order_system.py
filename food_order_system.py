print("=============================\n      FOOD ORDER SYSTEM\n ==============================\n")
print("2.place order\n3.view cart\n4.remove item\n5.generate bill\n6.exit\n")
print("================\n     MENU \n================\n")
print ("1.burger🍔   ₹120\n2.pizza🍕   ₹200\n3.sandwich🥪   ₹80\n4.pasta🍝   ₹150\n5.frenchfries🍟  ₹100\n6.coke🥤   ₹50\n7.exit")
cart=[]
choice = 0
while choice !=7:
    choice = int(input("enter your choice:"))
    if choice ==2:
        food_choice=int(input("enter the food number:"))
        quantity=int(input("enter quantity:"))
        if food_choice==1:
            cart.append(("burger", quantity))
            print("burger added to your cart")
        elif food_choice==2:
            cart.append(("pizza" , quantity))
            print("pizza added to your cart")
        elif food_choice==3:
            cart.append(("sandwich", quantity))
            print("sandwich added you cart")
        elif food_choice==4:
            cart.append(("pasta",quantity))
            print("pasta added to your cart ")
        elif food_choice==5:
            cart.append(("french fries", quantity))
            print("french fries added to your cart sucessfully")
        else:
            cart.append(("coke", quantity))
            print("coke added to your cart")
    elif choice ==3:
        print("================= YOUR CART =============")
        if len(cart)==0:
          print("your cart is empty")
        else:
         for item in cart:
            print(item[0], "x", item[1])
    elif choice == 4:
      food_number = int(input("Enter the food number to remove: "))

      if food_number == 1:
        food_name = "burger"

      elif food_number == 2:
        food_name = "pizza"

      elif food_number == 3:
        food_name = "sandwich"

      elif food_number == 4:
        food_name = "pasta"

      elif food_number == 5:
        food_name = "french fries"

      elif food_number == 6:
        food_name = "coke"

      else:
        print("Invalid food number")
    elif choice == 5:
     total = 0
     for item in cart:
        if item[0] == "burger":
            price = 120
        elif item[0] == "pizza":
            price = 200
        elif item[0] == "sandwich":
            price = 80
        elif item[0] == "pasta":
            price = 150
        elif item[0] == "french fries":
            price = 100
        elif item[0] == "coke":
            price = 50
        item_total = price * item[1]
        total = total + item_total
        print(item[0], "x", item[1], "=", item_total)
     print("-------------------------")
     print("Total: ₹", total)
       
    else:
       print("thank you ☺️")


