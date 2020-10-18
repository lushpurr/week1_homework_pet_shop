import pdb

# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(shop):
    return shop["name"]

def get_total_cash(shop):
    return shop["admin"]["total_cash"]

def add_or_remove_cash(shop, amount):
    shop["admin"]["total_cash"] = get_total_cash(shop) + amount

def get_pets_sold(shop):
    return shop["admin"]["pets_sold"]

def increase_pets_sold(shop, pet_sold_increase):
    shop["admin"]["pets_sold"] = get_pets_sold(shop) + pet_sold_increase

def get_stock_count(shop):
    return len(shop["pets"])

def get_pets_by_breed(shop, breed):
    pet_list = []
    for pet in shop["pets"]:
        if pet["breed"] == breed:
            pet_list.append(pet)
    return pet_list


def find_pet_by_name(shop, pet_name):
    for pet in shop["pets"]:
        if pet["name"] == pet_name:
            return pet

def remove_pet_by_name(shop,pet_name):
    for pet in shop["pets"]:
        if pet["name"] == pet_name:
            shop["pets"].remove(pet)
        
def add_pet_to_stock(shop, new_pet):
    shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, amount):
    customer["cash"] -= amount
    return customer["cash"]

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)
    return len(customer["pets"])


# check customers "cash" and compare it with price of pet
# if cash is >= pet "price"
# return true

def customer_can_afford_pet(customers, new_pet):
    for customer in customers:
        if customers["cash"] >= new_pet["price"]:
            return True
        else:
            return False
    

def sell_pet_to_customer(shop, new_pet, customer):
    add_pet_to_customer(customer, new_pet)
    increase_pets_sold(shop, 1) #?
    remove_customer_cash(customer, new_pet["price"])
    add_or_remove_cash(shop, new_pet["price"])







# add the pet to the customers pet list
# 12:30
# increase the pet shops number of pets sold
# 12:31
# take the price of the pet off of the customers cash amount
# 12:31
# add the price of the pet onto the pet shops total cash amount





    # pdb.set_trace()





