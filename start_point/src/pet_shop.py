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

def get_customer_cash(shop):
    return shop["cash"]

def remove_customer_cash(shop, amount):
    shop["cash"] -= amount
    return shop["cash"]

def get_customer_pet_count(shop):
    return len(shop["pets"])

def add_pet_to_customer(shop, new_pet):
    shop["pets"].append(new_pet)
    return len(shop["pets"])



# Simpler version:
# def all_favourite_foods(people):
#   favourite_foods = []
#   for person in people:
#     favourite_foods.extend(person["favourites"]["snacks"])
  
#   return favourite_foods


