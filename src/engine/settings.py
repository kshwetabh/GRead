# -*- coding: utf-8 -*-

"""
Settings manager.
Usage : 
import settings
settings.load()
value = settings.get('group', 'key')
settings.set('group', 'key', value, save=False)
settings.save()
# utils : settings.special_feeds, settings.auth_ready, settings.legal
"""

from PyQt4.QtCore import QSettings
from PyQt4.QtGui import QApplication
from utils.libgreader import GoogleReader
import os
from base64 import b64encode as be, b64decode as bd
from bz2 import compress as bzc, decompress as bzd

__ALL__ = ('load', 'save', 'get', 'set', 'auth_ready', 'special_feeds')

# about the application, organization and author
legal = {
    'organization': {
        'name': 'Twidi.com', 
        'domain': 'twidi.com', 
    }, 
    'application': {
        'name': 'Gread', 
    }, 
    'author': {
        'name': 'S.Angel / Twidi', 
        'email': 's.angel@twidi.com', 
    }
}


QApplication.setOrganizationName(legal['organization']['name'])
QApplication.setOrganizationDomain(legal['organization']['domain'])
QApplication.setApplicationName(legal['application']['name'])


# will hold the settings
_settings = {}
# will hold the QString object
_qsettings = None

# helpers for special settings
helpers = {
    'feeds_default': ['feeds', 'labels', ], # list and not tuple for using index method

    'feeds_specials': GoogleReader.SPECIAL_FEEDS,
    
    'items_show_mode': ['all-save', 'unread-save', 'all-nosave', 'unread-nosave'], 
    
    'info_banner_position': ['top', 'bottom', 'hide'], 

    'booleans': (
        'google.verified',
                 
        'feeds.show_' + GoogleReader.STARRED_LIST, 
        'feeds.show_' + GoogleReader.SHARED_LIST, 
        'feeds.show_' + GoogleReader.READING_LIST, 
        'feeds.show_' + GoogleReader.READ_LIST, 
        'feeds.show_' + GoogleReader.NOTES_LIST, 
        'feeds.show_' + GoogleReader.FRIENDS_LIST, 
        'feeds.show_' + GoogleReader.KEPTUNREAD_LIST, 

        'feeds.unread_only',
        
        'content.feed_in_title', 

        'other.portrait_mode',
        'other.scroll_titles',
        
        'info.banner_hide', 
    ), 
}

def add_helpers(new_helpers):
    """
    Allow a module to add helpers
    """
    for key in new_helpers:
        if key == 'booleans':
            helpers['booleans'] += new_helpers['booleans']
        else:
            helpers[key] = new_helpers[key]

# all available settings and their default values
_defaults = {
    'google': {
        'account': '',
        'password': '',
        'verified': False,
        'auth_token': '', 
        'token': '', 
    },
    'feeds': {
        'default':     'labels', # feeds or labels
        'unread_only': True,    # display all, or only unread feeds
        'unread_number': '100',   # number of unread items to fetch while synchronizing
        # special lists : 
        'show_' + GoogleReader.STARRED_LIST:   True,
        'show_' + GoogleReader.SHARED_LIST:     False, 
        'show_' + GoogleReader.READING_LIST:    False,
        'show_' + GoogleReader.READ_LIST:       False,
        'show_' + GoogleReader.NOTES_LIST:      False,
        'show_' + GoogleReader.FRIENDS_LIST:    True,
        'show_' + GoogleReader.KEPTUNREAD_LIST: False,
    }, 
    'items': {
        'show_mode': 'unread-save', # all-save, unread-save, all-nosave, unread-nosave
    }, 
    'content': {
        'feed_in_title': False, 
        'user_agent': '',
        'zoom_factor': 100, 
    }, 
    'other': {
        'portrait_mode': False,
        'scroll_titles': True,
    }, 
    'info': {
        'banner_position': 'bottom', # top, bottom, hide
        'banner_hide': True, 
        'banner_hide_delay': 2000, 
    }, 
}

def add_defaults(new_defaults):
    """
    Allow a module to add some new default values
    """
    global _defaults
    for key in new_defaults:
        if key in _defaults:
            _defaults[key].update(new_defaults[key])
        else:
            _defaults[key] = new_defaults[key]


# list of all special feeds with their name
special_feeds = {
    GoogleReader.STARRED_LIST:    { 'name': 'Starred',}, 
    GoogleReader.SHARED_LIST:     { 'name': 'Shared',}, 
    GoogleReader.READING_LIST:    { 'name': 'All',}, 
    GoogleReader.READ_LIST:       { 'name': 'Read',}, 
    GoogleReader.NOTES_LIST:      { 'name': 'Notes',}, 
    GoogleReader.FRIENDS_LIST:    { 'name': 'Friends',}, 
    GoogleReader.KEPTUNREAD_LIST: { 'name': 'Kept unread',}, 
}

def load():
    """
    Load settings from file or whatever via QSettings
    """
    global _qsettings, _settings, _defaults, helpers
    if not _qsettings:
        _qsettings = QSettings()
    new_settings = {}
    for group in _defaults:
        _qsettings.beginGroup(group)
        new_settings[group] = {}
        for key in _defaults[group]:
            value = _qsettings.value(key, _defaults[group][key])
            if '%s.%s' % (group, key) in helpers['booleans']:
                new_settings[group][key] = value.toBool()
            else:
                new_settings[group][key] = value.toString()
        _qsettings.endGroup()
    _settings = new_settings

def save():
    """
    Save settings into file or whatever via QSettings
    """
    global _qsettings, _settings
    for group in _settings:
        _qsettings.beginGroup(group)
        for key in _settings[group]:
             _qsettings.setValue(key, _settings[group][key])
        _qsettings.endGroup()
        
def get(group, key):
    """
    Return a value for the specified settings, or None
    """
    global _defaults, _settings
    return _settings.get(group, {}).get(key, _defaults.get(group, {}).get(key, None))

def get_group(group):
    """
    Return all values for a group
    """
    global defaults, _settings
    return _settings.get(group, _defaults.get(group, {}))

def is_default(group, key):
    """
    Check if a value is the default one
    """
    global _defaults
    value = get(group, key)
    return value == _defaults.get(group, {}).get(key, None)

def set(group, key, value, save_all=False):
    """
    Set the specified value for a settings, and save all settings if 
    save_all is True
    """
    global _settings
    _settings.setdefault(group, {})[key] = value
    if save_all:
        save()

_salt = None
def get_salt():
    """
    Generate a salt to use for crypt/uncrypt password
    """
    global _salt
    if _salt is None:
        try:
            device_id = os.uname()[1]
        except:
            device_id = 'unknown'
        _salt = be(legal['application']['name'] + device_id).rstrip('=')
    return _salt

def crypt(string):
    """
    Simply crypt a string in a reversible way
    """
    salt = get_salt()
    r = lambda x:x.rstrip(u'=')
    return r(be(bzc(r(be(u'%s%s'%(r(be(u'%s%s'%(string,salt))),salt))))[10:]))

def uncrypt(crypted):
    """
    Decrypt a string crypted by crypt
    """
    eq = lambda x:x+u'='*((divmod(len(x),4)[0]+1)*4-len(x))
    salt = get_salt()
    l = len(u'%s'%salt)
    return bd(eq(bd(eq(bzd(bzc(salt)[:10]+bd(eq(crypted)))))[:-l]))[:-l]

def auth_ready():
    """
    Return True if either google account and password are filled
    """
    global _settings
    try:
        return (_settings['google']['account'].replace(' ', '') != '' and uncrypt(_settings['google']['password']).replace(' ', '') != '')
    except:
        return False
