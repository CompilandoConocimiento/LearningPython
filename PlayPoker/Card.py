
class Card:
    def __init__(self, Color="Black", Number=1, Type="Diamonds"):
        self._Color = Color
        self._Number = Number
        self._Type = Type



    def getUnicodeAndColor(self):

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

        return (chr(int(UnicodeString, 16)), self._Color)

    @staticmethod
    def GetRandomCards():

        Data = list()

        for Type in ["Hearts", "Diamonds"]:
            for Number in range(1, 14):
                Data.append(Card("Red", Number, Type))

        for Type in ["Spades", "Clubs"]:
            for Number in range(1, 14):
                Data.append(Card("Black", Number, Type))

        return Data
