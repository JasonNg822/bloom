import datetime

order_summary = []
menus = {}
code_list = []
total = 0
detail = {}
order_code = []

current_menu = None
try:
    with open('product.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            
            if line.startswith("menu"):
                current_menu = line.split()[1]
                menus[current_menu] = []
            else:
                parts = line.split(',')
                if len(parts) >= 6:
                    menus[current_menu].append({
                        'code': parts[0],
                        'name': parts[1],
                        'category': parts[2],
                        'price': parts[3],
                        'rate': parts[4],
                        'status': parts[5]
                    })
except FileNotFoundError:
    print(f"File not found.")

def aline(product, name):
    lens = 0
    for menu_names, items in menus.items():
        for item in items:
            if len(item[name]) > lens:
                lens = len(item[name])
            else:
                continue
    return " " * (((lens - len(product))) + 4)

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
            order_item()
            return
        elif option2 == "2":
            back_to_menu("5")
            return
        elif option2 == "3":
            back_to_menu("1")
            return

def item_code_list(a):
    global code_list
    code_list = []
    for menu_name, items in menus.items():
        if menu_name == a:
            for item in items:
                if item["status"] == "Available":
                    code_list.append(item["code"])
                    print(f"{item['code']}\t  {item['name']}{aline(item['name'], 'name')}{item['category']}{aline(item['category'], 'category')}{item['price']}\t  {item['rate']}\t{item['status']}")

def price_sort(a):
    print()
    if a == "1":
        a = False
    elif a == "2":
        a = True
    for menu_name, items in menus.items():
        print(f"menu {menu_name}")
        sorted_items = sorted(items, key=lambda x: int(x["price"]), reverse = a)
        for item in sorted_items:
            print(f"{item['code']}\t  {item['name']}{aline(item['name'], 'name')}{item['category']}{aline(item['category'], 'category')}{item['price']}\t  {item['rate']}\t{item['status']}")

def rate_sort(a):
    print()
    if a == "1":
        a = False
    elif a == "2":
        a = True
    for menu_name, items in menus.items():
        print(f"menu {menu_name}")
        sorted_items = sorted(items, key=lambda x: int(x["rate"]), reverse = a)
        for item in sorted_items:
            print(f"{item['code']}\t  {item['name']}{aline(item['name'], 'name')}{item['category']}{aline(item['category'], 'category')}{item['price']}\t  {item['rate']}\t{item['status']}")

def category(a):
    for menu_name, items in menus.items():
        for item in items:
            if item["category"] == a:
                print(f"{item['code']}\t{item['name']}{aline(item['name'], 'name')}{item['category']}{aline(item['category'], 'category')}{item['price']}\t  {item['rate']}\t{item['status']}")

def print_out_menu(A):
    for menu_name, items in menus.items():
        if menu_name == A:
            print(f"menu {A}")
            for item in items:
                print(f"{item['code']}\t  {item['name']}{aline(item['name'], 'name')}{item['category']}{aline(item['category'], 'category')}{item['price']}\t  {item['rate']}\t{item['status']}")

def print_w_menu(A):
    for menu_name, items in menus.items():
        if menu_name == A:
            with open("product.txt", "w") as file:
                file.write(f"menu {A}\n")
            for item in items:
                with open("product.txt", "a") as file:
                    file.write(f"{item["code"]},{item["name"]},{item["category"]},{item["price"]},{item['rate']},{item["status"]}\n")

def print_a_menu(A):
    for menu_name, items in menus.items():
        if menu_name == A:
            with open("product.txt", "a") as file:
                file.write(f"menu {A}\n")
            for item in items:
                with open("product.txt", "a") as file:
                    file.write(f"{item["code"]},{item["name"]},{item["category"]},{item["price"]},{item['rate']},{item["status"]}\n")

def inventory_management():
    print("\nPlease select features.") # put menu or anything else will better ? ? ?
    print("1) View update blooms")
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
        update_code = input("\nPlease enter the item code that you want to update or enter 0 to go back: ")
        
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

            else:
                continue
        if found:
            break
        else:
            print("Invalid item code, please enter a valid item code.")

def view_update_blooms():
    global menus
    
    while True:
        update_code = input("\nPlease enter the item code that you want to update or enter 0 to go back: ")
        
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

            else:
                continue
        if found:
            break
        else:
            print("Invalid item code, please enter a valid item code.")

def add_new_blooms():
    while True:
        new_bloom = input("\nPlease enter new blooms details in format (item code,item name,category,price,rate,status) or 0 to go back.\n").title()
        if new_bloom == "0":
            back_to_menu("2")
            return 
        
        new_bloom.split(",")
        if len(new_bloom) == 5:
            new_bloom = {
                "code" : new_bloom[0],
                "name" : new_bloom[1],
                "category" : new_bloom[2],
                "price" : new_bloom[3],
                "rate" : new_bloom[4],
                "status" : new_bloom[5],
            }
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
        update_code = input("\nPlease enter the item code that you want to update or 0 to go back: ")
        
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
                            if len(new_info) == 5:
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
            else:
                continue
        if found:
            break
        else:
            print("Invalid item code, please enter a valid item code.")

def add_new_addon():
    while True:
        new_addon = input("\nPlease enter new add on details in format (item code,item name,category,price,rate,status) or 0 to go back.\n").title()
        if new_addon == "0":
            back_to_menu("2")
            return
        new_addon.split(",")
        if len(new_addon) == 6:
            new_addon = {
                "code" : new_addon[0],
                "name" : new_addon[1],
                "category" : new_addon[2],
                "price" : new_addon[3],
                "rate" : new_addon[4],
                "status" : new_addon[5],
            }
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

def back_to_menu(a):
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
            break
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
        code = input("Please enter a order code or 0 to go back: ")
        if code == "0":
            view_order()
            break
        found = False
        for codes in order_code:
            if code == codes["code"]:
                found = True
                if codes["status"] == "Cancelled":
                    print()
                    print("1) Yes")
                    print("2) No")
                    print("Current status is Cancelled, want change to preparing?\nPlease select 1 or 2. ")
                    while True:
                        ans = input("Number: ")
                        if ans not in ["1", "2"]:
                            print("Please select a number 1 or 2.")
                        if ans == "1":
                            codes["status"] = "Preparing"
                            view_order()
                            break
                        else:
                            break
                    break
                elif codes["status"] == "Preparing":
                    print()
                    print("1) Ready")
                    print("2) Cancelled")
                    print("3) Go Back")
                    print("Current status is Cancelled, want change to ready or cancelled?\nPlease select 1 or 2. ")
                    while True:
                        ans = input("Number: ")
                        if ans not in ["1", "2", "3"]:
                            print("Please select a number 1 or 2 or 3.")
                        if ans == "1":
                            codes["status"] = "Ready"
                            view_order()
                            break
                        elif ans == "2":
                            codes["status"] = "Cancelled"
                            view_order()
                        else:
                            break
                    break
                elif codes["status"] == "Ready":
                    print()
                    print("1) Preparing")
                    print("2) Closed")
                    print("3) Go Back")
                    print("Current status is Cancelled, want change to preparing or closed?\nPlease select 1 or 2. ")
                    while True:
                        ans = input("Number: ")
                        if ans not in ["1", "2", "3"]:
                            print("Please select a number 1 or 2 or 3.")
                        if ans == "1":
                            codes["status"] = "Preparing"
                            view_order()
                            break
                        elif ans == "2":
                            codes["status"] = "Closed"
                            view_order()
                            break
                        else:
                            break
                    break
                elif codes["status"] == "Closed":
                    print()
                    print("Current status is Closed, can't change status?\nPlease enter 1 to continue. ")
                    while True:
                        ans = input("Number: ")
                        if ans != "1":
                            print("Current status is Closed, can't change status?\nPlease enter 1 to continue.")
                        else:
                            view_order()
                            break
                    break
        if not found:
            print("Please enter a valid order code.")
        else:
            break

def view_order():
    global detail, order_code
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
                    break
                elif status == "2":
                    print()
                    for code_stutus in order_code:
                        if code_stutus["status"] == "Ready":
                            print(f"{code_stutus["code"]}\t{code_stutus["status"]}")
                    edit_order()
                    break
                elif status == "3":
                    print()
                    for code_stutus in order_code:
                        if code_stutus["status"] == "Cancelled":
                            print(f"{code_stutus["code"]}\t{code_stutus["status"]}")
                    edit_order()
                    break
                elif status == "4":
                    for code_stutus in order_code:
                        print()
                        if code_stutus["status"] == "Closed":
                            print(f"{code_stutus["code"]}\t{code_stutus["status"]}")
                    edit_order()
                    break
                else:
                    view_order()
            break
        elif option == "3":
            while True:
                print()
                codes = input("Please enter a order code you want to check or 0 to go back: ")
                if codes == "0":
                    view_order()
                    return
                else:
                    for order in order_code:
                        if codes != order["code"]:
                            continue
                        else:
                            print()
                            print(f"Delivery date:         {detail[codes]["delivery date"]}")
                            print(f"Same day delivery:     {detail[codes]['Same day delivery'][0]}, ${detail[code["code"]]['Same day delivery'][1]}")
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

def generate_order_code():
    if order_code == []:
        return "BBO-23-0001"
    else:
        last_code = order_code[-1]
        num = int(last_code["code"].split("-")[-1]) + 1 
        return f"BBO-23-{num:04d}"

def order_summarys():
    global order_summary
    for item in order_summary:
        print(f"{item['code']}\t  {item['name']}{aline(item['name'], 'name')}{item['category']}{aline(item['category'], 'category')}{item['price']}")

def order_item(s):
    global code_list, order_summary, menus, total, order_code
    order_summary = []
    while True:
        print()
        if s == "1":
            item_code_list("A")
        order = input("Please enter the item code or 9 to finish order or 0 to go back: ")
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
                            total += int(item["price"])
                            print()
                            print("Add on:")
                            item_code_list("B")
                            while True:
                                order = input("Please enter the add on item code or 0 to skip: ")
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
                                                    total += int(item["price"])
    print()
    customer_name = input("Please enter customer name: ")
    recipient_name = input("Please enter recipient's name: ")
    while True:
        message = input("Please enter message for recipient (max 300 character): ")
        if len(message) <= 300:
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
            address = input("Please enter delivery address: \n")
            while True:
                date = input("Please enter delivery date and time(eg: 2025-10-05 14:59)(delivery charge $35, same day delivery charge extra $35):\n")
                try:
                    date_format = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M")
                    if date_format.date() == datetime.date.today():
                        sameday = "YES"
                    else:
                        sameday = "NO"
                    break
                except ValueError:
                    print("Invalid format, please enter a date time in this format (eg: 15-Oct-2025 14:59)")
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
            order_code.append({"code":new_order_code, "status": "Preparing"})
            detail[new_order_code] = {
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
        elif cfm == "2":
            customer_name = input("Please enter customer name: ")
            recipient_name = input("Please enter recipient's name: ")
            message = input("Please enter message for recipient (max 300 character): ")
            new_order_code = generate_order_code()
            order_code.append({"code":new_order_code, "status": "preparing"})
            detail[new_order_code] = {
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
            break
        elif option == "2":
            sale_management()
            break
        else:
            break


main()