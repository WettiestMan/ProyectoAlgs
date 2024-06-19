import wx
import wx.html as html

class HtmlPanel(wx.Panel):
    
    def __init__ (self, *args, **kwargs):
        
        super(HtmlPanel, self).__init__(*args, **kwargs)
        htmlSizer = self.CreateHtmlPanelAndItsSizer(args[0])
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(htmlSizer, flag=wx.ALL, border=10)
        self.SetSizerAndFit(mainSizer)
        
    def CreateHtmlPanelAndItsSizer(self, parent):
        wndStyles = wx.VSCROLL | wx.HSCROLL | wx.BORDER_SIMPLE
        parent.htmlWnd  =  html.HtmlWindow(self, id=wx.ID_ANY, size=(400,200), style=wndStyles)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(parent.htmlWnd)
        return sizer