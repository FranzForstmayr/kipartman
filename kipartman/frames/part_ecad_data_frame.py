from dialogs.panel_part_ecad_data import PanelPartEcadData
import helper.tree
import kicad.kicad_lib_file
import kicad.kicad_mod_file
from configuration import configuration
import os

class PartEcadDataFrame(PanelPartEcadData):
    def __init__(self, parent): 
        super(PartEcadDataFrame, self).__init__(parent)
        
        self.part = None
        
    def SetPart(self, part):
        self.part = part
        self.showData()

    def showData(self):
        self.showSymbol()
    
    def showSymbol(self):
        # download symbol
        if self.part and self.part.symbol:
            print "symbol", self.part.symbol
            url = os.path.join(configuration.kipartbase, 'file', self.part.symbol.storage_path)
            url = url.replace('\\','/') #Work around for running on Windows
            print "url", url