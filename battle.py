"""
This module simulates a battle between two knights.

The module expects a module named `knights` to be available, which supplies
the following constants and classes:
    MAX_ATTRIBUTE_POINTS: which holds how many attribute points a knight can spend
    ATTRIBUTES: a list of attributes on which the points can be spent on
    
    KnightError: A class that can be raised for errors in knighting a new knight
    Knight: A class that represents a knight, whose constructor takes a name and
        one parameter for each available attribute.

        So if the available attributes are strength and vitality the knight should
        be constructed with Knight(name, strength_value, vitality_value)
"""
import inspect
import random

import knights
from util import class_tester, get_item_from_user as get_item


def get_class():
    """
    Displays a list of classes and lets the user choose one.

    It first lists all available members of the knights module, which is
    then filtered to only contain classes that either are the the knight class
    or are a subclass of it. It then displays the classes and their descriptions
    to let the user make an informed choice.

    Returns:
        the class reference the user chose
    """
    # this function lists all classes that are in the knights module
    knight_test = class_tester(knights.Knight)
    available_classes = inspect.getmembers(knights, knight_test)

    # if there is only one class available (when bonus task is not implemented)
    # then return that one class
    if len(available_classes) == 1:
        knight_class = available_classes[0][1]
    else:
        # list the classes and descriptions that are available and
        # let the user choose one of it
        print("Choose what kind of knight you want to be! Available classes are:")
        for i, class_ in enumerate(available_classes):
            # second index 0 and 1 since inspect.getmembers
            # returns tuples of names and classes
            class_name = class_[0]
            class_reference = class_[1]
            print(
                f"{i}: {class_name}:\n"
                f"{class_reference.description()}\n"
            )

        idx = get_item("Choose the class of your knight.", available_classes)
        knight_class = available_classes[idx][1]
    
    return knight_class
    

def create_knight():
    """
    Creates a new knight according to player input.

    Checks the knights module for how many points are to spend,
    and which attributes are available. It then asks the player
    for a name for the knight and to spend their points on the
    available attributes.

    Returns:
        A knight instance with the player's values
    """
    knight_class = get_class()

    # get the constants from the knights module
    max_attr_points = knights.MAX_ATTRIBUTE_POINTS
    attributes = knights.ATTRIBUTES
    knight = None # this will be the instance to be returned
    
    name = input("What is your name?\n")
    # reapet until the input was correct and a knight was created
    while not knight:
        # display the attributes and how many points are to be spent
        spent_points = input(
            f"You have {max_attr_points} points to spend on "
            f"the attributes: { ', '.join(attributes) }.\n"
            "Submit your points separated either by commas or by spaces, "
            "like the list above with numbers instead of attribute names. "
            "Points must be integers.\n"
        )
        
        try:
            # we allow to use commas or spaces, so we check what was used
            # we cast all input attribute points to integer since
            # attribute points are integer numbers
            if "," in spent_points:
                points = [int(val) for val in spent_points.split(",")]
            else:
                points = [int(val) for val in spent_points.split(" ")]
            
            # if not enough attributes were inputted, repeat the loop
            if len(points) != len(attributes): continue
            # knight the knight! Since knights take attributes as 
            # one parameter each, we unzip the input list into the call
            
            knight = knight_class(name, *points)
        except ValueError:
            # When the casting to integer fails
            print("Could not parse. Were the points all integer?")
            continue
        except knights.KnightError as e:
            # a special error from the knights module that occurs when
            # there are errors in knighting a new knight
            print(f"Could not knight the knight: {str(e)}")
            continue

    return knight


def attack(player):
    """
    Let a player attack.

    Get all available actions from the knight instance. Display them as
    options to the current player and let him choose which one to perform.

    Args:
        player: the knight instance of the current player that is attacking
    
    Returns:
        the result of the attack function call, which should be a damage value
        and a boolean whether it was a critical hit
    """
    # get the actions that the knight can perform
    available_actions = player.all_actions()
    # since the actions are methods, we use the __name__ attribute to display
    # them in a readable format to the terminal
    available_actions_names = [atk.__name__ for atk in available_actions]
    print(f"Available actions are: {', '.join(available_actions_names)}")

    idx = get_item("Choose what action to perform.", available_actions_names)
    action = available_actions[idx]
    
    # since we get a list of functions (not just function names),
    # we can directly call the function from the list, which will reference
    # the function inside the player instance. neat.
    return action()

def battle():
    """
    This is the main game loop.

    It starts the game by creating one knight for both players.
    Then a random player is chosen to make the first strike.
    Each turn the current player is updated. A game round:
        - the active player is saved into a variable
        - the current health is displayed
        - it's displayed whose turn it is
        - player is presented with possible actions
        - player chooses action
        - knight action is executed
        - other knight takes according damage
        - damage is displayed
        - turn boolean is flipped
    
    The game loop ends, once a knight is definitely not dead, but k.o.
    The winning player is displayed and a new round can be begun.
    Otherwise function ends.
    """
    # just keep playing
    play = 'y'
    while play == 'y':
        # each player gets a knight
        player1 = create_knight()
        player2 = create_knight()
        # turn_player1 is true when player1 is the active player this turn
        # randomly chosen who begins
        turn_player1 = random.choice([True, False])
        # for nice display reasons
        name_length = max(len(str(player1)), len(str(player2)))

        print() # for readability
        while player1.alive() and player2.alive():
            # current_player and other_player hold the reference to the active player
            # this way we can use one variable for the rest of the game loop instead
            # of constant if/else switches
            current_player = player1 if turn_player1 else player2
            other_player = player2 if turn_player1 else player1

            # print the health for both players
            for p in [player1, player2]:
                print(f"{str(p) : >{name_length}} has {p.health} health points remaining.")

            # print whose turn it is
            print(f"\nIt is {current_player}'s turn.")
            # player interaction! let a player attack and the other player take damage
            damage, crit = attack(current_player)
            other_player.take_damage(damage)
            # print the result of the attack. Extra text for crits
            print(
                f"{'POW! A critical hit!' if crit else ''}"
                f"{other_player} took {damage} damage from {current_player}.\n"
            )
            
            # flip who is active next turn
            turn_player1 = not turn_player1

        # WHO WON? WHO IS NEXT? current_player works, because the loop ends when
        # one player is dead and before current_player is updated
        print(f"\nCongratulations {current_player}! You were victorious!")
        
        # another duel?
        play = input("Play again? (y/n): ").lower()
    
    print("Until then. Battle will await you.")


# only start the game if this is the active module
if __name__ == '__main__':
    battle()
