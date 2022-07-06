"""Lab Objective: Understand how to use loops to determine code flow."""

money = 50
shopping_cart = []
fruits = {"Apple": 5, "Raspberry": 10, "Lemon": 20}

while True:
    if money <= 0:
        print("Thanks for shopping!")
        break
    else:
        player_choice = input(f"Select a fruit {fruits}: ").title()
        if player_choice in fruits:
            if money >= fruits[player_choice]:
                shopping_cart.append(player_choice)
                money -= fruits[player_choice]
                print(f"Shopping cart: {shopping_cart} \nMoney left: {money}")
            else:
                print("You don't have enough money to make this purchase.")
        else:
            print("Invalid choice.")

input("\nPress 'Enter' to exit the program")# prevents program from closing upon execution
