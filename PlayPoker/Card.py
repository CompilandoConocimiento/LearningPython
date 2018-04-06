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

        for Type in ["Hearts", "Diamonds", "Spades", "Clubs"]:
            for Number in range(1, 14):
                Data.append(Card(Number, Type))

        return Data


    """===========================================
    =========          INIT               ========
    ==========================================="""
    def __init__(self, Number=1, Type="Diamonds"):


        self._Type = Type if Type in {"Diamonds", "Spades", "Hearts", "Clubs"} else "Diamonds" 
        if self._Type in {"Diamonds", "Hearts"}: self._Color = "Red"
        else: self._Color = "Black"
        
        if (Number < 1 or Number > 13): Number = 1

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
        Keys = dict([
            ("1", 1), ("2", 2), ("3", 3), ("4", 4), ("5", 5), 
            ("6", 6), ("7", 7), ("8", 8), ("9", 9), ("A", 10), 
            ("B", 11), ("D", 12), ("E", 13)
        ])
        return Keys[self._Number]

    def NextNumber(self):
        Keys = dict([
            ("1", 2), ("2", 3), ("3", 4), ("4", 5), ("5", 6), 
            ("6", 7), ("7", 8), ("8", 9), ("9", 10), ("A", 11), 
            ("B", 12), ("D", 13), ("E", 1)
        ])
        return Keys[self._Number]




