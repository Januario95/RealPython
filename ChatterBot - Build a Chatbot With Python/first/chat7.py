from chatterbot import ChatBot

bot = ChatBot(
	'SQLMemoryTerminal',
	storage_adapter='chatterbot.storage.SQLStorageAdapter',
	database_uri=None,
	logic_adapters=[
		'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch'
	]
)

print(bot.get_response(
	'What time is it?'))

print(bot.get_response(
	'What is 7 plus 7'))


