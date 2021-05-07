import dialogue


class Item:
    def __init__(self, item_name, item_description, item_damage):
        self.name = item_name
        self.description = item_description
        self.damage = item_damage
        self.craft_item = None
        self.craft_result = None
        self.gem = False

    def set_craft_item(self, craft_item):
        self.craft_item = craft_item

    def set_craft_result(self, craft_result):
        self.craft_result = craft_result

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def announce(self):
        dialogue.update_textbox("There is a " + self.name)

    def describe(self):
        dialogue.update_textbox(self.description)

    def craft(self, other_item):
        if other_item.name == self.craft_item:
            dialogue.update_textbox("You successfully crafted " + self.craft_result)
            return self.craft_result
        else:
            return None


class Glove(Item):
    def __init__(self, item_name, item_description, item_damage):
        super().__init__(item_name, item_description, item_damage)
        self.damage = item_damage
        self.gems = []

    def craft(self, other_item):
        if other_item.gem:
            dialogue.update_textbox("You place the " + other_item.name +
                                    " into a depression on the glove. The glove feels much more powerful")
            self.gems.append(other_item.name)
            dialogue.update_textbox("The glove now holds the following gems:\n"
                                    + ', '.join(self.gems))
            if len(self.gems) == 4:
                dialogue.update_textbox("All of the stones are in place. The glove sparkles and vibrates. "
                                        "You have come so far... "
                                        "It's time... ")
                self.damage = 999999999
                print("DEBUG: glove is fully formed.")
                return self.name
            self.damage += 1
            print("DEBUG: damage is now ", self.damage)
            return self.name
        else:
            return None
