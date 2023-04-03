class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory # needs to be an empty list by default
    
    # adds single item to inventory and returns item added
    def add(self, item):  
        self.inventory.append(item)
        return item
    
    # removes single item from invetory, returns item removed | if not matching item in inventory, method should return False
    def remove(self, item): 
        if item in self.inventory: 
            self.inventory.remove(item)
            return item
        return False

    # this is described as a function and not a method - why? 
    def get_by_id(id):
        pass    
        # returns item with matching id from inventory
        # if no matching item, then explicitly return None


# instantiate a list and optionally pass in a list with keyword arg named inventory
# vendor_example = Vendor(inventory=[])   

# ******************************************
# just wanted to write my code to see if i'm understanding how to do this project!!
# class Vendor:
#     def __init__(self, inventory=None):
#         # inventory empty list
#         if inventory is None:
#             self.inventory = []
#         else:
#             self.inventory = inventory

#     # add item to inventory
#     def add(self, item):
#         self.inventory.append(item)
#         return item
    
#     # remove the item from inventory  
#     def remove(self, item):
#         if item in self.inventory:
#             self.inventory.remove(item)
#             return item
#         # unless the item isn't there... return false
#         else:
#             return False