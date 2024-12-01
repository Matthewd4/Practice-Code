# Matthew Derick
# October 8, 2021

def intro():  # displays the rules and move options when program runs
    print("Cornelius V. Irus's Haunted Hospital")
    print('Collect 6 items to win the game, or be infected by Cornelius V. Irus.')
    print("To add 'Item' to your inventory, enter: Get 'Item name'(ex. Get A Mask)")
    print("To move between rooms, enter: 'Go East, West, South or North'(or Go E,W,S,N).")
    print("To quit, enter 'Exit'")


def directions():  # tells player how to play
    print("To add 'Item' to your inventory, enter: Get 'Item name'(ex. Get A Mask)")
    print("To move between rooms, enter: 'Go East, West, South or North'(or Go E,W,S,N).")
    print("To quit, enter 'Exit'")


def player_stat(current, inventory, rooms):  # prints the current player status
    print('-' * 20)
    print('You are in the {}'.format(current))   # shows current room
    if len(inventory) >= 1:    # if something is in inventory
        print('You have {} in your inventory.'.format(inventory))   # shows inventory
    if 'Item' in rooms[current]:    # if item is in a room
        print('You see', rooms[current]['Item'])  # show item


def main():    # game loop
    inventory = []    # empty inventory
    rooms = {      # dictionary
        'Parking Lot': {'West': 'Main Entrance'},
        'Main Entrance': {'West': 'Bathroom', 'North': 'Patient Room 19', 'East': 'Parking Lot',
                          'Item': 'A Mask'},
        'Bathroom': {'East': 'Main Entrance', 'Item': 'Toilet Paper'},
        'Patient Room 19': {'South': 'Main Entrance', 'West': 'Equipment Storage',
                            'East': 'Intensive Care Unit', 'North': "Cornelius V. Irus's Lair",
                            'Item': 'Clorox Wipes'},
        'Intensive Care Unit': {'West': 'Patient Room 19', 'North': 'Cleaning Supply Room', 'Item': 'Hand Sanitizer'},
        'Cleaning Supply Room': {'South': 'Intensive Care Unit', 'Item': 'Disinfectant Spray'},
        'Equipment Storage': {'East': 'Patient Room 19', 'Item': 'A Six Foot Ruler'},
        "Cornelius V. Irus's Lair": {'South': 'Patient Room', 'Item': 'Cornelius V. Irus'},
    }
    current = 'Parking Lot'    # starting room set
    intro()     # print directions
    while True:    # infinite loop
        player_stat(current, inventory, rooms)   # show player stat
        if current != "Cornelius V. Irus's Lair":    # if not in boss room
            moves = rooms[current]     # moves is a variable to show possible moves
            print('Possible', current, 'moves: Go', *moves.keys())   # show the possible moves in current room
            print('Move corresponds to: ', *moves.values())  # show possible destinations- no items
            print('-' * 20)
        if current == "Cornelius V. Irus's Lair":    # if in boss room
            if len(inventory) == 6:     # and you have all items
                print('Congratulations! You collected all 6 items and disinfected the hospital of Cornelius!')
                print('Thank you for playing!')  # you win
                break   # end loop
            else:     # if you don't have all items
                print('You have failed to collect all 6 items and were infected by Cornelius V. Irus.')  # you lose
                print('Better luck next time!')
                print('Thank you for playing!')
                break   # end loop
        move = input('Enter your move: ').title().split(' ', 1)   # prompt for move, capitalize first word for every
        # move, and split one time
        if len(move) >= 2:   # if the input is equal to 2 words
            move[1] = move[1].strip()   # strip the input of whitespaces
            if move[1] == 'W':   # if the move is just the first letter of the cardinal direction
                move[1] = 'West'  # assign them to the actual direction
            if move[1] == 'E':
                move[1] = 'East'
            if move[1] == 'S':
                move[1] = 'South'
            if move[1] == 'N':
                move[1] = 'North'
        if not move:     # if user does not enter a move
            print('-' * 20)
            print('Invalid move, try again')
            print("To re-read the directions, enter 'directions'")   # offer directions
            continue    # continue loop
        if move[0] == 'Exit' or move[0] == 'E':   # if the first word in the move is exit
            print('-' * 20)
            print('Thanks for playing!')   # exit
            break   # end loop
        elif move[0] == 'Directions':    # if the first word in the move is directions
            directions()   # give directions
        elif move[0] == 'Go' and len(move) == 2:  # if player inputs "Go" followed by there move
            if move[1] != "Item" and move[1] in rooms[current]:   # if their move is not an item and is in the room
                current = rooms[current][move[1]]  # current room updated
            else:    # otherwise
                print("You can't go that way!")
                print("To re-read the directions, enter 'directions'")  # offer directions
        elif move[0] == 'Get' and len(move) == 2:    # if the input is 2 words and the first word is get
            if 'Item' in rooms[current] and move[1] and move[1] == rooms[current]['Item']:
                # if the second word is an item in the current room
                inventory.append(move[1])  # add that item to the inventory
                print('-' * 20)
                print('You got', move[1])    # confirm they received the item
                rooms[current].pop('Item', None)   # remove the item after you get it(no duplicates,
                # removes from possible moves and the room)
            elif 'Item' not in rooms[current]:   # if item is not in the current room
                print('-' * 20)
                print('That item is not in the', current)
                print("To re-read the directions, enter 'directions'")
                continue
            else:    # otherwise
                print('-' * 20)
                print("You can't get that item")
                print("To re-read the directions, enter 'directions'")  # offer instructions
        else:   # any other moves
            print('-' * 20)
            print('Invalid move, try again.')
            print("To re-read the directions, enter 'directions'")
    print('Play again soon!')   # exit message
    print('-' * 20)


main()
