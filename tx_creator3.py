# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'txcreator4e.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from ecdsa_functions import *
from address_functions import *
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtGui import QPixmap
import libre_tx_rc
import time


class Ui_Libre_Tx(object):
    def setupUi(self, Libre_Tx):
        Libre_Tx.setObjectName("Libre_Tx")
        Libre_Tx.resize(1618, 862)
        Libre_Tx.setMinimumSize(QtCore.QSize(1618, 862))
        Libre_Tx.setMaximumSize(QtCore.QSize(1618, 886))
        Libre_Tx.setProperty("script_pubkey", "")
        self.gridLayout = QtWidgets.QGridLayout(Libre_Tx)
        self.gridLayout.setObjectName("gridLayout")
        self.privkey6_box = QtWidgets.QLineEdit(Libre_Tx)
        self.privkey6_box.setMinimumSize(QtCore.QSize(460, 0))
        self.privkey6_box.setMaximumSize(QtCore.QSize(460, 16777215))
        self.privkey6_box.setObjectName("privkey6_box")
        self.gridLayout.addWidget(self.privkey6_box, 28, 4, 1, 1)
        self.multisig_spin_label = QtWidgets.QLabel(Libre_Tx)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.multisig_spin_label.setFont(font)
        self.multisig_spin_label.setObjectName("multisig_spin_label")
        self.gridLayout.addWidget(self.multisig_spin_label, 26, 1, 1, 1)
        self.scriptpub1_box = QtWidgets.QLineEdit(Libre_Tx)
        self.scriptpub1_box.setMinimumSize(QtCore.QSize(450, 0))
        self.scriptpub1_box.setMaximumSize(QtCore.QSize(450, 16777215))
        self.scriptpub1_box.setObjectName("scriptpub1_box")
        self.gridLayout.addWidget(self.scriptpub1_box, 6, 4, 1, 1)
        self.txin6_box = QtWidgets.QLineEdit(Libre_Tx)
        self.txin6_box.setMinimumSize(QtCore.QSize(525, 0))
        self.txin6_box.setMaximumSize(QtCore.QSize(525, 16777215))
        self.txin6_box.setObjectName("txin6_box")
        self.gridLayout.addWidget(self.txin6_box, 11, 3, 1, 1)
        self.privkey3_box = QtWidgets.QLineEdit(Libre_Tx)
        self.privkey3_box.setMinimumSize(QtCore.QSize(460, 0))
        self.privkey3_box.setMaximumSize(QtCore.QSize(460, 16777215))
        self.privkey3_box.setObjectName("privkey3_box")
        self.gridLayout.addWidget(self.privkey3_box, 23, 4, 1, 1)
        self.psbt_label = QtWidgets.QLabel(Libre_Tx)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.psbt_label.setFont(font)
        self.psbt_label.setObjectName("psbt_label")
        self.gridLayout.addWidget(self.psbt_label, 18, 6, 1, 1)
        self.inputindex1_box = QtWidgets.QLineEdit(Libre_Tx)
        self.inputindex1_box.setMinimumSize(QtCore.QSize(80, 0))
        self.inputindex1_box.setMaximumSize(QtCore.QSize(80, 16777215))
        self.inputindex1_box.setObjectName("inputindex1_box")
        self.gridLayout.addWidget(self.inputindex1_box, 6, 2, 1, 1)
        self.txinamounts_label = QtWidgets.QLabel(Libre_Tx)
        self.txinamounts_label.setMinimumSize(QtCore.QSize(0, 20))
        self.txinamounts_label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        self.txinamounts_label.setFont(font)
        self.txinamounts_label.setObjectName("txinamounts_label")
        self.gridLayout.addWidget(self.txinamounts_label, 5, 0, 1, 1)
        self.scriptpubkey_label = QtWidgets.QLabel(Libre_Tx)
        self.scriptpubkey_label.setMinimumSize(QtCore.QSize(0, 20))
        self.scriptpubkey_label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setItalic(False)
        self.scriptpubkey_label.setFont(font)
        self.scriptpubkey_label.setObjectName("scriptpubkey_label")
        self.gridLayout.addWidget(self.scriptpubkey_label, 5, 4, 1, 1)
        self.outputformat_label = QtWidgets.QLabel(Libre_Tx)
        self.outputformat_label.setMinimumSize(QtCore.QSize(0, 20))
        self.outputformat_label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.outputformat_label.setFont(font)
        self.outputformat_label.setObjectName("outputformat_label")
        self.gridLayout.addWidget(self.outputformat_label, 5, 5, 1, 1)
        self.inputindex2_box = QtWidgets.QLineEdit(Libre_Tx)
        self.inputindex2_box.setMinimumSize(QtCore.QSize(80, 0))
        self.inputindex2_box.setMaximumSize(QtCore.QSize(80, 16777215))
        self.inputindex2_box.setObjectName("inputindex2_box")
        self.gridLayout.addWidget(self.inputindex2_box, 7, 2, 1, 1)
        self.scriptout2_box = QtWidgets.QLineEdit(Libre_Tx)
        self.scriptout2_box.setMinimumSize(QtCore.QSize(450, 0))
        self.scriptout2_box.setMaximumSize(QtCore.QSize(450, 16777215))
        self.scriptout2_box.setObjectName("scriptout2_box")
        self.gridLayout.addWidget(self.scriptout2_box, 21, 3, 1, 1)
        self.walletstyle_combobox = QtWidgets.QComboBox(Libre_Tx)
        self.walletstyle_combobox.setObjectName("walletstyle_combobox")
        self.gridLayout.addWidget(self.walletstyle_combobox, 8, 5, 1, 1)
        self.scriptout3_box = QtWidgets.QLineEdit(Libre_Tx)
        self.scriptout3_box.setMinimumSize(QtCore.QSize(450, 0))
        self.scriptout3_box.setMaximumSize(QtCore.QSize(450, 16777215))
        self.scriptout3_box.setObjectName("scriptout3_box")
        self.gridLayout.addWidget(self.scriptout3_box, 23, 3, 1, 1)
        self.txinamount_box6 = QtWidgets.QLineEdit(Libre_Tx)
        self.txinamount_box6.setMinimumSize(QtCore.QSize(87, 0))
        self.txinamount_box6.setMaximumSize(QtCore.QSize(87, 16777215))
        self.txinamount_box6.setObjectName("txinamount_box6")
        self.gridLayout.addWidget(self.txinamount_box6, 11, 0, 1, 1)
        self.txtype_combobox_1 = QtWidgets.QComboBox(Libre_Tx)
        self.txtype_combobox_1.setMinimumSize(QtCore.QSize(85, 0))
        self.txtype_combobox_1.setMaximumSize(QtCore.QSize(85, 16777215))
        self.txtype_combobox_1.setObjectName("txtype_combobox")
        self.gridLayout.addWidget(self.txtype_combobox_1, 6, 1, 1, 1)
        self.inputindex5_box = QtWidgets.QLineEdit(Libre_Tx)
        self.inputindex5_box.setMinimumSize(QtCore.QSize(80, 0))
        self.inputindex5_box.setMaximumSize(QtCore.QSize(80, 16777215))
        self.inputindex5_box.setObjectName("inputindex5_box")
        self.gridLayout.addWidget(self.inputindex5_box, 10, 2, 1, 1)
        self.scriptpub6_box = QtWidgets.QLineEdit(Libre_Tx)
        self.scriptpub6_box.setMinimumSize(QtCore.QSize(450, 0))
        self.scriptpub6_box.setMaximumSize(QtCore.QSize(450, 16777215))
        self.scriptpub6_box.setObjectName("scriptpub6_box")
        self.gridLayout.addWidget(self.scriptpub6_box, 11, 4, 1, 1)
        self.txtype_combobox_4 = QtWidgets.QComboBox(Libre_Tx)
        self.txtype_combobox_4.setMinimumSize(QtCore.QSize(85, 0))
        self.txtype_combobox_4.setMaximumSize(QtCore.QSize(85, 16777215))
        self.txtype_combobox_4.setObjectName("txtype_combobox_4")
        self.gridLayout.addWidget(self.txtype_combobox_4, 9, 1, 1, 1)
        self.outputformat_combobox = QtWidgets.QComboBox(Libre_Tx)
        self.outputformat_combobox.setProperty("bitcoin_address", "")
        self.outputformat_combobox.setObjectName("outputformat_combobox")
        self.gridLayout.addWidget(self.outputformat_combobox, 6, 5, 1, 1)
        self.txin2_box = QtWidgets.QLineEdit(Libre_Tx)
        self.txin2_box.setMinimumSize(QtCore.QSize(525, 0))
        self.txin2_box.setMaximumSize(QtCore.QSize(525, 16777215))
        self.txin2_box.setObjectName("txin2_box")
        self.gridLayout.addWidget(self.txin2_box, 7, 3, 1, 1)
        self.txin3_box = QtWidgets.QLineEdit(Libre_Tx)
        self.txin3_box.setMinimumSize(QtCore.QSize(525, 0))
        self.txin3_box.setMaximumSize(QtCore.QSize(525, 16777215))
        self.txin3_box.setObjectName("txin3_box")
        self.gridLayout.addWidget(self.txin3_box, 8, 3, 1, 1)
        self.inputindex4_box = QtWidgets.QLineEdit(Libre_Tx)
        self.inputindex4_box.setMinimumSize(QtCore.QSize(80, 0))
        self.inputindex4_box.setMaximumSize(QtCore.QSize(80, 16777215))
        self.inputindex4_box.setObjectName("inputindex4_box")
        self.gridLayout.addWidget(self.inputindex4_box, 9, 2, 1, 1)
        self.inputindex6_box = QtWidgets.QLineEdit(Libre_Tx)
        self.inputindex6_box.setMinimumSize(QtCore.QSize(80, 0))
        self.inputindex6_box.setMaximumSize(QtCore.QSize(80, 16777215))
        self.inputindex6_box.setObjectName("inputindex6_box")
        self.gridLayout.addWidget(self.inputindex6_box, 11, 2, 1, 1)
        self.privkey1_box = QtWidgets.QLineEdit(Libre_Tx)
        self.privkey1_box.setMinimumSize(QtCore.QSize(460, 0))
        self.privkey1_box.setMaximumSize(QtCore.QSize(460, 16777215))
        self.privkey1_box.setObjectName("privkey1_box")
        self.gridLayout.addWidget(self.privkey1_box, 18, 4, 1, 1)
        self.privkey4_box = QtWidgets.QLineEdit(Libre_Tx)
        self.privkey4_box.setMinimumSize(QtCore.QSize(460, 0))
        self.privkey4_box.setMaximumSize(QtCore.QSize(460, 16777215))
        self.privkey4_box.setObjectName("privkey4_box")
        self.gridLayout.addWidget(self.privkey4_box, 25, 4, 1, 1)
        self.privkeyformat_label = QtWidgets.QLabel(Libre_Tx)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(11)
        self.privkeyformat_label.setFont(font)
        self.privkeyformat_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.privkeyformat_label.setObjectName("privkeyformat_label")
        self.gridLayout.addWidget(self.privkeyformat_label, 12, 4, 1, 1)
        self.scriptout1_box = QtWidgets.QLineEdit(Libre_Tx)
        self.scriptout1_box.setMinimumSize(QtCore.QSize(450, 0))
        self.scriptout1_box.setMaximumSize(QtCore.QSize(450, 16777215))
        self.scriptout1_box.setObjectName("scriptout1_box")
        self.gridLayout.addWidget(self.scriptout1_box, 18, 3, 1, 1)
        self.unsigned_label = QtWidgets.QLabel(Libre_Tx)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.unsigned_label.setFont(font)
        self.unsigned_label.setObjectName("unsigned_label")
        self.gridLayout.addWidget(self.unsigned_label, 23, 6, 1, 1)
        self.txin4_box = QtWidgets.QLineEdit(Libre_Tx)
        self.txin4_box.setMinimumSize(QtCore.QSize(525, 0))
        self.txin4_box.setMaximumSize(QtCore.QSize(525, 16777215))
        self.txin4_box.setObjectName("txin4_box")
        self.gridLayout.addWidget(self.txin4_box, 9, 3, 1, 1)
        self.multisig_spinbox = QtWidgets.QSpinBox(Libre_Tx)
        self.multisig_spinbox.setObjectName("multisig_spinbox")
        self.gridLayout.addWidget(self.multisig_spinbox, 28, 1, 1, 1)
        self.txinamount_box1 = QtWidgets.QLineEdit(Libre_Tx)
        self.txinamount_box1.setMinimumSize(QtCore.QSize(87, 0))
        self.txinamount_box1.setMaximumSize(QtCore.QSize(87, 16777215))
        self.txinamount_box1.setObjectName("txinamount_box1")
        self.gridLayout.addWidget(self.txinamount_box1, 6, 0, 1, 1)
        self.txtype_combobox_3 = QtWidgets.QComboBox(Libre_Tx)
        self.txtype_combobox_3.setMinimumSize(QtCore.QSize(85, 0))
        self.txtype_combobox_3.setMaximumSize(QtCore.QSize(85, 16777215))
        self.txtype_combobox_3.setObjectName("txtype_combobox_3")
        self.gridLayout.addWidget(self.txtype_combobox_3, 8, 1, 1, 1)
        self.txin5_box = QtWidgets.QLineEdit(Libre_Tx)
        self.txin5_box.setMinimumSize(QtCore.QSize(525, 0))
        self.txin5_box.setMaximumSize(QtCore.QSize(525, 16777215))
        self.txin5_box.setObjectName("txin5_box")
        self.gridLayout.addWidget(self.txin5_box, 10, 3, 1, 1)
        self.txinamount_box3 = QtWidgets.QLineEdit(Libre_Tx)
        self.txinamount_box3.setMinimumSize(QtCore.QSize(87, 0))
        self.txinamount_box3.setMaximumSize(QtCore.QSize(87, 16777215))
        self.txinamount_box3.setObjectName("txinamount_box3")
        self.gridLayout.addWidget(self.txinamount_box3, 8, 0, 1, 1)
        self.privkey2_box = QtWidgets.QLineEdit(Libre_Tx)
        self.privkey2_box.setMinimumSize(QtCore.QSize(460, 0))
        self.privkey2_box.setMaximumSize(QtCore.QSize(460, 16777215))
        self.privkey2_box.setObjectName("privkey2_box")
        self.gridLayout.addWidget(self.privkey2_box, 21, 4, 1, 1)
        self.sequence2_box = QtWidgets.QLineEdit(Libre_Tx)
        self.sequence2_box.setMinimumSize(QtCore.QSize(75, 0))
        self.sequence2_box.setMaximumSize(QtCore.QSize(75, 16777215))
        self.sequence2_box.setObjectName("sequence2_box")
        self.gridLayout.addWidget(self.sequence2_box, 21, 0, 1, 1)
        self.output_box = QtWidgets.QTextBrowser(Libre_Tx)
        self.output_box.setMinimumSize(QtCore.QSize(1600, 300))
        self.output_box.setMaximumSize(QtCore.QSize(1600, 300))
        self.output_box.setObjectName("output_box")
        self.gridLayout.addWidget(self.output_box, 34, 0, 4, 13)
        self.icon = QtWidgets.QLabel(Libre_Tx)
        self.icon.setMaximumSize(QtCore.QSize(100, 100))
        self.icon.setText("")
        self.icon.setPixmap(QtGui.QPixmap(":/images/libre_tx_working.jpg"))
        self.icon.setScaledContents(True)
        self.icon.setObjectName("icon")
        self.gridLayout.addWidget(self.icon, 6, 6, 7, 1)
        self.tx_type1_label = QtWidgets.QLabel(Libre_Tx)
        self.tx_type1_label.setMinimumSize(QtCore.QSize(0, 20))
        self.tx_type1_label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        self.tx_type1_label.setFont(font)
        self.tx_type1_label.setObjectName("tx_type1_label")
        self.gridLayout.addWidget(self.tx_type1_label, 5, 1, 1, 1)
        self.scriptpub3_box = QtWidgets.QLineEdit(Libre_Tx)
        self.scriptpub3_box.setMinimumSize(QtCore.QSize(450, 0))
        self.scriptpub3_box.setMaximumSize(QtCore.QSize(450, 16777215))
        self.scriptpub3_box.setObjectName("scriptpub3_box")
        self.gridLayout.addWidget(self.scriptpub3_box, 8, 4, 1, 1)
        self.sequence_label = QtWidgets.QLabel(Libre_Tx)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        self.sequence_label.setFont(font)
        self.sequence_label.setObjectName("sequence_label")
        self.gridLayout.addWidget(self.sequence_label, 12, 0, 1, 1)
        self.privkey5_box = QtWidgets.QLineEdit(Libre_Tx)
        self.privkey5_box.setMinimumSize(QtCore.QSize(460, 0))
        self.privkey5_box.setMaximumSize(QtCore.QSize(460, 16777215))
        self.privkey5_box.setObjectName("privkey5_box")
        self.gridLayout.addWidget(self.privkey5_box, 26, 4, 1, 1)
        self.amount1_box = QtWidgets.QLineEdit(Libre_Tx)
        self.amount1_box.setMinimumSize(QtCore.QSize(87, 0))
        self.amount1_box.setMaximumSize(QtCore.QSize(87, 16777215))
        self.amount1_box.setObjectName("amount1_box")
        self.gridLayout.addWidget(self.amount1_box, 18, 2, 1, 1)
        self.amount4_box = QtWidgets.QLineEdit(Libre_Tx)
        self.amount4_box.setMinimumSize(QtCore.QSize(87, 0))
        self.amount4_box.setMaximumSize(QtCore.QSize(87, 16777215))
        self.amount4_box.setObjectName("amount4_box")
        self.gridLayout.addWidget(self.amount4_box, 25, 2, 1, 1)
        self.txinamount_box5 = QtWidgets.QLineEdit(Libre_Tx)
        self.txinamount_box5.setMinimumSize(QtCore.QSize(87, 0))
        self.txinamount_box5.setMaximumSize(QtCore.QSize(87, 16777215))
        self.txinamount_box5.setObjectName("txinamount_box5")
        self.gridLayout.addWidget(self.txinamount_box5, 10, 0, 1, 1)
        self.txin1_box = QtWidgets.QLineEdit(Libre_Tx)
        self.txin1_box.setMinimumSize(QtCore.QSize(525, 0))
        self.txin1_box.setMaximumSize(QtCore.QSize(525, 16777215))
        self.txin1_box.setObjectName("txin1_box")
        self.gridLayout.addWidget(self.txin1_box, 6, 3, 1, 1)
        self.scriptout5_box = QtWidgets.QLineEdit(Libre_Tx)
        self.scriptout5_box.setMinimumSize(QtCore.QSize(450, 0))
        self.scriptout5_box.setMaximumSize(QtCore.QSize(450, 16777215))
        self.scriptout5_box.setObjectName("scriptout5_box")
        self.gridLayout.addWidget(self.scriptout5_box, 26, 3, 1, 1)
        self.txtype_combobox_5 = QtWidgets.QComboBox(Libre_Tx)
        self.txtype_combobox_5.setMinimumSize(QtCore.QSize(85, 0))
        self.txtype_combobox_5.setMaximumSize(QtCore.QSize(85, 16777215))
        self.txtype_combobox_5.setObjectName("txtype_combobox_5")
        self.gridLayout.addWidget(self.txtype_combobox_5, 10, 1, 1, 1)
        self.locktime_button = QtWidgets.QPushButton(Libre_Tx)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        self.locktime_button.setFont(font)
        self.locktime_button.setObjectName("locktime_button")
        self.gridLayout.addWidget(self.locktime_button, 11, 5, 1, 1)
        self.scriptpub4_box = QtWidgets.QLineEdit(Libre_Tx)
        self.scriptpub4_box.setMinimumSize(QtCore.QSize(450, 0))
        self.scriptpub4_box.setMaximumSize(QtCore.QSize(450, 16777215))
        self.scriptpub4_box.setObjectName("scriptpub4_box")
        self.gridLayout.addWidget(self.scriptpub4_box, 9, 4, 1, 1)
        self.amounts_label = QtWidgets.QLabel(Libre_Tx)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        self.amounts_label.setFont(font)
        self.amounts_label.setObjectName("amounts_label")
        self.gridLayout.addWidget(self.amounts_label, 12, 2, 1, 1)
        self.Title_label = QtWidgets.QLabel(Libre_Tx)
        self.Title_label.setMinimumSize(QtCore.QSize(20, 0))
        self.Title_label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Zero Hour")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.Title_label.setFont(font)
        self.Title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Title_label.setObjectName("Title_label")
        self.gridLayout.addWidget(self.Title_label, 0, 3, 1, 2)
        self.sequence3_box = QtWidgets.QLineEdit(Libre_Tx)
        self.sequence3_box.setMinimumSize(QtCore.QSize(75, 0))
        self.sequence3_box.setMaximumSize(QtCore.QSize(75, 16777215))
        self.sequence3_box.setObjectName("sequence3_box")
        self.gridLayout.addWidget(self.sequence3_box, 23, 0, 1, 1)
        self.txins_label = QtWidgets.QLabel(Libre_Tx)
        self.txins_label.setMinimumSize(QtCore.QSize(0, 20))
        self.txins_label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.txins_label.setFont(font)
        self.txins_label.setObjectName("txins_label")
        self.gridLayout.addWidget(self.txins_label, 5, 3, 1, 1)
        self.privkey_label = QtWidgets.QLabel(Libre_Tx)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.privkey_label.setFont(font)
        self.privkey_label.setObjectName("privkey_label")
        self.gridLayout.addWidget(self.privkey_label, 12, 4, 1, 1)
        self.sequence1_box = QtWidgets.QLineEdit(Libre_Tx)
        self.sequence1_box.setMinimumSize(QtCore.QSize(75, 0))
        self.sequence1_box.setMaximumSize(QtCore.QSize(75, 16777215))
        self.sequence1_box.setObjectName("sequence1_box")
        self.gridLayout.addWidget(self.sequence1_box, 18, 0, 1, 1)
        self.sequence5_box = QtWidgets.QLineEdit(Libre_Tx)
        self.sequence5_box.setMinimumSize(QtCore.QSize(75, 0))
        self.sequence5_box.setMaximumSize(QtCore.QSize(75, 16777215))
        self.sequence5_box.setObjectName("sequence5_box")
        self.gridLayout.addWidget(self.sequence5_box, 26, 0, 1, 1)
        self.inputindex_label = QtWidgets.QLabel(Libre_Tx)
        self.inputindex_label.setMinimumSize(QtCore.QSize(0, 20))
        self.inputindex_label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        self.inputindex_label.setFont(font)
        self.inputindex_label.setObjectName("inputindex_label")
        self.gridLayout.addWidget(self.inputindex_label, 5, 2, 1, 1)
        self.version_box = QtWidgets.QLineEdit(Libre_Tx)
        self.version_box.setMinimumSize(QtCore.QSize(100, 0))
        self.version_box.setMaximumSize(QtCore.QSize(100, 16777215))
        self.version_box.setObjectName("version_box")
        self.gridLayout.addWidget(self.version_box, 28, 5, 1, 1)
        self.signed_button = QtWidgets.QPushButton(Libre_Tx)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        self.signed_button.setFont(font)
        self.signed_button.setObjectName("Signed_button")
        self.gridLayout.addWidget(self.signed_button, 28, 6, 1, 1)
        self.txtype_combobox_2 = QtWidgets.QComboBox(Libre_Tx)
        self.txtype_combobox_2.setMinimumSize(QtCore.QSize(85, 0))
        self.txtype_combobox_2.setMaximumSize(QtCore.QSize(85, 16777215))
        self.txtype_combobox_2.setObjectName("txtype_combobox_2")
        self.gridLayout.addWidget(self.txtype_combobox_2, 7, 1, 1, 1)
        self.hashtype_box = QtWidgets.QLineEdit(Libre_Tx)
        self.hashtype_box.setMinimumSize(QtCore.QSize(100, 0))
        self.hashtype_box.setMaximumSize(QtCore.QSize(100, 16777215))
        self.hashtype_box.setObjectName("hashtype_box")
        self.gridLayout.addWidget(self.hashtype_box, 25, 5, 1, 1)
        self.currentblock_box = QtWidgets.QLineEdit(Libre_Tx)
        self.currentblock_box.setMinimumSize(QtCore.QSize(100, 0))
        self.currentblock_box.setMaximumSize(QtCore.QSize(100, 16777215))
        self.currentblock_box.setObjectName("currentblock_box")
        self.gridLayout.addWidget(self.currentblock_box, 10, 5, 1, 1)
        self.pubouts_label = QtWidgets.QLabel(Libre_Tx)
        self.pubouts_label.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.pubouts_label.setFont(font)
        self.pubouts_label.setObjectName("pubouts_label")
        self.gridLayout.addWidget(self.pubouts_label, 12, 3, 1, 1)
        self.amount6_box = QtWidgets.QLineEdit(Libre_Tx)
        self.amount6_box.setMinimumSize(QtCore.QSize(87, 0))
        self.amount6_box.setMaximumSize(QtCore.QSize(87, 16777215))
        self.amount6_box.setObjectName("amount6_box")
        self.gridLayout.addWidget(self.amount6_box, 28, 2, 1, 1)
        self.txinamount_box4 = QtWidgets.QLineEdit(Libre_Tx)
        self.txinamount_box4.setMinimumSize(QtCore.QSize(87, 0))
        self.txinamount_box4.setMaximumSize(QtCore.QSize(87, 16777215))
        self.txinamount_box4.setObjectName("txinamount_box4")
        self.gridLayout.addWidget(self.txinamount_box4, 9, 0, 1, 1)
        self.numins_combo = QtWidgets.QComboBox(Libre_Tx)
        self.numins_combo.setMinimumSize(QtCore.QSize(90, 0))
        self.numins_combo.setMaximumSize(QtCore.QSize(90, 16777215))
        self.numins_combo.setObjectName("numins_combo")
        self.gridLayout.addWidget(self.numins_combo, 18, 1, 1, 1)
        self.sequence6_box = QtWidgets.QLineEdit(Libre_Tx)
        self.sequence6_box.setMinimumSize(QtCore.QSize(75, 0))
        self.sequence6_box.setMaximumSize(QtCore.QSize(75, 16777215))
        self.sequence6_box.setObjectName("sequence6_box")
        self.gridLayout.addWidget(self.sequence6_box, 28, 0, 1, 1)
        self.amount3_box = QtWidgets.QLineEdit(Libre_Tx)
        self.amount3_box.setMinimumSize(QtCore.QSize(87, 0))
        self.amount3_box.setMaximumSize(QtCore.QSize(87, 16777215))
        self.amount3_box.setObjectName("amount3_box")
        self.gridLayout.addWidget(self.amount3_box, 23, 2, 1, 1)
        self.currentblock_label = QtWidgets.QLabel(Libre_Tx)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        self.currentblock_label.setFont(font)
        self.currentblock_label.setObjectName("currentblock_label")
        self.gridLayout.addWidget(self.currentblock_label, 9, 5, 1, 1)
        self.privkey_comboBox = QtWidgets.QComboBox(Libre_Tx)
        self.privkey_comboBox.setObjectName("privkey_comboBox")
        self.gridLayout.addWidget(self.privkey_comboBox, 12, 5, 1, 1)
        self.numouts_combo = QtWidgets.QComboBox(Libre_Tx)
        self.numouts_combo.setMinimumSize(QtCore.QSize(90, 0))
        self.numouts_combo.setMaximumSize(QtCore.QSize(90, 16777215))
        self.numouts_combo.setObjectName("numouts_combo")
        self.gridLayout.addWidget(self.numouts_combo, 23, 1, 1, 1)
        self.txinamount_box2 = QtWidgets.QLineEdit(Libre_Tx)
        self.txinamount_box2.setMinimumSize(QtCore.QSize(87, 0))
        self.txinamount_box2.setMaximumSize(QtCore.QSize(87, 16777215))
        self.txinamount_box2.setObjectName("txinamount_box2")
        self.gridLayout.addWidget(self.txinamount_box2, 7, 0, 1, 1)
        self.numins_label = QtWidgets.QLabel(Libre_Tx)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.numins_label.setFont(font)
        self.numins_label.setObjectName("numins_label")
        self.gridLayout.addWidget(self.numins_label, 12, 1, 1, 1)
        self.unsigned_buttton = QtWidgets.QPushButton(Libre_Tx)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        self.unsigned_buttton.setFont(font)
        self.unsigned_buttton.setObjectName("unsigned_buttton")
        self.gridLayout.addWidget(self.unsigned_buttton, 25, 6, 1, 1)
        self.hashtype_label = QtWidgets.QLabel(Libre_Tx)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.hashtype_label.setFont(font)
        self.hashtype_label.setObjectName("hashtype_label")
        self.gridLayout.addWidget(self.hashtype_label, 23, 5, 1, 1)
        self.signtx_label = QtWidgets.QLabel(Libre_Tx)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.signtx_label.setFont(font)
        self.signtx_label.setObjectName("signtx_label")
        self.gridLayout.addWidget(self.signtx_label, 26, 6, 1, 1)
        self.nlocktime_label = QtWidgets.QLabel(Libre_Tx)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.nlocktime_label.setFont(font)
        self.nlocktime_label.setObjectName("nlocktime_label")
        self.gridLayout.addWidget(self.nlocktime_label, 18, 5, 1, 1)
        self.numouts_label = QtWidgets.QLabel(Libre_Tx)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.numouts_label.setFont(font)
        self.numouts_label.setObjectName("numouts_label")
        self.gridLayout.addWidget(self.numouts_label, 21, 1, 1, 1)
        self.sequence4_box = QtWidgets.QLineEdit(Libre_Tx)
        self.sequence4_box.setMinimumSize(QtCore.QSize(75, 0))
        self.sequence4_box.setMaximumSize(QtCore.QSize(75, 16777215))
        self.sequence4_box.setObjectName("sequence4_box")
        self.gridLayout.addWidget(self.sequence4_box, 25, 0, 1, 1)
        self.scriptpub2_box = QtWidgets.QLineEdit(Libre_Tx)
        self.scriptpub2_box.setMinimumSize(QtCore.QSize(450, 0))
        self.scriptpub2_box.setMaximumSize(QtCore.QSize(450, 16777215))
        self.scriptpub2_box.setObjectName("scriptpub2_box")
        self.gridLayout.addWidget(self.scriptpub2_box, 7, 4, 1, 1)
        self.scriptout6_box = QtWidgets.QLineEdit(Libre_Tx)
        self.scriptout6_box.setMinimumSize(QtCore.QSize(450, 0))
        self.scriptout6_box.setMaximumSize(QtCore.QSize(450, 16777215))
        self.scriptout6_box.setObjectName("scriptout6_box")
        self.gridLayout.addWidget(self.scriptout6_box, 28, 3, 1, 1)
        self.txtype_combobox_6 = QtWidgets.QComboBox(Libre_Tx)
        self.txtype_combobox_6.setMinimumSize(QtCore.QSize(85, 0))
        self.txtype_combobox_6.setMaximumSize(QtCore.QSize(85, 16777215))
        self.txtype_combobox_6.setObjectName("txtype_combobox_6")
        self.gridLayout.addWidget(self.txtype_combobox_6, 11, 1, 1, 1)
        self.scriptpub5_box = QtWidgets.QLineEdit(Libre_Tx)
        self.scriptpub5_box.setMinimumSize(QtCore.QSize(450, 0))
        self.scriptpub5_box.setMaximumSize(QtCore.QSize(450, 16777215))
        self.scriptpub5_box.setObjectName("scriptpub5_box")
        self.gridLayout.addWidget(self.scriptpub5_box, 10, 4, 1, 1)
        self.scriptout4_box = QtWidgets.QLineEdit(Libre_Tx)
        self.scriptout4_box.setMinimumSize(QtCore.QSize(450, 0))
        self.scriptout4_box.setMaximumSize(QtCore.QSize(450, 16777215))
        self.scriptout4_box.setObjectName("scriptout4_box")
        self.gridLayout.addWidget(self.scriptout4_box, 25, 3, 1, 1)
        self.amount2_box = QtWidgets.QLineEdit(Libre_Tx)
        self.amount2_box.setMinimumSize(QtCore.QSize(87, 0))
        self.amount2_box.setMaximumSize(QtCore.QSize(87, 16777215))
        self.amount2_box.setObjectName("amount2_box")
        self.gridLayout.addWidget(self.amount2_box, 21, 2, 1, 1)
        self.psbt_button = QtWidgets.QPushButton(Libre_Tx)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        self.psbt_button.setFont(font)
        self.psbt_button.setObjectName("psbt_button")
        self.gridLayout.addWidget(self.psbt_button, 21, 6, 1, 1)
        self.nlocktime_box = QtWidgets.QLineEdit(Libre_Tx)
        self.nlocktime_box.setMinimumSize(QtCore.QSize(100, 0))
        self.nlocktime_box.setMaximumSize(QtCore.QSize(100, 16777215))
        self.nlocktime_box.setObjectName("nlocktime_box")
        self.gridLayout.addWidget(self.nlocktime_box, 21, 5, 1, 1)
        self.emulatewallet_label = QtWidgets.QLabel(Libre_Tx)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        self.emulatewallet_label.setFont(font)
        self.emulatewallet_label.setObjectName("emulatewallet_label")
        self.gridLayout.addWidget(self.emulatewallet_label, 7, 5, 1, 1)
        self.inputindex3_box = QtWidgets.QLineEdit(Libre_Tx)
        self.inputindex3_box.setMinimumSize(QtCore.QSize(80, 0))
        self.inputindex3_box.setMaximumSize(QtCore.QSize(80, 16777215))
        self.inputindex3_box.setObjectName("inputindex3_box")
        self.gridLayout.addWidget(self.inputindex3_box, 8, 2, 1, 1)
        self.education_checkbox = QtWidgets.QCheckBox(Libre_Tx)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(10)
        self.education_checkbox.setFont(font)
        self.education_checkbox.setObjectName("education_checkbox")
        self.gridLayout.addWidget(self.education_checkbox, 25, 1, 1, 1)
        self.version_label = QtWidgets.QLabel(Libre_Tx)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        self.version_label.setFont(font)
        self.version_label.setObjectName("version_label")
        self.gridLayout.addWidget(self.version_label, 26, 5, 1, 1)
        self.amount5_box = QtWidgets.QLineEdit(Libre_Tx)
        self.amount5_box.setMinimumSize(QtCore.QSize(87, 0))
        self.amount5_box.setMaximumSize(QtCore.QSize(87, 16777215))
        self.amount5_box.setObjectName("amount5_box")
        self.gridLayout.addWidget(self.amount5_box, 26, 2, 1, 1)

        # delete threse?##################################
        self.txtype_combobox_1.activated.connect(lambda: tx_select_func(1))
        self.txtype_combobox_2.activated.connect(lambda: tx_select_func(2))
        self.txtype_combobox_3.activated.connect(lambda: tx_select_func(3))
        self.txtype_combobox_4.activated.connect(lambda: tx_select_func(4))
        self.txtype_combobox_5.activated.connect(lambda: tx_select_func(5))
        self.txtype_combobox_6.activated.connect(lambda: tx_select_func(6))

        self.numins_combo.activated.connect(lambda: ins_activate(self.numins_combo.currentIndex()+1))
        self.numouts_combo.activated.connect(lambda: outs_activate(self.numouts_combo.currentIndex()+1))


        



        self.inputindex1_box.setDisabled(True)

        self.txinamount_box2.setDisabled(True)
        self.inputindex2_box.setDisabled(True)
        self.scriptpub2_box.setDisabled(True)
        self.scriptout2_box.setDisabled(True)
        self.txin2_box.setDisabled(True)
        self.privkey2_box.setDisabled(True)
        self.amount2_box.setDisabled(True)
        self.sequence2_box.setDisabled(True)

        self.txinamount_box3.setDisabled(True)
        self.inputindex3_box.setDisabled(True)
        self.scriptpub3_box.setDisabled(True)
        self.scriptout3_box.setDisabled(True)
        self.txin3_box.setDisabled(True)
        self.privkey3_box.setDisabled(True)
        self.amount3_box.setDisabled(True)
        self.sequence3_box.setDisabled(True)

        self.txinamount_box3.setDisabled(True)
        self.inputindex3_box.setDisabled(True)
        self.scriptpub3_box.setDisabled(True)
        self.scriptout3_box.setDisabled(True)
        self.txin3_box.setDisabled(True)
        self.privkey3_box.setDisabled(True)
        self.amount3_box.setDisabled(True)
        self.sequence3_box.setDisabled(True)

        self.txinamount_box4.setDisabled(True)
        self.inputindex4_box.setDisabled(True)
        self.scriptpub4_box.setDisabled(True)
        self.scriptout4_box.setDisabled(True)
        self.txin4_box.setDisabled(True)
        self.privkey4_box.setDisabled(True)
        self.amount4_box.setDisabled(True)
        self.sequence4_box.setDisabled(True)

        self.txinamount_box5.setDisabled(True)
        self.inputindex5_box.setDisabled(True)
        self.scriptpub5_box.setDisabled(True)
        self.scriptout5_box.setDisabled(True)
        self.txin5_box.setDisabled(True)
        self.privkey5_box.setDisabled(True)
        self.amount5_box.setDisabled(True)
        self.sequence5_box.setDisabled(True)

        self.txinamount_box6.setDisabled(True)
        self.inputindex6_box.setDisabled(True)
        self.scriptpub6_box.setDisabled(True)
        self.scriptout6_box.setDisabled(True)
        self.txin6_box.setDisabled(True)
        self.privkey6_box.setDisabled(True)
        self.amount6_box.setDisabled(True)
        self.sequence6_box.setDisabled(True)

        self.privkey_comboBox.addItems(['0','1','2'])
        
        self.numins_combo.addItems(['1','2','3','4','5','6'])
        self.numouts_combo.addItems(['1','2','3','4','5','6'])
        self.signed_button.clicked.connect(ok_button)

        self.txtype_combobox_1.addItems(['N/A','P2PKH','P2SH','P2SH-P2wPKH','P2WPKH','P2WSH','P2SH multisig', 'P2WSH multisig'])
        self.txtype_combobox_2.addItems(['N/A','P2PKH','P2SH','P2SH-P2wPKH','P2WPKH','P2WSH','P2SH multisig', 'P2WSH multisig'])
        self.txtype_combobox_3.addItems(['N/A','P2PKH','P2SH','P2SH-P2wPKH','P2WPKH','P2WSH','P2SH multisig', 'P2WSH multisig'])
        self.txtype_combobox_4.addItems(['N/A','P2PKH','P2SH','P2SH-P2wPKH','P2WPKH','P2WSH','P2SH multisig', 'P2WSH multisig'])
        self.txtype_combobox_5.addItems(['N/A','P2PKH','P2SH','P2SH-P2wPKH','P2WPKH','P2WSH','P2SH multisig', 'P2WSH multisig'])
        self.txtype_combobox_6.addItems(['N/A','P2PKH','P2SH','P2SH-P2wPKH','P2WPKH','P2WSH','P2SH multisig', 'P2WSH multisig'])

        self.locktime_button.clicked.connect(int_to_nlocktime)

        self.outputformat_combobox.addItems(['0','1'])

        self.hashtype_box.setText('01000000')

        self.nlocktime_box.setText('28f11700')

        self.inputindex1_box.setText('00000000')
        self.scriptpub1_box.setText('695221033a69d0acd6e9500844ca078fbc4d81b6c95d7967b3106e31618d5987633d41a92103775ebfa3681adf4bbc6b19d3de2d4d6b911c180be46c9aca8128d428c7a0e0a821039c96c76acfc3928c36b0ea7d9eea07341adbb3d136c533637dd8c91302b6124353ae')
        self.scriptout1_box.setText('n2ZzdQWjqP8tFizWG7vn8uja6bf2BkhZkn')
        self.txin1_box.setText('f2dbe3f179eb7d52e094ec417c062c163612bd28082a47275e2bb4194ade7739')
        self.privkey1_box.setText('cVGBPvF5SgvcCqur3iEbPCjycgWkzN29r3RMdFPdWGxDGdTTkYJh')
        self.privkey2_box.setText('cPViG6CgGk3jikHioCkjRPymeY97NKxdVr4SEXjfgawWsB1uT3BG')
        # self.privkey3_box.setText('cPVmuQC4yR9a6pmMmHaTsPSzmadpb68zfbosdQ4GhFjRgtDNg8ua')
        self.amount1_box.setText('0.000002')
        self.version_box.setText('02000000')

        self.sequence1_box.setText('fdffffff')



        self.retranslateUi(Libre_Tx)
        QtCore.QMetaObject.connectSlotsByName(Libre_Tx)

    def retranslateUi(self, Libre_Tx):
        _translate = QtCore.QCoreApplication.translate
        Libre_Tx.setWindowTitle(_translate("Libre_Tx", "Libre Tx"))
        self.multisig_spin_label.setText(_translate("Libre_Tx", "Multisig Total"))
        self.psbt_label.setText(_translate("Libre_Tx", "Create PSBT"))
        self.txinamounts_label.setText(_translate("Libre_Tx", "Txin Amounts"))
        self.scriptpubkey_label.setText(_translate("Libre_Tx", "Script pubkeys"))
        self.outputformat_label.setText(_translate("Libre_Tx", "Output Address Format"))
        self.privkeyformat_label.setText(_translate("Libre_Tx", "Priv Key Format"))
        self.unsigned_label.setText(_translate("Libre_Tx", "Create Unsigned"))
        self.tx_type1_label.setText(_translate("Libre_Tx", "Tx Type"))
        self.sequence_label.setText(_translate("Libre_Tx", "Sequence"))
        self.locktime_button.setText(_translate("Libre_Tx", "Convert L-Time"))
        self.amounts_label.setText(_translate("Libre_Tx", "Amounts"))
        self.Title_label.setText(_translate("Libre_Tx", "Libre Tx"))
        self.txins_label.setText(_translate("Libre_Tx", "Txins TXID\'s"))
        self.privkey_label.setText(_translate("Libre_Tx", "Priv Keys"))
        self.inputindex_label.setText(_translate("Libre_Tx", "Input Index"))
        self.signed_button.setText(_translate("Libre_Tx", "Create Signed"))
        self.pubouts_label.setText(_translate("Libre_Tx", "Script pub outs"))
        self.currentblock_label.setText(_translate("Libre_Tx", "Block hgt/UNIX Time"))
        self.numins_label.setText(_translate("Libre_Tx", "Num Ins"))
        self.unsigned_buttton.setText(_translate("Libre_Tx", "Create Unsigned"))
        self.hashtype_label.setText(_translate("Libre_Tx", "Hash type"))
        self.signtx_label.setText(_translate("Libre_Tx", "Sign Tx"))
        self.nlocktime_label.setText(_translate("Libre_Tx", "N-locktime"))
        self.numouts_label.setText(_translate("Libre_Tx", "Num Outs"))
        self.psbt_button.setText(_translate("Libre_Tx", "Create PSBT"))
        self.emulatewallet_label.setText(_translate("Libre_Tx", "Emulate Wallet"))
        self.education_checkbox.setText(_translate("Libre_Tx", "Edu Mode"))
        self.version_label.setText(_translate("Libre_Tx", "Version"))


        self.txtype_combobox_1.setItemText(0, _translate("Txcreator", "N/A"))
        self.txtype_combobox_1.setItemText(1, _translate("Txcreator", "P2PKH"))
        self.txtype_combobox_1.setItemText(2, _translate("Txcreator", "P2SH"))
        self.txtype_combobox_1.setItemText(3, _translate("Txcreator", "P2SH-P2wPKH"))
        self.txtype_combobox_1.setItemText(4, _translate("Txcreator", "P2WPKH"))
        self.txtype_combobox_1.setItemText(5, _translate("Txcreator", "P2WSH"))
        self.txtype_combobox_1.setItemText(6, _translate("Txcreator", "P2SH multisig"))
        self.txtype_combobox_1.setItemText(7, _translate("Txcreator", "P2WSH multisig"))
        
        self.txtype_combobox_2.setItemText(0, _translate("Txcreator", "N/A"))
        self.txtype_combobox_2.setItemText(1, _translate("Txcreator", "P2PKH"))
        self.txtype_combobox_2.setItemText(2, _translate("Txcreator", "P2SH"))
        self.txtype_combobox_2.setItemText(3, _translate("Txcreator", "P2SH-P2wPKH"))
        self.txtype_combobox_2.setItemText(4, _translate("Txcreator", "P2WPKH"))
        self.txtype_combobox_2.setItemText(5, _translate("Txcreator", "P2WSH"))
        self.txtype_combobox_2.setItemText(6, _translate("Txcreator", "P2SH multisig"))
        self.txtype_combobox_2.setItemText(7, _translate("Txcreator", "P2WSH multisig"))

        self.txtype_combobox_3.setItemText(0, _translate("Txcreator", "N/A"))
        self.txtype_combobox_3.setItemText(1, _translate("Txcreator", "P2PKH"))
        self.txtype_combobox_3.setItemText(2, _translate("Txcreator", "P2SH"))
        self.txtype_combobox_3.setItemText(3, _translate("Txcreator", "P2SH-P2wPKH"))
        self.txtype_combobox_3.setItemText(4, _translate("Txcreator", "P2WPKH"))
        self.txtype_combobox_3.setItemText(5, _translate("Txcreator", "P2WSH"))
        self.txtype_combobox_3.setItemText(6, _translate("Txcreator", "P2SH multisig"))
        self.txtype_combobox_3.setItemText(7, _translate("Txcreator", "P2WSH multisig"))

        self.txtype_combobox_4.setItemText(0, _translate("Txcreator", "N/A"))
        self.txtype_combobox_4.setItemText(1, _translate("Txcreator", "P2PKH"))
        self.txtype_combobox_4.setItemText(2, _translate("Txcreator", "P2SH"))
        self.txtype_combobox_4.setItemText(3, _translate("Txcreator", "P2SH-P2wPKH"))
        self.txtype_combobox_4.setItemText(4, _translate("Txcreator", "P2WPKH"))
        self.txtype_combobox_4.setItemText(5, _translate("Txcreator", "P2WSH"))
        self.txtype_combobox_4.setItemText(6, _translate("Txcreator", "P2SH multisig"))
        self.txtype_combobox_4.setItemText(7, _translate("Txcreator", "P2WSH multisig"))

        self.txtype_combobox_5.setItemText(0, _translate("Txcreator", "N/A"))
        self.txtype_combobox_5.setItemText(1, _translate("Txcreator", "P2PKH"))
        self.txtype_combobox_5.setItemText(2, _translate("Txcreator", "P2SH"))
        self.txtype_combobox_5.setItemText(3, _translate("Txcreator", "P2SH-P2wPKH"))
        self.txtype_combobox_5.setItemText(4, _translate("Txcreator", "P2WPKH"))
        self.txtype_combobox_5.setItemText(5, _translate("Txcreator", "P2WSH"))
        self.txtype_combobox_5.setItemText(6, _translate("Txcreator", "P2SH multisig"))
        self.txtype_combobox_5.setItemText(7, _translate("Txcreator", "P2WSH multisig"))

        self.txtype_combobox_6.setItemText(0, _translate("Txcreator", "N/A"))
        self.txtype_combobox_6.setItemText(1, _translate("Txcreator", "P2PKH"))
        self.txtype_combobox_6.setItemText(2, _translate("Txcreator", "P2SH"))
        self.txtype_combobox_6.setItemText(3, _translate("Txcreator", "P2SH-P2wPKH"))
        self.txtype_combobox_6.setItemText(4, _translate("Txcreator", "P2WPKH"))
        self.txtype_combobox_6.setItemText(5, _translate("Txcreator", "P2WSH"))
        self.txtype_combobox_6.setItemText(6, _translate("Txcreator", "P2SH multisig"))
        self.txtype_combobox_6.setItemText(7, _translate("Txcreator", "P2WSH multisig"))

        self.outputformat_combobox.setItemText(0, _translate("Txcreator", "Scriptpub"))
        self.outputformat_combobox.setItemText(1, _translate("Txcreator", "Address"))

        self.privkey_comboBox.setItemText(0, _translate("Txcreator", "WIF"))
        self.privkey_comboBox.setItemText(1, _translate("Txcreator", "Hex"))
        self.privkey_comboBox.setItemText(2, _translate("Txcreator", "Scalar"))


segwit_flag='0001'
SIGHASH_ALL = 1

#can these and their refrences go in the address functions file?
OP_HASH160 = b'\xa9'
OP_EQUAL = b'\x87'
EDU_MODE_OUTPUT=[]
EDU_MODE_UNSIGNED=[]
EDU_MODE_SIGS=[]

class tx_data_obj:

    def __init__(self, outs, tx_selection_types, segwitprefix, legacy_prefix, tx_inputs, input_secrets, script_pubs, segwit_input_infos, select_inputs):
        self.outs=outs
        self.tx_selection_types=tx_selection_types
        self.segwitprefix=segwitprefix
        self.legacy_prefix=legacy_prefix
        self.tx_inputs=tx_inputs
        self.input_secrets=input_secrets
        self.script_pubs=script_pubs
        self.segwit_input_infos=segwit_input_infos
        self.select_inputs=select_inputs

    
def tx_data():
    outs=[ui.scriptout1_box.text(),ui.scriptout2_box.text(),ui.scriptout3_box.text(),ui.scriptout4_box.text(),ui.scriptout5_box.text(),ui.scriptout6_box.text()] 
    if ui.outputformat_combobox.currentIndex() ==1: 
        outs_list=address_to_scriptpub(outs)
        outs=outs_list
    tx_selection_types=[ui.txtype_combobox_1.currentText(), ui.txtype_combobox_2.currentText(), ui.txtype_combobox_3.currentText(), ui.txtype_combobox_4.currentText(), ui.txtype_combobox_5.currentText(), ui.txtype_combobox_6.currentText()]
    segwitprefix=[ui.version_box.text(),segwit_flag,tx_num_func(ui.numins_combo.currentIndex())]
    legacy_prefix=[ui.version_box.text(),tx_num_func(ui.numins_combo.currentIndex())]
    #this is same as segwit- can merge
    tx_inputs=[[txid_endian(ui.txin1_box.text()), ui.inputindex1_box.text(),ui.sequence1_box.text()],[txid_endian(ui.txin2_box.text()), ui.inputindex2_box.text(),ui.sequence2_box.text()],[txid_endian(ui.txin3_box.text()), ui.inputindex3_box.text(),ui.sequence3_box.text()],[txid_endian(ui.txin4_box.text()), ui.inputindex4_box.text(),ui.sequence4_box.text()],[txid_endian(ui.txin5_box.text()), ui.inputindex5_box.text(),ui.sequence5_box.text()],[txid_endian(ui.txin6_box.text()), ui.inputindex6_box.text(),ui.sequence6_box.text()]]
    input_secrets=[ui.privkey1_box.text(),ui.privkey2_box.text(),ui.privkey3_box.text(),ui.privkey4_box.text(),ui.privkey5_box.text(),ui.privkey6_box.text()]
    script_pubs=[ui.scriptpub1_box.text(), ui.scriptpub2_box.text(), ui.scriptpub3_box.text(), ui.scriptpub4_box.text(),ui.scriptpub5_box.text(), ui.scriptpub6_box.text()]
    segwit_input_infos=[[txid_endian(ui.txin1_box.text())+ui.inputindex1_box.text()+ui.scriptpub1_box.text()+amount_to_txhex(ui.txinamount_box1.text())+ui.sequence1_box.text()],[txid_endian(ui.txin2_box.text())+ui.inputindex2_box.text()+ui.scriptpub2_box.text()+amount_to_txhex(ui.txinamount_box2.text())+ui.sequence2_box.text()],[txid_endian(ui.txin3_box.text())+ui.inputindex3_box.text()+ui.scriptpub3_box.text()+amount_to_txhex(ui.txinamount_box3.text())+ui.sequence3_box.text()],[txid_endian(ui.txin4_box.text())+ui.inputindex4_box.text()+ui.scriptpub4_box.text()+amount_to_txhex(ui.txinamount_box4.text())+ui.sequence4_box.text()],[txid_endian(ui.txin5_box.text())+ui.inputindex5_box.text()+ui.scriptpub5_box.text()+amount_to_txhex(ui.txinamount_box5.text())+ui.sequence5_box.text()],[txid_endian(ui.txin6_box.text())+ui.inputindex6_box.text()+ui.scriptpub6_box.text()+amount_to_txhex(ui.txinamount_box6.text())+ui.sequence6_box.text()]]
    select_inputs=[ui.txtype_combobox_1,ui.txtype_combobox_2,ui.txtype_combobox_3,ui.txtype_combobox_4,ui.txtype_combobox_5,ui.txtype_combobox_6]
    return tx_data_obj(outs, tx_selection_types, segwitprefix, legacy_prefix, tx_inputs, input_secrets, script_pubs, segwit_input_infos, select_inputs)


def ok_button():
    EDU_MODE_OUTPUT=[]
    gui_data=tx_data()
    
    dersigs=[]
    multisig_dersigs=[]
    witness_program=[]
    segwit_indexs=[]
    p2sh_segwit_indexs=[]
    ms_segwit_indexes=[]
    p2pkhindexs=[]
    segwit_multisigs=[]
    multisig_indexes=[]


    outs=gui_data.outs
    tx_selections=list(gui_data.tx_selection_types)
  
    count=0
    for item in tx_selections:
        if item == 'N/A':
            count+=1
            pass
        if item == 'P2PKH':
            try:
                result= join_info(0, count)
            except TypeError:
                ui.output_box.setText('Invalid Input- Please check your input data and try again')
                return
            dersigs.append(result)
             ## ADD THIS TO EDU MODE PRINTS
            print('DERSIG', dersigs)
            p2pkhindexs.append(count)
            count+=1

        if item== 'P2SH':
            try:
                result= join_info(99, count)
            except TypeError:
                ui.output_box.setText('Invalid Input- Please check your input data and try again')
                return
            dersigs.append(result)
             ## ADD THIS TO EDU MODE PRINTS
            print('DERSIG', dersigs)
            p2pkhindexs.append(count)### CORRECT???
            count+=1

        if item == 'P2SH-P2wPKH':
            try:
                result=join_segwit(1, count) 
            except TypeError:
                ui.output_box.setText('Invalid Input- Please check your input data and try again')
                return
            witness_program.append(result)
            print('P2SH WITNESS',count, witness_program)
            p2sh_segwit_indexs.append(count)
            count+=1

        if item == 'P2WPKH':
            try:
                result=join_segwit(1, count)
            except TypeError:
                ui.output_box.setText('Invalid Input- Please check your input data and try again')
                return
            witness_program.append(result)
            dersigs.append('00')
            print('WITNESS',count, witness_program)
            segwit_indexs.append(count)
            count+=1

        if item == 'P2WSH': 
            try:
                result=join_segwit(98, count)  # add flag here for p2wsh segwit
            except TypeError:
                ui.output_box.setText('Invalid Input- Please check your input data and try again')
                return
            witness_program.append(result)
            print('P2SH WITNESS',count, witness_program)
            segwit_indexs.append(count)
            count+=1

        # 00 here - nessesary
        if item == 'P2SH multisig':     
            tx_selections=gui_data.tx_selection_types
            first_index=tx_selections.index('P2SH multisig')
            try:
                result=join_info(count,first_index)
            except TypeError:
                ui.output_box.setText('Invalid Input- Please check your input data and try again')
                return
            if result=='00':
                multisig_dersigs.insert(0, result)
            else:
                multisig_dersigs.append(result)
            print('MULTI DERSIG', multisig_dersigs)
            multisig_indexes.append(count)
            count+=1

        if item == 'P2WSH multisig': 
            tx_selections=gui_data.tx_selection_types
            first_index=tx_selections.index('P2WSH multisig')
            try:
                result=join_segwit(count, first_index)  # add flag here for p2wsh segwit
            except TypeError:
                ui.output_box.setText('Invalid Input- Please check your input data and try again')
                return
            witness_program.append(result)
            dersigs.append('00')
            print('P2WSH WITNESS',count, witness_program)
            ms_segwit_indexes.append(count)
            count+=1
## change below to class reference- can I do it- i need the -outs- variables and they need to be converted if applicable first
    # can these be simplified at all?
    try:
        outputs=[tx_num_func(ui.numouts_combo.currentIndex()), amount_to_txhex(ui.amount1_box.text()),outs[0], amount_to_txhex(ui.amount2_box.text()),outs[1], amount_to_txhex(ui.amount3_box.text()),outs[2], amount_to_txhex(ui.amount4_box.text()),outs[3], amount_to_txhex(ui.amount5_box.text()),outs[4], amount_to_txhex(ui.amount6_box.text()),outs[5],ui.nlocktime_box.text()]
    except TypeError:
        ui.output_box.setText('Invalid Input- Please check your input data and try again4')
        print('ERROR ~ LINE 918')
        return
    tx_inputs=gui_data.tx_inputs
    if len(witness_program) != 0:
        print('segwit detected')
        prefix=gui_data.segwitprefix
        for txin in segwit_indexs:
            tx_inputs[txin].insert(2,'00')
        for txin in p2pkhindexs:
            tx_inputs[txin].insert(2, dersigs[txin])
        for txin in p2sh_segwit_indexs:
            tx_inputs[txin].insert(2, '171600'+(gui_data.script_pubs[txin])[6:-4])
        if len(p2pkhindexs) != 0:
            outputs.insert((len(outputs)-1),'00')
        if len(ms_segwit_indexes) != 0:
            tx_inputs[ms_segwit_indexes[0]].insert(2,'00')
            witness_program.insert(0,(bytes([len(ms_segwit_indexes)+2]).hex())+'00')
        print('WIT', witness_program)
        print('SEGWIT TX- DERSIGS', witness_program)
        outputs.insert((len(outputs)-1),"".join(witness_program) )
        # using and elif--- does the above function cover all instances- eg what if I have a segwit in and a multisig legacy in?
    elif len(multisig_indexes) != 0:
        print('multisig detected')
        prefix=gui_data.legacy_prefix
        # print('NUMBER OF BLANK MULTISIG SIGS', int(ui.multisig_spinbox.value())-len(multisig_indexes))
        for item in range(0, (int(ui.multisig_spinbox.value()))-len(multisig_indexes)+1):
            multisig_dersigs.insert(0, '00')

        complete_dersig=bytes.fromhex("".join(multisig_dersigs))
        print('COMPLETE DERSIG', complete_dersig.hex())
        final_dersig=len_in_hex(complete_dersig)+complete_dersig
        print('FINAL MULSIG SIG', final_dersig.hex())
        tx_inputs[(multisig_indexes[0])].insert(2, final_dersig.hex())

        for txin in list(range(0, int(ui.numins_combo.currentIndex())+1)):
            print('TXIN NUMBER', txin)
            try:
                tx_inputs[txin].insert(2, dersigs[txin])
            except IndexError:
                pass
    else:     
        print('$$ LEGACY TX')   
        prefix=gui_data.legacy_prefix
        for txin in list(range(0, int(ui.numins_combo.currentIndex())+1)):
            try:
                tx_inputs[txin].insert(2, dersigs[txin])
            except IndexError:
                ui.output_box.setText('Please Select a Transaction Type to Sign1')
                return
    combined_inputs=[y for x in tx_inputs for y in x]
    # print('FINAL_ins',combined_inputs)
    tx_components=[prefix, combined_inputs, outputs]
    input_info=[y for x in tx_components for y in x]
    # print('FINAL input info',input_info)
    signed_items=[(item) for item in input_info if item is not ""]
    ## ADD THIS TO EDU MODE PRINTS
    print('FINAL INPUT LIST',signed_items)

    for item in signed_items:
        try:
            EDU_MODE_OUTPUT.append(item+'\n')
        except TypeError:
            print('Line 1006- ** ERROR ***')
    try:
        signed_tx="".join(signed_items)
    except TypeError:
        ui.output_box.setText('Invalid Input- Please check your input data and try again')
        print('ERROR ~ LINE 1011')
        return
    if ui.education_checkbox.isChecked()==True:
        title_txt='TX DATA'+'\n'
        EDU_MODE_OUTPUT.insert(0,title_txt )
        edu_mode_print="".join(EDU_MODE_OUTPUT)
        ui.output_box.setText(edu_mode_print)
    else:
        ui.output_box.setText(signed_tx)
    # ADD TO EDU MODE
    print('SIGNED TX', signed_tx)
    return signed_tx



#### with both join and the sign functions- make variable names clearer eg multisg2, the multisig and script values
#multisig indexes- does this acually serve a purpose?
# combine these two join fucntions together> is it worth it?
def join_info(script, index):
    gui_data=tx_data()
    tx_selections=gui_data.tx_selection_types
    # multisig_indexs=[]
    # count=0
    # for tx in tx_selections:
    #     if tx=='P2SH multisig':
    #         multisig_indexs.append(count)
    #         count+=1
    try:
        final_index=len(tx_selections) - 1 - tx_selections[::-1].index('P2SH multisig')
        if final_index == script:
            s_value ='multisig_redeemscript'
            print('MULTISIG FINAL VALUE DETECTED')
        else:
            s_value='none'
            print('MULTISIG NON-FINAL DETECTED')
    except ValueError:
        s_value=0
        print('** NOT A MULTISIG ***')

    if script==99:
        s_value='p2sh_redeemscript'


    outs=gui_data.outs
    scriptpubs=gui_data.script_pubs
    insert_points=[ui.inputindex1_box.text, ui.inputindex2_box.text, ui.inputindex3_box.text, ui.inputindex4_box.text, ui.inputindex5_box.text, ui.inputindex6_box.text]
    
    # can these be changes to gui.data.prefix etc?
    prefix=[ui.version_box.text(),tx_num_func(ui.numins_combo.currentIndex())]
    inputs=[[txid_endian(ui.txin1_box.text()), ui.inputindex1_box.text(),ui.sequence1_box.text()],[txid_endian(ui.txin2_box.text()), ui.inputindex2_box.text(),ui.sequence2_box.text()],[txid_endian(ui.txin3_box.text()), ui.inputindex3_box.text(),ui.sequence3_box.text()],[txid_endian(ui.txin4_box.text()), ui.inputindex4_box.text(),ui.sequence4_box.text()],[txid_endian(ui.txin5_box.text()), ui.inputindex5_box.text(),ui.sequence5_box.text()],[txid_endian(ui.txin6_box.text()), ui.inputindex6_box.text(),ui.sequence6_box.text()]]
    
    #same witht his but has the -outs- issue as above
    outputs=[tx_num_func(ui.numouts_combo.currentIndex()),amount_to_txhex(ui.amount1_box.text())+outs[0]+amount_to_txhex(ui.amount2_box.text())+outs[1]+amount_to_txhex(ui.amount3_box.text())+outs[2]+amount_to_txhex(ui.amount4_box.text())+outs[3]+amount_to_txhex(ui.amount5_box.text())+outs[4]+amount_to_txhex(ui.amount6_box.text())+outs[5],ui.nlocktime_box.text(),ui.hashtype_box.text()]
    inputs[index].insert(2, scriptpubs[index])
    #can this be a class level variable?
    
    num_ins=list(range(0, int(ui.numins_combo.currentIndex()+1)))
    other_indexes=[value for value in num_ins if value != index]
    for num in other_indexes:
        inputs[num].insert(2, '00')
        

    combined_inputs=[y for x in inputs for y in x]
    print('Combined ins',combined_inputs)
    tx_components=[prefix, combined_inputs, outputs]
    input_info=[y for x in tx_components for y in x]
    # print('input info',input_info)
    input_list=[(item) for item in input_info if item is not ""]
    ## USE THIS AS THE FIRST EDU MODE PRINT OUT- BREAK IT DOWN INTO COMPONENTS
    print('INPUT LIST',input_list)
    rawtx="".join(input_list)

    ## ADD TO EDU MODE PRINT
    print('RAW TX', rawtx)
    ui.output_box.setText(rawtx)

    if s_value=='none':# I've changed from index to script as second arg- confimr this is right
        dersig=sign_tx(rawtx, script, s_value) #CONFIRM THIS IS SUPPOSED TO BE INDEX
    elif s_value =='multisig_redeemscript':
        dersig=sign_tx(rawtx, script, s_value)
    elif s_value =='p2sh_redeemscript': 
        dersig=sign_tx(rawtx, index, s_value)
    else:
        dersig=sign_tx(rawtx, index)
    return dersig

#multisig indexes- does this acually serve a purpose?
def join_segwit(script, index):
    gui_data=tx_data()
    tx_selections=gui_data.tx_selection_types
    multisig_indexs=[]
    # count=0
    # for tx in tx_selections:
    #     if tx=='P2WSH multisig':
    #         multisig_indexs.append(count)
    #         count+=1
    try:
        final_index=len(tx_selections) - 1 - tx_selections[::-1].index('P2WSH multisig')
        if final_index == script:
            s_value ='redeemscript'
            print('MULTISIG FINAL VALUE DETECTED')
        else:
            s_value ='none'
            print('MULTISIG NON-FINAL DETECTED')
    except ValueError:
        pass

    if tx_selections[index]=='P2SH-P2wPKH':
        s_value='public_point'
    if tx_selections[index]=='P2WPKH':
        s_value='public_point'
    if tx_selections[index]=='P2WSH':
        s_value='redeemscript'

    outs=gui_data.outs
    scriptpubs=gui_data.script_pubs
    input_infos=gui_data.segwit_input_infos
    this_tx_input_infos="".join(input_infos[index])

    # ADD BELOW TO EDU MODE
    print('segwit- ins to hash=',[txid_endian(ui.txin1_box.text())+ui.inputindex1_box.text()+txid_endian(ui.txin2_box.text())+ui.inputindex2_box.text()+txid_endian(ui.txin3_box.text())+ui.inputindex3_box.text()+txid_endian(ui.txin4_box.text())+ui.inputindex4_box.text()+txid_endian(ui.txin5_box.text())+ui.inputindex5_box.text()+txid_endian(ui.txin6_box.text())+ui.inputindex6_box.text()])

    # can these be class levels variables
    hash_ins=hash256(bytes.fromhex(txid_endian(ui.txin1_box.text())+ui.inputindex1_box.text()+txid_endian(ui.txin2_box.text())+ui.inputindex2_box.text()+txid_endian(ui.txin3_box.text())+ui.inputindex3_box.text()+txid_endian(ui.txin4_box.text())+ui.inputindex4_box.text()+txid_endian(ui.txin5_box.text())+ui.inputindex5_box.text()+txid_endian(ui.txin6_box.text())+ui.inputindex6_box.text()))
    hash_sequence=hash256(bytes.fromhex(ui.sequence1_box.text())+bytes.fromhex(ui.sequence2_box.text())+bytes.fromhex(ui.sequence3_box.text())+bytes.fromhex(ui.sequence4_box.text())+bytes.fromhex(ui.sequence5_box.text())+bytes.fromhex(ui.sequence6_box.text()))
    try:
        hash_outs=hash256(bytes.fromhex(amount_to_txhex(ui.amount1_box.text())+outs[0]+amount_to_txhex(ui.amount2_box.text())+outs[1]+amount_to_txhex(ui.amount3_box.text())+outs[2]+amount_to_txhex(ui.amount4_box.text())+outs[3]+amount_to_txhex(ui.amount5_box.text())+outs[4]+amount_to_txhex(ui.amount6_box.text())+outs[5]))
    except ValueError:
        ui.output_box.setText('Invalid Input- Please check your input data and try again')
        print('ERROR ~ LINE 1178')
        return



    input_info=[ui.version_box.text(), hash_ins.hex(),hash_sequence.hex(),this_tx_input_infos, hash_outs.hex(),ui.nlocktime_box.text(), ui.hashtype_box.text()]
    input_list=[(item) for item in input_info if item is not ""]
    
    rawtx="".join(input_list)
    # ADD TO EDU MODE PRINT
    print('RAWTX=',rawtx)
    ui.output_box.setText(rawtx)

    if script == 98:
        s_value='redeemscript'
        dersig='02'+sign_tx(rawtx, index, s_value)

    elif s_value=='none':
        dersig=sign_tx(rawtx, script, s_value)

    elif s_value =='redeemscript':
        dersig=sign_tx(rawtx, script, s_value)

    elif s_value == 'public_point':
        dersig='02'+sign_tx(rawtx, index)[2:]
        dersigpre='02'+sign_tx(rawtx, index)
        dersig1=dersigpre[2:]
    return dersig



def sign_tx(rawtx, index, s_value='public_point'):
    gui_data=tx_data()
    script_pubs=gui_data.script_pubs
    try:
        unsignedtx=bytes.fromhex(rawtx)
    except ValueError:
        ui.output_box.setText('Invalid Input- Please check your input data and try again')
        print('ERROR ~ LINE 1234')
        return
    unsigned_tx_hash = hash256(unsignedtx)
    ## ADD THIS TO EDU MODE PRINTS
    print('UTXHASH',unsigned_tx_hash.hex())
    input_secrets=gui_data.input_secrets

    #first option- does it serve a purpose, should I use elifs here?
    selection=ui.privkey_comboBox.currentIndex()
    # if input_secrets[index]=='00':
    #     return input_secrets[index]
    if selection==0:
         input_secret=scalar_from_wif(input_secrets[index])

    if ui.privkey_comboBox.currentIndex()==1:
        input_secret=scalar_from_hex(input_secrets[index])

    if ui.privkey_comboBox.currentIndex()==2:
        input_secret=int(input_secrets[index])
    private_key = PrivateKey(input_secret)
    public_key_bytes = private_key.point.sec(compressed=True)
    signature = private_key.sign(int.from_bytes(unsigned_tx_hash, byteorder='big'))
    signature_bytes =signature.der() + bytes([SIGHASH_ALL])
    signature_bytes2=bytes([len(signature_bytes)])+signature_bytes
    if s_value=='none':
        dersig_full = signature_bytes2
        print('MULTISIG1- && DERSIG &&', dersig_full)
    elif s_value=="multisig_redeemscript":
        sec2=bytes.fromhex(script_pubs[index])
        tx_selections=list(gui_data.tx_selection_types)
        final_index=len(tx_selections) - 1 - tx_selections[::-1].index('P2SH multisig')
        print('P2SH FINAL INDEX', final_index)
        if final_index>1:
            dersig_full=signature_bytes2+b'\x4c'+sec2
        else:
            dersig_full=signature_bytes2+sec2
    elif s_value=='p2sh_redeemscript':
        sec2=bytes.fromhex(script_pubs[index])
        dersig=signature_bytes2
        dersig_full=bytes([len(dersig+sec2)])+dersig+sec2
    elif s_value=='redeemscript':
        sec2=bytes.fromhex(script_pubs[index])
        dersig=signature_bytes2
        dersig_full=dersig+sec2
    elif s_value== 'public_point':
        sec=private_key.point.sec()
        sec2=bytes([len(sec)])+sec
        dersig=signature_bytes2+sec2
         ## ADD THIS TO EDU MODE PRINTS
        # print('NON MULTISIG- && DERSIG &&', dersig)
         ## ADD THIS TO EDU MODE PRINTS
        print('***SEC2***', sec2.hex())
        dersig_full=bytes([len(dersig)])+dersig
    print('DERSIG FULL',dersig_full.hex())
    return dersig_full.hex()



def tx_num_func(data):
    num_data=['01','02','03','04','05','06', '07', '08']
    selection=num_data[data]
    return selection

def amount_to_txhex(amount):  #concatanate this abit- use list comprehension?s
    if amount == '':
        return ''
    else:
        amount_flt=float(amount)
        amount_int=int(amount_flt*100000000)
        amount_hex=format(amount_int, 'x')
        amount_final=amount_hex.rjust(16, '0')
        tx_bytes=bytes(reversed(bytes.fromhex(amount_final)))
        return (tx_bytes.hex())



def txid_endian(txid):
    input_bytes=bytes(reversed(bytes.fromhex(txid)))
    return input_bytes.hex()


#move this to address functions?
def scalar_from_wif(priv_key):
    num = 0
    for c in priv_key.encode('ascii'):
        num *= 58
        num += BASE58.index(c)
    hex_secret=hex(num)[2:]
    combined = bytes.fromhex(hex_secret)
    checksum = combined[-4:]
    if hash256(combined[:-4])[:4] != checksum:
        raise RuntimeError('bad address: {} {}'.format(checksum, hash256(combined)[:4]))
    hex_secret_trimmed=codecs.encode(combined[1:-5], 'hex')
    hex_secret_trimmed_str=hex_secret_trimmed.decode("utf-8")
     ## ADD THIS TO EDU MODE PRINTS
    print('HEX SECRET=',hex_secret_trimmed_str)
    return int(hex_secret_trimmed_str, 16)

#move this to address functions?
def scalar_from_hex(hexstring):
    return int(hexstring, 16)


#move this to address functions?
def address_to_scriptpub(outs):
    scriptpub_list=[]
    for item in outs:
        if item[:2]=='tb':
            hex_chars=decode(item[:2], item)[1]
            hex_chars_list=[]
            for i in hex_chars:
                hex_chars_list.append(bytes([i]).hex())
                h256="".join(hex_chars_list)
            h256len=str(int((int(bytes([len(h256)]).hex())/2)))
            print('h256len', h256len)
            scriptpub_raw='00'+h256len+h256
            scriptpub=bytes([len(bytes.fromhex(scriptpub_raw))]).hex()+scriptpub_raw

        if item[:2]=='bc':
            hex_chars=decode(item[:2], item)[1]
            hex_chars_list=[]
            for i in hex_chars:
                hex_chars_list.append(bytes([i]).hex())
                h256="".join(hex_chars_list)
            h256len=str(int((int(bytes([len(h256)]).hex())/2)))
            print('h256len', h256len)
            scriptpub_raw='00'+h256len+h256
            scriptpub=bytes([len(bytes.fromhex(scriptpub_raw))]).hex()+scriptpub_raw
        
        if item[:1]=='3':# AND 2
            scriptpub='17a914'+decode_base58(item).hex()+'87'

        if item[:1]=='2':# AND 2
            scriptpub='17a914'+decode_base58(item).hex()+'87'

        if item[:1]=='m': #can m and n be put into one value to check for?
            try:
                scriptpub='1976a914'+decode_base58(item).hex()+'88ac'
            except ValueError:
                ui.output_box.setText('Invalid Input- Please check your input data and try again')
                return

        if item[:1]=='n':
            try:
                scriptpub='1976a914'+decode_base58(item).hex()+'88ac'
            except ValueError:
                ui.output_box.setText('Invalid Input- Please check your input data and try again')
                return

        if item[:1]=='1':
            try:
                scriptpub='1976a914'+decode_base58(item).hex()+'88ac'
            except ValueError:
                ui.output_box.setText('Invalid Input- Please check your input data and try again')
                return
        if item=='':
            scriptpub=''


        scriptpub_list.append(scriptpub)

    return scriptpub_list

def int_to_nlocktime():
    try:
        block=int(ui.currentblock_box.text())
    except ValueError:
        ui.output_box.setText('Invalid Input- Please check your input data and try again')
        return

    block_hex=bytes(reversed(block.to_bytes(4, 'big')))
    print(block_hex)
    ui.nlocktime_box.setText(block_hex.hex())
    return block_hex


def len_in_hex(item):
    length=len(item)
    if length > 4294967295:
        return b'\xFF' + (length).to_bytes(8, byteorder='little')
    elif length > 65535:
        return b'\xFE' + (length).to_bytes(4, byteorder='little')
    elif length > 252:
        return b'\xFD'+(length).to_bytes(2, byteorder='little')
    else:
        return length.to_bytes(1, byteorder='little')




def tx_select_func(index):
    print('SELEC ACT', index)
    inputs=[ui.txtype_combobox_1,ui.txtype_combobox_2,ui.txtype_combobox_3,ui.txtype_combobox_4,ui.txtype_combobox_5,ui.txtype_combobox_6]
    selection=inputs[index-1].currentText()


    ## refactor- delete the outpub boxes below and adjust list indess in conditions below

    boxes=[[ui.txinamount_box1,ui.inputindex1_box,ui.txin1_box,ui.scriptpub1_box,ui.sequence1_box,ui.amount1_box,ui.scriptout1_box,ui.privkey1_box],
            [ui.txinamount_box2,ui.inputindex2_box,ui.txin2_box,ui.scriptpub2_box,ui.sequence2_box,ui.amount2_box,ui.scriptout2_box,ui.privkey2_box],
            [ui.txinamount_box3,ui.inputindex3_box,ui.txin3_box,ui.scriptpub3_box,ui.sequence3_box,ui.amount3_box,ui.scriptout3_box,ui.privkey3_box],
            [ui.txinamount_box4,ui.inputindex4_box,ui.txin4_box,ui.scriptpub4_box,ui.sequence4_box,ui.amount4_box,ui.scriptout4_box,ui.privkey4_box],
            [ui.txinamount_box5,ui.inputindex5_box,ui.txin5_box,ui.scriptpub5_box,ui.sequence5_box,ui.amount5_box,ui.scriptout5_box,ui.privkey5_box],
            [ui.txinamount_box6,ui.inputindex6_box,ui.txin6_box,ui.scriptpub6_box,ui.sequence6_box,ui.amount6_box,ui.scriptout6_box,ui.privkey6_box]]

    if selection=='N/A':
        i=boxes[index-1]
        i[0].setDisabled(True)
        i[1].setDisabled(True)
        i[2].setDisabled(True)
        i[3].setDisabled(True)
        i[4].setDisabled(True)
        i[7].setDisabled(True)

    elif selection=='P2PKH':
        i=boxes[index-1]
        i[0].setDisabled(True)
        i[1].setDisabled(False)
        i[2].setDisabled(False)
        i[3].setDisabled(False)
        i[4].setDisabled(False)
        i[7].setDisabled(False)
    
    elif selection=='P2SH':
        i=boxes[index-1]
        i[0].setDisabled(True)
        i[1].setDisabled(False)
        i[2].setDisabled(False)
        i[3].setDisabled(False)
        i[4].setDisabled(False)
        i[7].setDisabled(False)

    elif selection=='P2SH multisig':
        i=boxes[index-1]
        i[0].setDisabled(True)
        i[1].setDisabled(False)
        i[2].setDisabled(False)
        i[3].setDisabled(False)
        i[4].setDisabled(False)
        i[7].setDisabled(False)

    else:
        i=boxes[index-1]
        i[0].setDisabled(False)
        i[1].setDisabled(False)
        i[2].setDisabled(False)
        i[3].setDisabled(False)
        i[4].setDisabled(False)
        i[7].setDisabled(False)
    return selection

def ins_activate(total):
    boxes=[[ui.txinamount_box1,ui.inputindex1_box,ui.txin1_box,ui.scriptpub1_box,ui.sequence1_box,ui.privkey1_box],
        [ui.txinamount_box2,ui.inputindex2_box,ui.txin2_box,ui.scriptpub2_box,ui.sequence2_box,ui.privkey2_box],
        [ui.txinamount_box3,ui.inputindex3_box,ui.txin3_box,ui.scriptpub3_box,ui.sequence3_box,ui.privkey3_box],
        [ui.txinamount_box4,ui.inputindex4_box,ui.txin4_box,ui.scriptpub4_box,ui.sequence4_box,ui.privkey4_box],
        [ui.txinamount_box5,ui.inputindex5_box,ui.txin5_box,ui.scriptpub5_box,ui.sequence5_box,ui.privkey5_box],
        [ui.txinamount_box6,ui.inputindex6_box,ui.txin6_box,ui.scriptpub6_box,ui.sequence6_box,ui.privkey6_box]]
    for outlist in boxes:
        for item in outlist:
            item.setDisabled(True)
    outs_list=range(0,total)
    for out in outs_list:
        i=boxes[out]
        i[0].setDisabled(False)
        i[1].setDisabled(False)
        i[2].setDisabled(False)
        i[3].setDisabled(False)
        i[4].setDisabled(False)
        i[5].setDisabled(False)


def outs_activate(total):
    boxes=[[ui.amount1_box,ui.scriptout1_box],[ui.amount2_box,ui.scriptout2_box],[ui.amount3_box,ui.scriptout3_box],[ui.amount4_box,ui.scriptout4_box],
            [ui.amount5_box,ui.scriptout5_box],[ui.amount6_box,ui.scriptout6_box]]
    for outlist in boxes:
        for item in outlist:
            item.setDisabled(True)
    outs_list=range(0,total)
    for out in outs_list:
        i=boxes[out]
        i[0].setDisabled(False)
        i[1].setDisabled(False)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    splash_pix = QPixmap('test_splash.png')
    splash = QtWidgets.QSplashScreen(splash_pix)
    splash.setMask(splash_pix.mask())
    splash.show()
    time.sleep(1)
    app.processEvents()



    Libre_Tx = QtWidgets.QDialog()
    ui = Ui_Libre_Tx()
    ui.setupUi(Libre_Tx)
    time.sleep(1)
    Libre_Tx.show()
    splash.finish(Libre_Tx)
    sys.exit(app.exec_())
