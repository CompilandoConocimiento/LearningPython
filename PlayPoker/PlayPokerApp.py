"""=========================================================
===============        PLAY POKER       ====================
========================================================="""

import wx as WX
import Card as CardClass
import random



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


        Cards = CardClass.Card.GetRandomCards()
        random.shuffle(Cards)

        # =============================
        # ===    CARDS PLAYER 1   =====
        # =============================
        CardsPlayer1 = Cards[0:5]

        CardsPlayer1String = ""

        Counter = 70
        for MiniCard in CardsPlayer1:
            
            CardsPlayer1String = MiniCard.getUnicodeAndColor()[0]

            Player1Card = WX.StaticText(PlayPokerPanel, label=CardsPlayer1String, pos=(Counter,150))
            Card1Font = Player1Card.GetFont()
            Card1Font.SetPointSize(150) 
            Player1Card.SetFont(Card1Font)
            ColorCardStr = MiniCard.getUnicodeAndColor()[1]
            if ColorCardStr == "Red": ColorCard = (211,47,47)
            else: ColorCard = (33,33,33)
            Player1Card.SetForegroundColour(ColorCard)

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
        CardsPlayer2 = Cards[5:10]

        CardsPlayer2String = ""

        Counter = 70
        for MiniCard in CardsPlayer2:
            
            CardsPlayer2String = MiniCard.getUnicodeAndColor()[0]

            Player2Card = WX.StaticText(PlayPokerPanel, label=CardsPlayer2String, pos=(Counter,350))
            Card2Font = Player2Card.GetFont()
            Card2Font.SetPointSize(150) 
            Player2Card.SetFont(Card2Font)
            ColorCardStr = MiniCard.getUnicodeAndColor()[1]
            if ColorCardStr == "Red": ColorCard = (211,47,47)
            else: ColorCard = (33,33,33)
            Player2Card.SetForegroundColour(ColorCard)

            Counter += 120

        Player2Title = WX.StaticText(PlayPokerPanel, label="Player 2 Cards", pos=(60, 330))
        Player2Title.SetForegroundColour((40,53,147))
        Player2TitleFont = Player1Title.GetFont()
        Player2TitleFont.SetPointSize(25) 
        Player2TitleFont = Player2TitleFont.Bold()
        Player2Title.SetFont(Player2TitleFont)



        # Create a menu bar
        self.makeMenuBar()

        # And a status bar
        self.CreateStatusBar()
        self.SetStatusText("Play Poker")


    def makeMenuBar(self):

        #=== OPTIONS MENU ====
        OptionsMenu = WX.Menu()

        ChangeCardPlayer1 = OptionsMenu.Append(-1, "&Change Cards for Player 1\tCtrl-1")
        ChangeCardPlayer2 = OptionsMenu.Append(-1, "&Change Cards for Player 2\tCtrl-2")
        OptionsMenu.AppendSeparator()
        exitItem = OptionsMenu.Append(WX.ID_EXIT)

        #=== GAME MENU ====
        GameMenu = WX.Menu()

        RestartItem = GameMenu.Append(-1, "&Restart\tCtrl-R")
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
        self.Bind(WX.EVT_MENU, self.OnChangeCards, ChangeCardPlayer1)
        self.Bind(WX.EVT_MENU, self.OnChangeCards, ChangeCardPlayer2)
        self.Bind(WX.EVT_MENU, self.OnRestart, RestartItem)
        self.Bind(WX.EVT_MENU, self.OnExit,  exitItem)
        self.Bind(WX.EVT_MENU, self.OnAbout, aboutItem)

    def OnExit(self, event):
        """Close the frame, terminating the PlayPokerApplication."""
        self.Close(True)


    def OnRestart(self, event):
        RestartDialog = WX.MessageDialog(self, "Restarting App", "Playing Poker", WX.OK)
        RestartDialog.ShowModal()
        RestartDialog.Destroy()

    def OnChangeCards(self, event):
        DialogCard = WX.TextEntryDialog(None, 'What card you want to change?')
        DialogCard.ShowModal()
        ResultStr = DialogCard.GetValue()
        DialogCard.Destroy()

        try: 
            Result = int(ResultStr)
            Result -= 1
        except ValueError:
            return 0


        print(f'Your name was {Result}')

        return Result


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


