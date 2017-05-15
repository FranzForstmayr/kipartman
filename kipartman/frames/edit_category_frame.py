from dialogs.dialog_edit_category import DialogEditCategory
from api.models import PartCategory

import wx

class EditCategoryFrame(DialogEditCategory):
    def __init__(self, parent): 
        super(EditCategoryFrame, self).__init__(parent)

    def addCategory(self):
        self.Title = "Add category"
        self.button_validate.LabelText = "Add"
        result = self.ShowModal()
        if result==wx.ID_OK:
            category = PartCategory(name=self.text_name.Value)
            return category
        return None
    
    def editCategory(self, category):
        self.Title = "Edit category"
        self.button_validate.LabelText = "Apply"
        self.text_name.Value = category.name
        result = self.ShowModal()
        if result==wx.ID_OK:
            category.name = self.text_name.Value
            return category
        return None
    
    # Virtual event handlers, overide them in your derived class
    def onValidateClick( self, event ):
        self.EndModal(wx.ID_OK)
    
    def onCancelClick( self, event ):
        self.EndModal(wx.ID_CANCEL)
    