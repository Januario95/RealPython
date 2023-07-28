from chatterbot import ChatBot

bot = ChatBot(
	'Terminal',
	storage_adapter='chatterbot.storage.SQLStorageAdapter',
	logic_adapters=[
		'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch'
	],
	database_uri='sqlite:///database.db'
)

while True:
	try:
		query = input('> ')
		response = bot.get_response(query)
		print(response)
	except (KeyboardInterrupt,
			EOFError, SystemExit):
		break





