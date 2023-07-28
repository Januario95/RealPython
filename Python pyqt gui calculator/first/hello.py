import sys

# 1. Import QApplication and all the required widgets
from PyQt6.QtWidgets import (
	QApplication, QLabel, QWidget
)

# 2. Create an instance of QApplication
app = QApplication([])

# 3. Create your application's GUI
window = QWidget()
window.setWindowTitle('PyQt App')
window.setGeometry(100, 100, 280, 80)
hellomMsg = QLabel(
	'<h1>Hello World!</h1>',
	parent=window)
hellomMsg.move(60, 15)


# 4. Show your application's GUI
window.show()

# 5. Run your application's event loop
sys.exit(app.exec())
