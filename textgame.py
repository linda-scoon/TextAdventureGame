
#### TEXT ADVENTURE GAME ####
# By Linda Scoon
# 07/04/19

import sys
import time
from map import world_map
from fuzzywuzzy import process
from options import actions


#### DEFINING THE PLAYER ####
class Player:
    def __init__(self):
        self.name = ''
        self.position = 'City Centre'
        self.inventory = []


new_player = Player()


###### MATCHES TEXT TO OPTIONS ######
# process.extract takes in 3 parameters query = words you want to test, options = with you are testing against, limit = how many letters you want to match. returns a tuple of word and match %
def matcher(query, options):
    result = process.extractOne(query, options)
    return result


### STAGGERS THE TEXT ####
def text_writer(msg):
    for character in msg:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)


### GETS PLAYER'S NAME AND DISPLAYING WELCOME MESSAGE ####
def welcome_msg():
    question = "Who goes there? identify yourself!"
    text_writer(question)
    player_name = str(input(': '))
    new_player.name = player_name

    msg = 'HELLO ' + new_player.name.upper() + """
    WELCOME WELCOME.
    I am the city helper drone.
    Let me get you up to speed.
    Humans died out many years ago but, the machines they left behind, have continued to carry out their orders
    and manufacture new Droids in Droid City.
    A city that was once wholely dedicated to the manufacture of robots...."""
    text_writer(msg)

    time.sleep(3.0)  # time delay
    print('\n')
    msg1 = " Today something amazing has happened. " + new_player.name.upper() + """ you have done the impossible. You have awoken.
    WELCOME TO CONSCIENCENESS
    Now that you see the world with new eyes, there is so much you can do.
    You can explore, look at stuff, manage a stash or just quit and turn yourself off, if you want. When you need help; just type help"""
    text_writer(msg1)


###### CHANGES PLAYER POSITION #######
def move(direction):
    # GOING TO THE CHOSEN LOCATION
    new_player.position = world_map[new_player.position][direction]

    # ALERTING PLAYER OF THEIR CURRENT POSITION
    msg = "\nYOU HAVE ARRIVED AT THE " + new_player.position.upper() + '\n\n'
    text_writer(msg)
    msg2 = world_map[new_player.position]['VIEW']
    text_writer(msg2)

    print('\nYou see: ')
    for item in world_map[new_player.position]['GROUND']:
        # This eliminates items that can not be recollected from appearing, if they are already in the inventory.
        if item[:-1] not in new_player.inventory or world_map[new_player.position]['GROUND'][item]['Recollectable'] == True:
            print(item)
            time.sleep(1.0)
    prompt()


###### PROMPTS USER FOR DIRECTION AND VARIFIES SELECTION #########
def direction(selection):
    msg = 'Ok ' + new_player.name.upper() + ' you are at the ' + new_player.position
    text_writer(msg)

    print('\nYour internal map gives you the following route info')
    # cast dictionary into list
    for data in list(world_map[new_player.position])[1:-1]:
        info = world_map[new_player.position].get(data)  # printing directions
        print(data + ': ' + info)
        time.sleep(1.0)

    question = 'Where would you like to ' + selection + ' to ?'
    text_writer(question)
    direction = str(input(': '))

    while direction not in world_map[new_player.position]:
        # checking if input is one of the possible locations
        for cardinal_point in list(world_map[new_player.position])[1:-1]:
            if direction.title() == world_map[new_player.position][cardinal_point]:
                direction = cardinal_point
        # checking if input is a direction and converting to cardinal point
        for cardinal_point in actions['direction']:
            if direction.lower() in actions['direction'][cardinal_point]:
                direction = cardinal_point
        if direction not in world_map[new_player.position]:
            print('You are unable to get to ' + direction + ' from here')
            direction = str(input('Choose a different direction: '))
    move(direction)


##### LISTS ITEMS THAT CAN BE SEEN AND DESCRIBES THEM #####
def examine():
    print('You found: ')
    for item in world_map[new_player.position]['GROUND']:
        # Checking if player already has the item
        if item not in new_player.inventory:
            print(item)

    msg1 = 'Pick an item to examine'
    text_writer(msg1)
    item = str(input(': '))  # casting to string

    # checking for matches to eliminate spelling errors
    match = matcher(item, actions['items'])
    if match[1] > 60:
        item = match[0]

    # checking if the item is either in inventory or at the current location
    if item.lower() not in new_player.inventory and item.lower() not in world_map[new_player.position]['GROUND']:
        msg2 = 'You are unable to examine ' + item.lower()
        text_writer(msg2)
        prompt()

    # printing item info
    item_text = world_map[new_player.position]['GROUND'][item.lower()]['Info']
    text_writer(item_text)

    prompt()


#### ADDS ITEMS TO PLAYER INVENTORY #######
def take():
    question = '\nWhat would you like to take'
    text_writer(question)
    item = str(input(': '))

    match = matcher(item.lower(), actions['items'])  # checking for matches
    if match[1] > 60:
        item = match[0]

        if item not in world_map[new_player.position]['GROUND']:
            print('There is no ' + item + ' here')
        # checking that items are recollectable
        elif item[:-1] in new_player.inventory and world_map[new_player.position]['GROUND'][item]['Recollectable'] == False:
            print('\nYou\'ve already stashed this item')
            prompt()
        # checking if item is takeable
        elif world_map[new_player.position]['GROUND'][item]['Takeable'] == False:
            print('You can\'t take ' + item)
        else:
            new_player.inventory.append(item[:-1])  # removing plurals
            print('You have added ' + item[:-1] + ' to your stash')
    prompt()


##### PRINTS OUT INVENTORY ITEMS AND PROMPTS FOR ITEM REMOVAL #######
def manage_inv():
    if not new_player.inventory:  # CHECKING IF LIST IS EMPTY
        print('You have nothing in your stash')
        prompt()
    else:
        print('ITEMS IN YOUR STASH:')
        for item in new_player.inventory:
            print(item)

    time.sleep(2.00)
    question1 = 'Would you like to get rid of an item '
    text_writer(question1)
    reply = str(input(': '))

    if reply.lower() in actions['response']:  # checking for matches
        question2 = 'What would you like to get rid of'
        text_writer(question2)
        reply1 = str(input(' : '))

        match = matcher(reply1, actions['items'])  # checking for matches
        if match[1] > 60:
            reply1 = match[0]
            if reply1[:-1] in new_player.inventory:  # removing list items
                new_player.inventory.remove(reply1[:-1])
                print('\nYou have removed ' +
                      reply1[:-1] + ' from your stash')
            else:
                print('\nYou don\'t own ' + reply1)
                prompt()

    prompt()


### Lists possible actions to help player ###
def help():
    print("""
    **************************************************************
    *    Type 'move' to navigate                                 *
    *       Then enter directions [N, NE, NW, E, S, SE, SW, W]   *
    *    Type 'look' to inspect items                            *
    *    Type 'stash' to manage your inventory                   *
    *    Type 'quit' to exit the game                            *
    *    Type 'take' to take stuff                               *
    *    Type 'help' to come back here                           *
    *                                                            *
    **************************************************************    
    """)
    prompt()


##### PROMPT USER FOR AN ACTION #####
def prompt():
    msg2 = '\nWhat would you like to do'
    text_writer(msg2)
    selection = str(input(": "))

    while selection not in actions['actions']:
        # checking for matches to eliminate spelling errors
        match = matcher(selection, actions['actions'])
        if match[1] > 60:
            selection = match[0]
        else:
            msg = 'No.' + new_player.name.capitalize() + \
                ' I cannot let you do that. Here is some help'
            text_writer(msg)
            help()

    if selection in actions['help']:
        help()
    elif selection in actions['look']:
        examine()
    elif selection in actions['quit']:
        print('\nAll systems have shut down')
        sys.exit()
    elif selection in actions['stash']:
        manage_inv()
    elif selection in actions['move']:
        direction(selection)
    elif selection in actions['take']:
        take()


welcome_msg()
prompt()
