import dialogue


class Player:
    def __init__(self, base_combat, base_charisma):
        self.base_combat_lvl = base_combat
        self.gameboy_found = False
        self.gun_found = False
        self.amulet_found = False
        self.charisma = base_charisma
        self.talk_count = 0
        self.kill_count = 0
        self.backpack = []

    def set_base_combat_lvl(self, base_combat_lvl):
        self.base_combat_lvl = base_combat_lvl

    def get_base_combat_lvl(self):
        return self.base_combat_lvl

    def gain_base_combat_lvl(self, combat_lvl_gain):
        self.base_combat_lvl += combat_lvl_gain
        dialogue.update_textbox("Your combat level has increased. It is now level " + str(self.base_combat_lvl))

    def set_charisma(self, charisma):
        self.charisma = charisma

    def get_charisma(self):
        return self.charisma

    def gain_charisma(self, charisma_gain):
        self.charisma += charisma_gain
        dialogue.update_textbox("Your charisma has levelled up. It is now level " + str(self.charisma))

    def inc_talk_count(self):
        self.talk_count += 1

    def inc_kill_count(self):
        self.kill_count += 1
