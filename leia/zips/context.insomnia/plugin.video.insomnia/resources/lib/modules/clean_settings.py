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

import xml.etree.ElementTree as ET
from resources.lib.modules import control


def clean_settings():
	def _make_content(dict_object):
		if kodi_version >= 18:
			content = '<settings version="2">'
			for item in dict_object:
				if item['id'] in active_settings:
					if 'default' in item and 'value' in item: content += '\n    <setting id="%s" default="%s">%s</setting>' % (item['id'], item['default'], item['value'])
					elif 'default' in item: content += '\n    <setting id="%s" default="%s"></setting>' % (item['id'], item['default'])
					elif 'value' in item: content += '\n    <setting id="%s">%s</setting>' % (item['id'], item['value'])
					else: content += '\n    <setting id="%s"></setting>'
				else: removed_settings.append(item)
		else:
			content = '<settings>'
			for item in dict_object:
				if item['id'] in active_settings:
					if 'value' in item: content += '\n    <setting id="%s" value="%s" />' % (item['id'], item['value'])
					else: content += '\n    <setting id="%s" value="" />' % item['id']
				else: removed_settings.append(item)
		content += '\n</settings>'
		return content
	kodi_version = control.getKodiVersion()
	for addon_id in ('plugin.video.insomnia', 'script.module.lescrapers'):
		try:
			removed_settings = []
			active_settings = []
			current_user_settings = []
			addon = control.addon(id=addon_id)
			addon_name = addon.getAddonInfo('name')
			addon_dir = control.transPath(addon.getAddonInfo('path'))
			profile_dir = control.transPath(addon.getAddonInfo('profile'))
			active_settings_xml = control.joinPath(addon_dir, 'resources', 'settings.xml')
			root = ET.parse(active_settings_xml).getroot()
			for item in root.findall('./category/setting'):
				setting_id = item.get('id')
				if setting_id:
					active_settings.append(setting_id)
			settings_xml = control.joinPath(profile_dir, 'settings.xml')
			root = ET.parse(settings_xml).getroot()
			for item in root:
				dict_item = {}
				setting_id = item.get('id')
				setting_default = item.get('default')
				if kodi_version >= 18:
					setting_value = item.text
				else: setting_value = item.get('value')
				dict_item['id'] = setting_id
				if setting_value:
					dict_item['value'] = setting_value
				if setting_default:
					dict_item['default'] = setting_default
				current_user_settings.append(dict_item)
			new_content = _make_content(current_user_settings)
			nfo_file = control.openFile(settings_xml, 'w')
			nfo_file.write(new_content)
			nfo_file.close()
			control.sleep(200)
			control.notification(title=addon_name, message=control.lang(32084).format(str(len(removed_settings))))
		except:
			from resources.lib.modules import log_utils
			log_utils.error()
			control.notification(title=addon_name, message=32115)