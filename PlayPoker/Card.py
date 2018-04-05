"""=========================================================
===============        CARD CLASS       ====================
========================================================="""
class Card:
    """
    Class modelate a poker card, it has esscencially 3 important
    features:
    - Type
    - Color
    - Number
    """

    """===========================================
    =========   CREATE A DECK OF CARDS    ========
    ==========================================="""
    @staticmethod
    def CreateDeckOfCards():
        """
        This create a list with all the cards in the Deck

        Returns:
            List of Cards: All the possible cards in a deck, and "semi" sorted
        """

        Data = list()

        for Type in ["Hearts", "Diamonds"]:
            for Number in range(1, 14):
                Data.append(Card("Red", Number, Type))

        for Type in ["Spades", "Clubs"]:
            for Number in range(1, 14):
                Data.append(Card("Black", Number, Type))

        return Data


    """===========================================
    =========          INIT               ========
    ==========================================="""
    def __init__(self, Color="Black", Number=1, Type="Diamonds"):
        self._Color = Color
        self._Number = Number
        self._Type = Type


    """===========================================
    =========          GETTERS            ========
    ==========================================="""

    """==============================
    =======     UNICODE       =======
    =============================="""
    def getUnicode(self):
        """
        Returns:
            str: The unicode of the specific card 
        """

        if self._Type == "Spades": TypeLetter = "A"
        elif self._Type == "Hearts": TypeLetter = "B"
        elif self._Type == "Diamonds": TypeLetter = "C"
        elif self._Type == "Clubs": TypeLetter = "D"

        if self._Number == 10: self._Number = "A"
        elif self._Number == 11: self._Number = "B"
        elif self._Number == 12: self._Number = "C"
        elif self._Number == 13: self._Number = "D"
        elif self._Number == 14: self._Number = "E"
        elif self._Number == 15: self._Number = "F"
        else: self._Number = str(self._Number)

        UnicodeString = f"0001F0{TypeLetter}{self._Number}"

        return chr(int(UnicodeString, 16))


    """==============================
    =======     UNICODE       =======
    =============================="""
    def getColorAsRGB(self):
        """
        Returns:
            (int, int, int): The RGB of the card 
        """

        if self._Color == "Red": 
            return (211,47,47)
        else: 
            return (33,33,33)

    """==============================
    =======     UNICODE       =======
    =============================="""
    def getData(self):
        """
        Returns:
            (int, str): The number and type of the card
        """

        return (self._Number, self._Type)



