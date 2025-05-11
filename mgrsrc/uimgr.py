"""

+-------------------------------+   ← top bar
|           TOP BAR            |
+-------------+----------------+
|             |                |
|   Sidebar   |   Main Page    |   ← middle section
|             |                |
+-------------+----------------+
|         BOTTOM BAR           |   ← bottom bar
+-------------------------------+


"""
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel

app = QApplication([])

window = QMainWindow()
central = QWidget()
layout = QVBoxLayout()
layout.addWidget(QLabel("Hello World!"))
central.setLayout(layout)
window.setCentralWidget(central)

window.show()
app.exec()