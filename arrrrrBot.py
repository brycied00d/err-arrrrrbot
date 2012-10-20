from errbot import BotPlugin, botcmd

class ArrrrrBot(BotPlugin):
	@botcmd
	def grog(self, mess, args):
		"""Cheers!"""
		return "GROG GROG GROG"

	@botcmd
	def lod(self, mess, args):
		"""Print the look of disapproval"""
		return "ಠ_ಠ"

	@botcmd
	def slap(self, mess, args):
		"""Let the bot slap people in the chatroom in an piratelike manner"""
		return "/me slaps " + args + " around a bit with a large trout."
