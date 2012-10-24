# encoding=utf-8

from config import CHATROOM_PRESENCE

from errbot import BotPlugin, botcmd
from errbot.utils import get_sender_username

class ArrrrrBot(BotPlugin):
	@botcmd
	def grog(self, mess, args):
		"""Cheers!"""
		return self.peek(mess, 'grog')

	@botcmd
	def lod(self, mess, args):
		"""Print the look of disapproval"""
		return self.peek(mess, 'lod')

	@botcmd
	def loa(self, mess, args):
		"""Print the look of approval"""
		return self.peek(mess, 'loa')

	@botcmd
	def slap(self, mess, args):
		"""Let the bot slap people in the chatroom in an piratelike manner"""
		return "{0} slaps {1} around a bit with a large trout.".format(get_sender_username(mess), args)

	@botcmd
	def peek(self, mess, args):
		"""Print a saved one-liner"""
		if self.has_key(args):
			return self[args]
		else:
			return "Nope."

	@botcmd
	def poke(self, mess, args):
		"""Save a one-liner : !poke name content"""
		argss = args.split(' ', 1)
		name = argss[0]
		if len(argss) == 1:
			del self[name]
		else:
			content = argss[1]
			if len(content) > 80 or '\n' in content:
				return "Nope."
			else:
				self[name] = content

	@botcmd
	def peekpoke(self, mess, args):
		"""List all saved one-liners (private message only)"""
		result = ''
		for name in self.keys():
			result += "{0}: \t {1}\n".format(name, self[name])
		return result

	@botcmd(admin_only = True)
	def hiersprichtgott(self, mess, args):
		self.send(CHATROOM_PRESENCE[0], args, message_type='groupchat')
