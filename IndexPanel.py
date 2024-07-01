import wx
import wx.html2
from bs4 import BeautifulSoup

class IndexPanel(wx.Panel):

    def __init__(self, parent, *args, **kw):
        super(IndexPanel, self).__init__(parent, *args, **kw)

        sizer = wx.BoxSizer(wx.VERTICAL)

        # Example buttons
        button1 = wx.Button(self, label="Button 1")
        button2 = wx.Button(self, label="Button 2")
        button3 = wx.Button(self, label="Button 3")
        
        sizer.Add(button1, 0, wx.ALL, 10)
        sizer.Add(button2, 0, wx.ALL, 10)
        sizer.Add(button3, 0, wx.ALL, 10)
        
        self.SetSizer(sizer)

