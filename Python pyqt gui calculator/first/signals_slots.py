import sys

from functools import partial
from PyQt6.QtWidgets import (
	QApplication,
	QLabel,
	QPushButton,
	QVBoxLayout,
	QWidget
)


def greet():
	if msgLabel.text():
		msgLabel.setText('')
	else:
		msgLabel.setText('Hello World')

def greeting(name):
	if msgLabel.text():
		msgLabel.setText('')
	else:
		msgLabel.setText(f'Hello, {name}')


app = QApplication([])
window = QWidget()
window.setWindowTitle('Signals and slots')
layout = QVBoxLayout()

button = QPushButton('Greet')
# button.clicked.connect(greet)
button.clicked.connect(partial(greeting, 'World'))

layout.addWidget(button)
msgLabel = QLabel('')
layout.addWidget(msgLabel)
window.setLayout(layout)
window.show()
sys.exit(app.exec())


