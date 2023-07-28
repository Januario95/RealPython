from chatterbot import ChatBot

bot = ChatBot(
	'Math & Time Bot',
	logic_adapters=[
		'chatterbot.logic.MathematicalEvaluation',
		'chatterbot.logic.TimeLogicAdapter'
	]
)

response = bot.get_response(
	'What is 4 + 12')
print(response)

response = bot.get_response(
	'Wwhat time is it?')
print(response)


