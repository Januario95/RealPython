from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

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

trainer = ChatterBotCorpusTrainer(bot)
trainer.train(
	'chatterbot.corpus.english')

while True:
	try:
		query = input('>  ')
		response = bot.get_response(query)
		print(query)
	except (KeyboardInterrupt,
			EOFError, SystemExit):
		break







