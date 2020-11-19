class Card:
"""
Class that represents a card object.
"""
  def __init__(self, number, suit):
    self._number = number
    self._suit = suit
  
  @property
  def number(self):
    return self._number
  
  @property
  def suit(self):
    return self._suit
  
  @number.setter
  def number(self, value):
    if isistance(value,int):
      if value > 0 and value < 11:
        self._number = value
      else:
        print("Error: number must be between 1 and 10")
    else:
      print("Error: number must be integer")
      
  @suit.setter
  def suit(self, value):
    if isistance(value,str):
      if value == "Cups" or value == "Golds" or value == "Cubs" or value == "Swords":
        self._suit = value
      else:
        print("Error: suit must be either Cups, Golds, Cubs or Swords")
    else:
      print("Error: number must be string")
      
  def show(self):
      print(self.number," of ",self.suit)
  
  
  
class Deck:
"""
Class that represents a deck of cards.
"""
  def __init__(self):
    self.cards = []
    suits = ["Cups","Golds","Cubs","Swords"]
    for j in suits:
      for i in range(1,11):
        self.cards.append(Card(i,j))

  
  
