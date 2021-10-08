# -*- coding: utf-8 -*-
#  ___  ____  _  _ 
# / __)( ___)( \/ )
#( (_-. )__)  \  / 
# \___/(__)   (__) 
#
#All credits to previous ...

from resources.lib.modules.control import addonPath, addonId, getPoisonIvyVersion, joinPath
from resources.lib.windows.textviewer import TextViewerXML


def get(file):
	poisonivy_path = addonPath(addonId())
	poisonivy_version = getPoisonIvyVersion()
	helpFile = joinPath(poisonivy_path, 'resources', 'help', file + '.txt')
	r = open(helpFile)
	text = r.read()
	r.close()
	heading = '[B]PoisonIvy -  v%s - %s[/B]' % (poisonivy_version, file)
	windows = TextViewerXML('textviewer.xml', poisonivy_path, heading=heading, text=text)
	windows.run()
	del windows