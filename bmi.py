import sys, os
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel
from PySide6.QtGui import QAction, QPixmap
from bmi_ui import Ui_MainWindow
from bmi_c import BMI


def resource_path(relative_path):
    """
    Najde cestu k souborům i po zabalení do .exe (PyInstaller)
    """
    try:
        base_path = sys._MEIPASS  # dočasná složka PyInstalleru
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class BMIMainWindow(QMainWindow, Ui_MainWindow):
    """Hlavní třída aplikace, která propojuje GUI a backend."""

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Label pro obrázek
        self.label_image = QLabel(self.centralwidget)
        self.label_image.setGeometry(20, 200, 150, 80)
        self.label_image.setScaledContents(True)

        # Propojení tlačítka
        self.button_calc.clicked.connect(self.calculate_bmi)

        # Menu
        self.create_menu()

    def create_menu(self):
        """Vytvoření menu bar položek."""
        file_menu = self.menubar.addMenu("File")
        end_action = QAction("End", self)
        end_action.triggered.connect(self.close)
        file_menu.addAction(end_action)

        help_menu = self.menubar.addMenu("Help")
        doc_action = QAction("Documentation", self)
        doc_action.triggered.connect(self.show_doc)
        help_menu.addAction(doc_action)

        about_action = QAction("About", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)

    def calculate_bmi(self):
        """Zpracuje vstupy z GUI, spočítá BMI a zobrazí výsledek + obrázek."""
        try:
            weight = float(self.input_weight.text())
            height = float(self.input_height.text()) / 100  # cm → m

            bmi_obj = BMI(weight, height)
            bmi_value = bmi_obj.vypocti()
            category = bmi_obj.get_kategorie()

            self.label_result.setText(f"BMI: {bmi_value:.2f} – {category}")
            self.statusbar.showMessage("Výpočet dokončen", 3000)

            self.show_image(category)

        except ValueError:
            self.label_result.setText("Chyba: zadej čísla!")
            self.statusbar.showMessage("Chyba vstupu", 3000)

    def show_image(self, category):
        """Zobrazí obrázek podle výsledné kategorie BMI."""
        img_path = None
        if "podvýživa" in category:
            img_path = resource_path("images/underweight.png")
        elif "ideální" in category:
            img_path = resource_path("images/normal.png")
        elif "nadváha" in category:
            img_path = resource_path("images/overweight.png")
        elif "obezita" in category:
            img_path = resource_path("images/obese.png")

        if img_path and os.path.exists(img_path):
            self.label_image.setPixmap(QPixmap(img_path))
        else:
            self.label_image.clear()

    def show_doc(self):
        """Zobrazí dokumentaci aplikace."""
        QMessageBox.information(
            self, "Documentation",
            "1. Zadej hmotnost v kg.\n"
            "2. Zadej výšku v cm.\n"
            "3. Klikni na 'Spočítat BMI'.\n"
            "Výsledek ukáže hodnotu BMI, kategorii a obrázek."
        )

    def show_about(self):
        """Zobrazí informace o autorovi."""
        QMessageBox.about(
            self, "About",
            "BMI Kalkulačka\n"
            "Autor: Student\n"
            "Verze: 1.0"
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BMIMainWindow()
    window.show()
    sys.exit(app.exec())
