# import uuid 
from swap_meet.item import Item


class Clothing(Item):
    def __init__(self, id = None, fabric="Unknown", condition = 0): 
        super().__init__(id, condition)
        # self.id = id
        self.fabric = fabric

    def __str__(self):
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."

