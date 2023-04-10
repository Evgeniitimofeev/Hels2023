from PyQt5.QtCore import Qt
from PyQt5.QtCore import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QGroupBox, QRadioButton,  QPushButton, QLabel, QListWidget, QLineEdit)

from instr import *

class FinalWin( QWidget)
  def __init__(self):
    super().__init__()
    self.initUT()
    self.set_appear()
    self.show()
  def initUT():
    self.workh_text = QLabel(txt_workheart)
    self.index_text = QLabel(txt_index)
    self.layout_line = QVBoxLayout()
    self.layout_line.addWidet(self.index_text, alignment = Qt.AlignCenter)
    self.layout_line.addWidet(self.workh_text
