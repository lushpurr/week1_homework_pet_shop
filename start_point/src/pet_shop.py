# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(list):
    return list["name"]

def get_total_cash(list):
    return list["admin"]["total_cash"]

def add_or_remove_cash(list, amount):
    list["admin"]["total_cash"] = get_total_cash(list) + amount


def get_pets_sold(list):
    return list["admin"]["pets_sold"]

# def increase_pets_sold(list, pets_increase): #append pets_sold by 2
#     return list["admin"]["pets_sold"].append(pets_increase)
