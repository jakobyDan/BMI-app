import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from bmi_ui import Ui_MainWindow
import bmi_c

class BMIApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Menu akce
        file_menu = self.ui.menubar.addMenu("File")
        help_menu = self.ui.menubar.addMenu("Help")

        # File -> End
        end_action = file_menu.addAction("End")
        end_action.triggered.connect(self.close)

        # Help -> Documentation
        doc_action = help_menu.addAction("Documentation")
        doc_action.triggered.connect(lambda: QMessageBox.information(self, "Documentation", "Tady může být dokumentace."))

        # Help -> About
        about_action = help_menu.addAction("About")
        about_action.triggered.connect(lambda: QMessageBox.information(self, "About", "BMI Kalkulačka v PySide6"))

        # Tlačítko výpočtu
        self.ui.button_calc.clicked.connect(self.calculate_bmi)

    def calculate_bmi(self):
        try:
            weight = float(self.ui.input_weight.text())
            height = float(self.ui.input_height.text())
            bmi_value = bmi_c.bmi(weight, height)
            category = bmi_c.category(bmi_value)
            self.ui.label_result.setText(f"BMI: {bmi_value:.2f}, Kategorie: {category}")
            self.statusBar().showMessage("Výpočet dokončen")
        except ValueError:
            self.statusBar().showMessage("Chyba: zadej čísla")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BMIApp()
    window.show()
    sys.exit(app.exec())
