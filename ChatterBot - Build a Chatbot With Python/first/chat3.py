from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot('Charlie')

trainer = ListTrainer(chatbot)
trainer.train([
	"Hi, can I help you?",
	"Sure, I'd like to book a flight to Sweden.",
	"Your flight has been booked."
])

response = chatbot.get_response(
	'I would like to book a flight')
print(response)

