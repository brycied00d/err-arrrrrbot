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
