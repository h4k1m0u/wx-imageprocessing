#!/usr/bin/env python
import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        # main frame
        wx.Frame.__init__(self, parent, id, title)
        self.Centre()

        # main layout
        self.mainbox = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.mainbox)

        # build menu
        self.BuildMenu()

        # build toolbar
        self.BuildToolBar()

        # add statusbar
        self.CreateStatusBar()

    def BuildMenu(self):
        """ Build the menu
        """
        # menu bar
        menubar = wx.MenuBar()

        # menus
        file = wx.Menu()
        edit = wx.Menu()
        help = wx.Menu()

        # menus-items
        open = wx.MenuItem(file, 101, '&Open', 'Open an Image')
        save = wx.MenuItem(file, 102, '&Save', 'Save the Image')
        quit = wx.MenuItem(file, 103, '&Quit', 'Quit the Application')
        bw = wx.MenuItem(edit, 201, '&Black and White', 'Black and White')
        about = wx.MenuItem(help, 301, '&About', 'About Image Processing')

        # set menu-items icons
        open.SetBitmap(wx.Image('icons/16x16/open-icon-16x16.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap())
        save.SetBitmap(wx.Image('icons/16x16/save-icon-16x16.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap())
        quit.SetBitmap(wx.Image('icons/16x16/quit-icon-16x16.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap())
        bw.SetBitmap(wx.Image('icons/16x16/exec-icon-16x16.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap())
        about.SetBitmap(wx.Image('icons/16x16/about-icon-16x16.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap())

        # append menu-items to menus
        file.AppendItem(open)
        file.AppendItem(save)
        file.AppendItem(quit)
        edit.AppendItem(bw)
        help.AppendItem(about)

        # append menus to menubar
        menubar.Append(file, '&File')
        menubar.Append(edit, '&Edit')
        menubar.Append(help, '&Help')

        # bind menu-items to events listeners
        self.Bind(wx.EVT_MENU, self.OnOpen, id=101)
        self.Bind(wx.EVT_MENU, self.OnSave, id=102)
        self.Bind(wx.EVT_MENU, self.OnQuit, id=103)
        self.Bind(wx.EVT_MENU, self.OnBlackAndWhite, id=201)
        self.Bind(wx.EVT_MENU, self.OnAbout, id=301)

        self.SetMenuBar(menubar)

    def BuildToolBar(self):
        """ Build the Toolbar
        """
        toolbar = wx.ToolBar(self, -1)

        # add buttons to toolbar
        toolbar.AddSimpleTool(1001, wx.Image('icons/open-icon.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'Open', 'Open an Image')
        toolbar.AddSimpleTool(1002, wx.Image('icons/save-icon.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'Save', 'Save the Image')
        toolbar.AddSimpleTool(1003, wx.Image('icons/quit-icon.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'Quit', 'Quit the Application')
        toolbar.AddSeparator()
        toolbar.AddSimpleTool(2001, wx.Image('icons/exec-icon.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'Black and White', 'Black and White')
        toolbar.AddSeparator()
        toolbar.AddSimpleTool(3001, wx.Image('icons/about-icon.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'About', 'About Image Processing')

        # bind menu-items to events listeners
        self.Bind(wx.EVT_MENU, self.OnOpen, id=1001)
        self.Bind(wx.EVT_MENU, self.OnSave, id=1002)
        self.Bind(wx.EVT_MENU, self.OnQuit, id=1003)
        self.Bind(wx.EVT_MENU, self.OnBlackAndWhite, id=2001)
        self.Bind(wx.EVT_MENU, self.OnAbout, id=3001)

        # render & add to layout
        toolbar.Realize()
        self.mainbox.Add(toolbar, 0, wx.EXPAND, 0, wx.EXPAND)

    def OnOpen(self, event):
        """ Called when clicking on 'open' menu-item
            to open a file dialog
        """
        pass

    def OnSave(self, event):
        """ Called when clicking on 'save' menu-item
        """
        pass

    def OnQuit(self, event):
        """ Called when clicking on 'quit' menu-item
            to quit the application
        """
        self.Close()

    def OnBlackAndWhite(self, event):
        """ Called when clicking on 'black and white' menu-item
        """
        pass

    def OnAbout(self, event):
        """ Called when clicking on 'about' menu-item
            to show a message box dialog
        """
        wx.MessageBox('Create by "h4k1m"')


class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, -1, 'Image processing')
        frame.Show(True)
        return True


app = MyApp(0)
app.MainLoop()
