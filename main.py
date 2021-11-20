import sys

from UI import Ui_Form
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor
from random import randint as rnd


class Example(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_paint.clicked.connect(self.paint)
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def paintEvent(self, event):
        if self.do_paint:
            painter = QPainter()
            painter.begin(self)
            self.draw_circle(painter)
            painter.end()

    def draw_circle(self, painter):
        painter.setBrush(QColor(rnd(0, 255), rnd(0, 255), rnd(0, 255)))
        radius = rnd(10, 200)
        painter.drawEllipse(100, 100, radius, radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())