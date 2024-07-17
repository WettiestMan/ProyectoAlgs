import wx
from gui import MainFrame


if __name__ == '__main__':

    app = wx.App()
    mframe = MainFrame(None, 'AI markdown system')
    app.MainLoop()