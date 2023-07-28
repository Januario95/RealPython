from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot(
	'Norman',
	storage_adapter='chatterbot.storage.SQLStorageAdapter',
	logic_adapters=[
		'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter'
	],
	database_uri='sqlite:///database.sqlite3'
)

trainer = ListTrainer(bot)
trainer.train([
	'How are you?',
    'I am good.',
    'That is good to hear.',
    'Thank you',
    'You are welcome.',
])

while True:
	try:
		query = input('> ')
		bot_input = bot.get_response(query)
		print(bot_input)
	except (KeyboardInterrupt,
			EOFError, SystemExit):
		break




