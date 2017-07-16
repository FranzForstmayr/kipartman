from dialogs.dialog_edit_part_parameter import DialogEditPartParameter
import wx

 
class EditPartParameterFrame(DialogEditPartParameter):
    def __init__(self, parent): 
        super(EditPartParameterFrame, self).__init__(parent)
        self.loadUnits()
        self.loadPrefixes()

    def loadUnits(self):
        units = UnitsQuery().get()
        choices = ["<none>"]
        for unit in units:
            choices.append(unit.symbol+"  "+unit.name)
        self.choice_part_parameter_unit.SetItems(choices)
        
    def loadPrefixes(self):
        prefixes = UnitPrefixesQuery().get()
        choices = ["<none>"]
        for prefix in prefixes:
            choices.append(prefix.symbol+"  "+prefix.name+" ("+prefix.power+")")
        self.choice_part_parameter_min_prefix.SetItems(choices)
        self.choice_part_parameter_nom_prefix.SetItems(choices)
        self.choice_part_parameter_max_prefix.SetItems(choices)
        
    def AddParameter(self, part):
        self.Title = "Add parameter"
        self.part = part
        self.previous_name = "" 
        self.onRadioNumeric(None)
        self.parameter = PartParameter()

        self.choice_part_parameter_unit.SetSelection(0)
        self.choice_part_parameter_min_prefix.SetSelection(0)
        self.choice_part_parameter_nom_prefix.SetSelection(0)
        self.choice_part_parameter_max_prefix.SetSelection(0)

        result = self.ShowModal()
        if result==wx.ID_OK:
            return self.parameter
        return None

    def EditParameter(self, part, parameter):
        self.Title = "Edit parameter"
        self.part = part
        self.previous_name = parameter.name 
        self.parameter = parameter

        self.edit_part_parameter_name.Value = parameter.name
        self.edit_part_parameter_description.Value = parameter.description
        
        if self.parameter.unit:
            self.choice_part_parameter_unit.SetSelection(self.parameter.unit.id)
        else:
            self.choice_part_parameter_unit.SetSelection(0)
            
        if self.parameter.numeric==True:
            self.onRadioNumeric(None)
            self.radio_choice_parameter_numeric.SetValue(True)
        else:
            self.onRadioText(None)
            self.radio_choice_parameter_text.SetValue(True)

        if self.parameter.text_value:
            self.edit_part_parameter_value.Value = self.parameter.text_value

        if self.parameter.min_value:
            self.edit_part_parameter_min_value.Value = str(self.parameter.min_value) 
        if self.parameter.min_prefix:
            self.choice_part_parameter_min_prefix.SetSelection(self.parameter.min_prefix.id)
        else:
            self.choice_part_parameter_min_prefix.SetSelection(0)
            
        if self.parameter.nom_value:
            self.edit_part_parameter_nom_value.Value = str(self.parameter.nom_value) 
        if self.parameter.nom_prefix:
            self.choice_part_parameter_nom_prefix.SetSelection(self.parameter.nom_prefix.id)
        else:
            self.choice_part_parameter_nom_prefix.SetSelection(0)
            
        if self.parameter.max_value:
            self.edit_part_parameter_max_value.Value = str(self.parameter.max_value) 
        if self.parameter.max_prefix:
            self.choice_part_parameter_max_prefix.SetSelection(self.parameter.max_prefix.id)
        else:
            self.choice_part_parameter_max_prefix.SetSelection(0)
            
        result = self.ShowModal()
        if result==wx.ID_OK:
            return self.parameter
        return None

    def onButtonPartParameterEditApply( self, event ):
        try:
            if self.edit_part_parameter_name.Value=='':
                raise ValueError('Name should not be empty')
            # check parameter not exists
            for param in self.part.parameters:
                if self.edit_part_parameter_name.Value!=self.previous_name and param.name==self.edit_part_parameter_name.Value:
                    raise ValueError('%s: parameter already exists' % (self.edit_part_parameter_name.Value))

            self.parameter.name = self.edit_part_parameter_name.Value
            self.parameter.description = self.edit_part_parameter_description.Value
            if self.choice_part_parameter_unit.GetSelection()==0:
                self.parameter.unit = None
            else:
                self.parameter.unit = UnitsQuery().get()[self.choice_part_parameter_unit.GetSelection()-1]
            if self.radio_choice_parameter_numeric.GetValue()==True:
                self.parameter.numeric = True
            else:
                self.parameter.numeric = False
            
            if self.edit_part_parameter_value.Value!='':
                self.parameter.text_value = self.edit_part_parameter_value.Value
            else:
                self.parameter.text_value = None
                
            if self.edit_part_parameter_min_value.Value!='':
                self.parameter.min_value = float(self.edit_part_parameter_min_value.Value)
            else:
                self.parameter.min_value = None
            if self.choice_part_parameter_min_prefix.GetSelection()==0:
                self.parameter.min_prefix = None
            else:
                self.parameter.min_prefix = UnitPrefixesQuery().get()[self.choice_part_parameter_min_prefix.GetSelection()-1]
    
            if self.edit_part_parameter_nom_value.Value!='':
                self.parameter.nom_value = float(self.edit_part_parameter_nom_value.Value)
            else:
                self.parameter.nom_value = None
            if self.choice_part_parameter_nom_prefix.GetSelection()==0:
                self.parameter.nom_prefix = None
            else:
                self.parameter.nom_prefix = UnitPrefixesQuery().get()[self.choice_part_parameter_nom_prefix.GetSelection()-1]
    
            if self.edit_part_parameter_max_value.Value!='':
                self.parameter.max_value = float(self.edit_part_parameter_max_value.Value)
            else:
                self.parameter.max_value = None
            if self.choice_part_parameter_max_prefix.GetSelection()==0:
                self.parameter.max_prefix = None
            else:
                self.parameter.max_prefix = UnitPrefixesQuery().get()[self.choice_part_parameter_max_prefix.GetSelection()-1]
        except ValueError as e:
            wx.MessageBox(format(e), 'Error', wx.OK | wx.ICON_ERROR)
            return
        except QueryError as e:
            wx.MessageBox(format(e), 'Error', wx.OK | wx.ICON_ERROR)
            return 

        self.EndModal(wx.ID_OK)

    def onButtonPartParameterEditCancel( self, event ):
        self.EndModal(wx.ID_CANCEL)
    
    def onRadioNumeric( self, event ):
        self.static_value.Hide()
        self.edit_part_parameter_value.Hide()
        
        self.static_min_value.Show()
        self.edit_part_parameter_min_value.Show()
        self.choice_part_parameter_min_prefix.Show()
        
        self.static_nom_value.Show()
        self.edit_part_parameter_nom_value.Show()
        self.choice_part_parameter_nom_prefix.Show()
        
        self.static_max_value.Show()
        self.edit_part_parameter_max_value.Show()
        self.choice_part_parameter_max_prefix.Show()
        
    def onRadioText( self, event ):
        self.static_value.Show()
        self.edit_part_parameter_value.Show()

        self.static_min_value.Hide()
        self.edit_part_parameter_min_value.Hide()
        self.choice_part_parameter_min_prefix.Hide()
        
        self.static_nom_value.Hide()
        self.edit_part_parameter_nom_value.Hide()
        self.choice_part_parameter_nom_prefix.Hide()
        
        self.static_max_value.Hide()
        self.edit_part_parameter_max_value.Hide()
        self.choice_part_parameter_max_prefix.Hide()
