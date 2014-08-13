#!/usr/bin/env python
import wx
from PIL import Image
import os


class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        # main frame
        wx.Frame.__init__(self, parent, id, title)
        self.Centre()
        self.Maximize(True)

        # main layout
        self.mainbox = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.mainbox)

        # build menu
        self.BuildMenu()

        # build toolbar
        self.BuildToolBar()

        # init images
        self.image = None
        self.filteredimage = None

        # add images containers
        self.AddImagesContainers()

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
        self.mainbox.Add(toolbar, 0, wx.EXPAND)

    def AddImagesContainers(self):
        """ Add image & filtered image containers
        """
        imagesbox = wx.BoxSizer(wx.HORIZONTAL)

        # add image container to layout
        imagesizer = wx.BoxSizer(wx.VERTICAL)
        self.imagecontainer = wx.StaticBitmap(self)
        imagesizer.Add(wx.StaticText(self, -1, label="Original image"), 0, wx.ALIGN_LEFT)
        imagesizer.Add(self.imagecontainer, 1, wx.ALIGN_LEFT)
        imagesbox.Add(imagesizer, 1, wx.ALIGN_LEFT)

        # add a separator
        separator = wx.StaticLine(self, -1, size=(0, 1000), style=wx.LI_VERTICAL)
        imagesbox.Add(separator, 0)

        # add filtered image container to layout
        filteredimagesizer = wx.BoxSizer(wx.VERTICAL)
        self.filteredimagecontainer = wx.StaticBitmap(self)
        filteredimagesizer.Add(wx.StaticText(self, -1, label="Filtered image"), 0, wx.ALIGN_LEFT)
        filteredimagesizer.Add(self.filteredimagecontainer, 1, wx.ALIGN_LEFT)
        imagesbox.Add(filteredimagesizer, 1, wx.ALIGN_LEFT)

        # add images layout to main layout
        self.mainbox.Add(imagesbox, 0, wx.EXPAND)

    def OnOpen(self, event):
        """ Called when clicking on 'open' menu-item
            to open a file dialog
        """
        dlg = wx.FileDialog(self, "Choose an image", "", "", "Image files (*jpg,*.png)|*.jpeg;*.png", wx.OPEN)

        # load selected image
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.image = Image.open(path)

            # show image
            self.imagecontainer.SetBitmap(wx.Bitmap(path))

            # get filename & file extension
            self.filename = os.path.basename(path)
            self.fileextension = os.path.splitext(path)[1]

            # change frame title
            self.SetTitle(path + " - Image Processing")

        dlg.Destroy()

    def OnSave(self, event):
        """ Called when clicking on 'save' menu-item
        """
        if not(self.filteredimage is None):
            dlg = wx.FileDialog(self, "Save the image", "", "", "Image fileds (*.jpg,*png)|*.jpeg;*.png", wx.SAVE)

            # save filtered image
            if dlg.ShowModal() == wx.ID_OK:
                self.filteredimage.save(dlg.GetPath() + self.fileextension)

            dlg.Destroy()
        else:
            wx.MessageBox("Image not filtered yet.", "Error", style=wx.ICON_ERROR)

    def OnQuit(self, event):
        """ Called when clicking on 'quit' menu-item
            to quit the application
        """
        self.Close()

    def OnBlackAndWhite(self, event):
        """ Called when clicking on 'black and white' menu-item
        """
        if not(self.image is None):
            self.filteredimage = self.image.convert('L')

            # save a temporary copy of filtered image
            tmpfilepath = '/tmp/' + self.filename
            self.filteredimage.save(tmpfilepath)

            # show filtered image
            self.filteredimagecontainer.SetBitmap(wx.Bitmap(tmpfilepath))
        else:
            wx.MessageBox("Image not opened yet.", "Error", style=wx.ICON_ERROR)

    def OnAbout(self, event):
        """ Called when clicking on 'about' menu-item
            to show a message box dialog
        """
        wx.MessageBox("Create by 'h4k1m'")


class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, -1, 'Image processing')
        frame.Show(True)
        return True


app = MyApp(0)
app.MainLoop()
