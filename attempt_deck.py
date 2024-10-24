from random import randint as r

class Deck:
    """A blueprint for representing a deck containing 52 cards"""
    def __init__(self, cards=[], card_amount=None):
        """self, list, int"""
        self.cards = cards
        self.card_amount = card_amount
    
    def insert_card(self, card):
        """adds the object Card into the desk's list
            Returns a message of successful or not
            updates the object's position state
        """
        if self.card_amount == 52:
            message = "There are already 52 cards we can not add any more cards"
            return message
        
        self.cards.append(card)
        card.position = self.card_amount  

        if self.card_amount == None: 
            self.card_amount = 1
        else:
            self.card_amount += 1

        message = f"""Inserting the card was successful the card {card.value} 
        of {card.suit} in the desk at position {card.position}"""
        return message

    def display_deck(self):
        """"""
        for card in self.cards:
            print(card.__str__())

    def shuffle_cards(self):
        """Reorders the position of Card objects in the desk"""
        if self.card_amount == 0:
            return """There are no cards to shuffle"""
        
        number_of_swaps = 0
        total_swaps = self.card_amount * 1.5
        # if total_swaps % 2 != 0:
        #     total_swaps -= 1
        
        while number_of_swaps < total_swaps:
            # get two random numbers from 1 to self.card_amount
            first_index = r(1, self.card_amount-1)
            second_index = r(1, self.card_amount-1)

            if first_index != second_index:
                current_card = self.cards[first_index]
                swap_card = self.cards[second_index]
        
                current_card.position, swap_card.position = swap_card.position, current_card.position

                number_of_swaps += 1


class Card:
    """A blueprint for representing a playing card"""
    def __init__(self, suit="", value=None, position=None):
        """self, str, int, int"""
        self.suit = suit
        self.value = value
        self.position = position

    def __str__(self) -> str:
        """Return a string about the state of the object"""
        if self.position == None:
            return f"This card is the {self.value} of {self.suit} and not in a deck"
        
        return f"This card is the {self.value} of {self.suit} in position {self.position} of the deck"
    
    def is_greater(self, otherCard):
        """Returns a tuple of Boolean Value of True if our obj has a higher value
        and a string as a message
        otherCard is Int --> otherCard.value
        """
        if not isinstance(otherCard, int):
            return "The value of the other card was not given"

        if self.value > otherCard:
            result = (True, "This card is greater")
            return result
        
        elif self.value == otherCard: 
            result = (False, "The cards are equal")
            return result
        else:
            result = (False, "The card is lesser")
            return result
        
suits = ["club", "heart", "spade", "diamond"]
card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

playingDeck = Deck()

for suit in suits:
    for value in card_values:
        card = Card(suit, value)
        playingDeck.insert_card(card)
