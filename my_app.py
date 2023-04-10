from PyQt5.QtCore import Qt
from PyQt5.Qtwidgats import (QApplication, Qwidgets, QHBoxLayout, OGroupBox, QRadioButton, QRusButton, QLadel,QLisWidget, QLneEdit)

from instr  import *
from second_win import *

class MainWin(QWidget):
  def __init__(self):
    super().__init__()
    
    self.initUT() #создаём и настраиваеь
    self.connects()
    self.set_appear()
    self.show()
  def initUT(self):
    self.btn_next = QPushButton(txt_next, self)
    self.hello_text = QLabel(txt_hello)
    self.instruction = QLabel(txt_instruction)
    self.layout_line = QVBoxLayout()
    self.layout_line.addWidget(self.hello_text, alignment = Qt.AlignLeft)
    self.layout_line.addWidget(self.instruction, alignment = Qt.AlignLeft)
    self.layout_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)
    self.setLayout(self.layout_line)
  def next_click(self):
    self.tw = Testwin()
    self.hide()
  def set.appear(self):
    self.setWindowTitle(txt_title)
    self.resize(win_width, win_height)
    self.move(win_x, win_y)
    
app = QApplication([])
mw MainWin()
app.exec_()
  

