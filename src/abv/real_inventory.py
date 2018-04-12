from abv.style_db import StyleDB
from abv.beer import Beer


class Inventory:
    def __init__(self):
        self.inventory = []

        tanczos_inventory =  MostRecentFile()
        style_db = StyleDB()

        for beer in tanczos_inventory:
            style = style_db.get_style(beer.name)
            full_beer = Beer(beer.name,beer.size,style,beer.price,beer.quantity)
            self.inventory.append(full_beer)

    def get_historic_inventory(self):
        return self.inventory
