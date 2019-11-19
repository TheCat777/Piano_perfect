import sys
from pathlib import Path

from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

BASE_DIR = Path(__file__).resolve().parent

class Example(QWidget):
    def __init__(self):
        super().__init__()
        QtWidgets.qApp.installEventFilter(self)
        # переменные, отвечающие за звук
        self.sound = 100
        self.Butsound = 1

        self.player = QMediaPlayer()
        self.player.setVolume(100)

        self.player1 = QMediaPlayer()
        self.player1.setVolume(100)

        self.player2 = QMediaPlayer()
        self.player2.setVolume(100)

        self.player3 = QMediaPlayer()
        self.player3.setVolume(100)

        self.player4 = QMediaPlayer()
        self.player4.setVolume(100)

        self.player5 = QMediaPlayer()
        self.player5.setVolume(100)

        self.player6 = QMediaPlayer()
        self.player6.setVolume(100)

        self.player7 = QMediaPlayer()
        self.player7.setVolume(100)

        self.player8 = QMediaPlayer()
        self.player8.setVolume(100)

        self.player9 = QMediaPlayer()
        self.player9.setVolume(100)

        self.player10 = QMediaPlayer()
        self.player10.setVolume(100)

        self.player11 = QMediaPlayer()
        self.player11.setVolume(100)

        self.player12 = QMediaPlayer()
        self.player12.setVolume(100)

        self.player13 = QMediaPlayer()
        self.player13.setVolume(100)

        self.player14 = QMediaPlayer()
        self.player14.setVolume(100)

        self.player15 = QMediaPlayer()
        self.player15.setVolume(100)

        self.player16 = QMediaPlayer()
        self.player16.setVolume(100)

        self.player17 = QMediaPlayer()
        self.player17.setVolume(100)

        self.player18 = QMediaPlayer()
        self.player18.setVolume(100)

        self.player19 = QMediaPlayer()
        self.player19.setVolume(100)

        self.player20 = QMediaPlayer()
        self.player20.setVolume(100)

        self.player21 = QMediaPlayer()
        self.player21.setVolume(100)

        self.player22 = QMediaPlayer()
        self.player22.setVolume(100)

        self.player23 = QMediaPlayer()
        self.player23.setVolume(100)

        self.player24 = QMediaPlayer()
        self.player24.setVolume(100)

        self.player25 = QMediaPlayer()
        self.player25.setVolume(100)

        self.player26 = QMediaPlayer()
        self.player26.setVolume(100)

        self.player27 = QMediaPlayer()
        self.player27.setVolume(100)

        self.player28 = QMediaPlayer()
        self.player28.setVolume(100)

        self.player29 = QMediaPlayer()
        self.player29.setVolume(100)

        self.player30 = QMediaPlayer()
        self.player30.setVolume(100)

        self.player31 = QMediaPlayer()
        self.player31.setVolume(100)

        self.player32 = QMediaPlayer()
        self.player32.setVolume(100)

        self.player33 = QMediaPlayer()
        self.player33.setVolume(100)

        self.player34 = QMediaPlayer()
        self.player34.setVolume(100)

        self.player35 = QMediaPlayer()
        self.player35.setVolume(100)

        self.player36 = QMediaPlayer()
        self.player36.setVolume(100)

        self.player37 = QMediaPlayer()
        self.player37.setVolume(100)

        self.player38 = QMediaPlayer()
        self.player38.setVolume(100)

        self.player39 = QMediaPlayer()
        self.player39.setVolume(100)

        self.player40 = QMediaPlayer()
        self.player40.setVolume(100)

        self.player41 = QMediaPlayer()
        self.player41.setVolume(100)

        self.player42 = QMediaPlayer()
        self.player42.setVolume(100)

        self.player43 = QMediaPlayer()
        self.player43.setVolume(100)

        self.player44 = QMediaPlayer()
        self.player44.setVolume(100)

        self.player45 = QMediaPlayer()
        self.player45.setVolume(100)

        self.player46 = QMediaPlayer()
        self.player46.setVolume(100)

        self.player47 = QMediaPlayer()
        self.player47.setVolume(100)

        self.player48 = QMediaPlayer()
        self.player48.setVolume(100)

        self.player49 = QMediaPlayer()
        self.player49.setVolume(100)

        self.player50 = QMediaPlayer()
        self.player50.setVolume(100)

        self.player51 = QMediaPlayer()
        self.player51.setVolume(100)

        self.player52 = QMediaPlayer()
        self.player52.setVolume(100)

        self.player53 = QMediaPlayer()
        self.player53.setVolume(100)

        self.player54 = QMediaPlayer()
        self.player54.setVolume(100)

        self.player55 = QMediaPlayer()
        self.player55.setVolume(100)

        self.player56 = QMediaPlayer()
        self.player56.setVolume(100)

        self.player57 = QMediaPlayer()
        self.player57.setVolume(100)

        self.player58 = QMediaPlayer()
        self.player58.setVolume(100)

        self.player59 = QMediaPlayer()
        self.player59.setVolume(100)

        self.player60 = QMediaPlayer()
        self.player60.setVolume(100)

        self.player61 = QMediaPlayer()
        self.player61.setVolume(100)

        self.player62 = QMediaPlayer()
        self.player62.setVolume(100)

        self.player63 = QMediaPlayer()
        self.player63.setVolume(100)

        self.player64 = QMediaPlayer()
        self.player64.setVolume(100)

        self.player65 = QMediaPlayer()
        self.player65.setVolume(100)

        self.player66 = QMediaPlayer()
        self.player66.setVolume(100)

        self.player67 = QMediaPlayer()
        self.player67.setVolume(100)

        self.player68 = QMediaPlayer()
        self.player68.setVolume(100)

        self.player69 = QMediaPlayer()
        self.player69.setVolume(100)

        self.player70 = QMediaPlayer()
        self.player70.setVolume(100)

        self.player71 = QMediaPlayer()
        self.player71.setVolume(100)

        self.player72 = QMediaPlayer()
        self.player72.setVolume(100)

        self.player73 = QMediaPlayer()
        self.player73.setVolume(100)

        self.player74 = QMediaPlayer()
        self.player74.setVolume(100)

        self.player75 = QMediaPlayer()
        self.player75.setVolume(100)

        self.player76 = QMediaPlayer()
        self.player76.setVolume(100)

        self.player77 = QMediaPlayer()
        self.player77.setVolume(100)

        self.player78 = QMediaPlayer()
        self.player78.setVolume(100)

        self.player79 = QMediaPlayer()
        self.player79.setVolume(100)

        self.player80 = QMediaPlayer()
        self.player80.setVolume(100)

        self.player81 = QMediaPlayer()
        self.player81.setVolume(100)

        self.player82 = QMediaPlayer()
        self.player82.setVolume(100)

        self.player83 = QMediaPlayer()
        self.player83.setVolume(100)

        self.player84 = QMediaPlayer()
        self.player84.setVolume(100)

        self.player85 = QMediaPlayer()
        self.player85.setVolume(100)

        self.player86 = QMediaPlayer()
        self.player86.setVolume(100)

        self.player87 = QMediaPlayer()
        self.player87.setVolume(100)

        # переменные для мультиустройства
        self.SizeWhite = 100
        self.SizeWindowX = QApplication.desktop().width()
        self.SizeWindowY = QApplication.desktop().height()
        self.SizeBut = 100

        # переменные, отвечающие за видимый диапозон клавиатуры
        self.FirstKey = 21
        self.LastKey = self.FirstKey + (self.SizeWindowX + 100) // 100
        
        self.initUI()

    def initUI(self):
        # настройка переменных
        windowx = self.SizeWindowX
        windowy = self.SizeWindowY
        butsize = self.SizeBut
        # создание окна
        self.setGeometry(0, 0, windowx, windowy)
        self.setWindowTitle('Perfect Piano 1.0')
        # картинка приложения
        self.setWindowIcon(QtGui.QIcon('icon.png'))

        #задний фон
        self.background = QPushButton("", self)
        self.background.resize(windowx, windowy)
        self.background.move(0, 0)
        self.background.setIcon(QIcon("background.png"))
        self.background.setIconSize(QSize(6000, 4000))

        # создание окна "Информация"
        _translate = QtCore.QCoreApplication.translate
        self.info = QPushButton('', self)
        self.info.resize(butsize, butsize)
        self.info.move(0, 0)
        self.info.setIcon(QIcon("information.png"))
        self.info.setIconSize(QSize(100, 100))
        self.info.setToolTip("информация")
        self.info.clicked.connect(self.information)

        # создание окна Звук
        self.zvyk = QPushButton("", self)
        self.zvyk.resize(butsize, butsize)
        self.zvyk.move(windowx - butsize, 0)
        self.zvyk.setToolTip("изменить звук")
        self.zvyk.setIcon(QIcon("sound.png"))
        self.zvyk.setIconSize(QSize(100, 100))
        self.zvyk.clicked.connect(self.ButtonSound)

        # Кнопка влево
        self.left = QPushButton("", self)
        self.left.resize(butsize, butsize / 2)
        self.left.move(0, 250)
        self.left.setIcon(QIcon("left.png"))
        self.left.setIconSize(QSize(100, 50))
        self.left.clicked.connect(self.GoLeft)

        # Кнопка вправо
        self.right = QPushButton("", self)
        self.right.resize(butsize, butsize / 2)
        self.right.setIcon(QIcon("right.png"))
        self.right.move(windowx - butsize, 250)
        self.right.setIconSize(QSize(100, 50))
        self.right.clicked.connect(self.GoRight)
        
        # Индикатор перемещения(сама клавиатура)
        self.paint = QPushButton("", self)
        self.paint.setIcon(QIcon("paint.jpg"))
        self.paint.setIconSize(QSize(980, 113))
        self.paint.move(windowx / 2 - 500, 100)

        # кнопка выбора звука фортепьяно
        self.piano = QPushButton('', self)
        self.piano.setIcon(QIcon("piano.png"))
        self.piano.setIconSize(QSize(50, 50))
        self.piano.resize(50, 50)
        self.piano.move(windowx / 2 - 50, 0)
        self.piano.clicked.connect(self.DPiano)

        # рамка вокруг иконки
        self.frame1 = QLabel('', self)
        self.frame1.move(windowx / 2 - 50, 0)
        self.frame1.setStyleSheet('border-style: solid; border-width: 5px; border-color: red;')
        self.frame1.resize(50, 50)

        # кнопка импортирования других звуков
        self.plus = QPushButton('', self)
        self.plus.setIcon(QIcon("plus.png"))
        self.plus.setIconSize(QSize(50, 50))
        self.plus.resize(50, 50)
        self.plus.clicked.connect(self.Add)
        self.plus.move(windowx / 2, 0)

        # Индикатор перемещения(рамка)
        self.frame = QLabel('', self)
        self.frame.move(windowx / 2 - 485 + 392.7, 100)
        self.frame.setStyleSheet('border-style: solid; border-width: 5px; border-color: red;')
        self.frame.resize((self.LastKey - self.FirstKey) * 18.7, 122)

        # белые клавиши клавиатуры
        self.kl1 = QPushButton("", self)
        self.kl1.resize(100, 400)
        self.kl1.move(-2140, windowy - 420)
        self.kl1.clicked.connect(self.dkl1)
        self.kl1.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl2 = QPushButton("", self)
        self.kl2.resize(100, 400)
        self.kl2.clicked.connect(self.dkl2)
        self.kl2.move(-2040, windowy - 420)
        self.kl2.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl3 = QPushButton("", self)
        self.kl3.resize(100, 400)
        self.kl3.clicked.connect(self.dkl3)
        self.kl3.move(-1940, windowy - 420)
        self.kl3.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl4 = QPushButton("", self)
        self.kl4.resize(100, 400)
        self.kl4.move(-1840, windowy - 420)
        self.kl4.clicked.connect(self.dkl4)
        self.kl4.setStyleSheet("""
    QPushButton:!hover { background-color: white }

    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl5 = QPushButton("", self)
        self.kl5.resize(100, 400)
        self.kl5.move(-1740, windowy - 420)
        self.kl5.clicked.connect(self.dkl5)
        self.kl5.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl6 = QPushButton("", self)
        self.kl6.resize(100, 400)
        self.kl6.move(-1640, windowy - 420)
        self.kl6.clicked.connect(self.dkl6)
        self.kl6.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl7 = QPushButton("", self)
        self.kl7.resize(100, 400)
        self.kl7.move(-1540, windowy - 420)
        self.kl7.clicked.connect(self.dkl7)
        self.kl7.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl8 = QPushButton("", self)
        self.kl8.resize(100, 400)
        self.kl8.move(-1440, windowy - 420)
        self.kl8.clicked.connect(self.dkl8)
        self.kl8.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl9 = QPushButton("", self)
        self.kl9.resize(100, 400)
        self.kl9.move(-1340, windowy - 420)
        self.kl9.clicked.connect(self.dkl9)
        self.kl9.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl10 = QPushButton("", self)
        self.kl10.resize(100, 400)
        self.kl10.move(-1240, windowy - 420)
        self.kl10.clicked.connect(self.dkl10)
        self.kl10.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl11 = QPushButton("", self)
        self.kl11.resize(100, 400)
        self.kl11.move(-1140, windowy - 420)
        self.kl11.clicked.connect(self.dkl11)
        self.kl11.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl12 = QPushButton("", self)
        self.kl12.resize(100, 400)
        self.kl12.move(-1040, windowy - 420)
        self.kl12.clicked.connect(self.dkl12)
        self.kl12.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl13 = QPushButton("", self)
        self.kl13.resize(100, 400)
        self.kl13.clicked.connect(self.dkl13)
        self.kl13.move(-940, windowy - 420)
        self.kl13.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl14 = QPushButton("", self)
        self.kl14.resize(100, 400)
        self.kl14.clicked.connect(self.dkl14)
        self.kl14.move(-840, windowy - 420)
        self.kl14.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl15 = QPushButton("", self)
        self.kl15.resize(100, 400)
        self.kl15.move(-740, windowy - 420)
        self.kl15.clicked.connect(self.dkl15)
        self.kl15.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl16 = QPushButton("", self)
        self.kl16.resize(100, 400)
        self.kl16.move(-640, windowy - 420)
        self.kl16.clicked.connect(self.dkl16)
        self.kl16.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl17 = QPushButton("", self)
        self.kl17.resize(100, 400)
        self.kl17.move(-540, windowy - 420)
        self.kl17.clicked.connect(self.dkl17)
        self.kl17.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl18 = QPushButton("", self)
        self.kl18.resize(100, 400)
        self.kl18.move(-440, windowy - 420)
        self.kl18.clicked.connect(self.dkl18)
        self.kl18.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl19 = QPushButton("", self)
        self.kl19.resize(100, 400)
        self.kl19.move(-340, windowy - 420)
        self.kl19.clicked.connect(self.dkl19)
        self.kl19.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl20 = QPushButton("", self)
        self.kl20.resize(100, 400)
        self.kl20.clicked.connect(self.dkl20)
        self.kl20.move(-240, windowy - 420)
        self.kl20.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl21 = QPushButton("", self)
        self.kl21.resize(100, 400)
        self.kl21.move(-140, windowy - 420)
        self.kl21.clicked.connect(self.dkl21)
        self.kl21.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl22 = QPushButton("", self)
        self.kl22.resize(100, 400)
        self.kl22.move(-40, windowy - 420)
        self.kl22.clicked.connect(self.dkl22)
        self.kl22.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl23 = QPushButton("", self)
        self.kl23.resize(100, 400)
        self.kl23.move(60, windowy - 420)
        self.kl23.clicked.connect(self.dkl23)
        self.kl23.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl24 = QPushButton("", self)
        self.kl24.resize(100, 400)
        self.kl24.clicked.connect(self.dkl24)
        self.kl24.move(160, windowy - 420)
        self.kl24.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl25 = QPushButton("", self)
        self.kl25.resize(100, 400)
        self.kl25.clicked.connect(self.dkl25)
        self.kl25.move(260, windowy - 420)
        self.kl25.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl26 = QPushButton("", self)
        self.kl26.resize(100, 400)
        self.kl26.move(360, windowy - 420)
        self.kl26.clicked.connect(self.dkl26)
        self.kl26.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl27 = QPushButton("", self)
        self.kl27.resize(100, 400)
        self.kl27.move(460, windowy - 420)
        self.kl27.clicked.connect(self.dkl27)
        self.kl27.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl28 = QPushButton("", self)
        self.kl28.resize(100, 400)
        self.kl28.move(560, windowy - 420)
        self.kl28.clicked.connect(self.dkl28)
        self.kl28.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl29 = QPushButton("", self)
        self.kl29.resize(100, 400)
        self.kl29.move(660, windowy - 420)
        self.kl29.clicked.connect(self.dkl29)
        self.kl29.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl30 = QPushButton("", self)
        self.kl30.resize(100, 400)
        self.kl30.move(760, windowy - 420)
        self.kl30.clicked.connect(self.dkl30)
        self.kl30.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl31 = QPushButton("", self)
        self.kl31.resize(100, 400)
        self.kl31.move(860, windowy - 420)
        self.kl31.clicked.connect(self.dkl31)
        self.kl31.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl32 = QPushButton("", self)
        self.kl32.resize(100, 400)
        self.kl32.move(960, windowy - 420)
        self.kl32.clicked.connect(self.dkl33)
        self.kl32.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl33 = QPushButton("", self)
        self.kl33.resize(100, 400)
        self.kl33.move(1060, windowy - 420)
        self.kl33.clicked.connect(self.dkl33)
        self.kl33.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl34 = QPushButton("", self)
        self.kl34.resize(100, 400)
        self.kl34.move(1160, windowy - 420)
        self.kl34.clicked.connect(self.dkl34)
        self.kl34.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl35 = QPushButton("", self)
        self.kl35.resize(100, 400)
        self.kl35.clicked.connect(self.dkl35)
        self.kl35.move(1260, windowy - 420)
        self.kl35.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl36 = QPushButton("", self)
        self.kl36.resize(100, 400)
        self.kl36.clicked.connect(self.dkl36)
        self.kl36.move(1360, windowy - 420)
        self.kl36.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl37 = QPushButton("", self)
        self.kl37.resize(100, 400)
        self.kl37.clicked.connect(self.dkl37)
        self.kl37.move(1460, windowy - 420)
        self.kl37.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl38 = QPushButton("", self)
        self.kl38.resize(100, 400)
        self.kl38.clicked.connect(self.dkl38)
        self.kl38.move(1560, windowy - 420)
        self.kl38.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl39 = QPushButton("", self)
        self.kl39.resize(100, 400)
        self.kl39.clicked.connect(self.dkl39)
        self.kl39.move(1660, windowy - 420)
        self.kl39.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl40 = QPushButton("", self)
        self.kl40.resize(100, 400)
        self.kl40.clicked.connect(self.dkl40)
        self.kl40.move(1760, windowy - 420)
        self.kl40.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl41 = QPushButton("", self)
        self.kl41.resize(100, 400)
        self.kl41.clicked.connect(self.dkl41)
        self.kl41.move(1860, windowy - 420)
        self.kl41.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl42 = QPushButton("", self)
        self.kl42.resize(100, 400)
        self.kl42.clicked.connect(self.dkl42)
        self.kl42.move(1960, windowy - 420)
        self.kl42.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl43 = QPushButton("", self)
        self.kl43.resize(100, 400)
        self.kl43.clicked.connect(self.dkl43)
        self.kl43.move(2060, windowy - 420)
        self.kl43.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl44 = QPushButton("", self)
        self.kl44.resize(100, 400)
        self.kl44.clicked.connect(self.dkl44)
        self.kl44.move(2160, windowy - 420)
        self.kl44.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl45 = QPushButton("", self)
        self.kl45.resize(100, 400)
        self.kl45.clicked.connect(self.dkl45)
        self.kl45.move(2260, windowy - 420)
        self.kl45.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl46 = QPushButton("", self)
        self.kl46.resize(100, 400)
        self.kl46.clicked.connect(self.dkl46)
        self.kl46.move(2360, windowy - 420)
        self.kl46.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl47 = QPushButton("", self)
        self.kl47.resize(100, 400)
        self.kl47.clicked.connect(self.dkl47)
        self.kl47.move(2460, windowy - 420)
        self.kl47.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl48 = QPushButton("", self)
        self.kl48.resize(100, 400)
        self.kl48.clicked.connect(self.dkl48)
        self.kl48.move(2560, windowy - 420)
        self.kl48.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl49 = QPushButton("", self)
        self.kl49.resize(100, 400)
        self.kl49.move(2660, windowy - 420)
        self.kl49.clicked.connect(self.dkl49)
        self.kl49.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl50 = QPushButton("", self)
        self.kl50.resize(100, 400)
        self.kl50.move(2760, windowy - 420)
        self.kl50.clicked.connect(self.dkl50)
        self.kl50.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl51 = QPushButton("", self)
        self.kl51.resize(100, 400)
        self.kl51.clicked.connect(self.dkl51)
        self.kl51.move(2860, windowy - 420)
        self.kl51.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.kl52 = QPushButton("", self)
        self.kl52.resize(100, 400)
        self.kl52.clicked.connect(self.dkl52)
        self.kl52.move(2960, windowy - 420)
        self.kl52.setStyleSheet("""
    QPushButton:!hover { background-color: white }
    QPushButton:pressed { background-color: rgb(0, 255, 0); }
""")

        self.bl1 = QPushButton("", self)
        self.bl1.resize(50, 250)
        self.bl1.clicked.connect(self.dbl1)
        self.bl1.move(-2065, windowy - 420)
        self.bl1.setStyleSheet("""
            QPushButton:!hover { background-color: black }
            QPushButton:pressed { background-color: darkgreen; }
        """)

        self.bl2 = QPushButton("", self)
        self.bl2.resize(50, 250)
        self.bl2.move(-1865, windowy - 420)
        self.bl2.clicked.connect(self.dbl2)
        self.bl2.setStyleSheet("""
            QPushButton:!hover { background-color: black }
            QPushButton:pressed { background-color: darkgreen; }
        """)

        self.bl3 = QPushButton("", self)
        self.bl3.resize(50, 250)
        self.bl3.move(-1765, windowy - 420)
        self.bl3.clicked.connect(self.dbl3)
        self.bl3.setStyleSheet("""
            QPushButton:!hover { background-color: black }
            QPushButton:pressed { background-color: darkgreen; }
        """)

        self.bl4 = QPushButton("", self)
        self.bl4.resize(50, 250)
        self.bl4.move(-1565, windowy - 420)
        self.bl4.clicked.connect(self.dbl4)
        self.bl4.setStyleSheet("""
            QPushButton:!hover { background-color: black }
            QPushButton:pressed { background-color: darkgreen; }
        """)

        self.bl5 = QPushButton("", self)
        self.bl5.resize(50, 250)
        self.bl5.clicked.connect(self.dbl5)
        self.bl5.move(-1465, windowy - 420)
        self.bl5.setStyleSheet("""
            QPushButton:!hover { background-color: black }
            QPushButton:pressed { background-color: darkgreen; }
        """)

        self.bl6 = QPushButton("", self)
        self.bl6.resize(50, 250)
        self.bl6.clicked.connect(self.dbl6)
        self.bl6.move(-1365, windowy - 420)
        self.bl6.setStyleSheet("""
            QPushButton:!hover { background-color: black }
            QPushButton:pressed { background-color: darkgreen; }
        """)

        self.bl7 = QPushButton("", self)
        self.bl7.resize(50, 250)
        self.bl7.clicked.connect(self.dbl7)
        self.bl7.move(-1165, windowy - 420)
        self.bl7.setStyleSheet("""
            QPushButton:!hover { background-color: black }
            QPushButton:pressed { background-color: darkgreen; }
        """)

        self.bl8 = QPushButton("", self)
        self.bl8.resize(50, 250)
        self.bl8.clicked.connect(self.dbl8)
        self.bl8.move(-1065, windowy - 420)
        self.bl8.setStyleSheet("""
            QPushButton:!hover { background-color: black }
            QPushButton:pressed { background-color: darkgreen; }
        """)

        self.bl9 = QPushButton("", self)
        self.bl9.resize(50, 250)
        self.bl9.clicked.connect(self.dbl9)
        self.bl9.move(-865, windowy - 420)
        self.bl9.setStyleSheet("""
            QPushButton:!hover { background-color: black }
            QPushButton:pressed { background-color: darkgreen; }
        """)

        self.bl10 = QPushButton("", self)
        self.bl10.resize(50, 250)
        self.bl10.move(-765, windowy - 420)
        self.bl10.clicked.connect(self.dbl10)
        self.bl10.setStyleSheet("""
            QPushButton:!hover { background-color: black }
            QPushButton:pressed { background-color: darkgreen; }
        """)

        self.bl11 = QPushButton("", self)
        self.bl11.resize(50, 250)
        self.bl11.move(-665, windowy - 420)
        self.bl11.clicked.connect(self.dbl11)
        self.bl11.setStyleSheet("""
            QPushButton:!hover { background-color: black }
            QPushButton:pressed { background-color: darkgreen; }
        """)

        self.bl12 = QPushButton("", self)
        self.bl12.resize(50, 250)
        self.bl12.clicked.connect(self.dbl12)
        self.bl12.move(-465, windowy - 420)
        self.bl12.setStyleSheet("""
            QPushButton:!hover { background-color: black }
            QPushButton:pressed { background-color: darkgreen; }
        """)

        self.bl13 = QPushButton("", self)
        self.bl13.resize(50, 250)
        self.bl13.clicked.connect(self.dbl13)
        self.bl13.move(-365, windowy - 420)
        self.bl13.setStyleSheet("""
            QPushButton:!hover { background-color: black }
            QPushButton:pressed { background-color: darkgreen; }
        """)

        self.bl14 = QPushButton("", self)
        self.bl14.resize(50, 250)
        self.bl14.clicked.connect(self.dbl14)
        self.bl14.move(-165, windowy - 420)
        self.bl14.setStyleSheet("""
            QPushButton:!hover { background-color: black }
            QPushButton:pressed { background-color: darkgreen; }
        """)

        self.bl15 = QPushButton("", self)
        self.bl15.resize(50, 250)
        self.bl15.clicked.connect(self.dbl15)
        self.bl15.move(-65, windowy - 420)
        self.bl15.setStyleSheet("""
            QPushButton:!hover { background-color: black }
            QPushButton:pressed { background-color: darkgreen; }
        """)

        self.bl16 = QPushButton("", self)
        self.bl16.resize(50, 250)
        self.bl16.clicked.connect(self.dbl16)
        self.bl16.move(35, windowy - 420)
        self.bl16.setStyleSheet("""
            QPushButton:!hover { background-color: black }
            QPushButton:pressed { background-color: darkgreen; }
        """)

        self.bl17 = QPushButton("", self)
        self.bl17.resize(50, 250)
        self.bl17.move(235, windowy - 420)
        self.bl17.clicked.connect(self.dbl17)
        self.bl17.setStyleSheet("""
            QPushButton:!hover { background-color: black }
            QPushButton:pressed { background-color: darkgreen; }
        """)

        self.bl18 = QPushButton("", self)
        self.bl18.resize(50, 250)
        self.bl18.clicked.connect(self.dbl18)
        self.bl18.move(335, windowy - 420)
        self.bl18.setStyleSheet("""
            QPushButton:!hover { background-color: black }
            QPushButton:pressed { background-color: darkgreen; }
        """)

        self.bl19 = QPushButton("", self)
        self.bl19.resize(50, 250)
        self.bl19.clicked.connect(self.dbl19)
        self.bl19.move(535, windowy - 420)
        self.bl19.setStyleSheet("""
            QPushButton:!hover { background-color: black }
            QPushButton:pressed { background-color: darkgreen; }
        """)

        self.bl20 = QPushButton("", self)
        self.bl20.resize(50, 250)
        self.bl20.clicked.connect(self.dbl20)
        self.bl20.move(635, windowy - 420)
        self.bl20.setStyleSheet("""
            QPushButton:!hover { background-color: black }
            QPushButton:pressed { background-color: darkgreen; }
        """)

        self.bl21 = QPushButton("", self)
        self.bl21.resize(50, 250)
        self.bl21.clicked.connect(self.dbl21)
        self.bl21.move(735, windowy - 420)
        self.bl21.setStyleSheet("""
            QPushButton:!hover { background-color: black }
            QPushButton:pressed { background-color: darkgreen; }
        """)

        self.bl22 = QPushButton("", self)
        self.bl22.resize(50, 250)
        self.bl22.move(935, windowy - 420)
        self.bl22.clicked.connect(self.dbl22)
        self.bl22.setStyleSheet("""
            QPushButton:!hover { background-color: black }
            QPushButton:pressed { background-color: darkgreen; }
        """)

        self.bl23 = QPushButton("", self)
        self.bl23.resize(50, 250)
        self.bl23.clicked.connect(self.dbl23)
        self.bl23.move(1035, windowy - 420)
        self.bl23.setStyleSheet("""
            QPushButton:!hover { background-color: black }
            QPushButton:pressed { background-color: darkgreen; }
        """)

        self.bl24 = QPushButton("", self)
        self.bl24.resize(50, 250)
        self.bl24.clicked.connect(self.dbl24)
        self.bl24.move(1235, windowy - 420)
        self.bl24.setStyleSheet("""
            QPushButton:!hover { background-color: black }
            QPushButton:pressed { background-color: darkgreen; }
        """)

        self.bl25 = QPushButton("", self)
        self.bl25.resize(50, 250)
        self.bl25.clicked.connect(self.dbl25)
        self.bl25.move(1335, windowy - 420)
        self.bl25.setStyleSheet("""
            QPushButton:!hover { background-color: black }
            QPushButton:pressed { background-color: darkgreen; }
        """)

        self.bl26 = QPushButton("", self)
        self.bl26.resize(50, 250)
        self.bl26.clicked.connect(self.dbl26)
        self.bl26.move(1435, windowy - 420)
        self.bl26.setStyleSheet("""
            QPushButton:!hover { background-color: black }
            QPushButton:pressed { background-color: darkgreen; }
        """)

        self.bl27 = QPushButton("", self)
        self.bl27.resize(50, 250)
        self.bl27.clicked.connect(self.dbl27)
        self.bl27.move(1635, windowy - 420)
        self.bl27.setStyleSheet("""
            QPushButton:!hover { background-color: black }
            QPushButton:pressed { background-color: darkgreen; }
        """)

        self.bl28 = QPushButton("", self)
        self.bl28.resize(50, 250)
        self.bl28.clicked.connect(self.dbl28)
        self.bl28.move(1735, windowy - 420)
        self.bl28.setStyleSheet("""
            QPushButton:!hover { background-color: black }
            QPushButton:pressed { background-color: darkgreen; }
        """)

        self.bl29 = QPushButton("", self)
        self.bl29.resize(50, 250)
        self.bl29.clicked.connect(self.dbl29)
        self.bl29.move(1935, windowy - 420)
        self.bl29.setStyleSheet("""
            QPushButton:!hover { background-color: black }
            QPushButton:pressed { background-color: darkgreen; }
        """)

        self.bl30 = QPushButton("", self)
        self.bl30.resize(50, 250)
        self.bl30.move(2035, windowy - 420)
        self.bl30.clicked.connect(self.dbl30)
        self.bl30.setStyleSheet("""
            QPushButton:!hover { background-color: black }
            QPushButton:pressed { background-color: darkgreen; }
        """)

        self.bl31 = QPushButton("", self)
        self.bl31.resize(50, 250)
        self.bl31.clicked.connect(self.dbl31)
        self.bl31.move(2135, windowy - 420)
        self.bl31.setStyleSheet("""
            QPushButton:!hover { background-color: black }
            QPushButton:pressed { background-color: darkgreen; }
        """)

        self.bl32 = QPushButton("", self)
        self.bl32.resize(50, 250)
        self.bl32.move(2335, windowy - 420)
        self.bl32.clicked.connect(self.dbl32)
        self.bl32.setStyleSheet("""
            QPushButton:!hover { background-color: black }
            QPushButton:pressed { background-color: darkgreen; }
        """)

        self.bl33 = QPushButton("", self)
        self.bl33.resize(50, 250)
        self.bl33.move(2435, windowy - 420)
        self.bl33.clicked.connect(self.dbl33)
        self.bl33.setStyleSheet("""
            QPushButton:!hover { background-color: black }
            QPushButton:pressed { background-color: darkgreen; }
        """)

        self.bl34 = QPushButton("", self)
        self.bl34.resize(50, 250)
        self.bl34.clicked.connect(self.dbl34)
        self.bl34.move(2635, windowy - 420)
        self.bl34.setStyleSheet("""
            QPushButton:!hover { background-color: black }
            QPushButton:pressed { background-color: darkgreen; }
        """)

        self.bl35 = QPushButton("", self)
        self.bl35.resize(50, 250)
        self.bl35.clicked.connect(self.dbl35)
        self.bl35.move(2735, windowy - 420)
        self.bl35.setStyleSheet("""
            QPushButton:!hover { background-color: black }
            QPushButton:pressed { background-color: darkgreen; }
        """)

        self.bl36 = QPushButton("", self)
        self.bl36.resize(50, 250)
        self.bl36.move(2835, windowy - 420)
        self.bl36.clicked.connect(self.dbl36)
        self.bl36.setStyleSheet("""
            QPushButton:!hover { background-color: black }
            QPushButton:pressed { background-color: darkgreen; }
        """)

        self.show()
    
    def dkl1(self):
        self.player1.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl1.mp3')))))
        self.player1.play()
    
    def dkl2(self):
        self.player2.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl2.mp3')))))
        self.player2.play()
    
    def dkl3(self):
        self.player3.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl3.mp3')))))
        self.player3.play()

    def dkl4(self):
        self.player4.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl4.mp3')))))
        self.player4.play()
    
    def dkl5(self):
        self.player5.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl5.mp3')))))
        self.player5.play()
    
    def dkl6(self):
        self.player6.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl6.mp3')))))
        self.player6.play()
    
    def dkl7(self):
        self.player7.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl7.mp3')))))
        self.player7.play()
    
    def dkl8(self):
        self.player8.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl8.mp3')))))
        self.player8.play()
    
    def dkl9(self):
        self.player9.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl9.mp3')))))
        self.player9.play()
    
    def dkl10(self):
        self.player10.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl10.mp3')))))
        self.player10.play()

    def dkl11(self):
        self.player11.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl11.mp3')))))
        self.player11.play()
    
    def dkl12(self):
        self.player12.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl12.mp3')))))
        self.player12.play()
    
    def dkl13(self):
        self.player13.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl13.mp3')))))
        self.player13.play()
    
    def dkl14(self):
        self.player14.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl14.mp3')))))
        self.player14.play()
    
    def dkl15(self):
        self.player15.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl15.mp3')))))
        self.player15.play()
    
    def dkl16(self):
        self.player16.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl16.mp3')))))
        self.player16.play()
    
    def dkl17(self):
        self.player17.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl17.mp3')))))
        self.player17.play()
    
    def dkl18(self):
        self.player18.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl18.mp3')))))
        self.player18.play()
    
    def dkl19(self):
        self.player19.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl19.mp3')))))
        self.player19.play()
    
    def dkl20(self):
        self.player20.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl20.mp3')))))
        self.player20.play()
    
    def dkl21(self):
        self.player21.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl21.mp3')))))
        self.player21.play()
    
    def dkl22(self):
        self.player22.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl22.mp3')))))
        self.player22.play()
    
    def dkl23(self):
        self.player23.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl23.mp3')))))
        self.player23.play()
    
    def dkl24(self):
        self.player24.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl24.mp3')))))
        self.player24.play()
    
    def dkl25(self):
        self.player25.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl25.mp3')))))
        self.player25.play()
    
    def dkl26(self):
        self.player26.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl26.mp3')))))
        self.player26.play()
    
    def dkl27(self):
        self.player27.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl27.mp3')))))
        self.player27.play()
    
    def dkl28(self):
        self.player28.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl28.mp3')))))
        self.player28.play()
    
    def dkl29(self):
        self.player29.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl29.mp3')))))
        self.player29.play()
    
    def dkl30(self):
        self.player30.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl30.mp3')))))
        self.player30.play()
    
    def dkl31(self):
        self.player31.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl31.mp3')))))
        self.player31.play()
    
    def dkl32(self):
        self.player32.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl32.mp3')))))
        self.player32.play()
    
    def dkl33(self):
        self.player33.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl33.mp3')))))
        self.player33.play()
    
    def dkl34(self):
        self.player34.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl34.mp3')))))
        self.player34.play()
    
    def dkl35(self):
        self.player35.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl35.mp3')))))
        self.player35.play()
    
    def dkl36(self):
        self.player36.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl36.mp3')))))
        self.player36.play()
    
    def dkl37(self):
        self.player37.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl37.mp3')))))
        self.player37.play()
    
    def dkl38(self):
        self.player38.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl38.mp3')))))
        self.player38.play()
    
    def dkl39(self):
        self.player39.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl39.mp3')))))
        self.player39.play()
    
    def dkl40(self):
        self.player40.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl40.mp3')))))
        self.player40.play()
    
    def dkl41(self):
        self.player41.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl41.mp3')))))
        self.player41.play()
    
    def dkl42(self):
        self.player42.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl42.mp3')))))
        self.player42.play()
    
    def dkl43(self):
        self.player43.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl43.mp3')))))
        self.player43.play()
    
    def dkl44(self):
        self.player44.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl44.mp3')))))
        self.player44.play()

    def dkl45(self):
        self.player45.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl45.mp3')))))
        self.player45.play()
    
    def dkl46(self):
        self.player46.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl46.mp3')))))
        self.player46.play()
    
    def dkl47(self):
        self.player47.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl47.mp3')))))
        self.player47.play()
    
    def dkl48(self):
        self.player48.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl48.mp3')))))
        self.player48.play()
    
    def dkl49(self):
        self.player49.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl49.mp3')))))
        self.player49.play()
    
    def dkl50(self):
        self.player50.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl50.mp3')))))
        self.player50.play()
    
    def dkl51(self):
        self.player51.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl51.mp3')))))
        self.player51.play()
    
    def dkl52(self):
        self.player52.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('kl52.mp3')))))
        self.player52.play()
    
    def dbl1(self):
        self.player53.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('bl1.mp3')))))
        self.player53.play()
    
    def dbl2(self):
        self.player54.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('bl2.mp3')))))
        self.player54.play()
    
    def dbl3(self):
        self.player55.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('bl3.mp3')))))
        self.player55.play()
    
    def dbl4(self):
        self.player56.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('bl4.mp3')))))
        self.player56.play()
    
    def dbl5(self):
        self.player57.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('bl5.mp3')))))
        self.player57.play()
    
    def dbl6(self):
        self.player58.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('bl6.mp3')))))
        self.player58.play()
    
    def dbl7(self):
        self.player59.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('bl7.mp3')))))
        self.player59.play()
    
    def dbl8(self):
        self.player60.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('bl8.mp3')))))
        self.player60.play()
    
    def dbl9(self):
        self.player61.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('bl9.mp3')))))
        self.player61.play()
    
    def dbl10(self):
        self.player62.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('bl10.mp3')))))
        self.player62.play()
    
    def dbl11(self):
        self.player63.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('bl11.mp3')))))
        self.player63.play()
    
    def dbl12(self):
        self.player64.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('bl12.mp3')))))
        self.player64.play()
    
    def dbl13(self):
        self.player65.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('bl13.mp3')))))
        self.player65.play()
    
    def dbl14(self):
        self.player66.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('bl14.mp3')))))
        self.player66.play()
    
    def dbl15(self):
        self.player67.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('bl15.mp3')))))
        self.player67.play()
    
    def dbl16(self):
        self.player68.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('bl16.mp3')))))
        self.player68.play()
    
    def dbl17(self):
        self.player69.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('bl17.mp3')))))
        self.player69.play()
    
    def dbl18(self):
        self.player70.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('bl18.mp3')))))
        self.player70.play()
    
    def dbl19(self):
        self.player71.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('bl19.mp3')))))
        self.player71.play()
    
    def dbl20(self):
        self.player72.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('bl20.mp3')))))
        self.player72.play()
    
    def dbl21(self):
        self.player73.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('bl21.mp3')))))
        self.player73.play()
    
    def dbl22(self):
        self.player74.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('bl22.mp3')))))
        self.player74.play()
    
    def dbl23(self):
        self.player75.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('bl23.mp3')))))
        self.player75.play()
    
    def dbl24(self):
        self.player76.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('bl24.mp3')))))
        self.player76.play()
   
    def dbl25(self):
        self.player77.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('bl25.mp3')))))
        self.player77.play()
    
    def dbl26(self):
        self.player78.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('bl26.mp3')))))
        self.player78.play()
    
    def dbl27(self):
        self.player79.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('bl27.mp3')))))
        self.player79.play()
    
    def dbl28(self):
        self.player80.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('bl28.mp3')))))
        self.player80.play()
    
    def dbl29(self):
        self.player81.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('bl29.mp3')))))
        self.player81.play()
    
    def dbl30(self):
        self.player82.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('bl30.mp3')))))
        self.player82.play()
    
    def dbl31(self):
        self.player83.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('bl31.mp3')))))
        self.player83.play()
    
    def dbl32(self):
        self.player84.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('bl32.mp3')))))
        self.player84.play()
    
    def dbl33(self):
        self.player85.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('bl33.mp3')))))
        self.player85.play()
    
    def dbl34(self):
        self.player86.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('bl34.mp3')))))
        self.player86.play()
    
    def dbl35(self):
        self.player87.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('bl35.mp3')))))
        self.player87.play()
    
    def dbl36(self):
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(str(BASE_DIR.joinpath('bl36.mp3')))))
        self.player.play()

    def Add(self):
        pass

    def DPiano(self):
        self.frame.move(self.SizeWindowX / 2 - 50, 0)

    def GoLeft(self):
        # проверка, можно ли двигаться
        if self.FirstKey > 0:
            # смещение клавиатуры
            self.kl1.move(self.kl1.x() + 100, self.SizeWindowY - 420)
            self.kl2.move(self.kl2.x() + 100, self.SizeWindowY - 420)
            self.kl3.move(self.kl3.x() + 100, self.SizeWindowY - 420)
            self.kl4.move(self.kl4.x() + 100, self.SizeWindowY - 420)
            self.kl5.move(self.kl5.x() + 100, self.SizeWindowY - 420)
            self.kl6.move(self.kl6.x() + 100, self.SizeWindowY - 420)
            self.kl7.move(self.kl7.x() + 100, self.SizeWindowY - 420)
            self.kl8.move(self.kl8.x() + 100, self.SizeWindowY - 420)
            self.kl9.move(self.kl9.x() + 100, self.SizeWindowY - 420)
            self.kl10.move(self.kl10.x() + 100, self.SizeWindowY - 420)
            self.kl11.move(self.kl11.x() + 100, self.SizeWindowY - 420)
            self.kl12.move(self.kl12.x() + 100, self.SizeWindowY - 420)
            self.kl13.move(self.kl13.x() + 100, self.SizeWindowY - 420)
            self.kl14.move(self.kl14.x() + 100, self.SizeWindowY - 420)
            self.kl15.move(self.kl15.x() + 100, self.SizeWindowY - 420)
            self.kl16.move(self.kl16.x() + 100, self.SizeWindowY - 420)
            self.kl17.move(self.kl17.x() + 100, self.SizeWindowY - 420)
            self.kl18.move(self.kl18.x() + 100, self.SizeWindowY - 420)
            self.kl19.move(self.kl19.x() + 100, self.SizeWindowY - 420)
            self.kl20.move(self.kl20.x() + 100, self.SizeWindowY - 420)
            self.kl21.move(self.kl21.x() + 100, self.SizeWindowY - 420)
            self.kl22.move(self.kl22.x() + 100, self.SizeWindowY - 420)
            self.kl23.move(self.kl23.x() + 100, self.SizeWindowY - 420)
            self.kl24.move(self.kl24.x() + 100, self.SizeWindowY - 420)
            self.kl25.move(self.kl25.x() + 100, self.SizeWindowY - 420)
            self.kl26.move(self.kl26.x() + 100, self.SizeWindowY - 420)
            self.kl27.move(self.kl27.x() + 100, self.SizeWindowY - 420)
            self.kl28.move(self.kl28.x() + 100, self.SizeWindowY - 420)
            self.kl29.move(self.kl29.x() + 100, self.SizeWindowY - 420)
            self.kl30.move(self.kl30.x() + 100, self.SizeWindowY - 420)
            self.kl31.move(self.kl31.x() + 100, self.SizeWindowY - 420)
            self.kl32.move(self.kl32.x() + 100, self.SizeWindowY - 420)
            self.kl33.move(self.kl33.x() + 100, self.SizeWindowY - 420)
            self.kl34.move(self.kl34.x() + 100, self.SizeWindowY - 420)
            self.kl35.move(self.kl35.x() + 100, self.SizeWindowY - 420)
            self.kl36.move(self.kl36.x() + 100, self.SizeWindowY - 420)
            self.kl37.move(self.kl37.x() + 100, self.SizeWindowY - 420)
            self.kl38.move(self.kl38.x() + 100, self.SizeWindowY - 420)
            self.kl39.move(self.kl39.x() + 100, self.SizeWindowY - 420)
            self.kl40.move(self.kl40.x() + 100, self.SizeWindowY - 420)
            self.kl41.move(self.kl41.x() + 100, self.SizeWindowY - 420)
            self.kl42.move(self.kl42.x() + 100, self.SizeWindowY - 420)
            self.kl43.move(self.kl43.x() + 100, self.SizeWindowY - 420)
            self.kl44.move(self.kl44.x() + 100, self.SizeWindowY - 420)
            self.kl45.move(self.kl45.x() + 100, self.SizeWindowY - 420)
            self.kl46.move(self.kl46.x() + 100, self.SizeWindowY - 420)
            self.kl47.move(self.kl47.x() + 100, self.SizeWindowY - 420)
            self.kl48.move(self.kl48.x() + 100, self.SizeWindowY - 420)
            self.kl49.move(self.kl49.x() + 100, self.SizeWindowY - 420)
            self.kl50.move(self.kl50.x() + 100, self.SizeWindowY - 420)
            self.kl51.move(self.kl51.x() + 100, self.SizeWindowY - 420)
            self.kl52.move(self.kl52.x() + 100, self.SizeWindowY - 420)
            # движение чёрных
            self.bl1.move(self.bl1.x() + 100, self.SizeWindowY - 420)
            self.bl2.move(self.bl2.x() + 100, self.SizeWindowY - 420)
            self.bl3.move(self.bl3.x() + 100, self.SizeWindowY - 420)
            self.bl4.move(self.bl4.x() + 100, self.SizeWindowY - 420)
            self.bl5.move(self.bl5.x() + 100, self.SizeWindowY - 420)
            self.bl6.move(self.bl6.x() + 100, self.SizeWindowY - 420)
            self.bl7.move(self.bl7.x() + 100, self.SizeWindowY - 420)
            self.bl8.move(self.bl8.x() + 100, self.SizeWindowY - 420)
            self.bl9.move(self.bl9.x() + 100, self.SizeWindowY - 420)
            self.bl10.move(self.bl10.x() + 100, self.SizeWindowY - 420)
            self.bl11.move(self.bl11.x() + 100, self.SizeWindowY - 420)
            self.bl12.move(self.bl12.x() + 100, self.SizeWindowY - 420)
            self.bl13.move(self.bl13.x() + 100, self.SizeWindowY - 420)
            self.bl14.move(self.bl14.x() + 100, self.SizeWindowY - 420)
            self.bl15.move(self.bl15.x() + 100, self.SizeWindowY - 420)
            self.bl16.move(self.bl16.x() + 100, self.SizeWindowY - 420)
            self.bl17.move(self.bl17.x() + 100, self.SizeWindowY - 420)
            self.bl18.move(self.bl18.x() + 100, self.SizeWindowY - 420)
            self.bl19.move(self.bl19.x() + 100, self.SizeWindowY - 420)
            self.bl20.move(self.bl20.x() + 100, self.SizeWindowY - 420)
            self.bl21.move(self.bl21.x() + 100, self.SizeWindowY - 420)
            self.bl22.move(self.bl22.x() + 100, self.SizeWindowY - 420)
            self.bl23.move(self.bl23.x() + 100, self.SizeWindowY - 420)
            self.bl24.move(self.bl24.x() + 100, self.SizeWindowY - 420)
            self.bl25.move(self.bl25.x() + 100, self.SizeWindowY - 420)
            self.bl26.move(self.bl26.x() + 100, self.SizeWindowY - 420)
            self.bl27.move(self.bl27.x() + 100, self.SizeWindowY - 420)
            self.bl28.move(self.bl28.x() + 100, self.SizeWindowY - 420)
            self.bl29.move(self.bl29.x() + 100, self.SizeWindowY - 420)
            self.bl30.move(self.bl30.x() + 100, self.SizeWindowY - 420)
            self.bl31.move(self.bl31.x() + 100, self.SizeWindowY - 420)
            self.bl32.move(self.bl32.x() + 100, self.SizeWindowY - 420)
            self.bl33.move(self.bl33.x() + 100, self.SizeWindowY - 420)
            self.bl34.move(self.bl34.x() + 100, self.SizeWindowY - 420)
            self.bl35.move(self.bl35.x() + 100, self.SizeWindowY - 420)
            self.bl36.move(self.bl36.x() + 100, self.SizeWindowY - 420)
            self.FirstKey -= 1
            self.LastKey -= 1
            
            #смещение индикатора
            self.frame.move(self.SizeWindowX / 2 - 485 + 18.7 * self.FirstKey, 100)

    def GoRight(self):
        # проверка, можно ли двигаться
        if self.LastKey < 52:
            # смещение клавиатуры
            self.kl1.move(self.kl1.x() - 100, self.SizeWindowY - 420)
            self.kl2.move(self.kl2.x() - 100, self.SizeWindowY - 420)
            self.kl3.move(self.kl3.x() - 100, self.SizeWindowY - 420)
            self.kl4.move(self.kl4.x() - 100, self.SizeWindowY - 420)
            self.kl5.move(self.kl5.x() - 100, self.SizeWindowY - 420)
            self.kl6.move(self.kl6.x() - 100, self.SizeWindowY - 420)
            self.kl7.move(self.kl7.x() - 100, self.SizeWindowY - 420)
            self.kl8.move(self.kl8.x() - 100, self.SizeWindowY - 420)
            self.kl9.move(self.kl9.x() - 100, self.SizeWindowY - 420)
            self.kl10.move(self.kl10.x() - 100, self.SizeWindowY - 420)
            self.kl11.move(self.kl11.x() - 100, self.SizeWindowY - 420)
            self.kl12.move(self.kl12.x() - 100, self.SizeWindowY - 420)
            self.kl13.move(self.kl13.x() - 100, self.SizeWindowY - 420)
            self.kl14.move(self.kl14.x() - 100, self.SizeWindowY - 420)
            self.kl15.move(self.kl15.x() - 100, self.SizeWindowY - 420)
            self.kl16.move(self.kl16.x() - 100, self.SizeWindowY - 420)
            self.kl17.move(self.kl17.x() - 100, self.SizeWindowY - 420)
            self.kl18.move(self.kl18.x() - 100, self.SizeWindowY - 420)
            self.kl19.move(self.kl19.x() - 100, self.SizeWindowY - 420)
            self.kl20.move(self.kl20.x() - 100, self.SizeWindowY - 420)
            self.kl21.move(self.kl21.x() - 100, self.SizeWindowY - 420)
            self.kl22.move(self.kl22.x() - 100, self.SizeWindowY - 420)
            self.kl23.move(self.kl23.x() - 100, self.SizeWindowY - 420)
            self.kl24.move(self.kl24.x() - 100, self.SizeWindowY - 420)
            self.kl25.move(self.kl25.x() - 100, self.SizeWindowY - 420)
            self.kl26.move(self.kl26.x() - 100, self.SizeWindowY - 420)
            self.kl27.move(self.kl27.x() - 100, self.SizeWindowY - 420)
            self.kl28.move(self.kl28.x() - 100, self.SizeWindowY - 420)
            self.kl29.move(self.kl29.x() - 100, self.SizeWindowY - 420)
            self.kl30.move(self.kl30.x() - 100, self.SizeWindowY - 420)
            self.kl31.move(self.kl31.x() - 100, self.SizeWindowY - 420)
            self.kl32.move(self.kl32.x() - 100, self.SizeWindowY - 420)
            self.kl33.move(self.kl33.x() - 100, self.SizeWindowY - 420)
            self.kl34.move(self.kl34.x() - 100, self.SizeWindowY - 420)
            self.kl35.move(self.kl35.x() - 100, self.SizeWindowY - 420)
            self.kl36.move(self.kl36.x() - 100, self.SizeWindowY - 420)
            self.kl37.move(self.kl37.x() - 100, self.SizeWindowY - 420)
            self.kl38.move(self.kl38.x() - 100, self.SizeWindowY - 420)
            self.kl39.move(self.kl39.x() - 100, self.SizeWindowY - 420)
            self.kl40.move(self.kl40.x() - 100, self.SizeWindowY - 420)
            self.kl41.move(self.kl41.x() - 100, self.SizeWindowY - 420)
            self.kl42.move(self.kl42.x() - 100, self.SizeWindowY - 420)
            self.kl43.move(self.kl43.x() - 100, self.SizeWindowY - 420)
            self.kl44.move(self.kl44.x() - 100, self.SizeWindowY - 420)
            self.kl45.move(self.kl45.x() - 100, self.SizeWindowY - 420)
            self.kl46.move(self.kl46.x() - 100, self.SizeWindowY - 420)
            self.kl47.move(self.kl47.x() - 100, self.SizeWindowY - 420)
            self.kl48.move(self.kl48.x() - 100, self.SizeWindowY - 420)
            self.kl49.move(self.kl49.x() - 100, self.SizeWindowY - 420)
            self.kl50.move(self.kl50.x() - 100, self.SizeWindowY - 420)
            self.kl51.move(self.kl51.x() - 100, self.SizeWindowY - 420)
            self.kl52.move(self.kl52.x() - 100, self.SizeWindowY - 420)
            # движение чёрных
            self.bl1.move(self.bl1.x() - 100, self.SizeWindowY - 420)
            self.bl2.move(self.bl2.x() - 100, self.SizeWindowY - 420)
            self.bl3.move(self.bl3.x() - 100, self.SizeWindowY - 420)
            self.bl4.move(self.bl4.x() - 100, self.SizeWindowY - 420)
            self.bl5.move(self.bl5.x() - 100, self.SizeWindowY - 420)
            self.bl6.move(self.bl6.x() - 100, self.SizeWindowY - 420)
            self.bl7.move(self.bl7.x() - 100, self.SizeWindowY - 420)
            self.bl8.move(self.bl8.x() - 100, self.SizeWindowY - 420)
            self.bl9.move(self.bl9.x() - 100, self.SizeWindowY - 420)
            self.bl10.move(self.bl10.x() - 100, self.SizeWindowY - 420)
            self.bl11.move(self.bl11.x() - 100, self.SizeWindowY - 420)
            self.bl12.move(self.bl12.x() - 100, self.SizeWindowY - 420)
            self.bl13.move(self.bl13.x() - 100, self.SizeWindowY - 420)
            self.bl14.move(self.bl14.x() - 100, self.SizeWindowY - 420)
            self.bl15.move(self.bl15.x() - 100, self.SizeWindowY - 420)
            self.bl16.move(self.bl16.x() - 100, self.SizeWindowY - 420)
            self.bl17.move(self.bl17.x() - 100, self.SizeWindowY - 420)
            self.bl18.move(self.bl18.x() - 100, self.SizeWindowY - 420)
            self.bl19.move(self.bl19.x() - 100, self.SizeWindowY - 420)
            self.bl20.move(self.bl20.x() - 100, self.SizeWindowY - 420)
            self.bl21.move(self.bl21.x() - 100, self.SizeWindowY - 420)
            self.bl22.move(self.bl22.x() - 100, self.SizeWindowY - 420)
            self.bl23.move(self.bl23.x() - 100, self.SizeWindowY - 420)
            self.bl24.move(self.bl24.x() - 100, self.SizeWindowY - 420)
            self.bl25.move(self.bl25.x() - 100, self.SizeWindowY - 420)
            self.bl26.move(self.bl26.x() - 100, self.SizeWindowY - 420)
            self.bl27.move(self.bl27.x() - 100, self.SizeWindowY - 420)
            self.bl28.move(self.bl28.x() - 100, self.SizeWindowY - 420)
            self.bl29.move(self.bl29.x() - 100, self.SizeWindowY - 420)
            self.bl30.move(self.bl30.x() - 100, self.SizeWindowY - 420)
            self.bl31.move(self.bl31.x() - 100, self.SizeWindowY - 420)
            self.bl32.move(self.bl32.x() - 100, self.SizeWindowY - 420)
            self.bl33.move(self.bl33.x() - 100, self.SizeWindowY - 420)
            self.bl34.move(self.bl34.x() - 100, self.SizeWindowY - 420)
            self.bl35.move(self.bl35.x() - 100, self.SizeWindowY - 420)
            self.bl36.move(self.bl36.x() - 100, self.SizeWindowY - 420)
            self.FirstKey += 1
            self.LastKey += 1
            
            #смещение индикатора
            self.frame.move(self.SizeWindowX / 2 - 485 + 18.7 * self.FirstKey, 100)


    def ButtonSound(self):
        i, okBtnPressed = QInputDialog.getInt(self, "Громкость",
                                              "Ведите громкость звука (от 0 до 100)",
                                              0, 0, 100, 1)
        if okBtnPressed:
            self.sound = i
            self.player.setVolume(self.sound)
            self.player1.setVolume(self.sound)
            self.player2.setVolume(self.sound)
            self.player3.setVolume(self.sound)
            self.player4.setVolume(self.sound)
            self.player5.setVolume(self.sound)
            self.player6.setVolume(self.sound)
            self.player7.setVolume(self.sound)
            self.player8.setVolume(self.sound)
            self.player9.setVolume(self.sound)
            self.player10.setVolume(self.sound)
            self.player11.setVolume(self.sound)
            self.player12.setVolume(self.sound)
            self.player13.setVolume(self.sound)
            self.player14.setVolume(self.sound)
            self.player15.setVolume(self.sound)
            self.player16.setVolume(self.sound)
            self.player17.setVolume(self.sound)
            self.player18.setVolume(self.sound)
            self.player19.setVolume(self.sound)
            self.player20.setVolume(self.sound)
            self.player21.setVolume(self.sound)
            self.player22.setVolume(self.sound)
            self.player23.setVolume(self.sound)
            self.player24.setVolume(self.sound)
            self.player25.setVolume(self.sound)
            self.player26.setVolume(self.sound)
            self.player27.setVolume(self.sound)
            self.player28.setVolume(self.sound)
            self.player29.setVolume(self.sound)
            self.player30.setVolume(self.sound)
            self.player31.setVolume(self.sound)
            self.player32.setVolume(self.sound)
            self.player33.setVolume(self.sound)
            self.player34.setVolume(self.sound)
            self.player35.setVolume(self.sound)
            self.player36.setVolume(self.sound)
            self.player37.setVolume(self.sound)
            self.player38.setVolume(self.sound)
            self.player39.setVolume(self.sound)
            self.player40.setVolume(self.sound)
            self.player41.setVolume(self.sound)
            self.player42.setVolume(self.sound)
            self.player43.setVolume(self.sound)
            self.player44.setVolume(self.sound)
            self.player45.setVolume(self.sound)
            self.player46.setVolume(self.sound)
            self.player47.setVolume(self.sound)
            self.player48.setVolume(self.sound)
            self.player49.setVolume(self.sound)
            self.player50.setVolume(self.sound)
            self.player51.setVolume(self.sound)
            self.player52.setVolume(self.sound)
            self.player53.setVolume(self.sound)
            self.player54.setVolume(self.sound)
            self.player55.setVolume(self.sound)
            self.player56.setVolume(self.sound)
            self.player57.setVolume(self.sound)
            self.player58.setVolume(self.sound)
            self.player59.setVolume(self.sound)
            self.player60.setVolume(self.sound)
            self.player61.setVolume(self.sound)
            self.player62.setVolume(self.sound)
            self.player63.setVolume(self.sound)
            self.player64.setVolume(self.sound)
            self.player65.setVolume(self.sound)
            self.player66.setVolume(self.sound)
            self.player67.setVolume(self.sound)
            self.player68.setVolume(self.sound)
            self.player69.setVolume(self.sound)
            self.player70.setVolume(self.sound)
            self.player71.setVolume(self.sound)
            self.player72.setVolume(self.sound)
            self.player73.setVolume(self.sound)
            self.player74.setVolume(self.sound)
            self.player75.setVolume(self.sound)
            self.player76.setVolume(self.sound)
            self.player77.setVolume(self.sound)
            self.player78.setVolume(self.sound)
            self.player79.setVolume(self.sound)
            self.player80.setVolume(self.sound)
            self.player81.setVolume(self.sound)
            self.player82.setVolume(self.sound)
            self.player83.setVolume(self.sound)
            self.player84.setVolume(self.sound)
            self.player85.setVolume(self.sound)
            self.player86.setVolume(self.sound)
            self.player87.setVolume(self.sound)

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.KeyPress:
            if event.key() == QtCore.Qt.Key_Q:
                self.dkl22()
                return 1
            if event.key() == QtCore.Qt.Key_W:
                self.dkl23()
                return 1
            if event.key() == QtCore.Qt.Key_E:
                self.dkl24()
                return 1
            if event.key() == QtCore.Qt.Key_R:
                self.dkl25()
                return 1
            if event.key() == QtCore.Qt.Key_T:
                self.dkl26()
                return 1
            if event.key() == QtCore.Qt.Key_Y:
                self.dkl27()
                return 1
            if event.key() == QtCore.Qt.Key_U:
                self.dkl28()
                return 1
            if event.key() == QtCore.Qt.Key_I:
                self.dkl29()
                return 1
            if event.key() == QtCore.Qt.Key_O:
                self.dkl30()
                return 1
            if event.key() == QtCore.Qt.Key_P:
                self.dkl31()
                return 1
            if event.key() == QtCore.Qt.Key_2:
                self.dbl16()
                return 1
            if event.key() == QtCore.Qt.Key_4:
                self.dbl17()
                return 1
            if event.key() == QtCore.Qt.Key_5:
                self.dbl18()
                return 1
            if event.key() == QtCore.Qt.Key_7:
                self.dbl19()
                return 1
            if event.key() == QtCore.Qt.Key_8:
                self.dbl20()
                return 1
            if event.key() == QtCore.Qt.Key_9:
                self.dbl21()
                return 1

        return super().eventFilter(obj, event)

    def information(self):
        # открытие информации
        i, okBtnPressed = QInputDialog.getItem(self, "Информация",
                                               "Функционал пианино:",
                                               ("Полная клавиатура пианино", "Регулятор громкости",
                                                "Переключение тембра", "Индикатор перемещения по клавиатуре",
                                                "Воиспроизведение звуков по нажатию на кнопки клавиатуры"),
                                               0, False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
