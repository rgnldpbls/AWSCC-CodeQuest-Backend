isTrue = True
shopping_list = []
while isTrue == True:
    print("Options:")
    print("1. Add item to the shopping list")
    print("2. View shopping list")
    print("3. Remove item from the shopping list")
    print("4. Quit")

    ip = int(input("Enter the number of your choice: "))
    if ip == 1:
        add_List = input("Enter the item you want to add: ")
        shopping_list.append(add_List)
        print(f"{add_List} has been added to your shopping list.\n")
    elif ip == 2:
        print("Your shopping List: ")
        for i in range(len(shopping_list)):
            print(f"{shopping_list[i]}")
        print("\n")
    elif ip == 3:
        remove_List = input("Enter the item you want to remove: ")
        shopping_list.remove(remove_List)
        print(f"{remove_List} has been removed from your shopping list.\n")
    elif ip == 4:
        print("Goodbye!")
        isTrue = False
    else:
        print("Invalid input")