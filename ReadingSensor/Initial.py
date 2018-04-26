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
        self.SensorTitle = WX.StaticText(self.ReadingSensorPanel, label="", pos=(225,5))
        self.SensorTitle.SetForegroundColour((165,214,167))
        self.SensorTitle.GetFont().SetPointSize(2300)
        SensorNameFont = self.SensorTitle.GetFont()
        SensorNameFont.SetPointSize(50) 
        SensorNameFont = SensorNameFont.Bold()
        self.SensorTitle.SetFont(SensorNameFont)


        # ==== MeasureName ======
        self.MeasureTitle = WX.StaticText(self.ReadingSensorPanel, label="", pos=(25,85))
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
            return str(Measure) + "from termistor"

        def PreasureFunction(Measure):
            return str(Measure) + "from preasure"

        self.Sensors = {
            'Temperature': {
                'Interpretate': TemperatureFunction,
                'Name': 'Termistor'
            },
            'Preasure': {
                'Interpretate': PreasureFunction,
                'Name': 'Preasure Sensor'
            }
        }

        self.ContinueReading = True
        self.Selected = "Temperature"



    """===========================================
    =======        MAKE A MENU BAR       =========
    ==========================================="""
    def makeMenuBar(self):

        #=== OPTIONS MENU ====
        OptionsMenu = WX.Menu()
        FinishItem  = OptionsMenu.Append(-1, "&Finish Program\tCtrl-E")
        OptionsMenu.AppendSeparator()

        #=== SENSOR MENU ====
        MeasureMenu = WX.Menu()
        StartItem  = MeasureMenu.Append(-1, "&Start Measure\tCtrl-Enter")
        EndItem  = MeasureMenu.Append(-1, "&End Measure\tCtrl-Escape")
        MeasureMenu.AppendSeparator()

        #=== SENSOR MENU ====
        SensorMenu = WX.Menu()
        TermistorSensor  = SensorMenu.Append(-1, "&Select Termistor\tCtrl-1")
        PreasureSensor  = SensorMenu.Append(-1, "&Select Preasure\tCtrl-2")
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
        self.Bind(WX.EVT_MENU, self.OnExit, FinishItem)
        self.Bind(WX.EVT_MENU, lambda event: self.OnChange(event, "Temperature"), TermistorSensor)
        self.Bind(WX.EVT_MENU, lambda event: self.OnChange(event, "Preasure"), PreasureSensor)





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
        
        self.ContinueReading = True
        Counter = 42
        while self.ContinueReading:
            
            SerialConection.write(str(chr(Counter)).encode())
            Data = SerialConection.readline().decode() 
            Data = self.Sensors[self.Selected]['Interpretate'](Data)

            print(Data)
            
            self.MeasureTitle.SetLabel(Data)
            WX.Yield()

            Counter = (Counter + 1) % 255 

    """============================================
    =======         END MEASURE           =========
    ==========================================="""
    def OnMesuareEnd(self, event):
        """Stop the measure"""
        self.ContinueReading = False
        self.MeasureTitle.SetLabel("")

        
    """===========================================
    =====      ON CHANGE SENSOR          =========
    ==========================================="""
    def OnChange(self, event, Selected): 

        self.Selected = Selected
        self.ContinueReading = False
        self.SensorTitle.SetLabel(self.Sensors[self.Selected]['Name'])
        self.MeasureTitle.SetLabel("")



"""=========================================================
===============            'MAIN'          =================
========================================================="""
if __name__ == '__main__':

    SeeSensorsApp = WX.App()
    SimpleGame = SeeSensorFrame(None, title='See Sensor')
    SimpleGame.Show()

    SeeSensorsApp.MainLoop()
