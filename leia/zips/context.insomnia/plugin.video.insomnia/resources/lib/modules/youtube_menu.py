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

import re
from sys import argv
try: #Py2
	from urllib2 import urlopen, Request
except ImportError: #Py3
	from urllib.request import urlopen, Request
from resources.lib.modules import control
from resources.lib.modules import log_utils
from resources.lib.modules import py_tools


class youtube_menu(object):
	def __init__(self):
		self.agent = 'INSOMNIAAddonAgent'
		self.key_id = 'AIzaSyA56rHBAyK0Cl0P4uDM_12sNOwUmAaas8E'

	def openMenuFile(self, menuFile):
		try:
			req = Request(menuFile)
			req.add_header('User-Agent', self.agent)
			response = urlopen(req)
			link=response.read()
			link = py_tools.ensure_text(link, errors='ignore')
			response.close()
			return link
		except:
			log_utils.error()

	def processMenuFile(self, menuFile):
		try:
			link = self.openMenuFile(menuFile).replace('\n','').replace('\r','')
			match = re.compile(r'name="(.+?)".+?ection="(.+?)".+?earch="(.+?)".+?ubid="(.+?)".+?laylistid="(.+?)".+?hannelid="(.+?)".+?ideoid="(.+?)".+?con="(.+?)".+?anart="(.+?)".+?escription="(.+?)"').findall(link)
			return match
		except:
			log_utils.error()

	def addMenuItem(self, name, action, subid, iconimage, fanart, description='', isFolder=True):
		try:
			url = '%s?action=%s&id=%s' % (argv[0], action, subid)
			try: liz = control.item(label=name, offscreen=True)
			except: liz = control.item(label=name)
			liz.setArt({'icon': 'DefaultFolder.png', 'thumb': iconimage, 'fanart': fanart})
			liz.setInfo(type='video', infoLabels={'title': name, 'plot': description})
			control.addItem(handle=int(argv[1]), url=url, listitem=liz, isFolder=isFolder)
		except:
			log_utils.error()

	def addSectionItem(self, name, iconimage, fanart):
		try:
			url = '%s?action=sectionItem' % argv[0]
			try: liz = control.item(label=name, offscreen=True)
			except: liz = control.item(label=name)
			liz.setArt({'icon': 'DefaultFolder.png', 'thumb': iconimage, 'fanart': fanart})
			liz.setInfo(type='video', infoLabels={'title': name, 'plot': description})
			control.addItem(handle=int(argv[1]), url=url, listitem=liz, isFolder=False)
		except:
			log_utils.error()

	def addSearchItem(self, name, search_id, icon, fanart):
		try:
			work_url = "plugin://plugin.video.youtube/kodion/search/query/?q=%s" % search_id
			liz = control.item(name)
			liz.setInfo( type='video', infoLabels={'title': name})
			liz.setArt({'thumb': icon, 'banner': 'DefaultVideo.png', 'fanart': fanart})
			control.addItem(handle=int(argv[1]), url=work_url, listitem=liz, isFolder=True)
		except:
			log_utils.error()

	def addChannelItem(self, name, channel_id, icon, fanart):
		try:
			work_url = "plugin://plugin.video.youtube/channel/%s/" % channel_id
			liz = control.item(name)
			liz.setInfo( type='video', infoLabels={'title': name})
			liz.setArt({'thumb': icon, 'banner': 'DefaultVideo.png', 'fanart': fanart})
			control.addItem(handle=int(argv[1]), url=work_url, listitem=liz, isFolder=True)
		except:
			log_utils.error()

	def addUserItem(self, name, channel_id, icon, fanart):
		try:
			user = channel_id
			work_url = "plugin://plugin.video.youtube/user/%s/" % user
			liz = control.item(name)
			liz.setInfo( type='video', infoLabels={'title': name})
			liz.setArt({'thumb': icon, 'banner': 'DefaultVideo.png', 'fanart': fanart})
			control.addItem(handle=int(argv[1]), url=work_url, listitem=liz, isFolder=True)
		except:
			log_utils.error()

	def addPlaylistItem(self, name, playlist_id, icon, fanart):
		try:
			work_url = "plugin://plugin.video.youtube/playlist/%s/" % playlist_id
			liz = control.item(name)
			liz.setInfo( type='video', infoLabels={'title': name})
			liz.setArt({'thumb': icon, 'banner': 'DefaultVideo.png', 'fanart': fanart})
			control.addItem(handle=int(argv[1]), url=work_url, listitem=liz, isFolder=True)
		except:
			log_utils.error()

	def addVideoItem(self, name, video_id, icon, fanart):
		try:
			work_url = "plugin://plugin.video.youtube/play/?video_id=%s" % video_id
			liz = control.item(name)
			liz.setInfo( type='video', infoLabels={'title': name})
			liz.setArt({'thumb': icon, 'banner': 'DefaultVideo.png', 'fanart': fanart})
			liz.setProperty('IsPlayable', 'true')
			control.addItem(handle=int(argv[1]), url=work_url, listitem=liz, isFolder=False)
		except:
			log_utils.error()