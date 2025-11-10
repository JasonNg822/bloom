# BBS 
# Author by Jason on 2025 Nov 10.

import datetime

ordered_item_code = []
order_summary = []
menus = {}
code_list = []
total = 0
detail = {}
order_code = []
cat = []
sales_hist = []

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

for menu_name, items in menus.items():
        for menu in menu_name:
            for item in items:
                if item["category"] in cat:
                    continue
                else:
                    cat.append(item["category"])

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

def title2():
    print(f"|" + "-" * (max_len('code') + 2) + "|" + "-" * (max_len('name') + 2) + "|" + "-" * (max_len('category') + 2) + "|" + "-" * 9 + "|")
    print(f"|" + "Code".center(max_len('code') + 2) + "|" + "Name".center(max_len('name') + 2) + "|" + "Category".center(max_len('category') + 2) + "|" + "Price".center(9) + "|")
    print(f"|" + "-" * (max_len('code') + 2) + "|" + "-" * (max_len('name') + 2) + "|" + "-" * (max_len('category') + 2) + "|" + "-" * 9 + "|")

def titles(a): 
    print("|" + f"-" * (max_len('code') + max_len('name') + max_len('category') + max_len('status') + 29) + "|")
    if a == "A":
        a = "Menu A"
    else:
        a = "Add On"
    print("|" + f"{a}".center((max_len('code') + max_len('name') + max_len('category') + max_len('status') + 29)) + "|")
    print("|" + f"-" * (max_len('code') + max_len('name') + max_len('category') + max_len('status') + 29) + "|")

def option1():
    global ordered_item_code, order_summary, menus, code_list, total, detail, order_code, cat, sales_hist
    while True:
        option1 = input("Please enter a category(not number): ").title()
        if option1 not in cat and option1 != str((len(cat) + 1)) and option1 != str((len(cat) + 2)):
            print("Please enter a corrrect category(not number). ")
        elif option1 in cat:
            print("_" * 150)
            print()
            category(option1)
            print("1) Order item")
            print("2) Back to filter category")
            print("3) Back to main menu")
            option2()                     
            return
        elif option1 == str((len(cat) + 1)) :
            print("_" * 150)
            back_to_menu("4")
            return
        elif option1 == str((len(cat) + 2)): 
            print("_" * 150)
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
            print("_" * 150)
            back_to_menu("1")
            return

def item_code_list(a): # to print out available item in a
    global ordered_item_code, order_summary, menus, code_list, total, detail, order_code, cat, sales_hist
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
    global ordered_item_code, order_summary, menus, code_list, total, detail, order_code, cat, sales_hist
    print()
    if a == "1":
        a = False
    elif a == "2":
        a = True
    for menu_name, items in menus.items():
        titles(menu_name)
        title()
        sorted_items = sorted(items, key=lambda x: float(x["price"]), reverse = a)
        for item in sorted_items:
            print("|" + f"{item['code']}".center(max_len('code') + 2) + "|" + f"{item['name']}".center(max_len('name') + 2) + "|" + f"{item['category']}".center(max_len('category') + 2) + "|" + f"{item['price']}".center(9) + "|" + f"{item['rate']}".center(7) + "|" + f"{item['status']}".center(max_len('status') + 2) + "|")

def rate_sort(a): # a is to decide the price amount sort from big to small or small to big
    global ordered_item_code, order_summary, menus, code_list, total, detail, order_code, cat, sales_hist
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

def category(a): # a is to decide the which category
    global ordered_item_code, order_summary, menus, code_list, total, detail, order_code, cat, sales_hist
    title()
    for menu_name, items in menus.items():
        for item in items:
            if item["category"] == a:
                print("|" + f"{item['code']}".center(max_len('code') + 2) + "|" + f"{item['name']}".center(max_len('name') + 2) + "|" + f"{item['category']}".center(max_len('category') + 2) + "|" + f"{item['price']}".center(9) + "|" + f"{item['rate']}".center(7) + "|" + f"{item['status']}".center(max_len('status') + 2) + "|")
    print()

def print_out_menu(a):
    global ordered_item_code, order_summary, menus, code_list, total, detail, order_code, cat, sales_hist
    for menu_name, items in menus.items():
        if menu_name == a:
            titles(a)
            title()
            for item in items:
                print("|" + f"{item['code']}".center(max_len('code') + 2) + "|" + f"{item['name']}".center(max_len('name') + 2) + "|" + f"{item['category']}".center(max_len('category') + 2) + "|" + f"{item['price']}".center(9) + "|" + f"{item['rate']}".center(7) + "|" + f"{item['status']}".center(max_len('status') + 2) + "|")
    

def print_w_menu(a): # use "w" to rewrite the menu in product.txt 
    global ordered_item_code, order_summary, menus, code_list, total, detail, order_code, cat, sales_hist
    for menu_name, items in menus.items():
        if menu_name == a:
            with open("product.txt", "w") as file:
                file.write(f"menu {a}\n")
            for item in items:
                with open("product.txt", "a") as file:
                    file.write(f"{item["code"]},{item["name"]},{item["category"]},{item["price"]},{item['rate']},{item["status"]}\n")

def print_a_menu(a): # use "a" to add the menu in product.txt
    global ordered_item_code, order_summary, menus, code_list, total, detail, order_code, cat, sales_hist
    for menu_name, items in menus.items():
        if menu_name == a:
            with open("product.txt", "a") as file:
                file.write(f"menu {a}\n")
            for item in items:
                with open("product.txt", "a") as file:
                    file.write(f"{item["code"]},{item["name"]},{item["category"]},{item["price"]},{item['rate']},{item["status"]}\n")

def inventory_management():
    print("\nPlease select a number.")
    print("1) View/update blooms")
    print("2) Add new blooms")
    print("3) View/update add on")
    print("4) Add new add on")
    print("5) Edit rating")
    print("6) Add new category")
    print("7) Back to previous page")
    while True:
        option = input("Please enter a number: ")
        if option not in ["1", "2", "3", "4", "5", "6", "7"]: 
            print("Please enter 1 or 2 or 3 or 4 or 5 or 6 or 7.")
        elif option == "1":
            print("_" * 150)
            view_update_blooms()
            return
        elif option == "2":
            print("_" * 150)
            add_new_blooms()
            return
        elif option == "3":
            print("_" * 150)
            view_update_addon()
            return
        elif option == "4":
            print("_" * 150)
            add_new_addon()
            return
        elif option == "5":
            print("_" * 150)
            update_rate()
            return
        elif option == "6":
            print("_" * 150)
            new_cat()
            return
        else: 
            print("_" * 150)
            back_to_menu("1")
            return

def update_rate():
    global ordered_item_code, order_summary, menus, code_list, total, detail, order_code, cat, sales_hist
    
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
                    title()
                    print("|" + f"{item['code']}".center(max_len('code') + 2) + "|" + f"{item['name']}".center(max_len('name') + 2) + "|" + f"{item['category']}".center(max_len('category') + 2) + "|" + f"{item['price']}".center(9) + "|" + f"{item['rate']}".center(7) + "|" + f"{item['status']}".center(max_len('status') + 2) + "|")
                    
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
                            print("\nUpdate successful!\n")
                            print_out_menu("A")
                            print_out_menu("B")
                            print()
                            print("_" * 150)
                            back_to_menu("1")
                            return
                        else:
                            continue

        if found:
            break
        else:
            print("Invalid item code, please enter a valid item code.")

def view_update_blooms():
    global ordered_item_code, order_summary, menus, code_list, total, detail, order_code, cat, sales_hist
    
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
                        print()
                        title()
                        print("|" + f"{item['code']}".center(max_len('code') + 2) + "|" + f"{item['name']}".center(max_len('name') + 2) + "|" + f"{item['category']}".center(max_len('category') + 2) + "|" + f"{item['price']}".center(9) + "|" + f"{item['rate']}".center(7) + "|" + f"{item['status']}".center(max_len('status') + 2) + "|")
                        
                        while True:
                            print()
                            new_info = input("Enter new (code,name,category,price,rate,status): ").title().split(',')
                            print("_" * 150)
                            if len(new_info) == 6:
                                item['code'] = new_info[0].upper()
                                item['name'] = new_info[1]
                                item['category'] = new_info[2]
                                item['price'] = new_info[3]
                                item['rate'] = new_info[4]
                                item['status'] = new_info[5]
                                
                                print_w_menu("A")
                                print_a_menu("B")
                                print("\nUpdate successful!\n")
                                print_out_menu("A")
                                print_out_menu("B")
                                print()
                                print("_" * 150)
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

def ref(a, A): # to give a recomment item code if when user add new item and the item code is repeated
    global ordered_item_code, order_summary, menus, code_list, total, detail, order_code, cat, sales_hist
    print("\nItem code repeated, please use another item code.")
    item_code = []
    letter = ""
    number = 0
    for menu_name, items in menus.items():
        if menu_name == A:
            for item in items:
                item_code.append(item["code"])

    for Item in item_code:
        if Item[0] == a[0]:
            if Item[0] == "A" and Item[1] == "D" and Item[2] == "D":
                print(f"{Item}")
                letter = ''.join([i for i in Item if i.isalpha()])
                number = int(''.join([i for i in Item if i.isdigit()]))
            elif Item[0] != "G" and Item[1] != "O" and a[0] != "G" and a[1] != "O":
                print(f"{Item}")
                letter = ''.join([i for i in Item if i.isalpha()])
                number = int(''.join([i for i in Item if i.isdigit()]))
            elif Item[0] == "G" and Item[1] == "O" and a[0] == "G" and a[1] == "O":
                print(f"{Item}")
                letter = ''.join([i for i in Item if i.isalpha()])
                number = int(''.join([i for i in Item if i.isdigit()]))
            else:
                print(f"{Item}")
                letter = ''.join([i for i in Item if i.isalpha()])
                number = int(''.join([i for i in Item if i.isdigit()]))
    number += 1 
    print(f"Do you mean {letter}{number:03d}?")
    print("_" * 150)

def new_cat():
    global ordered_item_code, order_summary, menus, code_list, total, detail, order_code, cat, sales_hist
    item_codes = []
    for menu_name, items in menus.items():
        if menu_name == "A":
            for item in items:
                item_codes.append(item["code"])
    while True:
        new_cats = input("Please enter new category: ").title()
        if new_cats in cat:
            print("This category already exist, please enter a new categort or 0 to go back")
        elif new_cats == "0":
            back_to_menu("2")
            return
        else:
            break
    while True:
        print("\nPlease select a number to add new category blooms.")
        print("1) Auto-generate item code")
        print("2) Manually enter item code")
        choice = input("Number: ")
        print("_" * 150)
        if choice not in ["1", "2"]:
            print("Please enter 1 or 2.")
        elif choice == "1":
            code = auto_generate(new_cats)
            while True:
                new_bloom = input("Please enter new item detail(item name,price,rate,status): \n")
                print("_" * 150)
                new_blooms = new_bloom.split(",")
                if len(new_blooms) != 4:
                    print("Invalid format!")
                    continue
                else:
                    new_blooms = f"{code},{new_blooms[0]},{new_cats},{','.join(new_blooms[1:])}"
                    new_blooms = new_blooms.split(",")
                    new_blooms = {
                                    "code" : new_blooms[0].upper(),
                                    "name" : new_blooms[1],
                                    "category" : new_blooms[2],
                                    "price" : new_blooms[3],
                                    "rate" : new_blooms[4],
                                    "status" : new_blooms[5],
                                }
                    menus["A"].append(new_blooms)
                    break
            break
        else:
            while True:
                new_bloom = input("Please enter new item detail (item code,item name,price,rate,status): \n")
                new_bloom = new_bloom.split(",")
                if len(new_bloom) != 5:
                    print("Invalid format")
                    continue
                else:
                    new_blooms = f"{new_bloom[0]},{new_bloom[1]},{new_cats},{','.join(new_bloom[2:])}"
                    new_blooms = new_blooms.split(",")
                    new_blooms = {
                                "code" : new_blooms[0].upper(),
                                "name" : new_blooms[1],
                                "category" : new_blooms[2],
                                "price" : new_blooms[3],
                                "rate" : new_blooms[4],
                                "status" : new_blooms[5],
                            }
                    if new_blooms["code"] in item_codes:
                        ref(new_blooms["code"], "A") # to give a recomment item code if when user add new item and the item code is repeated
                        continue
                    else:
                        menus["A"].append(new_blooms)
                        break
            break
    print_w_menu("A")
    print_a_menu("B")
    print("Add successful!\n")
    print_out_menu("A")
    print_out_menu("B")
    print()
    print("_" * 150)
    cat.append(new_cats)
    back_to_menu("1")


def auto_generate(a):
    global ordered_item_code, order_summary, menus, code_list, total, detail, order_code, cat, sales_hist
    number = 0
    for menu_name, items in menus.items():
        for item in items:
            if item['category'] == a.title():
                number += 1
    number += 1
    
    used = ["GO", "ADD",]
    for menu_name, items in menus.items():
        for item in items:
            letter = item['category'][0]
            used.append(letter.upper())
    if a.title() not in cat:
        if a[0].upper() in used:
            letters = a[0:2].upper()
        else:
            letters = a[0].upper()
    else:
        if a.title() == "Grand Opening":
            letters = "GO"
        elif a.title() == "Gift":
            letters = "ADD"
        else:
            letters = a[0].upper()
    
    code = letters + str(f"{number:03d}")
    return code

def add_new_blooms():
    global ordered_item_code, order_summary, menus, code_list, total, detail, order_code, cat, sales_hist
    item_codes = []
    catA = []
    number = 0
    for menu_name, items in menus.items():
        if menu_name == "A":
            for item in items:
                item_codes.append(item["code"])

    for menu_name, items in menus.items():
        if menu_name == "A":
            for item in items:
                if item["category"] in catA:
                    continue
                else:
                    catA.append(item["category"])

    while True:
        print("\nPlease select a number.")
        print("1) Auto-generate item code")
        print("2) Manually enter item code")
        choice = input("Number: ")
        print("_" * 150)
        if choice not in ["1", "2"]:
            print("Please enter 1 or 2.")
        elif choice == "1":
            while True:
                categorys = input("\nPlease enter a category: ").title()
                if categorys not in catA:
                    print(f"Please enter {' or '.join(catA)}")
                    continue
                else:
                    break
            code = auto_generate(categorys)
            while True:
                new_bloom = input("\nPlease enter new blooms details in format (item name,price,rate,status) or 0 to go back.\n").title()
                if new_bloom == "0":
                    back_to_menu("2")
                    return 
                else:
                    print("_" * 150)
                    new_blooms = new_bloom.split(",")
                    new_blooms = f"{code},{new_blooms[0]},{categorys},{','.join(new_blooms[1:])}"
                    new_blooms = new_blooms.split(",")
                    if len(new_blooms) == 6:
                        new_blooms[2] = categorys
                        new_blooms = {
                            "code" : new_blooms[0].upper(),
                            "name" : new_blooms[1],
                            "category" : new_blooms[2],
                            "price" : new_blooms[3],
                            "rate" : new_blooms[4],
                            "status" : new_blooms[5],
                        }
                        for menu_name, items in menus.items():
                            if menu_name == "A":
                                for item in items:
                                    if item["category"] != new_blooms["category"]:
                                        number += 1
                                    else:
                                        for menu_name, items in menus.items():
                                            for item in items:
                                                if item["category"] == new_blooms["category"]:
                                                    number += 1
                                        menus["A"].insert(number, new_blooms)
                                        break
                        break
                    else:
                        print("\nInvalid format!")
                        continue
            break
        else:
            while True:
                new_bloom = input("\nPlease enter new blooms details in format (item code,item name,category,price,rate,status) or 0 to go back.\n").title()
                if new_bloom == "0":
                    back_to_menu("2")
                    return 
                else:
                    print("_" * 150)
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
                            ref(new_bloom["code"], "A") # to give a recomment item code if when user add new item and the item code is repeated
                            continue
                        else:
                            if new_bloom["category"] not in catA:
                                print("Invalid category, please check your spelling or add new category")
                                continue
                            else:
                                menus["A"].insert(number, new_bloom)
                                break
                    else:
                        print("\nInvalid format!")
                        continue
            break

    print()
    print_w_menu("A")
    print_a_menu("B")
    print("Add successful!\n")
    print_out_menu("A") 
    print_out_menu("B")
    print()
    print("_" * 150)
    back_to_menu("1")

def view_update_addon():
    global ordered_item_code, order_summary, menus, code_list, total, detail, order_code, cat, sales_hist
    
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
                        print()
                        title()
                        print("|" + f"{item['code']}".center(max_len('code') + 2) + "|" + f"{item['name']}".center(max_len('name') + 2) + "|" + f"{item['category']}".center(max_len('category') + 2) + "|" + f"{item['price']}".center(9) + "|" + f"{item['rate']}".center(7) + "|" + f"{item['status']}".center(max_len('status') + 2) + "|")
                        
                        while True:
                            print()
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
                                print("\nUpdate successful!\n")
                                print_out_menu("A")
                                print_out_menu("B")
                                print()
                                print("_" * 150)
                                back_to_menu("1")
                                return
                            else:
                                print("Invalid format")
                                continue
            else:
                continue
        if found:
            return
        else:
            print("Invalid item code, please enter a valid item code.")

def add_new_addon():
    global ordered_item_code, order_summary, menus, code_list, total, detail, order_code, cat, sales_hist
    item_codes = []
    catB = []
    for menu_name, items in menus.items():
        if menu_name == "B":
            for item in items:
                item_codes.append(item["code"])
    
    for menu_name, items in menus.items():
        if menu_name == "B":
            for item in items:
                if item["category"] in catB:
                    continue
                else:
                    catB.append(item["category"])

    while True:
        print("\nPlease select a number.")
        print("1) Auto-generate item code")
        print("2) Manually enter item code")
        choice = input("Number: ")
        if choice not in ["1", "2"]:
            print("Please enter 1 or 2.")
            print("_" * 150)
            continue
        elif choice == "1":
            print("_" * 150)
            while True:
                categorys = input("\nPlease enter a category: ").title()
                if categorys not in catB:
                    print(f"Please enter {' or '.join(catB)}")
                    continue
                else:
                    break
            code = auto_generate('Gift')
            while True:
                new_addon = input("\nPlease enter new add on details in format (item name,price,rate,status) or 0 to go back.\n").title()
                if new_addon == "0":
                    back_to_menu("2")
                    return 
                else:
                    print("_" * 150)
                    new_addons = new_addon.split(",")
                    new_addons = f"{code},{new_addons[0]},Gift,{','.join(new_addons[1:])}"
                    new_addons = new_addons.split(",")
                    if len(new_addons) == 6:
                        new_addons = {
                            "code" : new_addons[0].upper(),
                            "name" : new_addons[1],
                            "category" : new_addons[2],
                            "price" : new_addons[3],
                            "rate" : new_addons[4],
                            "status" : new_addons[5],
                        }
                        menus["B"].append(new_addons)
                        break
                    else:
                        print("\nInvalid format!")
                        continue
            break
        else:
            while True:
                new_addon = input("\nPlease enter new add on details in format (item code,item name,category,price,rate,status) or 0 to go back.\n").title()
                print("_" * 150)
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
                            ref(new_addon["code"], "B") # to give a recomment item code if when user add new item and the item code is repeated
                            continue
                        else:
                            if new_addon["category"] not in catB:
                                print("Invalid category, please check your spelling or add new category")
                            else:
                                menus["B"].append(new_addon)
                                break
                    else:
                        print("\nInvalid format!")
                        continue
        break
        
    print()
    print_w_menu("A")
    print_a_menu("B")
    print("Add successful!\n")
    print_out_menu("A")
    print_out_menu("B")
    print()
    print("_" * 150)
    back_to_menu("1")

def back_to_menu(a): # a is to choose go back to which menu
    if a == "1":
        print("\nPlease select a number.")
        print("1) Inventory management")
        print("2) Sales management")
        print("3) Quit the program")
        while True:
            option = input("Please enter a number 1 or 2 or 3. ")
            if option not in ["1", "2", "3"]:
                print("Please enter 1 or 2 or 3. ")
            elif option == "1":
                print("_" * 150)
                inventory_management()
                return
            elif option == "2":
                print("_" * 150)
                sale_management()
                return
            else:
                return
    elif a == "2":
        print("_" * 150)
        inventory_management()
        return
    elif a == "3":
        print("_" * 150)
        sale_management()
        return
    elif a == "4":
        create_order()
        return
    elif a == "5":
        print("_" * 150)
        print("\nCategory:")
        number = 1
        for i in cat:
            print(f"{number}) {i}")
            number += 1
        print(f"{number}) Go back to previous page")
        number += 1
        print(f"{number}) Back to main menu")
        option1()
        return
    elif a == "6":
        print("_" * 150)
        edit_order()

def sale_management():
    print("\nPlease select a number.")
    print("1) Create order")
    print("2) View order")
    print("3) Sales history")
    print("4) Back to previous page")
    while True:
        option = input("Please enter a number: ")
        if option not in ["1", "2", "3", "4"]: 
            print("Please enter 1 or 2 or 3 or 4.")
        elif option == "1":
            create_order()
            return
        elif option == "2":
            view_order()
            return
        elif option == "3":
            history()
            return
        else:
            back_to_menu("1")
            return

def history():
    print("_" * 150)
    print()
    while True:
        print("Want to clear sales history?")
        print("1) Yes")
        print("2) No")
        print("3) Go back previous page")
        clear = input("Please select a number: ")
        if clear not in ["1", "2", "3"]:
            print("Please select a number 1 or 2 or 3.")
        elif clear == "1":
            with open('sales_history.txt', 'w') as historys:
                back_to_menu("3")
                return
        elif clear == "2":
            while True:
                try:
                    date = input("Enter date (YYYY-MM-DD): ")
                    date = datetime.datetime.strptime(date, "%Y-%m-%d")
                    break
                except Exception:
                    print("Invalid date format")
                    continue
            break
        else:
            back_to_menu("3")
            return

    print("_" * 150)
    print()
    date_line = []
    with open('sales_history.txt', 'r') as historys:
        lines = historys.readlines()

    found = False
    for i, line in enumerate(lines):
        if line.strip() == f"Date: {date.strftime('%Y-%m-%d')}":
            found = True
            date_line.append(i)
            for next in lines[i + 1 : i + 3]:
                print(next.strip())
            print()
        else:
            continue
    if not found:
        print(f"No record found for {date}.")
        history()
        return

    found_order = False
    while True:
        order = input("Please enter order code you want check: ").upper()
        print("_" * 150)
        print()
        for i in date_line:
            if lines[i + 2] == f"Order: {order}" or lines[i].startswith("Date:"):
                found_order = True
                for next in lines[i : i + 12]:
                    print(next.strip())
                back_to_menu("3")
                return
            if not found_order:
                print("Order not found")
                continue
        break
    
    back_to_menu("3")
    return

def sale_historys(a):
    with open('sales_history.txt', 'a') as history:
        for key, value in a.items():
            if isinstance(value, list):
                value = ", ".join(map(str, value))
            history.write(f"{key}: {value}\n")
        history.write("\n")

def create_order():
    global ordered_item_code, order_summary, menus, code_list, total, detail, order_code, cat, sales_hist
    print()
    print_out_menu("A")
    print_out_menu("B")
    print("_" * 150)
    print("\nPlease select a number.")
    print("1) Filter products by category")
    print("2) Sort products by price") 
    print("3) Sort products by rating")
    print("4) Order item")
    print("5) Back to previous page")
    print("6) Back to main menu")
    while True:
        option = input("Number: ")
        if option not in ["1", "2", "3", "4", "5", "6"]: 
            print("Please enter a number 1 or 2 or 3 or 4 or 5 or 6.")
        elif option == "1":
            print("_" * 150)
            print("\nCategory:")
            number = 1
            for i in cat:
                print(f"{number}) {i}")
                number += 1
            print(f"{number}) Go back to previous page")
            number += 1
            print(f"{number}) Back to main menu")
            option1()
            return
        elif option == "2":
            print("_" * 150)
            print("\nPlease select a number.") 
            print("1) Cheapest to most expensive")
            print("2) Most expensive to cheapest")
            print("3) Back to previous page")
            print("4) Back to main menu")
            while True:
                order = input("Please select a number: ")
                if order not in ["1", "2", "3", "4"]:
                    print("Please select a correct number.")
                elif order == "1":
                    price_sort(order)
                    print("_" * 150)
                    while True:
                        continues = input("\nContinue create order? (y/n): ")
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
                    print("_" * 150)
                    while True:
                        continues = input("\nContinue create order? (y/n): ")
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
                    print("_" * 150)
                    back_to_menu("1")
                    return
        elif option == "3":
            print("_" * 150)
            print("\nPlease select a number.")
            print("1) Rate from 1 - 5")
            print("2) Rate from 5 - 1")
            print("3) Back to previous page")
            print("4) Back to main menu")
            while True:
                rate = input("Please select a number: ")
                if rate not in ["1", "2", "3", "4"]:
                    print("Please select a correct number.")
                elif rate == "1":
                    rate_sort(rate)
                    print("_" * 150)
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
            print("_" * 150)
            order_item("1")
            return
        elif option == "5":
            back_to_menu("3")
            return
        else:
            print("_" * 150)
            back_to_menu("1")
            return

def edit_order():
    while True:
        code = input("\nPlease enter a order code to edit order or 0 to go back: ").upper()
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
                            continue
                        if ans == "1":
                            codes["status"] = "Open"
                            detail[codes["code"]]["status"] = "Open"
                            view_order()
                            return
                        else:
                            back_to_menu("6")
                            return
                elif codes["status"] == "Open":
                    print()
                    print("1) Preparing")
                    print("2) Cancelled")
                    print("3) Go Back")
                    print("Current status is Open, want change to ready or cancelled?\nPlease select 1 or 2 or 3. ")
                    while True:
                        ans = input("Number: ")
                        if ans not in ["1", "2", "3"]:
                            print("Please select a number 1 or 2 or 3.")
                            continue
                        if ans == "1":
                            codes["status"] = "Preparing"
                            detail[codes["code"]]["status"] = "Preparing"
                            view_order()
                            return
                        elif ans == "2":
                            codes["status"] = "Cancelled"
                            detail[codes["code"]]["status"] = "Cancelled"
                            view_order()
                            return
                        else:
                            back_to_menu("6")
                            return
                elif codes["status"] == "Preparing":
                    print()
                    print("1) Ready")
                    print("2) Go Back")
                    print("Current status is Preparing, want change to ready?\nPlease select 1 or 2. ")
                    while True:
                        ans = input("Number: ")
                        if ans not in ["1", "2"]:
                            print("Please select a number 1 or 2.")
                            continue
                        if ans == "1":
                            codes["status"] = "Ready"
                            detail[codes["code"]]["status"] = "Ready"
                            view_order()
                            return
                        else:
                            back_to_menu("6")
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
                            continue
                        if ans == "1":
                            codes["status"] = "Preparing"
                            detail[codes["code"]]["status"] = "Preparing"
                            view_order()
                            return
                        elif ans == "2":
                            codes["status"] = "Closed"
                            detail[codes["code"]]["status"] = "Closed"
                            view_order()
                            return
                        else:
                            back_to_menu("6")
                            return
                elif codes["status"] == "Closed":
                    print()
                    print("Current status is Closed, can't change status.\nPlease enter 1 to continue. ")
                    while True:
                        ans = input("Number: ")
                        if ans != "1":
                            print("Current status is Closed, can't change status?\nPlease enter 1 to continue.")
                            continue
                        else:
                            view_order()
                            return
        if not found:
            print("Please enter a valid order code.")
        else:
            return

def view_order():
    global ordered_item_code, order_summary, menus, code_list, total, detail, order_code, cat, sales_hist
    print("_" * 150)
    print()
    for code in order_code:
        print(f"{code["code"]}\t{code["status"]}")
    print()
    print("Please select a number.")
    print("1) Edit/Cancel order")
    print("2) Filter order by status")
    print("3) View order")
    print("4) Go back to previous page")
    print("5) Back to main menu")
    while True:
        option = input("Please select a number: ")
        if option not in ["1", "2", "3", "4", "5"]:
            print("Please enter numer 1 or 2 or 3 or 4 or 5.")
        elif option == "1":
            print("_" * 150)
            edit_order()
            return
        elif option == "2":
            print("_" * 150)
            print("\nPlease select a number.")
            print("1) Preparing")
            print("2) Ready")
            print("3) Cancelled")
            print("4) Closed")
            print("5) Open")
            print("6) Go to previous page")
            while True:
                status = input("Please enter a number: ")
                if status not in ["1", "2", "3", "4", "5", "6"]:
                    print("Please enter number 1 or 2 or 3 or 4 or 5 or 6.")
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
                elif status == "5":
                    for code_stutus in order_code:
                        print()
                        if code_stutus["status"] == "Open":
                            print(f"{code_stutus["code"]}\t{code_stutus["status"]}")
                    edit_order()
                    return
                else:
                    view_order()
                    return
        elif option == "3":
            while True:
                print("_" * 150)
                codes = input("\nPlease enter a order code you want to check or 0 to go back: ").upper()
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
                            print(f"Order status:          {detail[codes]["status"]}")
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
            print("_" * 150)
            back_to_menu("1")
            return

def generate_order_code(): # to auto generate order code with using format BBO-23-XXXX, XXXX is a number, this funtion will auto add 1 when new order created
    year = str(datetime.date.today().year)[-2:] # to generate YY in order code "BBO-YY-XXXX"
    if order_code == []:
        return f"BBO-{year}-0001"
    else:
        last_code = order_code[-1]
        number = int(last_code["code"].split("-")[-1]) + 1 
        return f"BBO-{year}-{number:04d}"

def order_summarys(): # to print out the order item in order_summary
    global ordered_item_code, order_summary, menus, code_list, total, detail, order_code, cat, sales_hist
    title2()
    for item in order_summary:
        print("|" + f"{item['code']}".center(max_len('code') + 2) + "|" + f"{item['name']}".center(max_len('name') + 2) + "|" + f"{item['category']}".center(max_len('category') + 2) + "|" + f"{item['price']}".center(9) + "|")

def order_item(s): # is s != 1, then will skip print available item
    global ordered_item_code, order_summary, menus, code_list, total, detail, order_code, cat, sales_hist
    order_summary = []
    ordered_item_code = []
    print()
    if s == "1":
        item_code_list("A") # to print out available item in menu "A"
    while True:
        for menu_name, items in menus.items():
            for item in items:
                if item["status"] == "Available":
                    code_list.append(item["code"])
        order = input("Please enter the item code or 9 to finish order or 0 to go back: ").upper()
        if order not in code_list and order != "9" and order != "0":
            print("Please enter a valid item code")
        elif order == "9":
            print("_" * 150)
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
                                    print()
                                    item_code_list("A")
                                    break
                                else:
                                    for menu_name, items in menus.items():
                                        if menu_name == "B":
                                            for item in items:
                                                if order == item["code"]:
                                                    order_summary.append(item)
                                                    ordered_item_code.append(item["code"])
                                                    total += int(item["price"])
    if len(ordered_item_code) == 0:
        back_to_menu("4")
        return
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
    
    print("\n" + "Order Summary".center(66, "-") + "\n")
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
    print("\nMessage for recipient: \n"+ message)
    print()
    print("Delivery address     :\n" + address)
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
            with open('sales_history.txt', 'a') as history:
                history.write(f"\nDate: {datetime.datetime.today().strftime("%Y-%m-%d")}\n")
                history.write(f"Time: {datetime.datetime.now().time().strftime("%H:%M:%S")}\n")
                history.write(f"Order: {new_order_code}\n")
            order_code.append({"code":new_order_code, "status": "Open"})
            detail[new_order_code] = {
                "order item": ordered_item_code,
                "status": order_code[-1]["status"],
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
            sale_historys(detail[new_order_code])
            total = 0
            print("_" * 150)
            back_to_menu("1")
            return
        elif cfm == "2":
            new_order_code = generate_order_code()
            customer_name = input("Please enter customer name: ")
            recipient_name = input("Please enter recipient's name: ")
            message = input("Please enter message for recipient (max 300 character): ")
            with open('sales_history.txt', 'a') as history:
                history.write(f"\nDate: {datetime.datetime.today().strftime("%Y-%m-%d")}\n")
                history.write(f"Time: {datetime.datetime.now().time().strftime("%H:%M:%S")}\n")
                history.write(f"Order: {new_order_code}\n")
            order_code.append({"code":new_order_code, "status": "Open"})
            detail[new_order_code] = {
                "order item": ordered_item_code,
                "status": order_code[-1]["status"],
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
            print("_" * 150)
            sale_historys(detail[new_order_code])
            back_to_menu("1")
            return
        elif cfm == "3":
            print("_" * 150)
            back_to_menu("4")
            return

def main():
    print("\nWelcome to Beautiful Blooms")
    print("\nPlease select a number.")
    print("1) Inventory management")
    print("2) Sales management")
    print("3) Quit the program.")
    while True:
        option = input("Please enter a number 1 or 2 or 3. ")
        print("_" * 150)
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
