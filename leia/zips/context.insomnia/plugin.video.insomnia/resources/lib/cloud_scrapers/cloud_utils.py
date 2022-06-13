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

from json import loads as jsloads
import re
from resources.lib.modules import cleantitle


def aliases_to_array(aliases, filter=None):
	try:
		if all(isinstance(x, str) for x in aliases): return aliases
		if not filter: filter = []
		if isinstance(filter, str): filter = [filter]
		return [x.get('title') for x in aliases if not filter or x.get('country') in filter]
	except:
		from resources.lib.modules import log_utils
		log_utils.error()
		return []

def cloud_check_title(title, aliases, release_title):
	try: aliases = aliases_to_array(jsloads(aliases))
	except: aliases = None
	title_list = []
	if aliases:
		for item in aliases:
			try:
				alias = item.replace('!', '').replace('(', '').replace(')', '').replace('&', 'and')
				# alias = re.sub(r'[^A-Za-z0-9\s\.-]+', '', alias)
				if alias in title_list: continue
				title_list.append(alias)
			except:
				from resources.lib.modules import log_utils
				log_utils.error()
	try:
		match = True
		title = title.replace('!', '').replace('(', '').replace(')', '').replace('&', 'and')
		# title = re.sub(r'[^A-Za-z0-9\s\.-]+', '', title)
		title_list.append(title)
		release_title = release_title_format(release_title).replace('!', '').replace('(', '').replace(')', '').replace('&', 'and') # converts to .lower()
		if all(cleantitle.get(i) not in cleantitle.get(release_title) for i in title_list): match = False
		return match
	except:
		from resources.lib.modules import log_utils
		log_utils.error()
		return match

def release_title_format(release_title):
	try:
		release_title = release_title.lower().replace("'", "").lstrip('.').rstrip('.')
		fmt = '.%s.' % re.sub(r'[^a-z0-9-~]+', '.', release_title).replace('.-.', '-').replace('-.', '-').replace('.-', '-').replace('--', '-')
		return fmt
	except:
		from resources.lib.modules import log_utils
		log_utils.error()
		return release_title

	def abbrev_title(self, title):
		try:
			split_title = title.split(' ')
			if len(split_title) == 1: return title
			abbrev_title = ''.join([i[:1] for i in split_title])
			return abbrev_title
		except:
			from resources.lib.modules import log_utils
			log_utils.error()
			return title

def extras_filter():
	return ['sample', 'extra', 'deleted', 'unused', 'footage', 'inside', 'blooper', 'making.of', 'feature', 'featurette', 'behind.the.scenes', 'trailer']