import wx
from gui import MainFrame


if __name__ == '__main__':

    app = wx.App()
    mframe = MainFrame(None, 'An original Markdown system')
    mframe.Show()
    app.MainLoop()