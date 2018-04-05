"""=========================================================
===============        PLAY POKER       ====================
========================================================="""

import wx as WX
import Card as CardClass
import random


P1Cards = list()
P2Cards = list()



class PlayPokerFrame(WX.Frame):
    """
    A Frame that show the cards for 2 players
    """


    def __init__(self, *args, **kw):
        
        # Ensure the parent's __init__ is called
        super(PlayPokerFrame, self).__init__(*args, **kw, size=(900,600))

        # Create a panel in the frame
        PlayPokerPanel = WX.Panel(self)
        self.SetBackgroundColour((102,187,106))

        # Make Title Look
        PanelTitle = WX.StaticText(PlayPokerPanel, label="Play Poker", pos=(25,5))
        PanelTitle.SetForegroundColour((27,94,32))
        PanelTitle.GetFont().SetPointSize(2300)
        PanelFont = PanelTitle.GetFont()
        PanelFont.SetPointSize(50) 
        PanelFont = PanelFont.Bold()
        PanelTitle.SetFont(PanelFont)

        self.Cards = CardClass.Card.CreateDeckOfCards()
        random.shuffle(self.Cards)


        # =============================
        # ===    CARDS PLAYER 1   =====
        # =============================
        CardsPlayer1 = self.Cards[0:5]

        CardsPlayer1String = ""

        Counter = 70
        for MiniCard in CardsPlayer1:
            
            CardsPlayer1String = MiniCard.getUnicode()

            Player1Card = WX.StaticText(PlayPokerPanel, label=CardsPlayer1String, pos=(Counter,150))
            P1Cards.append((MiniCard, Player1Card))
            Card1Font = Player1Card.GetFont()
            Card1Font.SetPointSize(150) 
            Player1Card.SetFont(Card1Font)
            Player1Card.SetForegroundColour(MiniCard.getColorAsRGB())

            Counter += 120

        Player1Title = WX.StaticText(PlayPokerPanel, label="Player 1 Cards", pos=(60, 120))
        Player1Title.SetForegroundColour((40,53,147))
        Player1TitleFontFont = Player1Title.GetFont()
        Player1TitleFontFont.SetPointSize(25) 
        Player1TitleFontFont = Player1TitleFontFont.Bold()
        Player1Title.SetFont(Player1TitleFontFont)


        # =============================
        # ===    CARDS PLAYER 2   =====
        # =============================
        CardsPlayer2 = self.Cards[5:10]

        CardsPlayer2String = ""

        Counter = 70
        for MiniCard in CardsPlayer2:
            
            CardsPlayer2String = MiniCard.getUnicode()

            Player2Card = WX.StaticText(PlayPokerPanel, label=CardsPlayer2String, pos=(Counter,350))
            P2Cards.append((MiniCard, Player2Card))
            Card2Font = Player2Card.GetFont()
            Card2Font.SetPointSize(150) 
            Player2Card.SetFont(Card2Font)
            Player2Card.SetForegroundColour(MiniCard.getColorAsRGB())

            Counter += 120

        Player2Title = WX.StaticText(PlayPokerPanel, label="Player 2 Cards", pos=(60, 330))
        Player2Title.SetForegroundColour((40,53,147))
        Player2TitleFont = Player1Title.GetFont()
        Player2TitleFont.SetPointSize(25) 
        Player2Title.SetFont(Player2TitleFont)


        # Create a menu bar
        self.makeMenuBar()

        # And a status bar
        self.CreateStatusBar()
        self.SetStatusText("Play Poker")
        self.NextAvailableCard = 10


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

    def OnExit(self, event):
        """Close the frame, terminating the PlayPokerApplication."""
        self.Close(True)


    def OnFinish(self, event):


        for Card in P1Cards:
            print(Card[0].getUnicode())

        print("")
        for Card in P2Cards:
            print(Card[0].getUnicode())



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

        MiniCard = self.Cards[self.NextAvailableCard]
        CardString = MiniCard.getUnicode()
        self.NextAvailableCard += 1

        if (Player == 1): PlayerCards = P1Cards
        else: PlayerCards = P2Cards

        PlayerCards[CardToChange][1].SetForegroundColour(MiniCard.getColorAsRGB())
        PlayerCards[CardToChange][1].SetLabel(CardString)
        PlayerCards[CardToChange] = (MiniCard, PlayerCards[CardToChange][1])


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
    frm = PlayPokerFrame(None, title='Play Poker')
    frm.Show()

    PlayPokerApp.MainLoop()


