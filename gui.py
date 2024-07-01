import wx
import os
from sys import argv
from HtmlPanel import HtmlPanel
from txting import MarkdownDoc
from Accesible import HTMLWndAccessibilityImpl
from IndexPanel import IndexPanel
import markdown

"""
Fun fact: las funciones y constantes que realizan centrado están escritas tanto en inglés americano
como en inglés británico (center & centre). Usen cualquiera XD
"""

"""
TODO: Implementar wx.Accessible para los widgets. (Si es posible tal vez se pueda hacer en un archivo
.py aparte)

También tengan en cuenta que solo está implementado el HtmlWindow, aunque falta su wx.Accessible.
Revisen el TODO del HtmlPanel también porque el atributo size está con un valor fijo
"""

    
class MainFrame(wx.Frame):
    
    def __init__(self, parent, title):
        
        # forwarding params
        wx.Frame.__init__(self, parent, -1 , title)

        self.SetMinSize(wx.Size(400, 300))

        splitter = wx.SplitterWindow(self)
        self.createMenu()
        self.htmlPanel = HtmlPanel(splitter, "")
        self.buttonsPanel = IndexPanel(splitter)

        self.Center()
        if(len(argv) >= 2):
            filepath = argv[1]
            self.loadFile(filepath)


        splitter.SplitVertically(self.buttonsPanel, self.htmlPanel, 100)
        splitter.SetSashGravity(0.2)

        entries = []
        entries.append((wx.ACCEL_CTRL, ord('O'), self.GetMenuBar().GetMenu(0).GetMenuItem(0).GetId()))
        entries.append((wx.ACCEL_CTRL, ord('Q'), self.GetMenuBar().GetMenu(0).GetMenuItem(1).GetId()))
        entries.append((wx.ACCEL_CTRL, ord('H'), self.GetMenuBar().GetMenu(1).GetMenuItem(0).GetId()))

        accTable = wx.AcceleratorTable(entries)
        self.SetAcceleratorTable(accTable)
        
        self.Show()
        
      
    def createMenu(self):

        fileSubMenu = wx.Menu()

        openItem = fileSubMenu.Append(wx.ID_OPEN, '&Abrir\tCtrl-O',
                                      "Abrir un documento en formato markdown")
        self.Bind(wx.EVT_MENU, self.OpenFile, openItem)
        
        fileSubMenu.AppendSeparator()

        exitItem = fileSubMenu.Append(wx.ID_EXIT, "Salir\tCtrl-Q",
                                      "Cerrar la aplicación")
        self.Bind(wx.EVT_MENU, self.CloseApp, exitItem)

        helpSubMenu = wx.Menu()

        helpItem = helpSubMenu.Append(wx.ID_HELP_COMMANDS, 'A&tajos\tCtrl-H',
                                      "Mostrar atajos del teclado")
        self.Bind(wx.EVT_MENU, self.ShowShortcuts, helpItem)

        menuBar = wx.MenuBar()
        menuBar.Append(fileSubMenu, "&Archivo")
        menuBar.Append(helpSubMenu, "A&yuda")

        self.SetMenuBar(menuBar)

    def OpenFile(self, event):

        with wx.FileDialog(self, "Abrir documento",
                           f"{os.path.expanduser('~')}\\Documents",
                           wildcard="Archivos Markdown (*.md;*.markdown;*.mdown;*.mkdn;*.mkd;"
                                    "*.mdwn;*.mdtxt;*.mdtext;*.text;*.Rmd)|*.md;*.markdown;"
                                    "*.mdown;*.mkdn;*.mkd;*.mdwn;*.mdtxt;*.mdtext;*.text;*.Rmd",
                                    style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fdialg:
            
            if fdialg.ShowModal() == wx.ID_CANCEL:
                return
            
            path = fdialg.GetPath()
            self.loadFile(path)

    def loadFile(self, filepath):
        
        try:
            with (open(filepath, 'r', encoding='UTF-8')) as file:
                
                html = markdown.markdown(file.read(), extensions=["toc"])
                self.htmlPanel.setHtmlContent(html)
                self.buttonsPanel.updateContext(html)
        except OSError:
            wx.MessageBox(f"""
            El archivo {filepath} no pudo ser abierto.
            Puede que el archivo no exista o no pueda ser leido por alguna
            otra razón. Intente de nuevo o abra otro archivo.
            """, "Error al abrir: {filepath}", wx.OK | wx.ICON_WARNING | wx.CENTRE,
            None)

    
    def CloseApp(self, event):
        decision = wx.MessageBox("¿Está seguro de que desea salir?", "Salir", wx.YES_NO |
                                 wx.ICON_ASTERISK | wx.CENTER | wx.CANCEL)
        if decision == 2:
            self.Close(True)

    def ShowShortcuts(self, event):
        # TODO: Implementar una ventana que muestre los atajos para cambiar el
        # 'focus' a un elemento de la ventana
        # por el momento, solo emite un mensaje cualquiera
        wx.MessageBox("En desarrollo (-_- ) z z z", "En desarrollo", wx.OK |
                      wx.ICON_HAND | wx.CENTER)
