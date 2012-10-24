# encoding=utf-8

from config import CHATROOM_PRESENCE

from errbot import BotPlugin, botcmd
from errbot.utils import get_sender_username

class ArrrrrBot(BotPlugin):
	@botcmd
	def grog(self, mess, args):
		"""Cheers!"""
		return "GROG!!! GROG!!! GROG!!!"

	@botcmd
	def lod(self, mess, args):
		"""Print the look of disapproval"""
		return "ಠ_ಠ"

	@botcmd
	def loa(self, mess, args):
		"""Print the look of approval"""
		return "ʘ‿ʘ"

	@botcmd
	def slap(self, mess, args):
		"""Let the bot slap people in the chatroom in an piratelike manner"""
		return "{0} slaps {1} around a bit with a large trout.".format(get_sender_username(mess), args)

	@botcmd(admin_only = True)
	def hiersprichtgott(self, mess, args):
		self.send(CHATROOM_PRESENCE[0], args, message_type='groupchat')
