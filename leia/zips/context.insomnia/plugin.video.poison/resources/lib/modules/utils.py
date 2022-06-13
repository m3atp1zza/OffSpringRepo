# -*- coding: utf-8 -*-
'''                                                                                                    
      * ***       ***      ***      *******                                                         
    *  ****     ** ***   ** ***   *       ***                           *                           
   *  *  ***   **   *** **   *** *         **                          ***                          
  *  **   ***  **       **       **        *                            *                           
 *  ***    *** **       **        ***             ****   ***  ****                                  
**   **     ** ******   ******   ** ***          * ***  * **** **** * ***   ***  ****     ****      
**   **     ** *****    *****     *** ***       *   ****   **   ****   ***   **** **** * *  ***  *  
**   **     ** **       **          *** ***    **    **    **           **    **   **** *    ****   
**   **     ** **       **            *** ***  **    **    **           **    **    ** **     **    
**   **     ** **       **              ** *** **    **    **           **    **    ** **     **    
 **  **     ** **       **               ** ** **    **    **           **    **    ** **     **    
  ** *      *  **       **                * *  **    **    **           **    **    ** **     **    
   ***     *   **       **      ***        *   *******     ***          **    **    ** **     **    
    *******    **       **     *  *********    ******       ***         *** * ***   *** ********    
      ***       **       **   *     *****      **                        ***   ***   ***  *** ***   
                              *                **                                              ***  
                               **              **                                        ****   *** 
                                                **                                     *******  **  
                                                                                      *     ****    
'''

import re
import simplejson as json
import six


# if six.PY2:
    # unicode = unicode
# elif six.PY3:
    # str = unicode = basestring = str


def json_load_as_str(file_handle):
    return byteify(json.load(file_handle, object_hook=byteify), ignore_dicts=True)


def json_loads_as_str(json_text):
    return byteify(json.loads(json_text, object_hook=byteify), ignore_dicts=True)


def byteify(data, ignore_dicts=False):
    if isinstance(data, six.string_types):
        if six.PY2:
            return data.encode('utf-8')
        else:
            return data
    if isinstance(data, list):
        return [byteify(item, ignore_dicts=True) for item in data]
    if isinstance(data, dict) and not ignore_dicts:
        return dict([(byteify(key, ignore_dicts=True), byteify(value, ignore_dicts=True)) for key, value in six.iteritems(data)])
    return data


def title_key(title):
    try:
        if title is None: title = ''
        articles_en = ['the', 'a', 'an']
        articles_de = ['der', 'die', 'das']
        articles = articles_en + articles_de

        match = re.match('^((\w+)\s+)', title.lower())
        if match and match.group(2) in articles:
            offset = len(match.group(1))
        else:
            offset = 0

        return title[offset:]
    except:
        return title


def chunks(l, n):
    """
    Yield successive n-sized chunks from l.
    """
    for i in list(range(0, len(l), n)):
        yield l[i:i + n]

