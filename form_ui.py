# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QDoubleSpinBox,
    QFormLayout, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QSizePolicy, QSpinBox,
    QSplitter, QStackedWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

from widget.routes_tree import RoutesTree
import resources_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1300, 600)
        icon = QIcon()
        icon.addFile(u":/routes/icons/branch.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        self.horizontalLayout_2 = QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.sidebar_splitter = QSplitter(Dialog)
        self.sidebar_splitter.setObjectName(u"sidebar_splitter")
        self.sidebar_splitter.setOrientation(Qt.Horizontal)
        self.sidebar_frame = QFrame(self.sidebar_splitter)
        self.sidebar_frame.setObjectName(u"sidebar_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sidebar_frame.sizePolicy().hasHeightForWidth())
        self.sidebar_frame.setSizePolicy(sizePolicy)
        self.sidebar_frame.setFrameShape(QFrame.StyledPanel)
        self.sidebar_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.sidebar_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.database_tree = RoutesTree(self.sidebar_frame)
        self.database_tree.setObjectName(u"database_tree")

        self.verticalLayout_3.addWidget(self.database_tree)

        self.sidebar_splitter.addWidget(self.sidebar_frame)
        self.center_frame = QFrame(self.sidebar_splitter)
        self.center_frame.setObjectName(u"center_frame")
        sizePolicy.setHeightForWidth(self.center_frame.sizePolicy().hasHeightForWidth())
        self.center_frame.setSizePolicy(sizePolicy)
        self.center_frame.setFrameShape(QFrame.StyledPanel)
        self.center_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.center_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.main_stacked_widget = QStackedWidget(self.center_frame)
        self.main_stacked_widget.setObjectName(u"main_stacked_widget")
        self.org_page = QWidget()
        self.org_page.setObjectName(u"org_page")
        self.verticalLayout_6 = QVBoxLayout(self.org_page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.org_frame = QFrame(self.org_page)
        self.org_frame.setObjectName(u"org_frame")
        self.org_frame.setFrameShape(QFrame.StyledPanel)
        self.org_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget = QWidget(self.org_frame)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 671, 241))
        self.org_frame_1 = QVBoxLayout(self.verticalLayoutWidget)
        self.org_frame_1.setObjectName(u"org_frame_1")
        self.org_frame_1.setContentsMargins(0, 0, 0, 0)
        self.org_label = QLabel(self.verticalLayoutWidget)
        self.org_label.setObjectName(u"org_label")
        font = QFont()
        font.setFamilies([u"Segoe UI Black"])
        font.setPointSize(22)
        font.setBold(True)
        self.org_label.setFont(font)
        self.org_label.setScaledContents(False)

        self.org_frame_1.addWidget(self.org_label)

        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.org_name_label = QLabel(self.verticalLayoutWidget)
        self.org_name_label.setObjectName(u"org_name_label")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.org_name_label)

        self.org_name_edit = QLineEdit(self.verticalLayoutWidget)
        self.org_name_edit.setObjectName(u"org_name_edit")

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.org_name_edit)

        self.org_id_label = QLabel(self.verticalLayoutWidget)
        self.org_id_label.setObjectName(u"org_id_label")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.org_id_label)

        self.org_id_edit = QLineEdit(self.verticalLayoutWidget)
        self.org_id_edit.setObjectName(u"org_id_edit")

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.org_id_edit)


        self.org_frame_1.addLayout(self.formLayout_5)


        self.verticalLayout_6.addWidget(self.org_frame)

        self.main_stacked_widget.addWidget(self.org_page)
        self.plant_page = QWidget()
        self.plant_page.setObjectName(u"plant_page")
        self.verticalLayout_7 = QVBoxLayout(self.plant_page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.plant_page)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget_2 = QWidget(self.frame_5)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, -3, 671, 201))
        self.plant_frame = QVBoxLayout(self.verticalLayoutWidget_2)
        self.plant_frame.setObjectName(u"plant_frame")
        self.plant_frame.setContentsMargins(0, 0, 0, 0)
        self.plant_label = QLabel(self.verticalLayoutWidget_2)
        self.plant_label.setObjectName(u"plant_label")
        self.plant_label.setFont(font)

        self.plant_frame.addWidget(self.plant_label)

        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.plant_name_label = QLabel(self.verticalLayoutWidget_2)
        self.plant_name_label.setObjectName(u"plant_name_label")

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.plant_name_label)

        self.plant_name_edit = QLineEdit(self.verticalLayoutWidget_2)
        self.plant_name_edit.setObjectName(u"plant_name_edit")

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.plant_name_edit)

        self.plant_id_label = QLabel(self.verticalLayoutWidget_2)
        self.plant_id_label.setObjectName(u"plant_id_label")

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.plant_id_label)

        self.plant_id_edit = QLineEdit(self.verticalLayoutWidget_2)
        self.plant_id_edit.setObjectName(u"plant_id_edit")

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.plant_id_edit)


        self.plant_frame.addLayout(self.formLayout_6)


        self.verticalLayout_7.addWidget(self.frame_5)

        self.main_stacked_widget.addWidget(self.plant_page)
        self.shop_page = QWidget()
        self.shop_page.setObjectName(u"shop_page")
        self.horizontalLayout = QHBoxLayout(self.shop_page)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.shop_page)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget_3 = QWidget(self.frame_7)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(0, 0, 671, 211))
        self.shop_frame = QVBoxLayout(self.verticalLayoutWidget_3)
        self.shop_frame.setObjectName(u"shop_frame")
        self.shop_frame.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.verticalLayoutWidget_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.shop_frame.addWidget(self.label_3)

        self.formLayout_7 = QFormLayout()
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.shop_name_label = QLabel(self.verticalLayoutWidget_3)
        self.shop_name_label.setObjectName(u"shop_name_label")

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.shop_name_label)

        self.shop_name_edit = QLineEdit(self.verticalLayoutWidget_3)
        self.shop_name_edit.setObjectName(u"shop_name_edit")

        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.shop_name_edit)

        self.shop_id_label = QLabel(self.verticalLayoutWidget_3)
        self.shop_id_label.setObjectName(u"shop_id_label")

        self.formLayout_7.setWidget(1, QFormLayout.LabelRole, self.shop_id_label)

        self.shop_id_edit = QLineEdit(self.verticalLayoutWidget_3)
        self.shop_id_edit.setObjectName(u"shop_id_edit")

        self.formLayout_7.setWidget(1, QFormLayout.FieldRole, self.shop_id_edit)


        self.shop_frame.addLayout(self.formLayout_7)


        self.horizontalLayout.addWidget(self.frame_7)

        self.main_stacked_widget.addWidget(self.shop_page)
        self.machine_page = QWidget()
        self.machine_page.setObjectName(u"machine_page")
        self.verticalLayout_4 = QVBoxLayout(self.machine_page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.machine_frame = QFrame(self.machine_page)
        self.machine_frame.setObjectName(u"machine_frame")
        self.machine_frame.setFrameShape(QFrame.StyledPanel)
        self.machine_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.machine_frame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, 9, -1, -1)
        self.machine_label = QLabel(self.machine_frame)
        self.machine_label.setObjectName(u"machine_label")
        self.machine_label.setFont(font)

        self.verticalLayout_9.addWidget(self.machine_label)

        self.machine_info_form = QFormLayout()
        self.machine_info_form.setObjectName(u"machine_info_form")
        self.machine_name_label = QLabel(self.machine_frame)
        self.machine_name_label.setObjectName(u"machine_name_label")

        self.machine_info_form.setWidget(0, QFormLayout.LabelRole, self.machine_name_label)

        self.machine_name_edit = QLineEdit(self.machine_frame)
        self.machine_name_edit.setObjectName(u"machine_name_edit")

        self.machine_info_form.setWidget(0, QFormLayout.FieldRole, self.machine_name_edit)

        self.machine_id_label = QLabel(self.machine_frame)
        self.machine_id_label.setObjectName(u"machine_id_label")

        self.machine_info_form.setWidget(1, QFormLayout.LabelRole, self.machine_id_label)

        self.machine_id_edit = QLineEdit(self.machine_frame)
        self.machine_id_edit.setObjectName(u"machine_id_edit")

        self.machine_info_form.setWidget(1, QFormLayout.FieldRole, self.machine_id_edit)

        self.machine_type_label = QLabel(self.machine_frame)
        self.machine_type_label.setObjectName(u"machine_type_label")

        self.machine_info_form.setWidget(2, QFormLayout.LabelRole, self.machine_type_label)

        self.machine_type_combo = QComboBox(self.machine_frame)
        self.machine_type_combo.addItem("")
        self.machine_type_combo.addItem("")
        self.machine_type_combo.addItem("")
        self.machine_type_combo.setObjectName(u"machine_type_combo")

        self.machine_info_form.setWidget(2, QFormLayout.FieldRole, self.machine_type_combo)


        self.verticalLayout_9.addLayout(self.machine_info_form)

        self.verticalLayout_9.setStretch(1, 1)

        self.verticalLayout_4.addWidget(self.machine_frame)

        self.main_stacked_widget.addWidget(self.machine_page)
        self.element_page = QWidget()
        self.element_page.setObjectName(u"element_page")
        self.verticalLayout = QVBoxLayout(self.element_page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.element_frame = QFrame(self.element_page)
        self.element_frame.setObjectName(u"element_frame")
        self.element_frame.setFrameShape(QFrame.StyledPanel)
        self.element_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.element_frame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.element_label = QLabel(self.element_frame)
        self.element_label.setObjectName(u"element_label")
        self.element_label.setFont(font)

        self.verticalLayout_8.addWidget(self.element_label)

        self.element_info_form = QFormLayout()
        self.element_info_form.setObjectName(u"element_info_form")
        self.element_name_label = QLabel(self.element_frame)
        self.element_name_label.setObjectName(u"element_name_label")

        self.element_info_form.setWidget(0, QFormLayout.LabelRole, self.element_name_label)

        self.element_name_edit = QLineEdit(self.element_frame)
        self.element_name_edit.setObjectName(u"element_name_edit")

        self.element_info_form.setWidget(0, QFormLayout.FieldRole, self.element_name_edit)

        self.element_id_label = QLabel(self.element_frame)
        self.element_id_label.setObjectName(u"element_id_label")

        self.element_info_form.setWidget(1, QFormLayout.LabelRole, self.element_id_label)

        self.element_id_edit = QLineEdit(self.element_frame)
        self.element_id_edit.setObjectName(u"element_id_edit")

        self.element_info_form.setWidget(1, QFormLayout.FieldRole, self.element_id_edit)

        self.element_type_label = QLabel(self.element_frame)
        self.element_type_label.setObjectName(u"element_type_label")

        self.element_info_form.setWidget(2, QFormLayout.LabelRole, self.element_type_label)

        self.element_type_combo = QComboBox(self.element_frame)
        self.element_type_combo.addItem("")
        self.element_type_combo.addItem("")
        self.element_type_combo.addItem("")
        self.element_type_combo.addItem("")
        self.element_type_combo.setObjectName(u"element_type_combo")

        self.element_info_form.setWidget(2, QFormLayout.FieldRole, self.element_type_combo)

        self.element_power_label = QLabel(self.element_frame)
        self.element_power_label.setObjectName(u"element_power_label")

        self.element_info_form.setWidget(3, QFormLayout.LabelRole, self.element_power_label)

        self.element_power_double = QDoubleSpinBox(self.element_frame)
        self.element_power_double.setObjectName(u"element_power_double")
        self.element_power_double.setMaximum(99999999.000000000000000)
        self.element_power_double.setSingleStep(250.000000000000000)

        self.element_info_form.setWidget(3, QFormLayout.FieldRole, self.element_power_double)

        self.element_speed_label = QLabel(self.element_frame)
        self.element_speed_label.setObjectName(u"element_speed_label")

        self.element_info_form.setWidget(4, QFormLayout.LabelRole, self.element_speed_label)

        self.element_speed_double = QDoubleSpinBox(self.element_frame)
        self.element_speed_double.setObjectName(u"element_speed_double")
        self.element_speed_double.setMaximum(99999.000000000000000)
        self.element_speed_double.setSingleStep(50.000000000000000)

        self.element_info_form.setWidget(4, QFormLayout.FieldRole, self.element_speed_double)

        self.element_foundation_label = QLabel(self.element_frame)
        self.element_foundation_label.setObjectName(u"element_foundation_label")

        self.element_info_form.setWidget(5, QFormLayout.LabelRole, self.element_foundation_label)

        self.element_foundation_combo = QComboBox(self.element_frame)
        self.element_foundation_combo.addItem("")
        self.element_foundation_combo.addItem("")
        self.element_foundation_combo.setObjectName(u"element_foundation_combo")

        self.element_info_form.setWidget(5, QFormLayout.FieldRole, self.element_foundation_combo)

        self.element_coupling_label = QLabel(self.element_frame)
        self.element_coupling_label.setObjectName(u"element_coupling_label")

        self.element_info_form.setWidget(6, QFormLayout.LabelRole, self.element_coupling_label)

        self.element_coupling_combo = QComboBox(self.element_frame)
        self.element_coupling_combo.addItem("")
        self.element_coupling_combo.addItem("")
        self.element_coupling_combo.setObjectName(u"element_coupling_combo")

        self.element_info_form.setWidget(6, QFormLayout.FieldRole, self.element_coupling_combo)

        self.element_npoints_label = QLabel(self.element_frame)
        self.element_npoints_label.setObjectName(u"element_npoints_label")

        self.element_info_form.setWidget(7, QFormLayout.LabelRole, self.element_npoints_label)

        self.element_npoints_spin = QSpinBox(self.element_frame)
        self.element_npoints_spin.setObjectName(u"element_npoints_spin")
        self.element_npoints_spin.setMinimum(1)
        self.element_npoints_spin.setMaximum(6)

        self.element_info_form.setWidget(7, QFormLayout.FieldRole, self.element_npoints_spin)


        self.verticalLayout_8.addLayout(self.element_info_form)

        self.element_schematic_frame = QFrame(self.element_frame)
        self.element_schematic_frame.setObjectName(u"element_schematic_frame")
        self.element_schematic_frame.setFrameShape(QFrame.StyledPanel)
        self.element_schematic_frame.setFrameShadow(QFrame.Raised)
        self.element_schematic = QLabel(self.element_schematic_frame)
        self.element_schematic.setObjectName(u"element_schematic")
        self.element_schematic.setGeometry(QRect(190, 40, 211, 171))
        self.element_schematic.setPixmap(QPixmap(u":/routes/icons/gear.svg"))
        self.element_schematic.setScaledContents(True)

        self.verticalLayout_8.addWidget(self.element_schematic_frame)

        self.verticalLayout_8.setStretch(1, 1)
        self.verticalLayout_8.setStretch(2, 1)

        self.verticalLayout.addWidget(self.element_frame)

        self.main_stacked_widget.addWidget(self.element_page)
        self.point_page = QWidget()
        self.point_page.setObjectName(u"point_page")
        self.verticalLayout_5 = QVBoxLayout(self.point_page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.point_page)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.frame_6)

        self.main_stacked_widget.addWidget(self.point_page)
        self.direction_page = QWidget()
        self.direction_page.setObjectName(u"direction_page")
        self.horizontalLayout_3 = QHBoxLayout(self.direction_page)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.direction_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.frame_2)

        self.main_stacked_widget.addWidget(self.direction_page)

        self.verticalLayout_2.addWidget(self.main_stacked_widget)

        self.sidebar_splitter.addWidget(self.center_frame)

        self.horizontalLayout_2.addWidget(self.sidebar_splitter)


        self.retranslateUi(Dialog)

        self.main_stacked_widget.setCurrentIndex(2)
        self.machine_type_combo.setCurrentIndex(-1)
        self.element_type_combo.setCurrentIndex(-1)
        self.element_foundation_combo.setCurrentIndex(-1)
        self.element_coupling_combo.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        ___qtreewidgetitem = self.database_tree.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("Dialog", u"ID", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("Dialog", u"Type", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Dialog", u"Name", None));
        self.org_label.setText(QCoreApplication.translate("Dialog", u"Organization Page", None))
        self.org_name_label.setText(QCoreApplication.translate("Dialog", u"Name       ", None))
        self.org_id_label.setText(QCoreApplication.translate("Dialog", u"ID             ", None))
        self.plant_label.setText(QCoreApplication.translate("Dialog", u"Plant Page", None))
        self.plant_name_label.setText(QCoreApplication.translate("Dialog", u"Name", None))
        self.plant_id_label.setText(QCoreApplication.translate("Dialog", u"ID", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Shop Page", None))
        self.shop_name_label.setText(QCoreApplication.translate("Dialog", u"Name", None))
        self.shop_id_label.setText(QCoreApplication.translate("Dialog", u"ID", None))
        self.machine_label.setText(QCoreApplication.translate("Dialog", u"Machine Page", None))
        self.machine_name_label.setText(QCoreApplication.translate("Dialog", u"Name", None))
        self.machine_id_label.setText(QCoreApplication.translate("Dialog", u"ID", None))
        self.machine_type_label.setText(QCoreApplication.translate("Dialog", u"Type", None))
        self.machine_type_combo.setItemText(0, QCoreApplication.translate("Dialog", u"Motor-Gearbox", None))
        self.machine_type_combo.setItemText(1, QCoreApplication.translate("Dialog", u"Electro-Fan", None))
        self.machine_type_combo.setItemText(2, QCoreApplication.translate("Dialog", u"Electro-Pump", None))

        self.element_label.setText(QCoreApplication.translate("Dialog", u"Element Page", None))
        self.element_name_label.setText(QCoreApplication.translate("Dialog", u"Name", None))
        self.element_name_edit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Name of the equipment", None))
        self.element_id_label.setText(QCoreApplication.translate("Dialog", u"ID", None))
        self.element_id_edit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Unique identifier of the equipment", None))
        self.element_type_label.setText(QCoreApplication.translate("Dialog", u"Type", None))
        self.element_type_combo.setItemText(0, QCoreApplication.translate("Dialog", u"Electromotor", None))
        self.element_type_combo.setItemText(1, QCoreApplication.translate("Dialog", u"Fan", None))
        self.element_type_combo.setItemText(2, QCoreApplication.translate("Dialog", u"Pump", None))
        self.element_type_combo.setItemText(3, QCoreApplication.translate("Dialog", u"Gearbox", None))

        self.element_power_label.setText(QCoreApplication.translate("Dialog", u"Power", None))
        self.element_speed_label.setText(QCoreApplication.translate("Dialog", u"Speed", None))
        self.element_foundation_label.setText(QCoreApplication.translate("Dialog", u"Foundation", None))
        self.element_foundation_combo.setItemText(0, QCoreApplication.translate("Dialog", u"Fixed", None))
        self.element_foundation_combo.setItemText(1, QCoreApplication.translate("Dialog", u"Rigid", None))

        self.element_coupling_label.setText(QCoreApplication.translate("Dialog", u"Coupling", None))
        self.element_coupling_combo.setItemText(0, QCoreApplication.translate("Dialog", u"Coupling", None))
        self.element_coupling_combo.setItemText(1, QCoreApplication.translate("Dialog", u"Belt & Pulley", None))

        self.element_npoints_label.setText(QCoreApplication.translate("Dialog", u"N-Points", None))
        self.element_schematic.setText("")
    # retranslateUi

