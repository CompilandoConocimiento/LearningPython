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
        self.ReadingSensorPanel = WX.Panel(self)
        self.SetBackgroundColour((38,50,56))

        # ====  Make Title Look ======
        PanelTitle = WX.StaticText(self.ReadingSensorPanel, label="Sensor: ", pos=(25,5))
        PanelTitle.SetForegroundColour((232,245,233))
        PanelTitle.GetFont().SetPointSize(2300)
        PanelFont = PanelTitle.GetFont()
        PanelFont.SetPointSize(50) 
        PanelFont = PanelFont.Bold()
        PanelTitle.SetFont(PanelFont)

        # ==== SensorName ======
        self.SensorTitle = WX.StaticText(self.ReadingSensorPanel, label="Temperature", pos=(225,5))
        self.SensorTitle.SetForegroundColour((165,214,167))
        self.SensorTitle.GetFont().SetPointSize(2300)
        SensorNameFont = self.SensorTitle.GetFont()
        SensorNameFont.SetPointSize(50) 
        SensorNameFont = SensorNameFont.Bold()
        self.SensorTitle.SetFont(SensorNameFont)


        # ==== SensorName ======
        self.MeasureTitle = WX.StaticText(self.ReadingSensorPanel, label="Hol", pos=(25,85))
        self.MeasureTitle.SetForegroundColour((165,214,167))
        self.MeasureTitle.GetFont().SetPointSize(2300)
        MeasureNameFont = self.MeasureTitle.GetFont()
        MeasureNameFont.SetPointSize(50) 
        MeasureNameFont = MeasureNameFont.Bold()
        self.MeasureTitle.SetFont(MeasureNameFont)

        # Create a menu bar
        self.makeMenuBar()

        # And a status bar
        self.CreateStatusBar()
        self.SetStatusText("See Sensor")

        def TemperatureFunction(Measure):
            return str(Measure) + " Hola"


        self.Sensors = {
            'Temperature': {
                'Interpretate': TemperatureFunction,
                'Name': 'Termistor'
            }
        }



    """===========================================
    =======        MAKE A MENU BAR       =========
    ==========================================="""
    def makeMenuBar(self):

        #=== OPTIONS MENU ====
        OptionsMenu = WX.Menu()
        exitItem = OptionsMenu.Append(WX.ID_EXIT)

        #=== SENSOR MENU ====
        MeasureMenu = WX.Menu()
        StartItem  = MeasureMenu.Append(-1, "&Start Measure\tCtrl-Enter")
        EndItem  = MeasureMenu.Append(-1, "&End Measure\tCtrl-Escape")
        MeasureMenu.AppendSeparator()

        #=== SENSOR MENU ====
        SensorMenu = WX.Menu()
        FinishItem  = SensorMenu.Append(-1, "&Finish\tCtrl-F")
        SensorMenu.AppendSeparator()

        #=== GENERAL MENU ====
        HelpMenu = WX.Menu()
        aboutItem = HelpMenu.Append(WX.ID_ABOUT)

        #=== MENU BAR ====
        menuBar = WX.MenuBar()
        menuBar.Append(OptionsMenu, "&Options")
        menuBar.Append(MeasureMenu, "&Measure")
        menuBar.Append(SensorMenu, "&Sensor")
        menuBar.Append(HelpMenu, "&Help")
        self.SetMenuBar(menuBar)
        
        #=== BIND ====
        self.Bind(WX.EVT_MENU, self.OnMesuareStart, StartItem)
        self.Bind(WX.EVT_MENU, self.OnMesuareEnd, EndItem)
        self.Bind(WX.EVT_MENU, self.OnFinish, FinishItem)
        self.Bind(WX.EVT_MENU, self.OnExit,  exitItem)
        self.Bind(WX.EVT_MENU, self.OnAbout, aboutItem)


    """===========================================
    =======            ON EXIT           =========
    ==========================================="""
    def OnExit(self, event):
        """Close the frame, terminating the ReadingSensorApplication."""
        self.Close(True)


    """============================================
    =======       START MEASURE           =========
    ==========================================="""
    def OnMesuareStart(self, event):
        """Start the measure"""

        Selected = "Temperature"
        
        Counter = 32

        self.SensorTitle.SetLabel(self.Sensors[Selected]['Name'])

        while True:
            
            SerialConection.write(str(chr(Counter)).encode())
            Data = SerialConection.readline().decode() 
            Data = self.Sensors[Selected]['Interpretate'](Data)

            print(Data)
            
            self.MeasureTitle.SetLabel(Data)
            WX.Yield()

            Counter = (Counter + 1) % 255 

    """============================================
    =======         END MEASURE           =========
    ==========================================="""
    def OnMesuareEnd(self, event):
        """Close stop the measure"""
        pass


    """===========================================
    =======          ON FINISH           =========
    ==========================================="""
    def OnFinish(self, event):
        pass
        





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
