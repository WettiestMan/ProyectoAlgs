import wx
import os
from sys import argv
from HtmlPanel import HtmlPanel
from txting import MarkdownDoc
from Accesible import HTMLWndAccessibilityImpl
from IndexPanel import IndexPanel
import markdown
from resumemodel import ResumeGen

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

        self.headers = ""
        
        # forwarding params
        wx.Frame.__init__(self, parent, -1 , title)

        self.SetMinSize(wx.Size(400, 300))

        splitter = wx.SplitterWindow(self)
        self.createMenu()
        self.htmlPanel = HtmlPanel(splitter, self, "")
        self.buttonsPanel = IndexPanel(splitter)

        self.Center()
        if(len(argv) >= 2):
            filepath = argv[1]
            self.loadFile(filepath)


        splitter.SplitVertically(self.buttonsPanel, self.htmlPanel, 100)
        splitter.SetSashGravity(0.2)

        self.Bind(wx.EVT_CLOSE, self.cleanThings)

        self.Show()

    
    def focusOnWebView(self, evt):
        self.htmlPanel.SetFocus()
    
    def focusOnToc(self, evt):
        self.buttonsPanel.SetFocus()

    def createMenu(self):

        try:
            fileSubMenu = wx.Menu()

            openItem = fileSubMenu.Append(wx.ID_OPEN, '&Abrir\tCtrl-O',
                                        "Abrir un documento en formato markdown")
            self.Bind(wx.EVT_MENU, self.OpenFile, openItem)
            
            fileSubMenu.AppendSeparator()

            exitItem = fileSubMenu.Append(wx.ID_EXIT, "Salir\tCtrl-Q",
                                        "Cerrar la aplicación")
            self.Bind(wx.EVT_MENU, self.CloseApp, exitItem)

            helpSubMenu = wx.Menu()

            resumeItem = helpSubMenu.Append(wx.NewId(), "&Generar resumen\tCtrl-G",
                                            "Obtener un resumen del texto en el lector")
            self.Bind(wx.EVT_MENU, self.GenerateResume, resumeItem)

            helpItem = helpSubMenu.Append(wx.ID_HELP_COMMANDS, 'A&tajos\tCtrl-H',
                                        "Mostrar atajos del teclado")
            self.Bind(wx.EVT_MENU, self.ShowShortcuts, helpItem)

            windowSubMenu = wx.Menu()

            tocItem = windowSubMenu.Append(wx.NewId(), "&Tabla de contenidos",
                                           "Acceda a la tabla de contenidos, o salga del lector")
            self.Bind(wx.EVT_MENU, self.focusOnToc, tocItem)

            webViewItem = windowSubMenu.Append(wx.NewId(), "&Lector",
                                               "Acceda al lector")
            self.Bind(wx.EVT_MENU, self.focusOnWebView, webViewItem)
            
            menuBar = wx.MenuBar()
            menuBar.Append(fileSubMenu, "&Archivo")
            menuBar.Append(helpSubMenu, "A&yuda")
            menuBar.Append(windowSubMenu, "&Ventana")

            (focusWebViewId, focusTocId) = [wx.NewId() for i in range(2)]

            self.Bind(wx.EVT_MENU, self.focusOnToc, id=focusTocId)
            self.Bind(wx.EVT_MENU, self.focusOnWebView, id=focusWebViewId)

            self.entries = [
                (wx.ACCEL_CTRL, ord('O'), openItem.GetId()),
                (wx.ACCEL_CTRL, ord('Q'), exitItem.GetId()),
                (wx.ACCEL_CTRL, ord('H'), helpItem.GetId()),
                (wx.ACCEL_CTRL, ord('G'), resumeItem.GetId()),
                (wx.ACCEL_ALT, ord('1'), focusWebViewId),
                (wx.ACCEL_ALT, ord('2'), focusTocId)
            ]

            self.accTable = wx.AcceleratorTable(self.entries)
            self.SetAcceleratorTable(self.accTable)

            self.SetMenuBar(menuBar)

        except Exception as e:
            print(e)


    def OpenFile(self, event):

        with wx.FileDialog(self, "Abrir documento",
                           f"{os.path.expanduser('~')}\\Documents",
                           wildcard="Archivos Markdown (*.md;*.markdown;*.mdown;*.mkdn;*.mkd;"
                                    "*.mdwn;*.mdtxt;*.mdtext;*.text;*.Rmd)|*.md;*.markdown;"
                                    "*.mdown;*.mkdn;*.mkd;*.mdwn;*.mdtxt;*.mdtext;*.text;*.Rmd",
                                    style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fdialg:
            
            if fdialg.ShowModal() == wx.ID_CANCEL:
                self.htmlStr = ""
                self.SetFocus()
                return
            
            path = fdialg.GetPath()
            self.loadFile(path)
            self.SetFocus()

    def loadFile(self, filepath):
        
        try:
            with (open(filepath, 'r', encoding='UTF-8')) as file:
                
                self.htmlStr = markdown.markdown(file.read(), extensions=["toc"])
                self.htmlPanel.setHtmlContent(self.htmlStr)
                self.buttonsPanel.updateContext(self.htmlStr)
        except OSError:
            wx.MessageBox(f"""
            El archivo {filepath} no pudo ser abierto.
            Puede que el archivo no exista o no pueda ser leido por alguna
            otra razón. Intente de nuevo o abra otro archivo.
            """, "Error al abrir: {filepath}", wx.OK | wx.ICON_WARNING | wx.CENTRE,
            None)

    
    def handle_key_event(self, modifiers, keycode):
        # Custom logic to handle specific key events
        # Return True if the event is handled, otherwise False
        if modifiers == wx.ACCEL_CTRL and keycode == ord('R'):
            self.on_ctrl_r(None)
            return True  # Prevent default behavior
        elif modifiers == wx.ACCEL_CTRL and keycode == ord('T'):
            self.on_ctrl_t(None)
            return True  # Prevent default behavior
        
        # Add more custom key handling as needed
        return False

    def on_ctrl_r(self, event):
        # Handle Ctrl+R key event (for example, prevent refresh)
        print("Ctrl+R pressed - Refresh prevented")

    def on_ctrl_t(self, event):
        # Handle Ctrl+T key event
        print("Ctrl+T pressed")
    
    def GenerateResume(self, event):
        if(hasattr(self, "htmlStr") and self.htmlStr != ""):
            headers = ResumeGen.reduceText(self.htmlStr)
            # you can write your logic in generate, or do it however you want
            resume = ResumeGen.generate(headers)

            wx.MessageBox(resume, "Resumen del texto", wx.ICON_QUESTION | wx.CENTER)
            self.SetFocus()
        else:
            wx.MessageBox("por favor, cargue un documento antes de usar", "Nada para resumir", wx.ICON_ASTERISK
                           | wx.CENTER)
            self.SetFocus()


    def CloseApp(self, event):

        decision = wx.MessageBox("¿Está seguro de que desea salir?", "Salir", wx.YES_NO |
                                 wx.ICON_ASTERISK | wx.CENTER | wx.CANCEL)
        if decision == 2:
            self.Close(True)
            return
        
        self.SetFocus()
    
    def cleanThings(self, event):
        self.Destroy()

    def ShowShortcuts(self, event):
        # TODO: Implementar una ventana que muestre los atajos para cambiar el
        # 'focus' a un elemento de la ventana
        # por el momento, solo emite un mensaje cualquiera
        message = """
Alt + 1: Dirigirse al lector.
Alt + 2: Dirigirse a la tabla de contenidos.
Otras combinaciones con Alt:
A: Menú archivo, Y: menú ayuda, V: menú ventana.
Ctrl + O: Abrir un documento.
Ctrl + G: Generar un resumen del texto actual.
Ctrl + Q: Cerrar el programa.
Ctrl + H: Mostrar esta ayuda.
"""
        wx.MessageBox(message, "Controles", wx.OK |
                      wx.ICON_INFORMATION | wx.CENTER)
        self.SetFocus()
