import math
import random

MAX_ATTRIBUTE_POINTS = 100 

ATTRIBUTES = ['vitality', 'strength', 'luck']

class KnightError(Exception):
    """ A class that can be raised for errors in knighting a new knight """
    pass

class Knight:
    """  A class that represents a knight, whose constructor takes a name and
        one parameter for each available attribute.
    """
    def __init__(self, name, vitality, strength, luck):

        self.name = name
        self.health = math.floor(vitality * 1.5)
        self.strength = strength
        self.luck = luck
        self.crit_modifier = 3
        self.available_actions = [self.light_attack, self.heavy_hit]

        # raises error if more or less points were given 
        if not(vitality + strength + luck == MAX_ATTRIBUTE_POINTS):
            raise KnightError


    def __str__(self):
        """ Returns name of the knight """
        return str(self.name)


    def alive(self):
        """ Returns true if health of knight is greater than 0 """
        if self.health > 0:
            return True
        else:
            return False

    def take_damage(self, damage):
        """ Reduces health of hit knight by damage """
        self.health -= damage
        

    def light_attack(self):
        """A lighter attack with smaller damage and a higher critical strike chance. 
      
        The function returns a tuple consisting of the damage and a boolean
        whether the attack was critical.
        """
        damage = 1 + 0.15 * self.strength

        # if it was critical hit
        if random.randint(0,99) < self.luck * 2:
            crit_hit = True
        else:
            crit_hit = False

        damage = math.floor(damage)
        return (damage, crit_hit)

    def heavy_hit(self):
        """A heavier attack with higher damage, but lower critical chance. 
        The function returns a tuple consisting of the damage and a boolean
        whether the attack was critical.
        """
        damage = 3 + 0.4 * self.strength

        # if it was critical hit
        if random.randint(0,99) < self.luck * 2:
            crit_hit = True
        else:
            crit_hit = False

        damage = math.floor(damage)
        return (damage, crit_hit)

    def all_actions(self):
        """ Returns the list of all actions this knight can take. """

        return self.available_actions

