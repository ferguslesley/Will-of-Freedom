import dialogue


class Room:
    # Create a class
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None
        self.locked = False
        self.unlock_item = None

    def get_name(self):
        return self.name

    def set_description(self, room_description):
        self.description = room_description

    def get_description(self):
        return self.description

    def describe(self):
        dialogue.update_textbox("You enter the " + self.name)
        dialogue.update_textbox(self.description)

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        dialogue.update_textbox("\n")
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            dialogue.update_textbox("The " + room.get_name() + " is " + direction)

    def set_character(self, character):
        self.character = character

    def get_character(self):
        return self.character
    
    def set_item(self, item):
        self.item = item

    def get_item(self):
        return self.item

    def set_unlock_item(self, unlock_item):
        self.unlock_item = unlock_item

    def get_unlock_item(self):
        return self.unlock_item

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            dialogue.update_textbox("You cannot go that way")
            return self

    def unlock(self, unlock_item):
        if unlock_item == self.unlock_item:
            dialogue.update_textbox("You use the "+unlock_item+" to open the door")
            self.locked = False
