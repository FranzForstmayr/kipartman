from os.path import expanduser
import os.path
import json
import wx.lib.newevent

class Configuration(object):
    
    def __init__(self):
        self.filename = expanduser("~")+'/'+'.kipartman'
        self.octopart_api_key = ''
        self.kipartbase = 'http://localhost:8100'
        
    def Load(self):
        if(os.path.isfile(self.filename)==False):
            return
        
        with open(self.filename, 'r') as infile:
            try:
                content = json.load(infile)
                print "Load configuration:", content
                self.kipartbase = content['kipartbase']
                self.octopart_api_key = content['octopart_api_key']
            except:
                print "Error: load configuration failed"

    def Save(self):
        content = {}
        with open(self.filename, 'w') as outfile:
            content['kipartbase'] = self.kipartbase
            content['octopart_api_key'] = self.octopart_api_key
            json.dump(content, outfile, sort_keys=True,
                  indent=4, separators=(',', ': '))
        print "Save configuration:", content

configuration=Configuration()
configuration.Load()