from PySide6.QtWidgets import (
    QFileDialog,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from models.asset_manager import AssetManager
from operations.filter_operation import FilterOperation
from services.exporter import ExportService
from services.importer import ImportService


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.asset_manager: AssetManager = AssetManager()

        widget: QWidget = QWidget()

        layout: QVBoxLayout = QVBoxLayout()

        self.import_btn: QPushButton = QPushButton("Import")
        self.filter_btn: QPushButton = QPushButton("Filter")
        self.export_btn: QPushButton = QPushButton("Export")

        layout.addWidget(self.import_btn)
        layout.addWidget(self.filter_btn)
        layout.addWidget(self.export_btn)

        widget.setLayout(layout)

        self.setCentralWidget(widget)

        self.import_btn.clicked.connect(self.import_file)
        self.filter_btn.clicked.connect(self.filter_file)
        self.export_btn.clicked.connect(self.export_file)

    def import_file(self):

        path, _ = QFileDialog.getOpenFileName(
            self, "Import File", "", "Excel (*.xlsx);;CSV (*.csv)"
        )

        if not path:
            return

        assets = ImportService.import_file(path)

        self.asset_manager.load_assets(assets)

    def filter_file(self):
        operation = FilterOperation("Public Material", "Copper")

        self.asset_manager.apply_operation(operation)

    def export_file(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Excel (*.xlsx)")

        if not path:
            return

        ExportService.export_excel(path, self.asset_manager.get_assets())

        QMessageBox.information(self, "Export Complete", "File exported successfully")
