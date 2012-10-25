import logging
import os
BOT_LOG_LEVEL = logging.DEBUG # or .INFO
# set the log file, None = console only, be sure the user of the bot can write there
BOT_LOG_FILE = None
BOT_ASYNC = False # If true, the bot will handle the commands asynchronously [EXPERIMENTAL]
BOT_DATA_DIR = '/tmp' # Point this to a writeable directory by the system user running the bot
BOT_EXTRA_PLUGIN_DIR = os.getcwd() # Add this directory to the plugin discovery (useful to develop a new plugin locally)
# Prefix used for commands. Note that in help strings, you should still use the
# default '!'. If the prefix is changed from the default, the help strings will
# be automatically adjusted.
BOT_PREFIX = '!'

BOT_LOG_SENTRY = False; SENTRY_DSN = ''; SENTRY_LOGLEVEL = BOT_LOG_LEVEL
CHATROOM_PRESENCE = (); CHATROOM_RELAY = {}; REVERSE_CHATROOM_RELAY = {}; CHATROOM_FN = 'bot'; DIVERT_TO_PRIVATE = ()
BOT_IDENTITY = { }; BOT_ADMINS = ('admin',); ACCESS_CONTROLS = {}
