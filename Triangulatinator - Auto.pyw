from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
import os
import calculate

width = 174
height = 142

class Application:
    def __init__(self, ui_file):
        # Create an instance of QApplication
        self.app = QApplication([])

        # Create a loader object
        loader = QUiLoader()

        # Load the ui file
        try:
            self.ui = loader.load(ui_file)
            print(f"Loaded {ui_file}")
        except FileNotFoundError:
            print(f"File not found: {ui_file}")

        # Connect the button's clicked signal to a slot
        self.ui.pushButton_2.clicked.connect(self.on_button_clicked)
        self.ui.pushButton_3.clicked.connect(self.on_button2_clicked)
        self.ui.pushButton.clicked.connect(self.on_submit_clicked)

        # Connect textChanged signals to a slot
        self.ui.lineEdit.textChanged.connect(self.check_text_edits)
        self.ui.lineEdit_2.textChanged.connect(self.check_text_edits)

        # Initially disable the button
        self.ui.pushButton.setEnabled(False)

        # Show the loaded ui
        self.ui.show()

    def check_text_edits(self):
        # Check if both text edits have content
        if self.ui.lineEdit.text() and self.ui.lineEdit_2.text():
            self.ui.pushButton.setEnabled(True)
        else:
            self.ui.pushButton.setEnabled(False)

    def on_submit_clicked(self):
        result = calculate.type_check(self.ui.lineEdit.text(), self.ui.lineEdit_2.text())
        self.ui.label.setText(str(result[0]) + " " + str(result[1]) + " D: " + str(result[2]) + "\n" + str(round(result[0] / 8)) + " " + str(round(result[1] / 8)) + " D: " + str(round(result[2] / 8)))

    def on_button_clicked(self):
        self.ui.lineEdit.clear()

    def on_button2_clicked(self):
        self.ui.lineEdit_2.clear()

if __name__ == "__main__":

    app = Application(os.path.join(os.path.split(os.path.abspath(__file__))[0], 'Triangulator Manual.ui'))

    # Start the application's event loop
    app.app.exec()
