from PyQt5.QtCore import Qt, QTimer, QTime

def timer_test(self):
  global time
  time = QTime(0, 0, 15)
  self.timer = QTimer
  self.timer.timeout.connect(self.timer1Event)
  self.timer.start(1000)
  
def timer_sits(self):
  global time
  time = QTime(0,0 30)
  self.timer = QTimer()
  self.timer.timeout.connect(self.timer2Event)
  self.timer.start(1500)
  
  def timer_final(self):
  global time
  time = QTime(0,0 30)
  self.timer = QTimer()
  self.timer.timeout.connect(self.timer3Event)
  self.timer.start(1000)
  
  def timer1Event(self):
    global time
    time = timeaddSecs(-1)
    self.text_timer.setText(time.toString('hh:mm:ss'))
    self.text_timer.setFont('Times', 36, QFont.Bold))
    self.text_timersetStyleSheet('color: rgb(0, 0, 0)')
    if time.toString('hh:mm:ss') == "00:00:00":
      self.timer.stop()
      
  def timer2Event(self):
    c
