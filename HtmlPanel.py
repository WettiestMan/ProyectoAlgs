import wx
import wx.html as html

# TODO: Ver como quitar el tamaño fijo del HtmlPanel

class HtmlPanel(wx.Panel):
    
    def __init__ (self, parent, parent_frame, size=(400, 600), *args, **kwargs):
        
        super(HtmlPanel, self).__init__(parent, *args, **kwargs)
        self.parent = parent_frame

        self.SetMinSize((800, 700))

        self.browser = wx.html2.WebView.New(self)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.browser, 1, wx.EXPAND)
        self.SetSizer(sizer)

        
        # Bind the key event to the frame
        self.browser.Bind(wx.EVT_CHAR_HOOK, self.on_key_char)

    def on_key_char(self, event):
        keycode = event.GetKeyCode()
        modifiers = self.get_modifiers(event)
        
        # Redirect the key event to the main app's handlers
        if self.parent.handle_key_event(modifiers, keycode):
            return  # Prevent default behavior if handled
        event.Skip()

    def get_modifiers(self, event):
        modifiers = 0
        if event.ControlDown():
            modifiers |= wx.ACCEL_CTRL
        if event.ShiftDown():
            modifiers |= wx.ACCEL_SHIFT
        if event.AltDown():
            modifiers |= wx.ACCEL_ALT
        if event.MetaDown():
            modifiers |= wx.ACCEL_CMD
        return modifiers

    
    def setHtmlContent(self, HtmlContent):
        self.browser.SetPage(HtmlContent, "")


    def moveToHeader(self, headerId):
        script = f"document.getElementById('{headerId}').scrollIntoView();"
        self.browser.RunScript(script)