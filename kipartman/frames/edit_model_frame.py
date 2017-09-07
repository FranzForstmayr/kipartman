from dialogs.panel_edit_model import PanelEditModel
from frames.select_snapeda_frame import SelectSnapedaFrame, EVT_SELECT_SNAPEDA_OK_EVENT
from frames.dropdown_dialog import DropdownDialog
import wx.lib.newevent
import urllib2
import tempfile
import os.path
import webbrowser
import cfscrape
import rest
from configuration import Configuration

EditModelApplyEvent, EVT_EDIT_FOOTPRINT_APPLY_EVENT = wx.lib.newevent.NewEvent()
EditModelCancelEvent, EVT_EDIT_FOOTPRINT_CANCEL_EVENT = wx.lib.newevent.NewEvent()

scraper = cfscrape.create_scraper()

none_image = os.path.abspath('resources/none-128x128.png')

def NoneValue(value, default):
    if value:
        return value
    return default

class EditModelFrame(PanelEditModel): 
    def __init__(self, parent):
        super(EditModelFrame, self).__init__(parent)
        
    def SetModel(self, model):
        self.model = model
        self.ShowModel(model)

    def ShowModel(self, model):
        configuration = Configuration()
        
        # set local files to be added
        self.local_file_image = None
        self.local_file_model = None
        
        # enable evrything else
        if model:
            self.edit_model_name.Value = NoneValue(model.name, '')
            self.edit_model_description.Value = NoneValue(model.description, '')
            self.edit_model_comment.Value = NoneValue(model.comment, '')

            try:
                self.button_open_file_image.Label = model.image.source_name
                try:
                    self.SetImage(configuration.kipartbase+'/file'+model.image.storage_path)
                except Exception as e:
                    wx.MessageBox(format(e), "Error, failed to load '%s'" % (configuration.kipartbase+model.image.storage_path), wx.OK | wx.ICON_ERROR)
            except:
                self.button_open_file_image.Label = "<None>"
                self.SetImage()
            
            try:
                self.button_open_file_model.Label = model.model.source_name
            except:
                self.button_open_file_model.Label = "<None>"

            if model.snapeda:
                self.button_open_url_snapeda.Label = NoneValue(model.snapeda, '')
            else:
                self.button_open_url_snapeda.Label = "<None>"
        else:
            self.edit_model_name.Value = ''
            self.edit_model_description.Value = ''
            self.edit_model_comment.Value = ''
            self.button_open_file_image.Label = "<None>"
            self.button_open_file_model.Label = "<None>"
            self.button_open_url_snapeda.Label = "<None>"

    def enable(self, enabled=True):
        self.edit_model_name.Enabled = enabled
        self.edit_model_description.Enabled = enabled
        self.edit_model_comment.Enabled = enabled
        self.button_remove_url_snapeda.Enabled = enabled
        self.button_add_file_model.Enabled = enabled
        self.button_add_file_image.Enabled = enabled
        self.button_model_editApply.Enabled = enabled
        self.button_model_editCancel.Enabled = enabled
        self.button_remove_file_model.Enabled = enabled
        self.button_remove_file_image.Enabled = enabled
        self.button_snapeda.Enabled = enabled
        
    def SetImage(self, filename=none_image):
        try:
            data = urllib2.urlopen(filename)
            print "Load url:", filename
            f = tempfile.gettempdir()+'/'+os.path.basename(filename)
            with open(f, 'wb') as outfile:
                outfile.write(data.read())
            outfile.close()
        except:  # invalid URL, this is a file
            print "Load file:", filename
            f = filename
         
        img = wx.Image(f, wx.BITMAP_TYPE_ANY)
        #img = wx.Bitmap(self.file_model_image.GetPath(), wx.BITMAP_TYPE_ANY)
        self.PhotoMaxSize = self.bitmap_edit_model.GetSize().x
        W = img.GetWidth()
        H = img.GetHeight()
        if W > H:
            NewW = self.PhotoMaxSize
            NewH = self.PhotoMaxSize * H / W
        else:
            NewH = self.PhotoMaxSize
            NewW = self.PhotoMaxSize * W / H
        img = img.Scale(NewW,NewH)
        img = img.ConvertToBitmap()

        self.bitmap_edit_model.SetBitmap(img)

    def onButtonSnapedaClick( self, event ):
        # create a snapeda frame
        # dropdown frame
        dropdown = DropdownDialog(self.button_snapeda, SelectSnapedaFrame, self.edit_model_name.Value)
        dropdown.panel.Bind( EVT_SELECT_SNAPEDA_OK_EVENT, self.onSelectSnapedaFrameOk )
        dropdown.Dropdown()

    def onSelectSnapedaFrameOk(self, event):
        snapeda = event.data
        if not snapeda:
            return
#        res = wx.MessageBox(format(e), 'Open SnapEDA to the selected ', wx.YES | wx.NO | wx.ICON_QUESTION)
        self.edit_model_name.Value = snapeda.part_number()
        self.edit_model_description.Value = snapeda.short_description()
        self.button_open_url_snapeda.Label = "https://www.snapeda.com"+snapeda._links().self().href()
        # download image
        if snapeda.image()!='':
            try:
                filename = tempfile.gettempdir()+'/'+os.path.basename(snapeda.image())
                content = scraper.get(snapeda.image()).content
                with open(filename, 'wb') as outfile:
                    outfile.write(content)
                outfile.close()
                
                self.button_open_file_image.Label = filename
                self.local_file_image = filename
                self.SetImage(filename)
            except:
                print "%s: Error loading" % snapeda.image()
            
        self.SetImage(self.button_open_file_image.Label)

    def onButtonOpenFileImageClick( self, event ):
        configuration = Configuration()
        if self.button_open_file_image.Label!="<None>":
            url = configuration.kipartbase+'/file'+self.model.image.storage_path
            webbrowser.open(url)

    def onButtonAddFileImageClick( self, event ):
        dlg = wx.FileDialog(
            self, message="Choose an image file",
            defaultDir=os.getcwd(),
            defaultFile="",
            wildcard="Bitmap (*.bmp)|*.bmp|PNG (*.png)|*.png|JPEG (*.jpg)|*.jpg|GIF (*.gif)|*.gif",
                style=wx.FD_OPEN |
                wx.FD_CHANGE_DIR | wx.FD_FILE_MUST_EXIST |
                wx.FD_PREVIEW
        )
        dlg.SetFilterIndex(0)

        # Show the dialog and retrieve the user response. If it is the OK response,
        # process the data.
        if dlg.ShowModal() == wx.ID_OK:
            self.button_open_file_image.Label = os.path.basename(dlg.GetPath())
            self.local_file_image = os.path.basename(dlg.GetPath())
            self.SetImage(dlg.GetPath())

            
    def onButtonRemoveFileImageClick( self, event ):
        self.button_open_file_image.Label = "<None>"
        self.local_file_image = ''
        self.SetImage()


    def onButtonOpenFileModelClick( self, event ):
        configuration = Configuration()
        if self.button_open_file_model.Label!="<None>":
            url = configuration.kipartbase+'/file'+self.model.model.storage_path
            webbrowser.open(url)
    
    def onButtonAddFileModelClick( self, event ):
        dlg = wx.FileDialog(
            self, message="Choose a model file",
            defaultDir=os.getcwd(),
            defaultFile="",
            wildcard="Model (*.kicad_mod)|*.kicad_mod",
                style=wx.FD_OPEN |
                wx.FD_CHANGE_DIR | wx.FD_FILE_MUST_EXIST |
                wx.FD_PREVIEW
        )
        dlg.SetFilterIndex(0)

        # Show the dialog and retrieve the user response. If it is the OK response,
        # process the data.
        if dlg.ShowModal() == wx.ID_OK:
            self.button_open_file_model.Label = os.path.basename(dlg.GetPath())
            self.local_file_model = os.path.basename(dlg.GetPath())
    
    def onButtonRemoveFileModelClick( self, event ):
        self.button_open_file_model.Label = "<None>"
        self.local_file_model = ''

    def onButtonModelEditApply( self, event ):
        model = self.model
        

        model.name = self.edit_model_name.Value
        model.description = self.edit_model_description.Value
        model.comment = self.edit_model_comment.Value
        
        try:
            if self.local_file_image=='':
                model.image = None
            elif self.local_file_image:
                model.image = rest.api.add_upload_file(upfile=self.local_file_image)
        except Exception as e:
            wx.MessageBox(format(e), 'Error', wx.OK | wx.ICON_ERROR)
            return
        
        try:
            if self.local_file_model=='':
                model.model = None
            elif self.local_file_model:
                model.model = rest.api.add_upload_file(upfile=self.local_file_model)
        except Exception as e:
            wx.MessageBox(format(e), 'Error', wx.OK | wx.ICON_ERROR)
            return
        
        model.snapeda = self.button_open_url_snapeda.Label
        # send result event
        event = EditModelApplyEvent(data=model)
        wx.PostEvent(self, event)
    
    def onButtonModelEditCancel( self, event ):
        event = EditModelCancelEvent()
        wx.PostEvent(self, event)

    def onButtonOpenUrlSnapedaClick( self, event ):
        if self.button_open_url_snapeda.Label!="<None>":
            webbrowser.open(self.button_open_url_snapeda.Label)
    
    def onButtonRemoveUrlSnapedaClick( self, event ):
        self.button_open_url_snapeda.Label = "<None>"
        self.button_open_url_snapeda = ''