import wx
import wx.html as html

# TODO: Ver como quitar el tamaño fijo del HtmlPanel

class HtmlPanel(wx.Panel):
    
    def __init__ (self, parent, html="", size=(400, 600), *args, **kwargs):
        
        super(HtmlPanel, self).__init__(parent, *args, **kwargs)


        self.SetMinSize((800, 700))


        self.browser = wx.html2.WebView.New(self)
        # Bind the key event to the custom handler
        self.browser.Bind(wx.EVT_CHAR, self.on_key_char)
        self.setHtmlContent("")


        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.browser, 1, wx.EXPAND)
        self.SetSizer(sizer)
        
    def on_key_char(self, event):
        # Prevent the default behavior for key events
        # You can specify conditions to disable specific shortcuts
        keycode = event.GetKeyCode()
        if keycode in [wx.WXK_CONTROL, wx.WXK_SHIFT, wx.WXK_ALT, wx.WXK_COMMAND]:
            event.Skip()
        else:
            return  # Prevent default behavior for other keys        

    
    def setHtmlContent(self, HtmlContent):
        self.browser.SetPage(HtmlContent, "")

    def moveToHeader(self, headerId):
        script = f"document.getElementById('{headerId}').scrollIntoView();"
        self.browser.RunScript(script)