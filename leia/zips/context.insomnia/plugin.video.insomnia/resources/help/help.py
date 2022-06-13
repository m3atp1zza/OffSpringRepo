# -*- coding: utf-8 -*-
'''
 ▄▀▀█▀▄    ▄▀▀▄ ▀▄  ▄▀▀▀▀▄  ▄▀▀▀▀▄   ▄▀▀▄ ▄▀▄  ▄▀▀▄ ▀▄  ▄▀▀█▀▄    ▄▀▀█▄  
█   █  █  █  █ █ █ █ █   ▐ █      █ █  █ ▀  █ █  █ █ █ █   █  █  ▐ ▄▀ ▀▄ 
▐   █  ▐  ▐  █  ▀█    ▀▄   █      █ ▐  █    █ ▐  █  ▀█ ▐   █  ▐    █▄▄▄█ 
    █       █   █  ▀▄   █  ▀▄    ▄▀   █    █    █   █      █      ▄▀   █ 
 ▄▀▀▀▀▀▄  ▄▀   █    █▀▀▀     ▀▀▀▀   ▄▀   ▄▀   ▄▀   █    ▄▀▀▀▀▀▄  █   ▄▀  
█       █ █    ▐    ▐               █    █    █    ▐   █       █ ▐   ▐   
▐       ▐ ▐                         ▐    ▐    ▐        ▐       ▐         

Credit to all previous authors
'''

from resources.lib.modules.control import addonPath, addonId, getINSOMNIAVersion, joinPath
from resources.lib.windows.textviewer import TextViewerXML


def get(file):
	insomnia_path = addonPath(addonId())
	insomnia_version = getINSOMNIAVersion()
	helpFile = joinPath(insomnia_path, 'resources', 'help', file + '.txt')
	r = open(helpFile)
	text = r.read()
	r.close()
	heading = '[B]INSOMNIA -  v%s - %s[/B]' % (insomnia_version, file)
	windows = TextViewerXML('textviewer.xml', insomnia_path, heading=heading, text=text)
	windows.run()
	del windows