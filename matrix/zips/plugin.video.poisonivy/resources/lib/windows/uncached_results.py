# -*- coding: utf-8 -*-
#  ___  ____  _  _ 
# / __)( ___)( \/ )
#( (_-. )__)  \  / 
# \___/(__)   (__) 
#
#All credits to previous ...

from json import dumps as jsdumps
try: #Py2
	from urllib import quote_plus
except ImportError: #Py3
	from urllib.parse import quote_plus
from resources.lib.modules.control import joinPath, transPath, dialog
from resources.lib.modules.source_utils import getFileType
from resources.lib.windows.base import BaseDialog


class UncachedResultsXML(BaseDialog):
	def __init__(self, *args, **kwargs):
		super(UncachedResultsXML, self).__init__(self, args)
		self.window_id = 2001
		self.uncached = kwargs.get('uncached')
		self.total_results = str(len(self.uncached))
		self.meta = kwargs.get('meta')
		self.info = None
		self.cm = None
		self.make_items()
		self.set_properties()

	def onInit(self):
		super(UncachedResultsXML, self).onInit()
		win = self.getControl(self.window_id)
		win.addItems(self.item_list)
		self.setFocusId(self.window_id)

	def run(self):
		self.doModal()
		try: del self.info
		except: pass
		try: del self.cm
		except: pass
		return self.selected

	def onAction(self, action):
		try:
			action_id = action.getId()# change to just "action" as the ID is already returned in that.
			if action_id in self.info_actions:
				chosen_source = self.item_list[self.get_position(self.window_id)]
				chosen_source = chosen_source.getProperty('poisonivy.source_dict')
				syssource = quote_plus(chosen_source)
				self.execute_code('RunPlugin(plugin://plugin.video.poisonivy/?action=sourceInfo&source=%s)' % syssource)
			if action_id in self.selection_actions:
				chosen_source = self.item_list[self.get_position(self.window_id)]
				source = chosen_source.getProperty('poisonivy.source')
				if 'UNCACHED' in source:
					debrid = chosen_source.getProperty('poisonivy.debrid')
					source_dict = chosen_source.getProperty('poisonivy.source_dict')
					link_type = 'pack' if 'package' in source_dict else 'single'
					sysname = quote_plus(self.meta.get('title'))
					if 'tvshowtitle' in self.meta and 'season' in self.meta and 'episode' in self.meta:
						poster = self.meta.get('season_poster') or self.meta.get('poster')
						sysname += quote_plus(' S%02dE%02d' % (int(self.meta['season']), int(self.meta['episode'])))
					elif 'year' in self.meta: sysname += quote_plus(' (%s)' % self.meta['year'])
					try: new_sysname = quote_plus(chosen_source.getProperty('poisonivy.name'))
					except: new_sysname = sysname
					self.execute_code('RunPlugin(plugin://plugin.video.poisonivy/?action=cacheTorrent&caller=%s&type=%s&title=%s&items=%s&url=%s&source=%s&meta=%s)' %
											(debrid, link_type, sysname, quote_plus(jsdumps(self.uncached)), quote_plus(chosen_source.getProperty('poisonivy.url')), quote_plus(source_dict), quote_plus(jsdumps(self.meta))))
					self.selected = (None, '')
				else:
					self.selected = (None, '')
				return self.close()
			elif action_id in self.context_actions:
				chosen_source = self.item_list[self.get_position(self.window_id)]
				source_dict = chosen_source.getProperty('poisonivy.source_dict')
				cm_list = [('[B]Additional Link Info[/B]', 'sourceInfo')]

				source = chosen_source.getProperty('poisonivy.source')
				if 'UNCACHED' in source:
					debrid = chosen_source.getProperty('poisonivy.debrid')
					seeders = chosen_source.getProperty('poisonivy.seeders')
					cm_list += [('[B]Cache to %s Cloud (seeders=%s)[/B]' % (debrid, seeders) , 'cacheToCloud')]

				chosen_cm_item = dialog.contextmenu([i[0] for i in cm_list])
				if chosen_cm_item == -1: return
				cm_action = cm_list[chosen_cm_item][1]

				if cm_action == 'sourceInfo':
					self.execute_code('RunPlugin(plugin://plugin.video.poisonivy/?action=sourceInfo&source=%s)' % quote_plus(source_dict))

				if cm_action == 'cacheToCloud':
					debrid = chosen_source.getProperty('poisonivy.debrid')
					source_dict = chosen_source.getProperty('poisonivy.source_dict')
					link_type = 'pack' if 'package' in source_dict else 'single'
					sysname = quote_plus(self.meta.get('title'))
					if 'tvshowtitle' in self.meta and 'season' in self.meta and 'episode' in self.meta:
						poster = self.meta.get('season_poster') or self.meta.get('poster')
						sysname += quote_plus(' S%02dE%02d' % (int(self.meta['season']), int(self.meta['episode'])))
					elif 'year' in self.meta: sysname += quote_plus(' (%s)' % self.meta['year'])
					try: new_sysname = quote_plus(chosen_source.getProperty('poisonivy.name'))
					except: new_sysname = sysname
					self.execute_code('RunPlugin(plugin://plugin.video.poisonivy/?action=cacheTorrent&caller=%s&type=%s&title=%s&items=%s&url=%s&source=%s&meta=%s)' %
											(debrid, link_type, sysname, quote_plus(jsdumps(self.uncached)), quote_plus(chosen_source.getProperty('poisonivy.url')), quote_plus(source_dict), quote_plus(jsdumps(self.meta))))
			elif action in self.closing_actions:
				self.selected = (None, '')
				self.close()
		except:
			from resources.lib.modules import log_utils
			log_utils.error()

	def get_quality_iconPath(self, quality):
		try:
			return joinPath(transPath('special://home/addons/plugin.video.poisonivy/resources/skins/Default/media/resolution'), '%s.png' % quality)
		except:
			from resources.lib.modules import log_utils
			log_utils.error()

	def debrid_abv(self, debrid):
		try:
			d_dict = {'AllDebrid': 'AD', 'Premiumize.me': 'PM', 'Real-Debrid': 'RD'}
			d = d_dict[debrid]
		except:
			d = ''
		return d

	def make_items(self):
		def builder():
			for count, item in enumerate(self.uncached, 1):
				try:
					listitem = self.make_listitem()
					quality = item.get('quality', 'SD')
					quality_icon = self.get_quality_iconPath(quality)
					extra_info = item.get('info')
					try:
						size_label = extra_info.split('|', 1)[0]
						if any(value in size_label for value in ['HEVC', '3D']): size_label = ''
					except: size_label = ''

					try: f = ' / '.join(['%s' % info.strip() for info in extra_info.split('|')])
					except: f = ''
					if 'name_info' in item: t = getFileType(name_info=item.get('name_info'))
					else: t = getFileType(url=item.get('url'))
					t = '%s /%s' % (f, t) if (f != '' and f != '0 ' and f != ' ') else t
					if t == '': t = getFileType(url=item.get('url'))
					extra_info = t

					listitem.setProperty('poisonivy.source_dict', jsdumps([item]))
					listitem.setProperty('poisonivy.debrid', self.debrid_abv(item.get('debrid')))
					listitem.setProperty('poisonivy.provider', item.get('provider').upper())
					listitem.setProperty('poisonivy.source', item.get('source').upper())
					listitem.setProperty('poisonivy.seeders', str(item.get('seeders')))
					listitem.setProperty('poisonivy.hash', item.get('hash', 'N/A'))
					listitem.setProperty('poisonivy.name', item.get('name'))
					listitem.setProperty('poisonivy.quality', quality.upper())
					listitem.setProperty('poisonivy.quality_icon', quality_icon)
					listitem.setProperty('poisonivy.url', item.get('url'))
					listitem.setProperty('poisonivy.extra_info', extra_info)
					if size_label: listitem.setProperty('poisonivy.size_label', size_label)
					else: listitem.setProperty('poisonivy.size_label', 'NA')
					listitem.setProperty('poisonivy.count', '%02d.)' % count)
					yield listitem
				except:
					from resources.lib.modules import log_utils
					log_utils.error()
		try:
			self.item_list = list(builder())
			self.total_results = str(len(self.item_list))
		except:
			from resources.lib.modules import log_utils
			log_utils.error()

	def set_properties(self):
		try:
			if self.meta is None: return
			# self.setProperty('poisonivy.mediatype', self.meta.get('mediatype', ''))
			self.setProperty('poisonivy.season', str(self.meta.get('season', '')))
			if self.meta.get('season_poster'):	self.setProperty('poisonivy.poster', self.meta.get('season_poster', ''))
			else: self.setProperty('poisonivy.poster', self.meta.get('poster', ''))
			# self.setProperty('poisonivy.fanart', self.meta.get('fanart', ''))
			# self.setProperty('poisonivy.clearart', self.meta.get('clearart', ''))
			self.setProperty('poisonivy.clearlogo', self.meta.get('clearlogo', ''))
			self.setProperty('poisonivy.plot', self.meta.get('plot', ''))
			self.setProperty('poisonivy.year', str(self.meta.get('year', '')))
			self.setProperty('poisonivy.premiered', str(self.meta.get('premiered', '')))
			if self.meta.get('mpaa'): self.setProperty('poisonivy.mpaa', self.meta.get('mpaa'))
			else: self.setProperty('poisonivy.mpaa', 'NA ')
			if self.meta.get('duration'):
				duration = int(self.meta.get('duration')) / 60
				self.setProperty('poisonivy.duration', str(int(duration)))
			else: self.setProperty('poisonivy.duration', 'NA ')
			self.setProperty('poisonivy.total_results', self.total_results)
		except:
			from resources.lib.modules import log_utils
			log_utils.error()