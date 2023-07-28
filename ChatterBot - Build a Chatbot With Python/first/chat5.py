from chatterbot import ChatBot

bot = ChatBot(
	'Terminal',
	storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
	logic_adapters=[
		'chatterbot.logic.BestMatch'
	],
	database_uri='mongodb://localhost:27017/chatterbot-database'
)

while True:
	try:
		query = input('> ')
		response = bot.get_response(query)
		print(response)
	except (KeyboardInterrupt,
			EOFError, SystemError):
		break
