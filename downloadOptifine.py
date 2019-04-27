#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import re

def getVersions(version=None):
    bs = BeautifulSoup(requests.get('https://optifine.net/downloads').text,features='html.parser')
    if version != 'all' and version != None:
        tmp = bs.find(text='Minecraft '+version)
        if tmp is None:
            tmp = bs.find(text=re.compile(version+' '))
            if tmp is None: return
            else: return [tmp.string], [tmp.findNext(class_='downloadLineDownload').a['href']]
        tmp = tmp.findNext(class_='downloadTable')
    else:
        tmp = bs

    names = [i.string for i in tmp.findAll('td',class_=re.compile('downloadLineFile'))]
    links = [i.a['href'] for i in tmp.findAll('td',class_='downloadLineMirror')]

    return tuple(zip(names,links))


if __name__ == '__main__':
    import os
    import json

    template = '{"formatVersion": 1, "+libraries": [{"name": "net.minecraft:launchwrapper:1.12"}, {"name": "optifine:optifinePrefix:optifineVersion", "MMC-hint": "local", "MMC-filename": "optifinePrefix_optifineVersion.jar"}], "+tweakers": ["optifine.OptiFineTweaker"], "fileId": "optifine.OptiFine", "mainClass": "net.minecraft.launchwrapper.Launch", "requires": [{"uid": "net.minecraft", "equals": "mcversion"}], "name": "OptiFine", "version": "optifineVersion"}'
    
    def downloadOptifine(url, path=''):
        bs = BeautifulSoup(requests.get(url).text,features='html.parser')
        r = requests.get('https://optifine.net/' + bs.find(id='Download').a.get('href'),
            headers={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'})
        filename = re.findall('filename="(.*)"',r.headers['Content-Disposition'])[0].replace('/','_')
        open(os.path.join(path,filename),'wb').write(r.content)
        return filename

    os.chdir(input('Input the folder of the instance you want to install optifine on: '))

    with open('mmc-pack.json', 'r+') as f:
        mmcpack = json.load(f)
        for j,i in enumerate(mmcpack['components']):
            if i.get('cachedName') == 'OptiFine':
                mmcpack['components'].pop(j)
                break
        mmcpack['components'].append({'cachedName': 'OptiFine','cachedVersion': '1','uid': 'optifine.OptiFine'})
        f.seek(0)
        f.truncate()
        json.dump(mmcpack,f,indent=4)

    mcversion = None
    for i in mmcpack['components']:
        if i.get('uid') == 'net.minecraft':
            mcversion = i['version']
            break

    if mcversion != None: yn = input(f'Minecraft {mcversion} was detected, use it? [y/n] ')

    if mcversion == None or yn == 'n':
        mcversion = input('Input the minecraft version you\'d like to use: ')

    versions = getVersions(mcversion)
    for i, n in enumerate(versions): print(f'{i} - {n[0]}')
    choice = int(input(f'Please choose a version [0-{len(versions)-1}] '))

    if not os.path.exists('libraries'):
        os.mkdir('libraries')

    print('Downloading '+versions[choice][0])
    filename = downloadOptifine(versions[choice][1], path='libraries')
    optifinePrefix, optifineVersion = re.match(r'((?:preview_)?OptiFine)_(.+)\.jar', filename).groups()

    if not os.path.exists('patches'):
        os.mkdir('patches')

    with open('patches/optifine.OptiFine.json', 'w') as file:
        template = template.replace('optifinePrefix', optifinePrefix).replace(
            'optifineVersion',optifineVersion).replace('mcversion', mcversion)
        file.write(json.dumps(json.loads(template), indent=4))

    input('Done, press enter to exit... ')