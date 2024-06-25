import wx

class HTMLWndAccessibilityImpl(wx.Accessible):

    def __init__(self, widget):
        super(HTMLWndAccessibilityImpl, self).__init__(wx.ACC_SELF)
        self.widget = widget

    def GetName(self, id):
        return (wx.ACC_OK, "Documento")
    
    def GetRole(self, id):
        return (wx.ACC_OK, wx.ROLE_SYSTEM_TEXT)
    
    def GetKeyboardShortcut(self, childId):
        return (wx.ACC_OK, )
    