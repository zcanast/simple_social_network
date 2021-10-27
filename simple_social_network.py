""" A simple social network for tracking networks between people"""

class Person:
    """ Represents a person in a social network
    
    Attributes:
        name (str): the person's name
        connections (set of Person): other people in the social network who know
            this person.
    """
    
    def __init__(self, name):
        self.name = name
        self.connections = set()
    
    def connect(self, person2):
        """ Connect with person2
        
        Args:
            person2 (Person): the other person to connect to.
        """