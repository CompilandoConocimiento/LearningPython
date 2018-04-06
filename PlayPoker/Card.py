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
        self._Type = Type
        
        if Number == 10: self._Number = "A"
        elif Number == 11: self._Number = "B"
        elif Number == 12: self._Number = "D"
        elif Number == 13: self._Number = "E"
        else: self._Number = str(Number)


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


    @property
    def type(self):
        return self._Type

    @property
    def number(self):
        if self._Number == "1": return 1
        elif self._Number == "2": return 2
        elif self._Number == "3": return 3
        elif self._Number == "4": return 4
        elif self._Number == "5": return 5
        elif self._Number == "6": return 6
        elif self._Number == "7": return 7
        elif self._Number == "8": return 8
        elif self._Number == "9": return 9
        elif self._Number == "A": return 10
        elif self._Number == "B": return 11
        elif self._Number == "D": return 12
        elif self._Number == "E": return 13
        return 13

    def NextNumber(self):
        if self._Number == "1": return 2
        elif self._Number == "2": return 3
        elif self._Number == "3": return 4
        elif self._Number == "4": return 5
        elif self._Number == "5": return 6
        elif self._Number == "6": return 7
        elif self._Number == "7": return 8
        elif self._Number == "8": return 9
        elif self._Number == "9": return 10
        elif self._Number == "A": return 11
        elif self._Number == "B": return 12
        elif self._Number == "D": return 13
        return 1



