import csv

inv = {'rope': 1, "torch": 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
zsák = {'kötél': 1, 'valami': 6, 'pénz': 2, 'alma': 1, 'arrow': 12}

def display_inventory(inventory):
    print("Inventory:")
    total = (sum(inventory.values()))
    for key, value in inventory.items():
        print(value, key)
    print(f"Total number of items: {total}")

def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory.keys():
            inventory[item] += 1
        else:
            inventory[item] = 1

def print_table(inventory, order=None):
    total = (sum(inventory.values()))
    if order == "desc":
        inventory = sorted(inventory.items(), reverse = True, key = lambda k: k[1])
        print("Inventory:\n" + "count".rjust(7) + "item name".rjust(15))
        print('-'*20)
        for key, value in inventory:
            print(str(value).rjust(5) + key.rjust(15))
        print('-' * 20,f"\nTotal number of items: {total}")
    elif order == "asc":
        inventory = sorted(inventory.items(), key = lambda k: k[1])
        print("Inventory:\n" + "count".rjust(5) + "item name".rjust(15))
        print('-' * 20)
        for key, value in inventory:
            print(str(value).rjust(5) + key.rjust(15))
        print('-' * 20,f"\nTotal number of items: {total}")
    else:
        print("Inventory:\n" + "count".rjust(7) + "item name".rjust(15))
        print('-'*20)
        for key, value in inventory.items():
            print(str(value).rjust(5) + key.rjust(15))
        print('-' * 20,f"\nTotal number of items: {total}")

def import_inventory(inventory, filename="import_inventory.csv"):
    csvfile = open(filename)
    reader = csv.reader(csvfile)
    for added_items in reader:
        add_to_inventory(inventory, added_items)
        


def export_inventory(inventory, filename="export_inventory.csv"):
    new_inv = []
    for k, v in inventory.items():
        new_inv.extend([k] * v)
    with open(filename, "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(new_inv)
    csvfile.close()
          
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
add_to_inventory(inv, dragon_loot)
import_inventory(inv,filename="import_inventory.csv") 
print_table(inv, 'asc')
export_inventory(inv, filename="export_inventory.csv")