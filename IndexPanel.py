import wx
import wx.html2
from bs4 import BeautifulSoup
import markdown
import re

class IndexPanel(wx.Panel):

    def __init__(self, parent, context="", *args, **kw):
        super(IndexPanel, self).__init__(parent, *args, **kw)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.updateContext(context)
        


    def updateContext(self, context):
        self.destroyButtons()

        
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        
        soup = BeautifulSoup(context, features='lxml')
        for header in soup.findAll(re.compile("^h[1-6]$")):
            self.addButton(header)

        self.SetSizer(self.sizer)
        self.sizer.Layout()
        self.Update()
        self.Refresh()


    def addButton(self, header):

        button = wx.Button(self, label=header.contents[0])
        button.Bind(wx.EVT_BUTTON, lambda event: self.Parent.GetWindow2().moveToHeader(header.get("id")))

        self.sizer.Add(button, 0, wx.ALL, 10)


    def destroyButtons(self):
        
        for child in self.GetChildren():
            if isinstance(child, wx.Button):
                child.Destroy()
        
        
        self.sizer.Layout()
