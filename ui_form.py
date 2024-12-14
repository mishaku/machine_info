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
    QFormLayout, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QStackedWidget, QVBoxLayout, QWidget)
import rc_resources

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(600, 600)
        icon = QIcon()
        icon.addFile(u":/routes/icons/information.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        self.horizontalLayout_2 = QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.center_frame = QFrame(Dialog)
        self.center_frame.setObjectName(u"center_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
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
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.element_info_layout = QFrame(self.element_frame)
        self.element_info_layout.setObjectName(u"element_info_layout")
        self.element_info_layout.setFrameShape(QFrame.StyledPanel)
        self.element_info_layout.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.element_info_layout)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.general_info_gb = QGroupBox(self.element_info_layout)
        self.general_info_gb.setObjectName(u"general_info_gb")
        self.element_info_form = QFormLayout(self.general_info_gb)
        self.element_info_form.setObjectName(u"element_info_form")
        self.element_name_label = QLabel(self.general_info_gb)
        self.element_name_label.setObjectName(u"element_name_label")

        self.element_info_form.setWidget(0, QFormLayout.LabelRole, self.element_name_label)

        self.element_name_edit = QLineEdit(self.general_info_gb)
        self.element_name_edit.setObjectName(u"element_name_edit")

        self.element_info_form.setWidget(0, QFormLayout.FieldRole, self.element_name_edit)

        self.element_id_label = QLabel(self.general_info_gb)
        self.element_id_label.setObjectName(u"element_id_label")

        self.element_info_form.setWidget(1, QFormLayout.LabelRole, self.element_id_label)

        self.element_id_edit = QLineEdit(self.general_info_gb)
        self.element_id_edit.setObjectName(u"element_id_edit")

        self.element_info_form.setWidget(1, QFormLayout.FieldRole, self.element_id_edit)

        self.element_type_label = QLabel(self.general_info_gb)
        self.element_type_label.setObjectName(u"element_type_label")

        self.element_info_form.setWidget(2, QFormLayout.LabelRole, self.element_type_label)

        self.element_type_combo = QComboBox(self.general_info_gb)
        self.element_type_combo.addItem("")
        self.element_type_combo.addItem("")
        self.element_type_combo.addItem("")
        self.element_type_combo.addItem("")
        self.element_type_combo.setObjectName(u"element_type_combo")

        self.element_info_form.setWidget(2, QFormLayout.FieldRole, self.element_type_combo)

        self.element_power_label = QLabel(self.general_info_gb)
        self.element_power_label.setObjectName(u"element_power_label")

        self.element_info_form.setWidget(3, QFormLayout.LabelRole, self.element_power_label)

        self.element_power_double = QDoubleSpinBox(self.general_info_gb)
        self.element_power_double.setObjectName(u"element_power_double")
        self.element_power_double.setMaximum(99999999.000000000000000)
        self.element_power_double.setSingleStep(250.000000000000000)

        self.element_info_form.setWidget(3, QFormLayout.FieldRole, self.element_power_double)

        self.element_speed_label = QLabel(self.general_info_gb)
        self.element_speed_label.setObjectName(u"element_speed_label")

        self.element_info_form.setWidget(4, QFormLayout.LabelRole, self.element_speed_label)

        self.element_speed_double = QDoubleSpinBox(self.general_info_gb)
        self.element_speed_double.setObjectName(u"element_speed_double")
        self.element_speed_double.setMaximum(99999.000000000000000)
        self.element_speed_double.setSingleStep(50.000000000000000)

        self.element_info_form.setWidget(4, QFormLayout.FieldRole, self.element_speed_double)

        self.element_foundation_label = QLabel(self.general_info_gb)
        self.element_foundation_label.setObjectName(u"element_foundation_label")

        self.element_info_form.setWidget(5, QFormLayout.LabelRole, self.element_foundation_label)

        self.element_foundation_combo = QComboBox(self.general_info_gb)
        self.element_foundation_combo.addItem("")
        self.element_foundation_combo.addItem("")
        self.element_foundation_combo.setObjectName(u"element_foundation_combo")

        self.element_info_form.setWidget(5, QFormLayout.FieldRole, self.element_foundation_combo)

        self.element_coupling_label = QLabel(self.general_info_gb)
        self.element_coupling_label.setObjectName(u"element_coupling_label")

        self.element_info_form.setWidget(6, QFormLayout.LabelRole, self.element_coupling_label)

        self.element_coupling_combo = QComboBox(self.general_info_gb)
        self.element_coupling_combo.addItem("")
        self.element_coupling_combo.addItem("")
        self.element_coupling_combo.setObjectName(u"element_coupling_combo")

        self.element_info_form.setWidget(6, QFormLayout.FieldRole, self.element_coupling_combo)

        self.element_npoints_label = QLabel(self.general_info_gb)
        self.element_npoints_label.setObjectName(u"element_npoints_label")

        self.element_info_form.setWidget(7, QFormLayout.LabelRole, self.element_npoints_label)

        self.element_npoints_spin = QSpinBox(self.general_info_gb)
        self.element_npoints_spin.setObjectName(u"element_npoints_spin")
        self.element_npoints_spin.setMinimum(1)
        self.element_npoints_spin.setMaximum(6)

        self.element_info_form.setWidget(7, QFormLayout.FieldRole, self.element_npoints_spin)


        self.horizontalLayout_5.addWidget(self.general_info_gb)

        self.specific_info_gb = QGroupBox(self.element_info_layout)
        self.specific_info_gb.setObjectName(u"specific_info_gb")
        self.horizontalLayout_6 = QHBoxLayout(self.specific_info_gb)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.specific_info_sw = QStackedWidget(self.specific_info_gb)
        self.specific_info_sw.setObjectName(u"specific_info_sw")
        self.gearbox_page = QWidget()
        self.gearbox_page.setObjectName(u"gearbox_page")
        self.formLayout = QFormLayout(self.gearbox_page)
        self.formLayout.setObjectName(u"formLayout")
        self.gb_gearbox_type_label = QLabel(self.gearbox_page)
        self.gb_gearbox_type_label.setObjectName(u"gb_gearbox_type_label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.gb_gearbox_type_label)

        self.gb_gearbox_type_combo = QComboBox(self.gearbox_page)
        self.gb_gearbox_type_combo.addItem("")
        self.gb_gearbox_type_combo.addItem("")
        self.gb_gearbox_type_combo.addItem("")
        self.gb_gearbox_type_combo.addItem("")
        self.gb_gearbox_type_combo.addItem("")
        self.gb_gearbox_type_combo.addItem("")
        self.gb_gearbox_type_combo.setObjectName(u"gb_gearbox_type_combo")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.gb_gearbox_type_combo)

        self.gb_stage_label = QLabel(self.gearbox_page)
        self.gb_stage_label.setObjectName(u"gb_stage_label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.gb_stage_label)

        self.gb_stage_sb = QSpinBox(self.gearbox_page)
        self.gb_stage_sb.setObjectName(u"gb_stage_sb")
        self.gb_stage_sb.setMinimum(1)
        self.gb_stage_sb.setMaximum(10)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.gb_stage_sb)

        self.gb_input_speed_label = QLabel(self.gearbox_page)
        self.gb_input_speed_label.setObjectName(u"gb_input_speed_label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.gb_input_speed_label)

        self.gb_input_speed_dsb = QDoubleSpinBox(self.gearbox_page)
        self.gb_input_speed_dsb.setObjectName(u"gb_input_speed_dsb")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.gb_input_speed_dsb)

        self.gb_output_speed_label = QLabel(self.gearbox_page)
        self.gb_output_speed_label.setObjectName(u"gb_output_speed_label")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.gb_output_speed_label)

        self.gb_output_speed_dsb = QDoubleSpinBox(self.gearbox_page)
        self.gb_output_speed_dsb.setObjectName(u"gb_output_speed_dsb")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.gb_output_speed_dsb)

        self.gb_bearing_label = QLabel(self.gearbox_page)
        self.gb_bearing_label.setObjectName(u"gb_bearing_label")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.gb_bearing_label)

        self.gb_bearing_button = QPushButton(self.gearbox_page)
        self.gb_bearing_button.setObjectName(u"gb_bearing_button")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.gb_bearing_button)

        self.gb_gear_label = QLabel(self.gearbox_page)
        self.gb_gear_label.setObjectName(u"gb_gear_label")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.gb_gear_label)

        self.gb_gear_button = QPushButton(self.gearbox_page)
        self.gb_gear_button.setObjectName(u"gb_gear_button")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.gb_gear_button)

        self.specific_info_sw.addWidget(self.gearbox_page)
        self.motor_page = QWidget()
        self.motor_page.setObjectName(u"motor_page")
        self.specific_info_sw.addWidget(self.motor_page)
        self.fan_page = QWidget()
        self.fan_page.setObjectName(u"fan_page")
        self.specific_info_sw.addWidget(self.fan_page)
        self.pump_page = QWidget()
        self.pump_page.setObjectName(u"pump_page")
        self.specific_info_sw.addWidget(self.pump_page)
        self.turbine_page = QWidget()
        self.turbine_page.setObjectName(u"turbine_page")
        self.specific_info_sw.addWidget(self.turbine_page)
        self.compressor_page = QWidget()
        self.compressor_page.setObjectName(u"compressor_page")
        self.specific_info_sw.addWidget(self.compressor_page)

        self.horizontalLayout_6.addWidget(self.specific_info_sw)


        self.horizontalLayout_5.addWidget(self.specific_info_gb)


        self.verticalLayout_8.addWidget(self.element_info_layout)

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


        self.horizontalLayout_2.addWidget(self.center_frame)


        self.retranslateUi(Dialog)

        self.main_stacked_widget.setCurrentIndex(4)
        self.machine_type_combo.setCurrentIndex(-1)
        self.element_type_combo.setCurrentIndex(-1)
        self.element_foundation_combo.setCurrentIndex(-1)
        self.element_coupling_combo.setCurrentIndex(-1)
        self.specific_info_sw.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Input Information Dialog", None))
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

        self.general_info_gb.setTitle(QCoreApplication.translate("Dialog", u"General Info", None))
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
        self.specific_info_gb.setTitle(QCoreApplication.translate("Dialog", u"Specific Info", None))
        self.gb_gearbox_type_label.setText(QCoreApplication.translate("Dialog", u"Gearbox Type", None))
        self.gb_gearbox_type_combo.setItemText(0, QCoreApplication.translate("Dialog", u"Parallel Shaft", None))
        self.gb_gearbox_type_combo.setItemText(1, QCoreApplication.translate("Dialog", u"Planetary", None))
        self.gb_gearbox_type_combo.setItemText(2, QCoreApplication.translate("Dialog", u"Helical Bevel", None))
        self.gb_gearbox_type_combo.setItemText(3, QCoreApplication.translate("Dialog", u"Worm", None))
        self.gb_gearbox_type_combo.setItemText(4, QCoreApplication.translate("Dialog", u"Epicyclic (Planetary) Reduction", None))
        self.gb_gearbox_type_combo.setItemText(5, QCoreApplication.translate("Dialog", u"Inline Shaft", None))

        self.gb_stage_label.setText(QCoreApplication.translate("Dialog", u"Number of stages", None))
        self.gb_input_speed_label.setText(QCoreApplication.translate("Dialog", u"Input Speed", None))
        self.gb_output_speed_label.setText(QCoreApplication.translate("Dialog", u"Output Speed", None))
        self.gb_bearing_label.setText(QCoreApplication.translate("Dialog", u"Bearings (Code)", None))
        self.gb_bearing_button.setText(QCoreApplication.translate("Dialog", u"Set Bearing Info", None))
        self.gb_gear_label.setText(QCoreApplication.translate("Dialog", u"Gears (Teeth)", None))
        self.gb_gear_button.setText(QCoreApplication.translate("Dialog", u"Set Gear Info", None))
        self.element_schematic.setText("")
    # retranslateUi

