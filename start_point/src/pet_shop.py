import pdb

# WRITE YOUR FUNCTIONS HERE

# return pet shop name
def get_pet_shop_name(shop):
    return shop["name"]
# return total cash 
def get_total_cash(shop):
    return shop["admin"]["total_cash"]

# add or remove cash to total cash
def add_or_remove_cash(shop, amount):
    shop["admin"]["total_cash"] = get_total_cash(shop) + amount

# return number of pets sold
def get_pets_sold(shop):
    return shop["admin"]["pets_sold"]

# increase number of pets sold
def increase_pets_sold(shop, pet_sold_increase):
    shop["admin"]["pets_sold"] = get_pets_sold(shop) + pet_sold_increase

# return stock count
def get_stock_count(shop):
    return len(shop["pets"])

# return number of pets of same breed
def get_pets_by_breed(shop, breed):
    pet_list = []
    for pet in shop["pets"]:
        if pet["breed"] == breed:
            pet_list.append(pet)
    return pet_list

# return pet by name
def find_pet_by_name(shop, pet_name):
    for pet in shop["pets"]:
        if pet["name"] == pet_name:
            return pet

# remove pet by name
def remove_pet_by_name(shop,pet_name):
    for pet in shop["pets"]:
        if pet["name"] == pet_name:
            shop["pets"].remove(pet)

# add pet to stock        
def add_pet_to_stock(shop, new_pet):
    shop["pets"].append(new_pet)

# return customer cash
def get_customer_cash(customer):
    return customer["cash"]

# return customer cash - amount
def remove_customer_cash(customer, amount):
    customer["cash"] -= amount
    return customer["cash"]

# return customer pet count
def get_customer_pet_count(customer):
    return len(customer["pets"])

# add new pet to customer pet list
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
    
# if pet is in shop and customer can afford pet
# add pet to customers pet list
# increase number of pets sold
# remove price form customers cash
# add price to pet shops total cash
# pdb.set_trace()
def sell_pet_to_customer(shop, pet, customer):
    if pet != None:
        if find_pet_by_name(shop, pet["name"]) != None  and customer_can_afford_pet(customer, pet) == True:
            add_pet_to_customer(customer, pet)
            increase_pets_sold(shop, len(customer["pets"])) 
            remove_customer_cash(customer, pet["price"])
            add_or_remove_cash(shop, pet["price"])







