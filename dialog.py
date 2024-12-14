# This Python file uses the following encoding: utf-8
import sys

import PySide6.QtWidgets as qtw
import PySide6.QtCore as qtc
import PySide6.QtGui as qtg
from PySide6.QtCore import Signal
from mapping import PAGE_INDEX_MAPPING
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Dialog

class Dialog(qtw.QDialog):
    def __init__(self, tree_object, object_type:str, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)    

        # Add maximize & minimize buttons
        self.setWindowFlags(
            self.windowFlags() |
            qtc.Qt.WindowMaximizeButtonHint |
            qtc.Qt.WindowMinimizeButtonHint
        )

        # Set relavent page as current page
        page_index = PAGE_INDEX_MAPPING[object_type]
        self.ui.main_stacked_widget.setCurrentIndex(page_index)

        # Add events to update tree object info 
        ## e.g.:
        self.ui.element_speed_double.valueChanged.connect(lambda value: setattr(tree_object, 'speed',  value))
        self.ui.gb_bearing_button.clicked.connect(lambda: print(getattr(tree_object, 'speed', 'NOT SET YET!')))
        
        

class TestObject:
    pass

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    test_object = TestObject()
    widget = Dialog(tree_object=test_object, object_type='element')
    widget.show()
    sys.exit(app.exec())
