import wx
import wx.html2 as html

class AccelCreator:

    @staticmethod
    def createBindingsForAccelTable(parent, ids: list[int], functionlist: list[callable]):

        assert len(ids) == len(functionlist)
        for i in range(len(ids)):
            parent.Bind(wx.EVT_MENU, functionlist[i], id=ids[i])

    @staticmethod
    def createAcceleratorTable(parent, ids: list[int], bindings: list[tuple[int, str]]):

        assert len(ids) == len(bindings)
        entries = []
        for i in range(len(ids)):
            entries.append((bindings[i][0], ord(bindings[i][1]), ids[i]))

        accel = wx.AcceleratorTable(entries)
        parent.SetAcceleratorTable(accel)