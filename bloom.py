import datetime

ordered_item_code = []
order_summary = []
menus = {}
code_list = []
total = 0
detail = {}
order_code = []

current_menu = None

with open('product.txt', 'r') as file: 
    for line in file:
        line = line.strip()
        if not line:
            continue
        
        if line.startswith("menu"):
            current_menu = line.split()[1]
            menus[current_menu] = []
        else:
            parts = line.split(',') # split every product to 6 part
            if len(parts) == 6: # make sure very product got 6 part
                menus[current_menu].append({
                    'code': parts[0],
                    'name': parts[1],
                    'category': parts[2],
                    'price': parts[3],
                    'rate': parts[4],
                    'status': parts[5]
                })

def max_len(name):
    lens = 0
    for menu_name, items in menus.items():
        for menu in menu_name:
            for item in items:
                if len(item[name]) > lens:
                    lens = len(item[name])
                else:
                    continue
    return lens

def title():
    print(f"|" + "-" * (max_len('code') + 2) + "|" + "-" * (max_len('name') + 2) + "|" + "-" * (max_len('category') + 2) + "|" + "-" * 9 + "|" + "-" * 7 + "|" + "-" * (max_len('status') + 2) + "|")
    print(f"|" + "Code".center(max_len('code') + 2) + "|" + "Name".center(max_len('name') + 2) + "|" + "Category".center(max_len('category') + 2) + "|" + "Price".center(9) + "|" + "Rate".center(7) + "|" + "Status".center(max_len('status') + 2) + "|")
    print(f"|" + "-" * (max_len('code') + 2) + "|" + "-" * (max_len('name') + 2) + "|" + "-" * (max_len('category') + 2) + "|" + "-" * 9 + "|" + "-" * 7 + "|" + "-" * (max_len('status') + 2) + "|")

def titles(a): 
    print("|" + f"-" * (max_len('code') + max_len('name') + max_len('category') + max_len('status') + 29) + "|")
    print("|" + f"Menu{a}".center((max_len('code') + max_len('name') + max_len('category') + max_len('status') + 29)) + "|")
    print("|" + f"-" * (max_len('code') + max_len('name') + max_len('category') + max_len('status') + 29) + "|")

def option1():
    while True:
        option1 = input("Please select a category number: ")
        if option1 not in ["1", "2", "3", "4", "5", "6", "7"]:
            print("Please select a category number: ")
        elif option1 == "1":
            print()
            category("Romantic")
            print("\n1) Order item")
            print("2) Back to filter category")
            print("3) Back to main menu")
            option2()                     
            return
        elif option1 == "2":
            print()
            category("Birthday")
            print("\n1) Order item")
            print("2) Back to filter category")
            print("3) Back to main menu")
            option2()
            return
        elif option1 == "3":
            print()
            category("Grand Openning")
            print("\n1) Order item")
            print("2) Back to filter category")
            print("3) Back to main menu")
            option2()
            return
        elif option1 == "4":
            print()
            category("Condolence")
            print("\n1) Order item")
            print("2) Back to filter category")
            print("3) Back to main menu")
            option2()
            return
        elif option1 == "5":
            print()
            category("Anniversary")
            print("\n1) Order item")
            print("2) Back to filter category")
            print("3) Back to main menu")
            option2()
            return
        elif option1 == "6":
            back_to_menu("4")
            return
        else: 
            back_to_menu("1")
            return

def option2():
    while True:
        option2 = input("Please select a number: ")
        if option2 not in ["1", "2", "3"]:
            print("Please select a number 1 or 2 or 3.")
        elif option2 == "1":
            order_item("2")
            return
        elif option2 == "2":
            back_to_menu("5")
            return
        elif option2 == "3":
            back_to_menu("1")
            return

def item_code_list(a): # to print out available item in a
    global code_list
    titles(a)
    title()
    code_list = [] # to empty the code_list
    for menu_name, items in menus.items():
        if menu_name == a:
            for item in items:
                if item["status"] == "Available":
                    code_list.append(item["code"]) # to add available item code into code_list
                    print("|" + f"{item['code']}".center(max_len('code') + 2) + "|" + f"{item['name']}".center(max_len('name') + 2) + "|" + f"{item['category']}".center(max_len('category') + 2) + "|" + f"{item['price']}".center(9) + "|" + f"{item['rate']}".center(7) + "|" + f"{item['status']}".center(max_len('status') + 2) + "|")
    print()

def price_sort(a): # a is to decide the price amount sort from big to small or small to big
    print()
    if a == "1":
        a = False
    elif a == "2":
        a = True
    for menu_name, items in menus.items():
        titles(menu_name)
        title()
        sorted_items = sorted(items, key=lambda x: int(x["price"]), reverse = a)
        for item in sorted_items:
            print("|" + f"{item['code']}".center(max_len('code') + 2) + "|" + f"{item['name']}".center(max_len('name') + 2) + "|" + f"{item['category']}".center(max_len('category') + 2) + "|" + f"{item['price']}".center(9) + "|" + f"{item['rate']}".center(7) + "|" + f"{item['status']}".center(max_len('status') + 2) + "|")
    print()

def rate_sort(a): # a is to decide the price amount sort from big to small or small to big
    print()
    if a == "1":
        a = False
    elif a == "2":
        a = True
    for menu_name, items in menus.items():
        titles(menu_name)
        title()
        sorted_items = sorted(items, key=lambda x: int(x["rate"]), reverse = a)
        for item in sorted_items:
            print("|" + f"{item['code']}".center(max_len('code') + 2) + "|" + f"{item['name']}".center(max_len('name') + 2) + "|" + f"{item['category']}".center(max_len('category') + 2) + "|" + f"{item['price']}".center(9) + "|" + f"{item['rate']}".center(7) + "|" + f"{item['status']}".center(max_len('status') + 2) + "|")
    print()

def category(a): # a is to decide the which category
    title()
    for menu_name, items in menus.items():
        for item in items:
            if item["category"] == a:
                print("|" + f"{item['code']}".center(max_len('code') + 2) + "|" + f"{item['name']}".center(max_len('name') + 2) + "|" + f"{item['category']}".center(max_len('category') + 2) + "|" + f"{item['price']}".center(9) + "|" + f"{item['rate']}".center(7) + "|" + f"{item['status']}".center(max_len('status') + 2) + "|")
    print()

def print_out_menu(a):
    for menu_name, items in menus.items():
        if menu_name == a:
            titles(a)
            title()
            for item in items:
                print("|" + f"{item['code']}".center(max_len('code') + 2) + "|" + f"{item['name']}".center(max_len('name') + 2) + "|" + f"{item['category']}".center(max_len('category') + 2) + "|" + f"{item['price']}".center(9) + "|" + f"{item['rate']}".center(7) + "|" + f"{item['status']}".center(max_len('status') + 2) + "|")
    

def print_w_menu(a): # use "w" to rewrite the menu in product.txt 
    for menu_name, items in menus.items():
        if menu_name == a:
            with open("product.txt", "w") as file:
                file.write(f"menu {a}\n")
            for item in items:
                with open("product.txt", "a") as file:
                    file.write(f"{item["code"]},{item["name"]},{item["category"]},{item["price"]},{item['rate']},{item["status"]}\n")

def print_a_menu(a): # use "a" to add the menu in product.txt
    for menu_name, items in menus.items():
        if menu_name == a:
            with open("product.txt", "a") as file:
                file.write(f"menu {a}\n")
            for item in items:
                with open("product.txt", "a") as file:
                    file.write(f"{item["code"]},{item["name"]},{item["category"]},{item["price"]},{item['rate']},{item["status"]}\n")

def inventory_management():
    print("\nPlease select features.") # put menu or anything else will better ? ? ?
    print("1) View/update blooms")
    print("2) Add new blooms")
    print("3) View/update add on")
    print("4) Add new add on")
    print("5) Edit rating")
    print("6) Back to previous page")
    while True:
        option = input("Please enter a number: ")
        if option not in ["1", "2", "3", "4", "5", "6"]: 
            print("Please enter 1 or 2 or 3 or 4 or 5 or 6.")
        elif option == "1":
            view_update_blooms()
            return
        elif option == "2":
            add_new_blooms()
            return
        elif option == "3":
            view_update_addon()
            return
        elif option == "4":
            add_new_addon()
            return
        elif option == "5":
            update_rate()
            return
        else: 
            back_to_menu("1")
            return

def update_rate():
    global menus
    
    while True:
        update_code = input("\nPlease enter the item code that you want to update or enter 0 to go back: ").upper()
        
        found = False
        for menu_name, items in menus.items():
            for item in items:
                if update_code == "0":
                    back_to_menu("2")
                    found = True
                    return
                elif update_code == item['code']:
                    found = True
                    print(f"{item["code"]}\t{item['name']}\t{item['category']}\t{item['price']}\t  {item['rate']}\t{item['status']}")
                    
                    while True:
                        new_info = input("Enter new (code,name,category,price,rate,status): ").title().split(',')
                        if len(new_info) == 6:
                            item['code'] = new_info[0]
                            item['name'] = new_info[1]
                            item['category'] = new_info[2]
                            item['price'] = new_info[3]
                            item['rate'] = new_info[4]
                            item['status'] = new_info[5]
                            
                            print_w_menu("A")
                            print_a_menu("B")
                            print("Update successful!\n")
                            print_out_menu("A")
                            print_out_menu("B")
                            print()
                            back_to_menu("1")
                            return
                        else:
                            continue

        if found:
            break
        else:
            print("Invalid item code, please enter a valid item code.")

def view_update_blooms():
    global menus
    
    while True:
        update_code = input("\nPlease enter the item code that you want to update or enter 0 to go back: ").upper()
        
        found = False
        for menu_name, items in menus.items():
            if menu_name == "A":
                for item in items:
                    if update_code == "0":
                        back_to_menu("2")
                        found = True
                        return
                    elif update_code == item['code']:
                        found = True
                        print(f"{item["code"]}\t{item['name']}\t{item['category']}\t{item['price']}\t  {item['rate']}\t{item['status']}")
                        
                        while True:
                            new_info = input("Enter new (code,name,category,price,rate,status): ").title().split(',')
                            if len(new_info) == 6:
                                item['code'] = new_info[0].upper()
                                item['name'] = new_info[1]
                                item['category'] = new_info[2]
                                item['price'] = new_info[3]
                                item['rate'] = new_info[4]
                                item['status'] = new_info[5]
                                
                                print_w_menu("A")
                                print_a_menu("B")
                                print("Update successful!\n")
                                print_out_menu("A")
                                print_out_menu("B")
                                print()
                                back_to_menu("1")
                                return
                            else:
                                continue

            else:
                continue
        if found:
            return
        else:
            print("Invalid item code, please enter a valid item code.")

def ref(a): # to give a recomment item code if when user add new item and the item code is repeated
    print("\nItem code repeated, please use another item code.")
    item_code = []
    letter = ""
    number = 0
    for menu_name, items in menus.items():
        for item in items:
            item_code.append(item["code"])

    for Item in item_code:
        if Item[0] == a[0]:
            if Item[0] == "A" and Item[1] == "D" and Item[2] == "D":
                print(f"{Item}")
                letter = Item[0:3]
                number = int(Item[3:])
            elif Item[0] != "G" and Item[1] != "O" and a[0] != "G" and a[1] != "O":
                print(f"{Item}")
                letter = Item[0]
                number = int(Item[1:])
            elif Item[0] == "G" and Item[1] == "O" and a[0] == "G" and a[1] == "O":
                print(f"{Item}")
                letter = Item[0:2]
                number = int(Item[2:])
    number += 1 
    print(f"Do you mean {letter}{number:03d}?")

def add_new_blooms():
    item_codes = []
    for menu_name, items in menus.items():
        if menu_name == "A":
            for item in items:
                item_codes.append(item["code"])
    while True:
        new_bloom = input("\nPlease enter new blooms details in format (item code,item name,category,price,rate,status) or 0 to go back.\n").title()
        if new_bloom == "0":
            back_to_menu("2")
            return 
        else:
            new_bloom = new_bloom.split(",")
            if len(new_bloom) == 6:
                new_bloom = {
                    "code" : new_bloom[0].upper(),
                    "name" : new_bloom[1],
                    "category" : new_bloom[2],
                    "price" : new_bloom[3],
                    "rate" : new_bloom[4],
                    "status" : new_bloom[5],
                }
                if new_bloom["code"] in item_codes:
                    ref(new_bloom["code"]) # to give a recomment item code if when user add new item and the item code is repeated
                else:
                    menus["A"].append(new_bloom)
                    break
            else:
                continue

    print()
    print_w_menu("A")
    print_a_menu("B")
    print_out_menu("A") 
    print_out_menu("B")
    print()
    back_to_menu("1")

def view_update_addon():
    global menus
    
    while True:
        update_code = input("\nPlease enter the add on item code that you want to update or 0 to go back: ").upper()
        
        found = False
        for menu_name, items in menus.items():
            if menu_name == "B":
                for item in items:
                    if update_code == "0":
                        back_to_menu("2")
                        found = True
                        return
                    elif update_code == item['code']:
                        found = True
                        print(f"{item["code"]}\t{item['name']}\t{item['category']}\t{item['price']}\t  {item['rate']}\t{item['status']}")
                        
                        while True:
                            new_info = input("Enter new (code,name,category,price,rate,status): ").title().split(',')
                            if len(new_info) == 6:
                                item['code'] = new_info[0].upper()
                                item['name'] = new_info[1]
                                item['category'] = new_info[2]
                                item['price'] = new_info[3]
                                item['rate'] = new_info[4]
                                item['status'] = new_info[5]
                                
                                print_w_menu("A")
                                print_a_menu("B")
                                print("Update successful!\n")
                                print_out_menu("A")
                                print_out_menu("B")
                                print()
                                back_to_menu("1")
                                return
                            else:
                                continue
            else:
                continue
        if found:
            return
        else:
            print("Invalid item code, please enter a valid item code.")

def add_new_addon():
    item_codes = []
    for menu_name, items in menus.items():
        if menu_name == "B":
            for item in items:
                item_codes.append(item["code"])
    while True:
        new_addon = input("\nPlease enter new add on details in format (item code,item name,category,price,rate,status) or 0 to go back.\n").title()
        if new_addon == "0":
            back_to_menu("2")
            return
        else:
            new_addon = new_addon.split(",")
            if len(new_addon) == 6:
                new_addon = {
                    "code" : new_addon[0].upper(),
                    "name" : new_addon[1],
                    "category" : new_addon[2],
                    "price" : new_addon[3],
                    "rate" : new_addon[4],
                    "status" : new_addon[5],
                }
                if new_addon["code"] in item_codes:
                    ref(new_addon["code"]) # to give a recomment item code if when user add new item and the item code is repeated
                else:
                    menus["B"].append(new_addon)
                    break
            else:
                continue
        
    print()
    print_w_menu("A")
    print_a_menu("B")
    print_out_menu("A")
    print_out_menu("B")
    print()
    back_to_menu("1")

def back_to_menu(a): # a is to choose go back to which menu
    if a == "1":
        print("\nPlease select features.") # put menu or anything else will better? ? ?
        print("1) Inventory management")
        print("2) Sales management")
        print("3) Quit the program")
        while True:
            option = input("Please enter a number 1 or 2 or 3. ")
            if option not in ["1", "2", "3"]:
                print("Please enter 1 or 2 or 3. ")
            elif option == "1":
                inventory_management()
                return
            elif option == "2":
                sale_management()
                return
            else:
                return
    elif a == "2":
        inventory_management()
        return
    elif a == "3":
        sale_management()
        return
    elif a == "4":
        create_order()
        return
    elif a == "5":
        print("\nCategory:")
        print("1) Romantic")
        print("2) Birthday")
        print("3) Grand Openning")
        print("4) Condolence")
        print("5) Anniversary")
        print("6) Go back")
        print("7) Back to main menu")
        option1()
        return

def sale_management():
    print("\nPlease select features.") # put menu or anything else will better ? ? ?
    print("1) Create order")
    print("2) View order")
    print("3) Back to previous page")
    while True:
        option = input("Please enter a number: ")
        if option not in ["1", "2", "3"]: 
            print("Please enter '1' or '2' or '3'.")
        elif option == "1":
            create_order()
            return
        elif option == "2":
            view_order()
            return
        elif option == "3":
            back_to_menu("1")
            return

def create_order():
    print()
    print_out_menu("A")
    print_out_menu("B")
    print("\nPlease select features.") # put menu or anything else will better ? ? ?
    print("1) Filter products by category")
    print("2) Sort products by price") 
    print("3) sort products by rating")
    print("4) Order item")
    print("5) Back to previous page")
    print("6) Back to main menu")
    while True:
        option = input("Number: ")
        if option not in ["1", "2", "3", "4", "5", "6"]: 
            print("Please enter a number 1 or 2 or 3 or 4 or 5 or 6.")
        elif option == "1":
            print("\nCategory:")
            print("1) Romantic")
            print("2) Birthday")
            print("3) Grand Openning")
            print("4) Condolence")
            print("5) Anniversary")
            print("6) Go back to previous page")
            print("7) Back to main menu")
            option1()
            return
        elif option == "2":
            print("\nPlease select features.") # put menu or anything else will better ? ? ?
            print("1) Cheapest to most expensive")
            print("2) Most expensive to cheapest")
            print("3) Back to previous page")
            print("4) Back to main menu")
            while True:
                order = input("Please select a number: ")
                if order not in ["1", "2", "3", "4"]:
                    print("Please select a number: ")
                elif order == "1":
                    price_sort(order)
                    while True:
                        continues = input("Continue create order? (y/n): ")
                        if continues not in ["y", "n"]:
                            print("Please enter y or n.")
                        elif continues == "y":
                            order_item("2")
                            return
                        else:
                            create_order()
                            return
                elif order == "2":
                    price_sort(order)
                    while True:
                        continues = input("Continue create order? (y/n): ")
                        if continues not in ["y", "n"]:
                            print("Please enter y or n.")
                        elif continues == "y":
                            order_item("2")
                            return
                        else:
                            create_order()
                            return
                elif order == "3":
                    back_to_menu("4")
                    return
                else:
                    back_to_menu("1")
                    return
        elif option == "3":
            print()
            print("\nPlease select features.") # put menu or anything else will better ? ? ?
            print("1) Rate from 1 - 5")
            print("2) Rate from 5 - 1")
            print("3) Back to previous page")
            print("4) Back to main menu")
            while True:
                rate = input("Please select a number: ")
                if rate not in ["1", "2", "3", "4"]:
                    print("Please select a number: ")
                elif rate == "1":
                    rate_sort(rate)
                    while True:
                        print()
                        continues = input("Continue create order? (y/n): ")
                        if continues not in ["y", "n"]:
                            print("Please enter y or n.")
                        elif continues == "y":
                            order_item("2")
                            return
                        else:
                            create_order()
                            return
                elif rate == "2":
                    rate_sort(rate)
                    while True:
                        print()
                        continues = input("Continue create order? (y/n): ")
                        if continues not in ["y", "n"]:
                            print("Please enter y or n.")
                        elif continues == "y":
                            order_item("2")
                            return
                        else:
                            create_order()
                            return
                elif rate == "3":
                    back_to_menu("4")
                    return
                else:
                    back_to_menu("1")
                    return
        elif option == "4":
            order_item("1")
            return
        elif option == "5":
            back_to_menu("3")
            return
        else:
            back_to_menu("1")
            return

def edit_order():
    while True:
        code = input("\nPlease enter a order code to edit order or 0 to go back: ")
        if code == "0":
            view_order()
            return
        found = False
        for codes in order_code:
            if code == codes["code"]:
                found = True
                if codes["status"] == "Cancelled":
                    print()
                    print("1) Yes")
                    print("2) No")
                    print("Current status is Cancelled, want change to open?\nPlease select 1 or 2. ")
                    while True:
                        ans = input("Number: ")
                        if ans not in ["1", "2"]:
                            print("Please select a number 1 or 2.")
                        if ans == "1":
                            codes["status"] = "Open"
                            view_order()
                            return
                        else:
                            return
                elif codes["status"] == "Open":
                    print()
                    print("1) Preparing")
                    print("2) Cancelled")
                    print("3) Go Back")
                    print("Current status is Preparing, want change to ready or cancelled?\nPlease select 1 or 2 or 3. ")
                    while True:
                        ans = input("Number: ")
                        if ans not in ["1", "2", "3"]:
                            print("Please select a number 1 or 2 or 3.")
                        if ans == "1":
                            codes["status"] = "Preparing"
                            view_order()
                            return
                        elif ans == "2":
                            codes["status"] = "Cancelled"
                            view_order()
                            return
                        else:
                            return
                elif codes["status"] == "Preparing":
                    print()
                    print("1) Ready")
                    print("2) Go Back")
                    print("Current status is Preparing, want change to ready or cancelled?\nPlease select 1 or 2. ")
                    while True:
                        ans = input("Number: ")
                        if ans not in ["1", "2"]:
                            print("Please select a number 1 or 2 or 3.")
                        if ans == "1":
                            codes["status"] = "Ready"
                            view_order()
                            return
                        else:
                            return
                elif codes["status"] == "Ready":
                    print()
                    print("1) Preparing")
                    print("2) Closed")
                    print("3) Go Back")
                    print("Current status is Ready, want change to preparing or closed?\nPlease select 1 or 2. ")
                    while True:
                        ans = input("Number: ")
                        if ans not in ["1", "2", "3"]:
                            print("Please select a number 1 or 2 or 3.")
                        if ans == "1":
                            codes["status"] = "Preparing"
                            view_order()
                            return
                        elif ans == "2":
                            codes["status"] = "Closed"
                            view_order()
                            return
                        else:
                            return
                elif codes["status"] == "Closed":
                    print()
                    print("Current status is Closed, can't change status?\nPlease enter 1 to continue. ")
                    while True:
                        ans = input("Number: ")
                        if ans != "1":
                            print("Current status is Closed, can't change status?\nPlease enter 1 to continue.")
                        else:
                            view_order()
                            return
        if not found:
            print("Please enter a valid order code.")
        else:
            return

def view_order():
    global detail, order_code,ordered_item_code
    for code in order_code:
        print(f"{code["code"]}\t{code["status"]}")
    print()
    print("1) Edit/Cancel order")
    print("2) Filter order by status")
    print("3) view order")
    print("4) Go back to previous page")
    print("5) Back to main menu")
    while True:
        option = input("Please select a number: ")
        if option not in ["1", "2", "3", "4", "5"]:
            print("Please enter numer 1 or 2 or 3 or 4 or 5.")
        elif option == "1":
            edit_order()
            return
        elif option == "2":
            print()
            print("1) Preparing")
            print("2) Ready")
            print("3) Cancelled")
            print("4) Closed")
            print("5) Go to privious page")
            while True:
                status = input("Please enter a number: ")
                if status not in ["1", "2", "3", "4", "5"]:
                    print("Please enter number 1 or 2 or 3 or 4 or 5.")
                elif status == "1":
                    print()
                    for code_stutus in order_code:
                        if code_stutus["status"] == "Preparing":
                            print(f"{code_stutus["code"]}\t{code_stutus["status"]}")
                    edit_order()
                    return
                elif status == "2":
                    print()
                    for code_stutus in order_code:
                        if code_stutus["status"] == "Ready":
                            print(f"{code_stutus["code"]}\t{code_stutus["status"]}")
                    edit_order()
                    return
                elif status == "3":
                    print()
                    for code_stutus in order_code:
                        if code_stutus["status"] == "Cancelled":
                            print(f"{code_stutus["code"]}\t{code_stutus["status"]}")
                    edit_order()
                    return
                elif status == "4":
                    for code_stutus in order_code:
                        print()
                        if code_stutus["status"] == "Closed":
                            print(f"{code_stutus["code"]}\t{code_stutus["status"]}")
                    edit_order()
                    return
                else:
                    view_order()
                    return
        elif option == "3":
            while True:
                print()
                codes = input("Please enter a order code you want to check or 0 to go back: ").upper()
                if codes == "0":
                    view_order()
                    return
                else:
                    for order in order_code:
                        if codes != order["code"]:
                            continue
                        else:
                            print()
                            print(f"Order item:            {', '.join(detail[codes]['order item'])}")
                            print(f"Delivery date:         {detail[codes]["delivery date"]}")
                            print(f"Same day delivery:     {detail[codes]['Same day delivery'][0]}, ${detail[code["code"]]['Same day delivery'][1]}")
                            print(f"Weekend delivery:      {detail[codes]["Weekend delivery"]}")
                            print(f"Delivery charge:       {detail[codes]["delivery charge"]}")
                            print(f"Total:                 {detail[codes]["total"]}")
                            print(f"Customer name:         {detail[codes]["customer name"]}")
                            print(f"Recipient name:        {detail[codes]["recipient name"]}")
                            print(f"Message for recipient: {detail[codes]["message for recipient"]}")
                            print(f"Delivery address:      {detail[codes]["delivery address"]}")
        elif option == "4":
            back_to_menu("3")
            return
        else: 
            back_to_menu("1")
            return

def generate_order_code(): # to auto generate order code with using format BBO-23-XXXX, XXXX is a number, this funtion will auto add 1 when new order created
    if order_code == []:
        return "BBO-23-0001"
    else:
        last_code = order_code[-1]
        number = int(last_code["code"].split("-")[-1]) + 1 
        return f"BBO-23-{number:04d}"

def order_summarys(): # to print out the order item in order_summary
    global order_summary
    title()
    for item in order_summary:
        print("|" + f"{item['code']}".center(max_len('code') + 2) + "|" + f"{item['name']}".center(max_len('name') + 2) + "|" + f"{item['category']}".center(max_len('category') + 2) + "|" + f"{item['price']}".center(9) + "|" + f"{item['rate']}".center(7) + "|" + f"{item['status']}".center(max_len('status') + 2) + "|")

def order_item(s): # is s != 1, then will skip print available item
    global code_list, order_summary, menus, total, order_code, ordered_item_code
    order_summary = []
    ordered_item_code = []
    while True:
        print()
        if s == "1":
            item_code_list("A") # to print out available item in menu "A"
        for menu_name, items in menus.items():
            for item in items:
                if item["status"] == "Available":
                    code_list.append(item["code"])
        order = input("Please enter the item code or 9 to finish order or 0 to go back: ").upper()
        if order not in code_list and order != "9" and order != "0":
            print("Please enter a valid item code")
        elif order == "9":
            break
        elif order == "0":
            back_to_menu("4")
            return
        else:
            for menu_name, items in menus.items():
                if menu_name == "A":
                    for item in items:
                        if order == item["code"]:
                            order_summary.append(item)
                            ordered_item_code.append(item["code"])
                            total += int(item["price"])
                            print()
                            print("Add on:")
                            item_code_list("B") # to print out available item in menu "B"
                            while True:
                                order = input("Please enter the add on item code or 0 to skip: ").upper()
                                if order not in code_list and order != "0":
                                    print("Please enter a valid add on item code")
                                elif order == "0":
                                    break
                                else:
                                    for menu_name, items in menus.items():
                                        if menu_name == "B":
                                            for item in items:
                                                if order == item["code"]:
                                                    order_summary.append(item)
                                                    ordered_item_code.append(item["code"])
                                                    total += int(item["price"])
    print()
    customer_name = input("Please enter customer name: ")
    recipient_name = input("Please enter recipient's name: ")
    while True:
        message = input("Please enter message for recipient (max 300 character): ")
        if len(message) <= 300: # to make sure the message is not longer than 300 charcater
            break
        else:
            continue
    print()
    print("1) Customer pick up")
    print("2) Recipient pick up")
    print("3) Delivery")
    while True:
        collect = input("Please select a number: ")
        if collect not in ["1", "2", "3"]:
            print("Please select a number 1 or 2 or 3.")
        elif collect == "1":
            date_format = "Customer pick up"
            sameday = "NO"
            address = "Customer pick up"
            break
        elif collect == "2":
            date_format = "Recipient pick up"
            sameday = "NO"
            address = "Recipient pick up"
            break
        elif collect == "3":
            address = input("Please enter delivery address:\n")
            while True:
                date = input("Please enter delivery date and time(eg: 2025-10-13 14:59)(delivery charge $35, same day delivery charge extra $35):\n")
                try:
                    date_format = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M") # to make sure the date is yyyy-mm-dd hh:mm
                    if date_format.date() == datetime.date.today(): # check the date user input is today date or not
                        sameday = "YES"
                    else:
                        sameday = "NO"
                    break
                except ValueError:
                    print("Invalid format, please enter a date time in this format (eg: 2025-10-13 14:59)")
            break
    
    print("\nOrder Summary")
    order_summarys()
    print()
    print("Delivery date        :", date_format)
    fee = 0
    weekend = 0
    samedayfee = 0
    if collect == "3":
        fee += 35
        total += 35
    if sameday == "YES":
        samedayfee += 35
        total += 35
    if date_format == "Customer pick up" or date_format == "Recipient pick up":
        pass
    else:
        if date_format.weekday() >= 5:
            weekend = 10
            total += 10
    print("Same day delivery    :", samedayfee)
    print("Weekend delivery     :", weekend)
    print("Delivery charge      :", fee)
    print("Total                :", total)
    print("Customer's name      :",customer_name)
    print("Recipient's name     :", recipient_name)
    print("Message for recipient: \n"+ message)
    print("Delivery address: \n"+ address)
    while True:
        print()
        print("1) Confirm")
        print("2) Edit info")
        print("3) Cancel")
        cfm = input("Please select a number: ")
        if cfm not in ["1", "2", "3"]:
            print("Please select a number '1' or '2' or '3'.")
        elif cfm == "1":
            new_order_code = generate_order_code()
            order_code.append({"code":new_order_code, "status": "Open"})
            detail[new_order_code] = {
                "order item": ordered_item_code,
                "delivery date": date_format,
                "Same day delivery": [sameday,samedayfee],
                "Weekend delivery": weekend,
                "delivery charge": fee,
                "total":total,
                "customer name":customer_name,
                "recipient name": recipient_name,
                "message for recipient": message,
                "delivery address": address,
            }
            total = 0
            back_to_menu("1")
            return
        elif cfm == "2":
            customer_name = input("Please enter customer name: ")
            recipient_name = input("Please enter recipient's name: ")
            message = input("Please enter message for recipient (max 300 character): ")
            new_order_code = generate_order_code()
            order_code.append({"code":new_order_code, "status": "preparing"})
            detail[new_order_code] = {
                "order item": ordered_item_code,
                "delivery date": date_format,
                "Same day delivery": [sameday,samedayfee],
                "delivery charge": fee,
                "total":total,
                "customer name":customer_name,
                "recipient name": recipient_name,
                "message for recipient": message,
                "delivery address": address,
            }
            total = 0
            back_to_menu("1")
            return
        elif cfm == "3":
            back_to_menu("4")
            return

def main():
    print("\nWelcome to Beautiful Blooms")
    print("\nPlease select features.") # put menu or anything else will better? ? ?
    print("1) Inventory management")
    print("2) Sales management")
    print("3) Quit the program.")
    while True:
        option = input("Please enter a number 1 or 2 or 3. ")
        if option not in ["1", "2", "3"]:
            print("Please enter 1 or 2 or 3. ")
        elif option == "1":
            inventory_management()
            return
        elif option == "2":
            sale_management()
            return
        else:
            return


main()
