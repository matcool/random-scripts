import wx
import os
import json
import requests
from bs4 import BeautifulSoup
import re

def getVersions(ver):
    bs = BeautifulSoup(requests.get('https://optifine.net/downloads').text,features='html.parser')
    if ver != 'all':
        tmp = bs.find(text='Minecraft '+ver)
        if tmp is None:
            tmp = bs.find(text=re.compile(ver+' '))
            if tmp is None: return
            else: return [tmp.string], [tmp.findNext(class_='downloadLineDownload').a['href']]
        tmp = tmp.findNext(class_='downloadTable')
    else:
        tmp = bs

    names = [i.string for i in tmp.findAll('td',class_=re.compile('downloadLineFile'))]
    links = [i.a['href'] for i in tmp.findAll('td',class_='downloadLineMirror')]

    return names,links

def downloadOptifine(url, path=''):
    bs = BeautifulSoup(requests.get(url).text,features='html.parser')
    r = requests.get('https://optifine.net/' + bs.find(id='Download').a.get('href'),
        headers={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'})
    filename = re.findall('filename="(.*)"',r.headers['Content-Disposition'])[0].replace('/','_')
    open(os.path.join(path,filename),'wb').write(r.content)
    return filename

class MainFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MainFrame, self).__init__(*args, **kw)
        
        self.instpath = None
        self.mcversion = None
        self.mmcpack = None
        self.versions = None
        self.versionsLBox = None

        self.panel = wx.Panel(self)

        folderBtn = wx.Button(self.panel, label='Select folder', pos=(10,10))
        folderBtn.Bind(wx.EVT_BUTTON,self.getInstanceFolder)

    def OnExit(self, event):
        self.Close(True)

    def getInstanceFolder(self, event):
        ddialog = wx.DirDialog(None,message='Select the instance\'s folder')
        i = ddialog.ShowModal()
        if i != wx.ID_CANCEL:
            self.instpath = ddialog.GetPath()
            if not os.path.isfile(self.instpath+'/mmc-pack.json'):
                wx.MessageBox(caption='select the right one next time you idiot',message='Invalid folder! mmc-pack.json not found.')
                self.instpath = None
            else: 
                self.getmmcpack()
                self.getMCVersion()
                self.versions = getVersions(self.mcversion)
                self.showVersions()

    def getmmcpack(self):
        with open(self.instpath+'/mmc-pack.json','r+') as f:
            self.mmcpack = json.load(f)
            for j,i in enumerate(self.mmcpack['components']):
                if i['cachedName'] == 'OptiFine':
                    self.mmcpack['components'].pop(j)
                    break
            self.mmcpack['components'].append({'cachedName': 'OptiFine','cachedVersion': '1','uid': 'optifine.OptiFine'})
            f.seek(0)
            f.truncate()
            json.dump(self.mmcpack,f,indent=4)

    def getMCVersion(self):
        self.mcversion = None
        for i in self.mmcpack['components']:
            if i['uid'] == 'net.minecraft':
                self.mcversion = i['version']
                wx.MessageBox(message=f'Version {self.mcversion} was found')
                break

    def showVersions(self):
        self.versionsLBox = wx.ListBox(self.panel, choices=self.versions[0], pos=(160,10), size=(150,200))
        dlBtn = wx.Button(self.panel, label='Download and apply', pos=(10,50))
        dlBtn.Bind(wx.EVT_BUTTON, self.downloadApply)

    def downloadApply(self, event):
        selected = self.versionsLBox.GetSelection()
        if selected == wx.NOT_FOUND:
            wx.MessageBox(message='select one godamnit')
            return
        selected = self.versions[1][selected]

        template = '{"formatVersion": 1, "+libraries": [{"name": "net.minecraft:launchwrapper:1.12"}, {"name": "optifine:optifinePrefix:optifineVersion", "MMC-hint": "local", "MMC-filename": "optifinePrefix_optifineVersion.jar"}], "+tweakers": ["optifine.OptiFineTweaker"], "fileId": "optifine.OptiFine", "mainClass": "net.minecraft.launchwrapper.Launch", "requires": [{"uid": "net.minecraft", "equals": "mcversion"}], "name": "OptiFine", "version": "optifineVersion"}'

        if not os.path.exists(self.instpath+'/libraries'):
            os.mkdir(self.instpath+'/libraries')

        filename = downloadOptifine(selected,path=self.instpath+'/libraries')
        optifinePrefix, optifineVersion = re.match(r'((?:preview_)?OptiFine)_(.+)\.jar',filename).groups()

        if not os.path.exists(self.instpath+'/patches'):
            os.mkdir(self.instpath+'/patches')

        with open(self.instpath+'/patches/optifine.OptiFine.json','w') as file:
            template = template.replace('optifinePrefix',optifinePrefix).replace(
                'optifineVersion',optifineVersion).replace('mcversion',self.mcversion)
            file.write(json.dumps(json.loads(template), indent=4))

        wx.MessageBox(message='done???? i fucking hope so')


if __name__ == '__main__':
    app = wx.App()
    frm = MainFrame(None, title='MultiMC Optifine Downloader', size=(330,250))
    frm.Show()
    app.MainLoop()