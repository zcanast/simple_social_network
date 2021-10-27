""" A simple social network for tracking networks between people"""

class Person:
    """ Represents a person in a social network
    
    Attributes:
        name (str): the person's name
        connections (set of Person): other people in the social network who know
            this person.
    """