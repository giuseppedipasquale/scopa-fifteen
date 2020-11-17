class Card:
  def __init__(self, number, suit):
    self._number = number
    self._suit = suit
  @property
  def number(self):
    return self._number
  @property
  def suit(self):
    return self._suit
    
