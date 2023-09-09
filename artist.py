"""
Artist object

Author: Dylan Mack, dylan.mackb9@gmail.com, 

Creation: July 15, 2023, 4:31pm
"""



class Artist:

  def __init__(self, id, name, followers, genres):
    self.id = id
    self.name = name
    self.followers = followers
    self.genres = genres

  def __str__(self):
    """
    Sets print() or str() value 
    """
    return self.name


  def __repr__(self):
    '''
    Defines string representation 
    '''
    return self.id


  def __eq__(self, other):
    """
    Called automatically whenever 2 artist objects are equated using ==
    """
    return self.id == other.id


  def __hash__(self):
    """
    Called automatically when an Artist object is hashed
    """
    return hash(self.id)

  