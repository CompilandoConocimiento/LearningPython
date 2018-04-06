"""==============================================================================
===========================        PLAY POKER       =============================
=============================================================================="""

import wx as WX
import Card as CardClass
import random


Player1CardsData = list()
Player2CardsData = list()


"""=========================================================
===============       PLAY POKER        ====================
========================================================="""
class PlayPokerFrame(WX.Frame):
    """
    A Frame that show the cards for 2 players, just that
    """

    """===========================================
    =============        INIT        =============
    ==========================================="""
    def __init__(self, *args, **kw):
        
        # Ensure the parent's __init__ is called
        super(PlayPokerFrame, self).__init__(*args, **kw, size=(900,600))

        # Create a panel in the frame
        PlayPokerPanel = WX.Panel(self)
        self.SetBackgroundColour((102,187,106))

        # ====  Make Title Look ======
        PanelTitle = WX.StaticText(PlayPokerPanel, label="Play Poker", pos=(25,5))
        PanelTitle.SetForegroundColour((27,94,32))
        PanelTitle.GetFont().SetPointSize(2300)
        PanelFont = PanelTitle.GetFont()
        PanelFont.SetPointSize(50) 
        PanelFont = PanelFont.Bold()
        PanelTitle.SetFont(PanelFont)

        self.Cards = CardClass.Card.CreateDeckOfCards()
        random.shuffle(self.Cards)

        """===========================================
        ===========   PLAYER DATA        =============
        ==========================================="""
        for Player in range(1, 3):

            DataList = Player1CardsData if Player == 1 else Player2CardsData
            YCoordinate = 150 if Player == 1 else 350
            HeaderTitle = (60, 120) if Player == 1 else (60, 330)
            HeaderLabel = f"Player {Player} Cards"
            InitialCards = self.Cards[0:5] if Player == 1 else self.Cards[5:10]

            PlayerTitle = WX.StaticText(PlayPokerPanel, label=HeaderLabel, pos=HeaderTitle)
            PlayerTitle.SetForegroundColour((40,53,147))

            PlayerTitleFontFont = PlayerTitle.GetFont()
            PlayerTitleFontFont.SetPointSize(25) 
            PlayerTitleFontFont = PlayerTitleFontFont.Bold()

            PlayerTitle.SetFont(PlayerTitleFontFont)

            """===========================================
            ===========   PRINT EACH CARD    =============
            ==========================================="""
            Counter = 70
            for card in InitialCards:

                Coordinate = (Counter, YCoordinate)
                WXCard = WX.StaticText(PlayPokerPanel, label=card.getUnicode(), pos=Coordinate)
                DataList.append((card, WXCard))

                CardFont = WXCard.GetFont()
                CardFont.SetPointSize(150)

                WXCard.SetFont(CardFont)
                WXCard.SetForegroundColour(card.getColorAsRGB())

                Counter += 120


        # Create a menu bar
        self.makeMenuBar()

        # And a status bar
        self.CreateStatusBar()
        self.SetStatusText("Play Poker")
        self.NextAvailableCard = 10


    """===========================================
    =======        MAKE A MENU BAR       =========
    ==========================================="""
    def makeMenuBar(self):

        #=== OPTIONS MENU ====
        OptionsMenu = WX.Menu()

        ChangeCardPlayer1 = OptionsMenu.Append(-1, "&Change Cards for Player 1\tCtrl-1")
        ChangeCardPlayer2 = OptionsMenu.Append(-1, "&Change Cards for Player 2\tCtrl-2")
        OptionsMenu.AppendSeparator()
        exitItem = OptionsMenu.Append(WX.ID_EXIT)

        #=== GAME MENU ====
        GameMenu = WX.Menu()
        FinishItem  = GameMenu.Append(-1, "&Finish Game\tCtrl-F")
        GameMenu.AppendSeparator()

        #=== GENERAL MENU ====
        helpMenu = WX.Menu()
        aboutItem = helpMenu.Append(WX.ID_ABOUT)

        #=== MENU BAR ====
        menuBar = WX.MenuBar()
        menuBar.Append(OptionsMenu, "&Options")
        menuBar.Append(GameMenu, "&Game")
        menuBar.Append(helpMenu, "&Help")
        self.SetMenuBar(menuBar)
        
        #=== BIND ====
        self.Bind(WX.EVT_MENU, lambda event: self.OnChangeCards(event, 1), ChangeCardPlayer1)
        self.Bind(WX.EVT_MENU, lambda event: self.OnChangeCards(event, 2), ChangeCardPlayer2)
        self.Bind(WX.EVT_MENU, self.OnFinish, FinishItem)
        self.Bind(WX.EVT_MENU, self.OnExit,  exitItem)
        self.Bind(WX.EVT_MENU, self.OnAbout, aboutItem)


    """===========================================
    =======            ON EXIT           =========
    ==========================================="""
    def OnExit(self, event):
        """Close the frame, terminating the PlayPokerApplication."""
        self.Close(True)


    """===========================================
    =======          ON FINISH           =========
    ==========================================="""
    def OnFinish(self, event):

        def IsRoyalFlush(Hand):
            HandType = Hand[0].type
            if all(card.type == HandType for card in Hand) == False:
                return False

            Numbers = {card.number for card in Hand}
            return True if {13, 12, 11, 10, 1} == Numbers else False


        def IsStraightFlush(Hand):

            HandType = Hand[0].type
            if all(card.type == HandType for card in Hand) == False:
                return False

            Numbers = [card.number for card in Hand]
            if (set(Numbers) != 5): return False

            CounterOfFalse = 0
            for card in Hand:
                if (card.NextNumber() in Numbers) == False:
                    CounterOfFalse += 1

            return max(Numbers) if CounterOfFalse == 1 else False

        def IsQuad(Hand):

            Mode = dict()
            for element in Hand:

                if element.number not in Mode:
                    Mode[element.number] = 1
                else:
                    Mode[element.number] += 1
                
                if Mode[element.number] == 4:
                    return element.number


            return False

        def IsFullHouse(Hand):

            Mode = dict()
            for element in Hand:
                if element.number not in Mode:
                    Mode[element.number] = 1
                else:
                    Mode[element.number] += 1
                

            if set(Mode.values()) == {3, 2}:
                for key in Mode.keys():
                    if (Mode[key] == 3): return key
            return False

        def IsColor(Hand):
            HandType = Hand[0].type
            if all(card.type == HandType for card in Hand) == False:
                return False

            return sorted([card.number for card in Hand])

        def IsStraight(Hand):
            Numbers = [card.number for card in Hand]
            if (set(Numbers) != 5): return False

            print(f"Im in Straight an numbers = {Numbers}")
            CounterOfFalse = 0
            for card in Hand:
                print(f"The next of {card.number} is {card.NextNumber()}")
                if (card.NextNumber() in Numbers) == False:
                    CounterOfFalse += 1

            return max(Numbers) if CounterOfFalse == 1 else False

        def IsSet(Hand):
            Mode = dict()
            for element in Hand:
                if element.number not in Mode:
                    Mode[element.number] = 1
                else:
                    Mode[element.number] += 1
                

            if 3 in set(Mode.values()):
                for key in Mode.keys():
                    if (Mode[key] == 3): return key
            return False

        def IsPocket(Hand):
            Mode = dict()
            for element in Hand:
                if element.number not in Mode:
                    Mode[element.number] = 1
                else:
                    Mode[element.number] += 1

            Result = []
            for key in Mode.keys():
                if (Mode[key] == 2): Result.append(key)

            if (len(Result) != 2): return False

            return sorted(Result)

            return False

        def IsPair(Hand):
            Mode = dict()
            for element in Hand:
                if element.number not in Mode:
                    Mode[element.number] = 1
                else:
                    Mode[element.number] += 1

            Result = []
            if 2 in set(Mode.values()):
                for key in Mode.keys():
                    if (Mode[key] == 2): Result.append(key)

                return max(Result)
            else:
                return False

        def Mapping(Hand):
            Numbers = [card.number for card in Hand]
            return sorted(Numbers)

        def ShowDialog(Message):
            WX.MessageBox(Message,"Winner is..,", WX.OK|WX.ICON_INFORMATION)


        Player1Cards = [card[0] for card in Player1CardsData]
        Player2Cards = [card[0] for card in Player2CardsData]

        FindCard = [False, False]
        FindCard[0] = IsRoyalFlush(Player1Cards)
        FindCard[1] = IsRoyalFlush(Player2Cards)

        if FindCard[0] != False and FindCard[1] != False:
            return ShowDialog("The 2 have Royal Flush, Tie")

        elif FindCard[0] != False or FindCard[1] != False:
            return ShowDialog(f"For having a Royal Flush, wins {'Player 1' if FindCard[0] else 'Player 2'}")

        PossibleHands = [
            [IsStraightFlush, "Straight Flush", False], 
            [IsQuad, "Quad", False], 
            [IsFullHouse, "Full House", False],
            [IsColor, "Color", True],
            [IsStraight, "Straight", False],
            [IsSet, "Set", False],
            [IsPocket, "Pocket", False],
            [IsPocket, "Pocket", True],
            [IsPocket, "Pocket", True],
            [IsPair, "Pair", False],
            [Mapping, "high card", True]
        ]


        for card in Player1Cards: print(card.getData())
        for card in Player2Cards: print(card.getData())

        for idea in PossibleHands:

            FindCard[0] = idea[0](Player1Cards)
            FindCard[1] = idea[0](Player2Cards)

            print(f"Trying {idea[1]}")
            print(FindCard[0])
            print(FindCard[1])
            print()

            if FindCard[0] != False and FindCard[1] != False:
                if FindCard[0] == FindCard[1]:
                    return ShowDialog(f"It's a Tie, You 2 have a {idea[1]}")

                if idea[2]:
                    for i in range(0, 5):
                        Winner = "Player 1" if FindCard[0][4-i] > FindCard[1][4-i] else "Player 2"
                    return ShowDialog(f"Winner is by having a higger {idea[1]} {Winner}")

                else:
                    Winner = "Player 1" if FindCard[0] > FindCard[1] else "Player 2"
                    return ShowDialog(f"Winner is by having a higger {idea[1]} {Winner}")

            elif FindCard[0] != False or FindCard[1] != False:
                return ShowDialog(f"For having a {idea[1]}, wins {'Player 1' if FindCard[0] != False else 'Player 2'}")






    """===========================================
    =======      TO CHANGE CARDS         =========
    ==========================================="""
    def OnChangeCards(self, event, Player):
        
        DialogCard = WX.TextEntryDialog(None, f'What card do you want to change Player {Player}?')
        DialogCard.ShowModal()
        ResultStr = DialogCard.GetValue()
        DialogCard.Destroy()

        CardToChange = 0
        Error = False
        try: 
            CardToChange = int(ResultStr) - 1

            if (CardToChange < 0 or CardToChange > 4):
                Error = True
        except ValueError:
            Error = True

        if (Error):
            WX.MessageBox("Not valid card, please select a number from 0 to 5",
            "Change Cards",
            WX.OK|WX.ICON_INFORMATION)

            return;

        if (self.NextAvailableCard == 52):
            WX.MessageBox("No more cards",
            "Change Cards",
            WX.OK|WX.ICON_INFORMATION)

            return;

        card = self.Cards[self.NextAvailableCard]
        CardString = card.getUnicode()
        self.NextAvailableCard += 1

        PlayerCards = Player1CardsData if Player == 1 else Player2CardsData

        PlayerCards[CardToChange][1].SetForegroundColour(card.getColorAsRGB())
        PlayerCards[CardToChange][1].SetLabel(CardString)
        PlayerCards[CardToChange] = (card, PlayerCards[CardToChange][1])


    """===========================================
    =======          ON ABOUT            =========
    ==========================================="""
    def OnAbout(self, event):
        """Display an About Dialog"""
        WX.MessageBox("""
            This is a simple app to play 'poker' ... or something
            like this, I don't know what I'm doing""",
            "Play Poker",
            WX.OK|WX.ICON_INFORMATION)









"""=========================================================
===============            'MAIN'          =================
========================================================="""
if __name__ == '__main__':

    PlayPokerApp = WX.App()
    SimpleGame = PlayPokerFrame(None, title='Play Poker')
    SimpleGame.Show()

    PlayPokerApp.MainLoop()

