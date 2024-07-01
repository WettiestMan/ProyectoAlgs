import wx
import wx.html as html

# TODO: Ver como quitar el tamaño fijo del HtmlPanel

class HtmlPanel(wx.Panel):
    
    def __init__ (self, parent, html="", size=(400, 600), *args, **kwargs):
        
        super(HtmlPanel, self).__init__(parent, *args, **kwargs)

        self.SetMinSize((800, 700))


        self.browser = wx.html2.WebView.New(self)
        self.setHtmlContent("")

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.browser, 1, wx.EXPAND)
        self.SetSizer(sizer)

    
    def setHtmlContent(self, HtmlContent):
        self.browser.SetPage(HtmlContent, "")