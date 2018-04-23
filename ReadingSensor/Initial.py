# ====================================================================
# ==============      READ FROM SERIAL PORT     ======================
# ====================================================================
from time import sleep
import serial
import wx as WX


try:
    SerialConection = serial.Serial('/dev/tty.usbmodem621', 9600)
except:
    SerialConection = serial.Serial('/dev/tty.usbmodem411', 9600)





"""=========================================================
===============       SEE SENSOR        ====================
========================================================="""
class SeeSensorFrame(WX.Frame):
    """
    A Frame that show the cards for 2 players, just that
    """

    """===========================================
    =============        INIT        =============
    ==========================================="""
    def __init__(self, *args, **kw):
        
        # Ensure the parent's __init__ is called
        super(SeeSensorFrame, self).__init__(*args, **kw, size=(900,600))

        # Create a panel in the frame
        PlayPokerPanel = WX.Panel(self)
        self.SetBackgroundColour((102,187,106))

        # ====  Make Title Look ======
        PanelTitle = WX.StaticText(PlayPokerPanel, label="See Sensor", pos=(25,5))
        PanelTitle.SetForegroundColour((27,94,32))
        PanelTitle.GetFont().SetPointSize(2300)
        PanelFont = PanelTitle.GetFont()
        PanelFont.SetPointSize(50) 
        PanelFont = PanelFont.Bold()
        PanelTitle.SetFont(PanelFont)


        # Create a menu bar
        self.makeMenuBar()

        # And a status bar
        self.CreateStatusBar()
        self.SetStatusText("See Sensor")



    """===========================================
    =======        MAKE A MENU BAR       =========
    ==========================================="""
    def makeMenuBar(self):

        #=== OPTIONS MENU ====
        OptionsMenu = WX.Menu()
        exitItem = OptionsMenu.Append(WX.ID_EXIT)

        #=== GAME MENU ====
        GameMenu = WX.Menu()
        FinishItem  = GameMenu.Append(-1, "&Finish\tCtrl-F")
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

        Counter = 32

        while True:
            
            SerialConection.write(str(chr(Counter)).encode())
            print(SerialConection.readline().decode())
            
            Counter = (Counter + 1) % 255 






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

    SeeSensorsApp = WX.App()
    SimpleGame = SeeSensorFrame(None, title='See Sensor')
    SimpleGame.Show()

    SeeSensorsApp.MainLoop()
