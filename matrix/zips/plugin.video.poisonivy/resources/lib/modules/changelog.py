# -*- coding: utf-8 -*-
#  ___  ____  _  _ 
# / __)( ___)( \/ )
#( (_-. )__)  \  / 
# \___/(__)   (__) 
#
#All credits to previous ...

from resources.lib.modules.control import addonPath, addonId, getPoisonIvyVersion, joinPath
from resources.lib.windows.textviewer import TextViewerXML


def get():
	poisonivy_path = addonPath(addonId())
	poisonivy_version = getPoisonIvyVersion()
	changelogfile = joinPath(poisonivy_path, 'changelog.txt')
	r = open(changelogfile)
	text = r.read()
	r.close()
	heading = '[B]PoisonIvy -  v%s - ChangeLog[/B]' % poisonivy_version
	windows = TextViewerXML('textviewer.xml', poisonivy_path, heading=heading, text=text)
	windows.run()
	del windows