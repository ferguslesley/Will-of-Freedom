import dialogue


class Character:
    # create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.choices = None
        self.item = None
        self.favourite_thing = None
        self.bribe_reward = None
        self.talk_reward = None
        self.dead = None

    # describe this character
    def describe(self):
        dialogue.update_textbox("\n")
        dialogue.update_textbox(self.name + " is here!")
        dialogue.update_textbox(self.description)

    # set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # talk to this character
    def talk(self):
        if self.conversation is not None:
            for i in self.conversation:
                dialogue.update_textbox("[" + self.name + " says] " + i)
            dialogue.update_textbox(self.name + " leaves you alone")
            if self.talk_reward is not None:
                return 'reward'
            else:
                return 'nothing'
        else:
            dialogue.update_textbox(self.name + " does not want to talk.")
            return 'silent'

    # player talks to character
    def player_talk(self, player_charisma, choice):
        pass

    # fight with this character
    def fight(self, item, item_damage, player_base_combat_lvl):
        dialogue.update_textbox("You brutally murder "
                                + self.name +
                                ", who was completely defenseless, with the " + item)
        self.dead = True
        return True

    # bribe this character
    def bribe(self, bribe_item):
        if bribe_item == self.favourite_thing:
            dialogue.update_textbox("You bribe " + self.name + " with the " + bribe_item)
            return True
        elif self.favourite_thing is None:
            dialogue.update_textbox("This enemy cannot be bribed")
            return False
        else:
            dialogue.update_textbox(self.name + " refuses your bribe of " + bribe_item)
            return False

    # set item given by character
    def set_item(self, item):
        self.item = item

    # character gives an item
    def get_item(self):
        return self.item

    # character drops an item
    def drop(self):
        dialogue.update_textbox("From its corpse, you find a " + self.item)

    # set character's favourite thing
    def set_favourite_thing(self, favourite_thing):
        self.favourite_thing = favourite_thing

    # return character's favourite thing
    def get_favourite_thing(self):
        return self.favourite_thing

    # set reward for bribing character
    def set_bribe_reward(self, bribe_reward):
        self.bribe_reward = bribe_reward

    # get reward for bribing character
    def get_bribe_reward(self):
        dialogue.update_textbox(self.name + " gives you a " + self.bribe_reward + " in return")

    def set_talk_reward(self, talk_reward):
        self.talk_reward = talk_reward

    def get_talk_reward(self):
        dialogue.update_textbox(self.name + " gives you a " + self.talk_reward + " as a reward")


class Enemy(Character):
    # create an enemy
    def __init__(self, char_name, char_description, combat_lvl, charisma):
        super().__init__(char_name, char_description)
        self.weakness = None
        self.combat_lvl = combat_lvl
        self.charisma = charisma
        self.scared = False

    # set enemy's weakness
    def set_weakness(self, weakness):
        self.weakness = weakness

    # return enemy's weakness
    def get_weakness(self):
        return self.weakness

    # set enemy scared or not (true/false)
    def is_scared(self, boolean):
        self.scared = boolean

    # fight the enemy
    def fight(self, item, item_damage, player_base_combat_lvl):
        player_combat_lvl = player_base_combat_lvl + item_damage
        if item == self.weakness:
            dialogue.update_textbox("You eliminate " + self.name + " with the " + item)
            return True
        elif player_combat_lvl >= self.combat_lvl < 9999:
            dialogue.update_textbox("You fend off " + self.name + " with the " + item)
            return True
        elif player_combat_lvl > 99999:
            return True
        else:
            dialogue.update_textbox(self.name + " crushes you, puny adventurer")
            return False

    # bribe the enemy
    def bribe(self, bribe_item):
        if bribe_item == self.favourite_thing:
            dialogue.update_textbox("You bribe " + self.name + " with the " + bribe_item)
            dialogue.update_textbox("the enemy leaves you alone")
            return True
        elif self.favourite_thing is None:
            dialogue.update_textbox("This enemy cannot be bribed")
            return False
        else:
            dialogue.update_textbox(self.name + " refuses your bribe of " + bribe_item + " and attacks you")
            return 'attack'

    # talk to the enemy
    def talk(self):
        if self.conversation is not None:
            for i in self.conversation[0]:
                dialogue.update_textbox("[" + self.name + " says] " + i)  # print all dialogue in index 0
            dialogue.update_textbox("\nChoose:")
            for x in self.choices:
                dialogue.update_textbox(x)
        else:
            dialogue.update_textbox("The enemy does not want to talk.")
            return 'silent'

    # player talks to enemy
    def player_talk(self, player_charisma, choice):
        try:
            choice = int(choice)
        except ValueError:
            dialogue.update_textbox("\nChoose:")
            for x in self.choices:
                dialogue.update_textbox(x)
            print("DEBUG: ValueError")
            return "bad_input"
        # determine outcomes
        if choice == 1:
            for i in self.conversation[1]:
                dialogue.update_textbox(("[" + self.name + " says]" + i))
            return "fight"  # choice 1 always results in a fight
        if choice == 2:
            if player_charisma >= self.charisma:
                for i in self.conversation[2]:
                    dialogue.update_textbox(("[" + self.name + " says]" + i))
                dialogue.update_textbox(self.name + " is done talking")  # choice 2 either results in:
                if self.talk_reward is not None:
                    return "enemy_reward"  # a reward, if the character has one
                else:
                    if self.scared:
                        return "flee"  # the enemy fleeing, if it has no reward.
                    else:
                        return "stay"  # the enemy staying in the room, if it has no reward and isn't scared
            else:
                for i in self.conversation[3]:
                    dialogue.update_textbox(("[" + self.name + " says]" + i))
                return "fight"  # a fight, if player does not meet charisma requirement.
        else:
            dialogue.update_textbox("\nChoose:")
            for x in self.choices:
                dialogue.update_textbox(x)
            print("DEBUG: wrong number")
            return "bad_input"


class PacifistWill(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.node = None

    def set_node(self, node):
        self.node = node
