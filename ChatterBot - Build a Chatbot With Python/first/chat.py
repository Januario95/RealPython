from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chabot = ChatBot('Ron Obvious')

conversation = [
	"Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

trainer = ListTrainer(chabot)
trainer.train(conversation)

response = chabot.get_response(
	"Good morning")
print(response)















