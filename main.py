#   Imports ------------------------------------------------------------------------------------------------------------

import random
from character import *
from item import *
from player import Player
from room import Room
from window import *
from graph import GraphNode
import time

#   Debug --------------------------------------------------------------------------------------------------------------

ALL_ITEMS = False
PACIFIST = False
GENOCIDAL = False
BORING = False
if ALL_ITEMS:
    print("DEBUG: Player has all items")
if PACIFIST:
    print("DEBUG: Player is pacifist")
if GENOCIDAL:
    print("DEBUG: Player is genocidal")
if BORING:
    print("DEBUG: Player is boring")


#   Room map -----------------------------------------------------------------------------------------------------------

# MAP 1
'''
column 0      column 1      column 2    column 3     column 4
             [ballroom] -> [library]     [boss1]             row 0
                  ^          ^  |           ^                
[kitchen] -> [dining hall]   |  |      > [cellar]  > [boss2] row 1
                \/           |  \/    /    \/               
             [bedroom]  -> [bathroom]    [boss3]             row 2
'''

# MAP 2
'''
 column 0          column 1          column 2          column 3           column 4
[dungeon room 2]  [dungeon room 4]  [dungeon room 7]  [dungeon room 10]  [dungeon room 13]   row 0

[dungeon room 1]  [dungeon room 5]  [dungeon room 8]  [dungeon room 11]  [dungeon room 14]   row 1

[dungeon room 3]  [dungeon room 6]  [dungeon room 9]  [dungeon room 12]  [dungeon room 15]   row 2
'''

#   Non-functioning (old) code -----------------------------------------------------------------------------------------

'''
# pygame GUI

pygame.init()

pygame.display.set_caption('Text Adventure')
window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('blue'))

is_running = True

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    window_surface.blit(background, (0,0))

    pygame.display.update()


# create *old* GUI map
window = tk.Tk()

for i in range(3):
    window.rowconfigure(i, weight=1, minsize=75)
    for j in range(5):
        window.columnconfigure(j, weight=1, minsize=75)
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Label(master=frame, text=room_positions[j][i])
        label.grid(row=i, column=j, padx=5, pady=5)

window.mainloop()


for i in range(3):
    f2.rowconfigure(i, weight=1, minsize=75)
    for j in range(5):
        f2.columnconfigure(j, weight=1, minsize=75)
        f2.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Label(master=f2, text=room_positions[j][i])
        label.pack(padx=5, pady=5)

Label(f3, text='FRAME 3').pack()
Button(f3, text='Go to frame 1', command=lambda: raise_frame(f1)).pack()
'''

#   Create rooms -------------------------------------------------------------------------------------------------------

kitchen = Room("Kitchen")
kitchen.set_description("A disgusting food preparation room. it reeks of sweat, blood and tears.")

dining_hall = Room("Dining Hall")
dining_hall.set_description("It appears fine meals were once eaten here")

ballroom = Room("Ballroom")
ballroom.set_description("A room full of balls")

library = Room("Library")
library.set_description("Dusty bookshelves stretch on for what seems like miles")

bedroom = Room("Bedroom")
bedroom.set_description("A large bedroom, the bed still has a dent from someone sleeping in it.")

bathroom = Room("Bathroom")
bathroom.set_description("The room looks filthy. The floor is wet.")
bathroom.locked = True
bathroom.set_unlock_item("handle")

cellar = Room("Cellar")
cellar.set_description("A dark, dank cellar. The floor is made of dirt")

bossroom1 = Room("BOSS ROOM")
bossroom1.set_description("THE FINAL ROOM")
bossroom1.locked = True
bossroom1.set_unlock_item("sock")

bossroom2 = Room("BOSS ROOM")
bossroom2.set_description("THE FINAL ROOM")
bossroom2.locked = True
bossroom2.set_unlock_item("key")

bossroom3 = Room("BOSS ROOM")
bossroom3.set_description("THE FINAL ROOM")
bossroom3.locked = True
bossroom3.set_unlock_item("tear")


dungeonroom1 = Room("Dungeon Room")
dungeonroom1.set_description("A dusty room. The walls, ceiling and floor are all stone.")
dungeonroom2 = Room("Dungeon Room")
dungeonroom2.set_description("A dusty room. The walls, ceiling and floor are all stone.")
dungeonroom3 = Room("Dungeon Room")
dungeonroom3.set_description("A dusty room. The walls, ceiling and floor are all stone.")
dungeonroom4 = Room("Dungeon Room")
dungeonroom4.set_description("A dusty room. The walls, ceiling and floor are all stone.")
dungeonroom5 = Room("Dungeon Room")
dungeonroom5.set_description("A dusty room. The walls, ceiling and floor are all stone.")
dungeonroom6 = Room("Dungeon Room")
dungeonroom6.set_description("A dusty room. The walls, ceiling and floor are all stone.")
dungeonroom7 = Room("Dungeon Room")
dungeonroom7.set_description("A dusty room. The walls, ceiling and floor are all stone.")
dungeonroom8 = Room("Dungeon Room")
dungeonroom8.set_description("A dusty room. The walls, ceiling and floor are all stone.")
dungeonroom9 = Room("Dungeon Room")
dungeonroom9.set_description("A dusty room. The walls, ceiling and floor are all stone.")
dungeonroom10 = Room("Dungeon Room")
dungeonroom10.set_description("A dusty room. The walls, ceiling and floor are all stone.")
dungeonroom11 = Room("Dungeon Room")
dungeonroom11.set_description("A dusty room. The walls, ceiling and floor are all stone.")
dungeonroom12 = Room("Dungeon Room")
dungeonroom12.set_description("A dusty room. The walls, ceiling and floor are all stone.")
dungeonroom13 = Room("Dungeon Room")
dungeonroom13.set_description("A dusty room. The walls, ceiling and floor are all stone.")
dungeonroom14 = Room("Dungeon Room")
dungeonroom14.set_description("A dusty room. The walls, ceiling and floor are all stone.")
dungeonroom15 = Room("Dungeon Room")
dungeonroom15.set_description("A dusty room. The walls, ceiling and floor are all stone.")


#   Link rooms ---------------------------------------------------------------------------------------------------------

kitchen.link_room(dining_hall, "east")  # dining hall is east of kitchen
dining_hall.link_room(kitchen, "west")  # kitchen is west of dining hall

dining_hall.link_room(ballroom, "north")  # ballroom is north of dining hall
ballroom.link_room(dining_hall, "south")  # dining hall is south of ballroom

dining_hall.link_room(bedroom, "south")  # bedroom is south of dining hall
bedroom.link_room(dining_hall, "north")  # dining hall is north of bedroom

ballroom.link_room(library, "east")  # library is east of ballroom
library.link_room(ballroom, "west")  # ballrom is west of library

bedroom.link_room(bathroom, "east")  # bathroom is east of bedroom
bathroom.link_room(bedroom, "west")  # bedroom is west of bathroom

library.link_room(bathroom, "south")  # bathroom is south of library
bathroom.link_room(library, "north")  # libary is north of bathroom

library.link_room(cellar, "east")  # cellar is east of library
cellar.link_room(library, "west")  # library is west of cellar

cellar.link_room(bossroom1, "north")  # bossroom1 is north of cellar
cellar.link_room(bossroom2, "east")  # bossroom2 is east of cellar
cellar.link_room(bossroom3, "south")  # bossroom3 is south of cellar


dungeonroom1.link_room(dungeonroom2, "north")  # dungeonroom2 is north of dungeonroom1
dungeonroom2.link_room(dungeonroom1, "south")  # dungeonroom1 is south of dungeonroom2

dungeonroom1.link_room(dungeonroom3, "south")  # dungeonroom3 is south of dungeonroom1
dungeonroom3.link_room(dungeonroom1, "north")  # dungeonroom1 is north of dungeonroom3

dungeonroom2.link_room(dungeonroom4, "east")
dungeonroom4.link_room(dungeonroom2, "west")

dungeonroom1.link_room(dungeonroom5, "east")
dungeonroom5.link_room(dungeonroom1, "west")

dungeonroom3.link_room(dungeonroom6, "east")
dungeonroom6.link_room(dungeonroom3, "west")

dungeonroom4.link_room(dungeonroom5, "south")
dungeonroom5.link_room(dungeonroom4, "north")

dungeonroom5.link_room(dungeonroom6, "south")
dungeonroom6.link_room(dungeonroom5, "north")

dungeonroom4.link_room(dungeonroom7, "east")
dungeonroom7.link_room(dungeonroom4, "west")

dungeonroom5.link_room(dungeonroom8, "east")
dungeonroom8.link_room(dungeonroom5, "west")

dungeonroom6.link_room(dungeonroom9, "east")
dungeonroom9.link_room(dungeonroom6, "west")

dungeonroom7.link_room(dungeonroom8, "south")
dungeonroom8.link_room(dungeonroom7, "north")

dungeonroom8.link_room(dungeonroom9, "south")
dungeonroom9.link_room(dungeonroom8, "north")

dungeonroom7.link_room(dungeonroom10, "east")
dungeonroom10.link_room(dungeonroom7, "west")

dungeonroom8.link_room(dungeonroom11, "east")
dungeonroom11.link_room(dungeonroom8, "west")

dungeonroom9.link_room(dungeonroom12, "east")
dungeonroom12.link_room(dungeonroom9, "west")

dungeonroom10.link_room(dungeonroom11, "south")
dungeonroom11.link_room(dungeonroom10, "north")

dungeonroom11.link_room(dungeonroom12, "south")
dungeonroom12.link_room(dungeonroom11, "north")

dungeonroom10.link_room(dungeonroom13, "east")
dungeonroom13.link_room(dungeonroom10, "west")

dungeonroom11.link_room(dungeonroom14, "east")
dungeonroom14.link_room(dungeonroom11, "west")

dungeonroom12.link_room(dungeonroom15, "east")
dungeonroom15.link_room(dungeonroom12, "west")

dungeonroom13.link_room(dungeonroom14, "south")
dungeonroom14.link_room(dungeonroom13, "north")

dungeonroom14.link_room(dungeonroom15, "south")
dungeonroom15.link_room(dungeonroom14, "north")

#   Create characters --------------------------------------------------------------------------------------------------

dave = Enemy("Dave", "A decrepit zombie", 5, 0)
dave.set_weakness("cheese")
dave.set_item("shovel")
dave.set_favourite_thing("brain")
dave.is_scared(True)

john = Enemy("John", "An angry security guard", 8, 2)
john.set_favourite_thing("money")
john.set_item("library card")
john.is_scared(True)

remy = Enemy("Remy", "A giant rat, the size of a large horse. It seems rather intelligent.", 5, 0)
remy.set_favourite_thing("cheese")
remy.set_item("brain")
remy.set_bribe_reward("library card")

lucas = Character("Lucas", "A fellow adventurer, he seems friendly enough. He smells like a dog...")
lucas.set_favourite_thing("dog toy")
lucas.set_item("gameboy")
lucas.set_bribe_reward("gameboy")

will = Character("Will", "A poor gremlin, he's never seen the light of day")
will.set_favourite_thing("gameboy")
will.set_item("key")
will.set_bribe_reward("key")

janice = Enemy("Janice", "A kindly librarian, she seems eager to get your attention", 5, 3)
janice.set_favourite_thing("library card")
janice.set_bribe_reward("handle")
janice.set_item("handle")
janice.set_talk_reward("handle")


spider = Enemy("Spider", "A giant spider. It hisses at you menacingly. It looks fragile...", 9, 0)
spider.set_item("black jewel")
kobold = Enemy("Kobold", "A reptilian humanoid with a long tail. It weilds a spear. There is a fire within...", 10, 0)
kobold.set_item("cracked gem")
yeti = Enemy("Yeti", "An ape-like creature that thrives in the cold. It doesn't cope well in heat...", 11, 0)
yeti.set_item("ice opal")
will2 = Enemy("Will", "His eyes are black, with red pupils.. He has no mouth.. He is impossibly powerful...", 718920, 0)


#   Set conversations --------------------------------------------------------------------------------------------------

dave.conversation = [
    [
        # initial dialogue
        "GuuHhhH, Braiiinsss",
        "Youuu.. Haaave.. Brraiiins?"
    ],
    [
        # option 1 chosen
        "I...",
        "Eat...",
        "Your...",
        "Braaiiinn"
    ],
    [
        # option 2 chosen, skill check succeeded
        "Thaaank Yoouu",
        "I wiill gooo oover theere",
        "aand eeat braaaiin",
        "...for a really long tiime"
    ],
    [
        # option 2 chosen, skill check failed
        "This should never happen, as Dave's charisma stat is zero."
    ]
]

dave.choices = [
    "[1] Yes... I have a brain.",
    "[2] Yep, there's a brain over in the corner of the room. (1 Charisma Required)"
]

john.conversation = [
    [
        # initial dialogue
        "Oi! You There!",
        "You got a loisense to be here??"
    ],
    [
        # option 1 chosen
        "NO?? I'm gonna have to escort you out then!",
        "WITH A NIGHTSTICK!"
    ],
    [
        # option 2 chosen, skill check succeeded
        "I- err",
        "Please don't tell my boss!"
    ],
    [
        # option 2 chosen, skill check failed
        "YES I BLEEDIN DO",
        "I'M GONNA TEACH YOU NOT TO TALK TO AN OFFICER LOIKE THAT"
    ]
]

john.choices = [
    "[1] Err, no. Just passing through",
    "[2] Oi! You got a loisense to ask for my loisense?? (2 Charisma Required)"
]

janice.conversation = [
    [
        # initial dialogue
        "Oh! um, excuse me!",
        "You haven't signed in your book you borrowed!",
        "You'll either need to pay for that or give me back the book!"
    ],
    [
        # option 1 chosen
        "EXCUSE ME!?!?",
        "I'LL TAKE THAT BOOK FROM YOUR CORPSE"
    ],
    [
        # option 2 chosen, skill check succeeded
        "Oooh!",
        "Sorry dearie, I'm getting old you know..",
        "Here, I found this on the floor,",
        "You can take it, as a token of my apology."
    ],
    [
        # option 2 chosen, skill check failed
        "I'm not that stupid..",
        "GIVE ME BACK MY BOOK"
    ]
]

janice.choices = [
    "[1] Oh shut up, you old cow",
    "[2] You're making a mistake. I haven't taken any books. (3 Charisma Required)"
]

lucas.conversation = [
    "Hey, have you seen my dog?",
    "I've been looking everywhere for him",
    "I wish I had something to lure him out of hiding."
]

will.conversation = [
    "P-please don't hurt me..",
    "H-have you seen my gameboy?"
]

will_unlocked_conversation = [
    "Greetings, adventurer",
    "I am William.",
    "I watch over this house,",
    "Thank you for being peaceful to the creatures that dwell in this place",
    "I know they may seem hostile, so I am grateful.",
    "Venture north, you fill find the treasure you seek."
]
#   Create items -------------------------------------------------------------------------------------------------------

#   (name, description, attack value)
fists = Item("fists", "Your feeble fists", 1)
cheese = Item("cheese", "An old wedge of cheese. The label reads 'Warning: Harmful to undead'", 0)
gun = Item("gun", "It's just a gun, it shoots things.", 20)
money = Item("money", "A wad of dollar bills", 0)
shovel = Item("shovel", "A heavy, metal shovel", 5)
library_card = Item("library card", "A plastic library card - it might be useful for something", 0)
gameboy = Item("gameboy", "A Nintendo Gameboy - it seems barely functional", 0)
key = Item("key", "A rusty, old key", 0)
amulet = Item("amulet", "Edd's amulet. It looks to be thousands of years old. You sense it has immense power..", 99)
sock = Item("sock", "Will's dirty sock", 0)
dog_toy = Item("dog toy", "A dog chew toy.", 0)
brain = Item("brain", "Ew.. An actual brain.", 0)
handle = Item("handle", "A door handle.", 1)
tear = Item("tear", "A single one of Will's tears", 9999)

glove = Glove("glove",
              "A silver glove. It feels heavy. There are depressions on the back of the glove,"
              " as if something is missing.", 10)  # first item found.  kills spider

black_jewel = Item("black jewel",
                   "A dark jewel. You feel a sinister energy being emitted. If only you could harness it.",
                   0)  # dropped by spider
black_jewel.gem = True

time_stone = Item("time stone",
                  "The time stone. This can reverse damage caused by the elements. It can repair anything."
                  "It only has enough power to repair one item..", 0)  # found
time_stone.set_craft_item("cracked gem")
time_stone.set_craft_result("fire gem")

cracked_gem = Item("cracked gem",
                   "A cracked red gem. It has immense firey power, but it has been damaged.", 0)  # dropped by kobold
cracked_gem.set_craft_item("time stone")
cracked_gem.set_craft_result("fire gem")

fire_gem = Item("fire gem",
                "A red fire gem. It has immense firey power. It melts anything with an icy heart.", 0)
fire_gem.gem = True

air_diamond = Item("air diamond",
                   "A beautiful diamond. It has the unstoppable force of the wind.", 0)  # found
air_diamond.gem = True

ice_opal = Item("ice opal",
                "An opal, cold to the touch. It could freeze a thousand suns.", 0)  # dropped by yeti
ice_opal.gem = True


#   Create items dictionary + list -------------------------------------------------------------------------------------

items_dict = {
    "fists": fists,
    "cheese": cheese,
    "gun": gun,
    "money": money,
    "shovel": shovel,
    "library card": library_card,
    "gameboy": gameboy,
    "key": key,
    "amulet": amulet,
    "sock": sock,
    "tear": tear,
    "dog toy": dog_toy,
    "brain": brain,
    "handle": handle,
    "glove": glove,
    "black jewel": black_jewel,
    "time stone": time_stone,
    "cracked gem": cracked_gem,
    "fire gem": fire_gem,
    "air diamond": air_diamond,
    "ice opal": ice_opal
}

items_list = (
    "fists",
    "cheese",
    "gun",
    "money",
    "shovel",
    "library card",
    "gameboy",
    "key",
    "amulet",
    "sock",
    "dog toy",
    "brain",
    "handle",
    "glove",
    "black jewel",
    "time stone",
    "cracked gem",
    "fire gem",
    "air diamond",
    "ice opal"
)

#   Set room items and characters --------------------------------------------------------------------------------------

kitchen.set_item(cheese)
kitchen.set_character(remy)

dining_hall.set_item(money)
dining_hall.set_character(dave)

ballroom.set_character(john)

bedroom.set_character(lucas)

library.set_character(janice)

cellar.set_character(will)

bathroom.set_item(dog_toy)

dungeonroom2.set_item(glove)
dungeonroom9.set_item(time_stone)
dungeonroom7.set_item(air_diamond)

dungeonroom5.set_character(spider)
dungeonroom8.set_character(kobold)
dungeonroom11.set_character(yeti)
dungeonroom14.set_character(will2)
#   List of commands ---------------------------------------------------------------------------------------------------

command_list = [
    "look",
    "north, east, south, west",
    "talk",
    "fight",
    "bribe",
    "take",
    "dig",
    "quit"
]

#   Hints --------------------------------------------------------------------------------------------------------------

hint_list = (
    "Hint: It may be wise to avoid some interactions at first.",
    "Hint: Try looking at your surroundings",
    "Hint: There may be more than one way to approach an interaction",
    "Hint: You can explore all of the rooms",
    "Hint: Your actions may have consequences",
    "Hint: Remember to use help"

)

#   Pacifist Will Dialogue Tree ----------------------------------------------------------------------------------------

BOSS1 = PacifistWill("Will the peaceful", "A friendly gentleman.")

node1 = GraphNode("Hi there! \nI'm going to do a little job interview. \nHave you been having a good day?")

node2 = GraphNode("I'm glad :) \nAre you a motivated person?")

node3 = GraphNode("I'm sorry to hear that. \nDo you have any prior job experience?")

node4 = GraphNode("Interesting. \nAre you planning on having children?")

node5 = GraphNode("Interesting. \nHave you ever taken drugs?")

node6 = GraphNode("That's good to hear. \nShould I hire you?")

node7 = GraphNode("Noted. Thank you. \nDo you like cue cards?")

node8 = GraphNode("That is good. \nDo you like fallout?")

node9 = GraphNode("Okay. \nWhich is a legitimate state?")

node10 = GraphNode("That is disgusting. "
                   "\nWe do not allow degenerates who defile their bodies by consuming such filth."
                   "\nWe will not be hiring you.")

node11 = GraphNode("Wonderful!"
                   "\nCongratulations, you're hired.")

node12 = GraphNode("Ok!"
                   "\nYou're hired!")

node13 = GraphNode("Ok.")

node14 = GraphNode("Good, I can see you are organised."
                   "\nYou're hired.")

node15 = GraphNode("Please leave my presence.")

node16 = GraphNode("Wondeful! You are a man of culture."
                   "\nYou're hired!")

node17 = GraphNode("..."
                   "\nWe won't be hiring you.")

node18 = GraphNode("I think this interview is over."
                   "\nWe will not be hiring you.")

node19 = GraphNode("Wonderful, thank you for your time."
                   "\nYou are hired.")

node1.set_children([node2, node3])
node2.set_children([node4, node5])
node3.set_children([node6, node7])
node4.set_children([node8, node9])
node5.set_children([node10, node11])
node6.set_children([node12, node13])
node7.set_children([node14, node15])
node8.set_children([node16, node17])
node9.set_children([node18, node19])

node2.set_parent(node1)
node3.set_parent(node1)
node4.set_parent(node2)
node5.set_parent(node2)
node6.set_parent(node3)
node7.set_parent(node3)
node8.set_parent(node4)
node9.set_parent(node4)
node10.set_parent(node5)
node11.set_parent(node5)
node12.set_parent(node6)
node13.set_parent(node6)
node14.set_parent(node7)
node15.set_parent(node7)
node16.set_parent(node8)
node17.set_parent(node8)
node18.set_parent(node9)
node19.set_parent(node9)

node10.set_outcome("rejected")
node11.set_outcome("hired")
node12.set_outcome("hired")
node13.set_outcome("rejected")
node14.set_outcome("hired")
node15.set_outcome("rejected")
node16.set_outcome("hired")
node17.set_outcome("rejected")
node18.set_outcome("rejected")
node19.set_outcome("hired")

node1.set_arc_text(["[1] Yes",                        # Text leading to node 2
                    "[2] No"                          # Text leading to node 3
                    ])
node2.set_arc_text(["[1] Yes",                         # Text leading to node 4,
                    "[2] No"                          # Text leading to node 5
                    ])
node3.set_arc_text(["[1] Yes",                        # Text leading to node 6
                    "[2] No"                          # Text leading to node 7
                    ])
node4.set_arc_text(["[1] Yes",                        # Text leading to node 8
                    "[2] No"                          # Text leading to node 9
                    ])
node5.set_arc_text(["[1] Yes, I've had paracetamol",  # Text leading to node 10
                    "[2] No, never."                  # Text leading to node 11
                    ])
node6.set_arc_text(["[1] Yes",                        # Text leading to node 12
                    "[2] No"                          # Text leading to node 13
                    ])
node7.set_arc_text(["[1] Yes",                        # Text leading to node 14
                    "[2] No"                          # Text leading to node 15
                    ])
node8.set_arc_text(["[1] Yes",                        # Text leading to node 16
                    "[2] No"                          # Text leading to node 17
                    ])
node9.set_arc_text(["[1] Israel",                     # Text leading to node 18
                    "[2] Palestine"                   # Text leading to node 19
                    ])


def get_result(choice):
    try:
        choice = int(choice)
    except ValueError:
        print("DEBUG: ValueError")
        dialogue.update_textbox("Please choose either 1 or 2")
        return "bad_input"

    # determine outcomes
    if choice == 1:
        return 0
    if choice == 2:
        return 1
    else:
        print("DEBUG: wrong number")
        dialogue.update_textbox("Please choose either 1 or 2")
        return "bad_input"


def talk_tree(node, choice):
    global game_state
    result = get_result(choice)
    if result == "bad_input":
        new_node = node
    else:
        new_node = node.children[result]
    more_dialogue = new_node.print_question()
    if more_dialogue is False:
        game_state = new_node.outcome
        print("DEBUG: OUTCOME IS", game_state)
    return new_node


#   Riddle Will --------------------------------------------------------------------------------------------------------

attempts = 3
question = 0

riddles = ["David's Father has three sons: Snap, Crackle, and who?",
           "If you were running a race, and you passed the person in 2nd place, what place would you be in now?",
           "What gets more useful once broken?",
           "I have a head, a tail, but no body. What am I?"]

answers = [["David", "david"],
           ["2nd", "second", "Second", "2"],
           ["egg", "Egg", "an egg", "An egg", "An Egg", "an Egg"],
           ["coin", "a coin", "Coin", "A coin", "A Coin", "penny", "a penny", "Penny", "A Penny", "A penny"]]


def riddle_will():
    global will
    global riddles
    global question
    global game_state
    dialogue.update_textbox("You go through the door")
    dialogue.update_textbox("And find yourself in a cramped room containing two chairs")
    if will.dead:
        dialogue.update_textbox("One chair is empty, the other is occupied by")
        dialogue.update_textbox("*The Ghost of Will*")
    else:
        dialogue.update_textbox("One chair is empty, the other is occupied by Will")
    dialogue.update_textbox("Your task is to answer a series of riddles.")
    dialogue.update_textbox(riddles[question])
    game_state = 'riddle_will'


def guess(answer):
    global attempts
    global question
    global riddles
    global answers
    global game_state
    if attempts > 0:
        if answer in answers[question]:
            dialogue.update_textbox("Correct! Next question.")
            question += 1
            if question == 4:
                win_riddle()
            else:
                dialogue.update_textbox(riddles[question])
        else:
            attempts -= 1
            dialogue.update_textbox("Incorrect. You have " + str(attempts) + " attempts left")
    else:
        dialogue.update_textbox("You have failed to solve the riddles.")
        dialogue.update_textbox("As a result, you will rot in this cellar forever.")
        game_state = 'dead'


def win_riddle():
    global game_state
    dialogue.update_textbox("You have completed all of the riddles! Congratulations.")
    game_state = 'won'

#   Genocidal Will -----------------------------------------------------------------------------------------------------


def genocidal_will():
    global current_room
    global app
    app.destroy()
    app = App(parse, False)
    app.geometry("430x300")
    app.resizable(False, False)
    current_room = dungeonroom1
    player.backpack = ['fists']
    inventory.reset_items()
    command_list.append('craft')
    dialogue.update_textbox("(**WAIT FOR ROOM DESCRIPTION BEFORE ENTERING COMMANDS**)")
    dialogue.update_textbox("You go through the door")
    dialogue.update_textbox("And find yourself in a dark, dusty dungeon.")
    app.update()
    time.sleep(8)
    dialogue.update_textbox("\n")
    dialogue.update_textbox("Every room seems to look the same.")
    dialogue.update_textbox("It feels like you've gained a new skill")
    dialogue.update_textbox("Your backpack feels much lighter")
    app.update()
    time.sleep(6)
    dialogue.update_textbox("\n")
    dialogue.update_textbox("** You feel evil deep within the dungeon **")
    dialogue.update_textbox("** Your backpack is now empty **")
    dialogue.update_textbox("** You have gained the ability to craft **")
    app.update()
    time.sleep(4)
    dialogue.update_textbox("\n")
    current_room.describe()


#   Functions ----------------------------------------------------------------------------------------------------------


def move(direction):
    new_room = current_room.move(direction)
    if new_room.locked:
        dialogue.update_textbox("The door is locked.")
        if new_room.unlock_item in player.backpack:
            new_room.unlock(new_room.unlock_item)
            # describe the room
            new_room.describe()
            return new_room
        else:
            dialogue.update_textbox("You don't have the right item to unlock this door.")
            return current_room
    else:
        # describe the room
        new_room.describe()
        return new_room


def talk():
    global game_state
    if inhabitant is not None:
        result = inhabitant.talk()
        if result == 'nothing':  # no reward
            inhabitant.set_conversation(None)
            player.inc_talk_count()
            game_state = 'parse'

        elif result == 'reward':  # no reward
            inhabitant.get_talk_reward()
            player.backpack.append(inhabitant.talk_reward)
            inventory.update_item(inhabitant.talk_reward, 'add')
            current_room.set_character(None)
            player.inc_talk_count()
            game_state = 'parse'

        elif result == 'silent':  # no conversation
            game_state = 'parse'

        else:  # i.e. result is None (no return)
            game_state = 'talk'
    else:
        dialogue.update_textbox("There is no one to talk to")
        game_state = 'parse'
    print("DEBUG: after talk(), talk count is:", player.talk_count)


def player_talk(choice):
    global game_state
    if inhabitant is not None:
        # check outcomes
        result = inhabitant.player_talk(player.charisma, choice)

        if result == "fight":  # if skill check on enemy fails OR player chooses option 1
            dialogue.update_textbox("You start fighting " + inhabitant.name + "!!")
            dialogue.update_textbox("What do you fight with?")
            game_state = 'fight'

        elif result == "enemy_reward":  # if enemy has reward
            player.gain_charisma(1)
            inhabitant.get_talk_reward()
            player.backpack.append(inhabitant.talk_reward)
            inventory.update_item(inhabitant.talk_reward, 'add')
            current_room.set_character(None)
            player.inc_talk_count()
            game_state = 'parse'

        elif result == "flee":  # if enemy has no reward and is scared
            player.gain_charisma(1)
            current_room.set_character(None)
            player.inc_talk_count()
            game_state = 'parse'

        elif result == "stay":  # if enemy has no reward and isn't scared
            inhabitant.set_conversation(None)
            player.gain_charisma(1)
            player.inc_talk_count()
            game_state = 'parse'

        elif result == "reward":  # if character has reward
            inhabitant.get_talk_reward()
            player.backpack.append(inhabitant.talk_reward)
            inventory.update_item(inhabitant.talk_reward, 'add')
            current_room.set_character(None)
            player.inc_talk_count()
            game_state = 'parse'

        elif result == "bad_input":
            pass

        else:  # if character has no reward
            inhabitant.set_conversation(None)
            player.inc_talk_count()
            game_state = 'parse'

    else:
        dialogue.update_textbox("There's no one to talk to")
        game_state = 'parse'
    print("DEBUG: after player_talk(), talk count is:", player.talk_count)


def fight(weapon):
    global game_state
    if inhabitant is not None:
        fighting = True
        while fighting:
            if weapon not in player.backpack:
                dialogue.update_textbox("You don't have that")
                check_backpack()
                app.update()
                fighting = False
            else:
                weapon_obj = items_dict.get(weapon)
                weapon_damage = weapon_obj.damage

                # get outcome
                result = inhabitant.fight(weapon, weapon_damage, player.base_combat_lvl)
                if not result:
                    if inhabitant == will2:
                        dialogue.update_textbox("You were not strong enough...\n"
                                                "Only the strong can survive this gauntlet\n"
                                                "Will obliterates you...")
                    dialogue.update_textbox("You have died :( type quit")
                    game_state = 'dead'
                else:
                    if inhabitant == will2:
                        dialogue.update_textbox("You hold the glove, combined with all of the power stones.\n"
                                                "The glove shakes uncontrollably. The gems seem to morph together.\n"
                                                "A beam is sent out from the glove, shattering it instantly.\n"
                                                "The beam goes through Will's head.\n"
                                                "It is finished...")
                        game_state = 'genocide_won'
                        return
                    if inhabitant.item is not None:
                        inhabitant.drop()
                        player.backpack.append(inhabitant.item)
                        inventory.update_item(inhabitant.item, 'add')
                        drop_obj = items_dict.get(inhabitant.item)
                        drop_obj.describe()
                    current_room.set_character(None)
                    player.gain_base_combat_lvl(1)
                    player.inc_kill_count()
                    game_state = 'parse'
                fighting = False
    else:
        dialogue.update_textbox("There's no one to fight")
        game_state = 'parse'


def bribe(bribe_item):
    global game_state
    if inhabitant is not None:
        if bribe_item not in player.backpack:
            dialogue.update_textbox("You don't have that")
            game_state = 'parse'
        else:
            result = inhabitant.bribe(bribe_item)
            if result is True:
                player.backpack.remove(bribe_item)
                if inhabitant.bribe_reward is not None:
                    inhabitant.get_bribe_reward()
                    player.backpack.append(inhabitant.bribe_reward)
                    inventory.update_item(inhabitant.bribe_reward, 'add')
                current_room.set_character(None)
                game_state = 'parse'

            if result == 'attack':
                dialogue.update_textbox("You start fighting " + inhabitant.name + "!!")
                dialogue.update_textbox("What do you fight with?")
                game_state = 'fight'
    else:
        dialogue.update_textbox("There is no one to bribe")
        game_state = 'parse'


def take():
    if items is not None:
        dialogue.update_textbox("You take the " + items.name)
        player.backpack.append(items.name)
        inventory.update_item(items.name, 'add')
        current_room.set_item(None)
    else:
        dialogue.update_textbox("There is nothing to take")


def check_backpack():
    if player.backpack is not None:
        dialogue.update_textbox("Your backpack contains: " + ', '.join(player.backpack))
    else:
        dialogue.update_textbox("Your backpack is empty")


def dig():
    global current_room
    if "shovel" not in player.backpack:
        dialogue.update_textbox("You need a shovel to dig")
        return
    if current_room.name != "Cellar":
        dialogue.update_textbox("you can't dig here, the floor is too solid.")
        return

    chance = random.randint(1, 1000)
    print(chance)
    if 17 <= chance <= 200 and player.gameboy_found is False:  # 18.3% chance to find gameboy, if not already found
        dialogue.update_textbox("You dig up a gameboy")
        player.backpack.append("gameboy")
        inventory.update_item("gameboy", 'add')
        player.gameboy_found = True
    elif 6 <= chance <= 16 and player.gun_found is False:  # 1% to find gun
        dialogue.update_textbox("You find a gun!!")
        player.backpack.append("gun")
        inventory.update_item("gun", 'add')
        player.gun_found = True
    elif 1 <= chance <= 5 and player.amulet_found is False:  # 0.5% to find amulet
        dialogue.update_textbox("You are absurdly lucky..")
        dialogue.update_textbox("You found Edd's Amulet!")
        player.backpack.append("amulet")
        inventory.update_item("amulet", 'add')
        player.amulet_found = True
    else:
        dialogue.update_textbox("you dig and find nothing.")


def pre_craft():
    global game_state
    dialogue.update_textbox("Select first item to craft with")
    game_state = 'craft'


def craft1(item):
    global item1
    global item1_obj
    global game_state
    if item in items_list:
        if item in player.backpack:
            item1 = item
            item1_obj = items_dict.get(item1)
            if item1_obj.craft_item is not None or item1_obj == glove:
                dialogue.update_textbox("Select second item to craft with")
                game_state = 'craft2'
            else:
                dialogue.update_textbox("This item can't be crafted into anything")
                game_state = 'parse'
        else:
            dialogue.update_textbox("You don't have that")
            game_state = 'parse'
    else:
        dialogue.update_textbox("That item does not exist")
        game_state = 'parse'


def craft2(item):
    global item1
    global item1_obj
    global game_state
    if item in items_list:
        if item in player.backpack:
            item2 = item
            item2_obj = items_dict.get(item2)
            result = item1_obj.craft(item2_obj)
            if result is not None:
                result_obj = items_dict.get(result)
                if result_obj is not glove:
                    result_obj.describe()
                player.backpack.remove(item1)
                inventory.update_item(item1, 'remove')
                player.backpack.remove(item2)
                inventory.update_item(item2, 'remove')
                player.backpack.append(result)
                inventory.update_item(result, 'add')
                game_state = 'parse'
            else:
                dialogue.update_textbox("You can't use that on " + item1)
                game_state = 'parse'
        else:
            dialogue.update_textbox("You don't have that")
            game_state = 'parse'
    else:
        dialogue.update_textbox("That item does not exist")
        game_state = 'parse'


def look():
    if inhabitant is not None:
        inhabitant.describe()
    if items is not None:
        items.announce()
        items.describe()
    current_room.get_details()


def cellar():
    global game_state
    talk_count = player.talk_count
    kill_count = player.kill_count
    print("DEBUG: cellar game state active")
    print("DEBUG: talk count is ", talk_count)
    print("DEBUG: kill count is ", kill_count)
    if talk_count == 4 and kill_count == 0:
        # player has talked to every character possible - pacifist run
        will.conversation = will_unlocked_conversation
        will.talk_reward = "sock"
        game_state = 'parse'
        print("DEBUG: outcome: player is pacifist")

    elif kill_count >= 5:
        # player has killed every character possible - genocide run
        will.set_item("tear")
        game_state = 'parse'
        print("DEBUG: outcome: player is genocidal")

    else:
        game_state = 'parse'
        print("DEBUG: outcome: player is boring")


def help():
    dialogue.update_textbox("The commands are: ")
    dialogue.update_textbox(', '.join(command_list))


#   Main function - command parsing ------------------------------------------------------------------------------------

def parse(command):
    global inhabitant
    global current_room
    global items
    global game_state
    global current_node
    global app
    global bossroom3_unvisited
    dialogue.update_textbox("\n" + "> " + command)
    entry_box.clear_entry()

    if game_state == 'pacifist_boss':
        current_node = talk_tree(current_node, command)

    if game_state == 'rejected':
        print("DEBUG: GAME OVER, PLAYER IS REJECTED")
        dialogue.update_textbox("Game over. You have not been hired by Will :( type quit")
        dialogue.update_textbox(random.choice(hint_list))
        if command == 'quit':
            exit()

    if game_state == 'hired':
        print("DEBUG: GAME OVER, PLAYER IS HIRED")
        dialogue.update_textbox("Game over. You have been hired by Will :) type quit")
        if command == 'quit':
            exit()

    if game_state == 'dead':
        dialogue.update_textbox("Game over. You have died :( type quit")
        dialogue.update_textbox(random.choice(hint_list))
        if command == 'quit':
            exit()

    if game_state == 'won':
        dialogue.update_textbox("Game over. You have beaten Will's riddles. Congratulations! Type quit")
        if command == 'quit':
            exit()

    if game_state == 'genocide_won':
        dialogue.update_textbox("Game over. You have beaten Will. Congratulations! Type quit")
        if command == 'quit':
            exit()

    if game_state == 'fight':
        fight(command)

    elif game_state == 'talk':
        player_talk(command)

    elif game_state == 'bribe':
        bribe(command)

    elif game_state == 'craft':
        craft1(command)

    elif game_state == 'riddle_will':
        guess(command)

    elif game_state == 'craft2':
        craft2(command)

    elif game_state == 'parse':

        if command == "look":
            look()

        elif command in ["north", "south", "east", "west"]:
            current_room = move(command)

            if current_room.name == 'Cellar':
                cellar()

            if current_room == bossroom1:
                current_node.print_question()
                game_state = 'pacifist_boss'

            if current_room == bossroom2:
                riddle_will()

            if current_room == bossroom3 and bossroom3_unvisited:
                bossroom3_unvisited = False
                genocidal_will()

        elif command == "talk":
            talk()

        elif command == "fight":
            if inhabitant is not None:
                dialogue.update_textbox("You start fighting " + inhabitant.name + "!!")
                dialogue.update_textbox("What do you fight with?")
                game_state = 'fight'
            else:
                dialogue.update_textbox("There is no one to fight")

        elif command == "bribe":
            if inhabitant is not None:
                dialogue.update_textbox("You try to bribe " + inhabitant.name)
                dialogue.update_textbox("What do you want to bribe with?")
                game_state = 'bribe'
            else:
                dialogue.update_textbox("There is no one to bribe")

        elif command == "take":
            take()
        elif command == "backpack":
            check_backpack()
        elif command == "dig":
            dig()
        elif command == "craft":
            pre_craft()
        elif command == "help":
            help()
        elif command == "quit":
            exit()
        else:
            dialogue.update_textbox("For a list of commands, type 'help'")

    # Get room info
    inhabitant = current_room.get_character()
    items = current_room.get_item()


# Initial commands, only ever ran once

# Initialize window with a function, parse

app = App(parse, True)

# Define app attributes

app.geometry("430x300")
app.resizable(False, False)

# Set base stats

player = Player(1, 1)
player.backpack = ["fists"]
inventory.update_item("fists", 'add')
if ALL_ITEMS:
    player.backpack = list(items_list)

# Define initial starting parameters

if PACIFIST:
    current_room = library
    player.talk_count = 4
elif GENOCIDAL:
    current_room = library
    player.kill_count = 5
elif BORING:
    current_room = library
else:
    current_room = kitchen

current_node = node1
inhabitant = current_room.get_character()
items = current_room.get_item()
game_state = 'parse'
bossroom3_unvisited = True
item1 = 'fists'
item1_obj = fists

# Other starting commands
current_room.describe()
current_room.describe()
current_room.get_details()

app.mainloop()
