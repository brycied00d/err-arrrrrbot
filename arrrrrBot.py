from errbot import BotPlugin, botcmd

class ArrrrrBot(BotPlugin):
	@botcmd
	def grog(self, mess, args):
		"""Cheers!"""
		return "GROG GROG GROG"
