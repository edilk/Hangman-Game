import sys, random, os
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from time import sleep
from random import choice

words = ['captivity', 'america', 'europe', 'federal', 'gluten', 'ridiculous', 'automatic', 'television', 'difficult', 'severe', 'interesting', 'indonesia', 'industrial',
     'automotive', 'president', 'terrestrial', 'academic', 'comedic', 'comical', 'genuine', 'suitcase', 'vietnam', 'achievement', 'careless', 'monarchy', 'monetary', 
     'quarantine', 'supernatural', 'illuminate', 'optimal', 'application', 'scientist', 'software', 'hardware', 'program', 'colonial', 'algorithm', 'intelligent', 
     'electricity', 'verification', 'broadband', 'quality', 'validation', 'online', 'telephone', 'dictionary', 'keyboard', 'china', 'london', 'jamaica', 'biology', 
     'chemistry', 'history', 'historian', 'africa', 'mathematics', 'computer', 'literature', 'gravity', 'guitar', 'violin', 'illuminate', 'england', 'china', 'japan',
     'canada', 'suitcase', 'wireless', 'internet']


HANGMAN_PARMS = 131, 222, Qt.KeepAspectRatio, Qt.FastTransformation

def log_uncaught_exceptions(ex_cls, ex, tb):
    text = '{}: {}:\n'.format(ex_cls.__name__, ex)
    import traceback
    text += ''.join(traceback.format_tb(tb))

    print(text)
    QMessageBox.critical(None, 'Error', text)
    quit()



sys.excepthook = log_uncaught_exceptions


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setWindowTitle("HangMan Game!")
        self.setWindowIcon(QIcon(os.path.join('icons', 'Hangman-icon.png')))

        self.initUI()
        self.setFixedSize(500, 450)
        self.show()
    
    def initUI(self):

        self.chances = 6
        self.num = 0
        self.img = QLabel(self)
        self.img.setPixmap(QPixmap('hangman{}.png'.format(self.num)).scaled(*HANGMAN_PARMS))
        self.img.resize(131,222)
        self.img.move(20,40)

        self.word = choice(words)
        blank_word = "_ " * len(self.word)
        blank_word.rstrip()
        self.guess = None

        self.bwlabel = QLabel("{}".format(blank_word), self)
        font1 = self.bwlabel.font()
        font1.setPointSize(14)
        self.bwlabel.setFont(font1)
        self.bwlabel.move(200, 200)
        self.bwlabel.setFixedWidth(200)

        self.guessedLetters = ""

        self.trylbl = QLabel("You have only {} chance(s)".format(self.chances), self)
        self.trylbl.move(200, 40)
        font1 = self.trylbl.font()
        font1.setPointSize(12)
        self.trylbl.setFont(font1)
        self.trylbl.setFixedWidth(200)
        self.trylbl.setVisible(True)

        self.led = QLineEdit(self)
        self.led.move(150,285)
        regex = QRegExp("[a-z_]+")
        validator = QRegExpValidator(regex)
        self.led.setValidator(validator)
        font2 = self.led.font()
        font2.setPointSize(16)
        self.led.setFont(font2)
        self.led.setMaxLength(1)
        self.led.returnPressed.connect(self.Check)

        self.btn = QPushButton("Check",self)
        self.btn.move(260, 285)
        self.btn.setFont(QFont('SansSerif', 16))
        self.btn.clicked.connect(self.Check)

        self.cor = QLabel("Right",self)
        self.cor.move(200, 150)
        font1 = self.cor.font()
        font1.setPointSize(12)
        self.cor.setFont(font1)
        self.cor.setFixedWidth(200)
        self.cor.setVisible(False)
        
        self.incor = QLabel("Oops!",self)
        self.incor.move(200, 150)
        font1 = self.incor.font()
        font1.setPointSize(12)
        self.incor.setFont(font1)
        self.incor.setFixedWidth(200)
        self.incor.setVisible(False)
        
        self.lose = QLabel("Oops! \nYou lost!",self)
        self.lose.move(200, 40)
        font1 = self.lose.font()
        font1.setPointSize(14)
        self.lose.setFont(font1)
        self.lose.setFixedWidth(200)
        self.lose.setFixedHeight(50)
        self.lose.setVisible(False)

        self.win = QLabel("Congratulations!\nYou win!",self)
        self.win.move(200, 90)
        font1 = self.win.font()
        font1.setPointSize(14)
        self.win.setFont(font1)
        self.win.setFixedWidth(200)
        self.win.setFixedHeight(50)
        self.win.setVisible(False)

        self.answer = QLabel("The word was: \n'{}'".format(self.word), self)
        self.answer.move(200, 130)
        font1 = self.answer.font()
        font1.setPointSize(14)
        self.answer.setFont(font1)
        self.answer.setFixedWidth(200)
        self.answer.setFixedHeight(50)
        self.answer.setVisible(False)
        
        
        #Buttons
        buttonQ = QPushButton('q', self)
        buttonQ.move(20, 325)
        buttonQ.resize(40,25)
        buttonQ.setFont(QFont('SansSerif', 14))
        buttonQ.clicked.connect(self.buttonClicked)

        buttonW = QPushButton('w', self)
        buttonW.move(66.66, 325)
        buttonW.resize(40,25)
        buttonW.setFont(QFont('SansSerif', 14))
        buttonW.clicked.connect(self.buttonClicked)

        buttonE = QPushButton('e', self)
        buttonE.move(113.32, 325)
        buttonE.resize(40,25)
        buttonE.setFont(QFont('SansSerif', 14))
        buttonE.clicked.connect(self.buttonClicked)

        buttonR = QPushButton('r', self)
        buttonR.move(159.98, 325)
        buttonR.resize(40,25)
        buttonR.setFont(QFont('SansSerif', 14))
        buttonR.clicked.connect(self.buttonClicked)

        buttonT = QPushButton('t', self)
        buttonT.move(206.64, 325)
        buttonT.resize(40,25)
        buttonT.setFont(QFont('SansSerif', 14))
        buttonT.clicked.connect(self.buttonClicked)

        buttonY = QPushButton('y', self)
        buttonY.move(253.30, 325)
        buttonY.resize(40,25)
        buttonY.setFont(QFont('SansSerif', 14))
        buttonY.clicked.connect(self.buttonClicked)

        buttonU = QPushButton('u', self)
        buttonU.move(299.96, 325)
        buttonU.resize(40,25)
        buttonU.setFont(QFont('SansSerif', 14))
        buttonU.clicked.connect(self.buttonClicked)

        buttonI = QPushButton('i', self)
        buttonI.move(346.62, 325)
        buttonI.resize(40,25)
        buttonI.setFont(QFont('SansSerif', 14))
        buttonI.clicked.connect(self.buttonClicked)

        buttonO = QPushButton('o', self)
        buttonO.move(393.28, 325)
        buttonO.resize(40,25)
        buttonO.setFont(QFont('SansSerif', 14))
        buttonO.clicked.connect(self.buttonClicked)

        buttonP = QPushButton('p', self)
        buttonP.move(439.94, 325)
        buttonP.resize(40,25)
        buttonP.setFont(QFont('SansSerif', 14))
        buttonP.clicked.connect(self.buttonClicked)

        buttonA = QPushButton('a', self)
        buttonA.move(43.36, 355)
        buttonA.resize(40,25)
        buttonA.setFont(QFont('SansSerif', 14))
        buttonA.clicked.connect(self.buttonClicked)

        buttonS = QPushButton('s', self)
        buttonS.move(90.02, 355)
        buttonS.resize(40,25)
        buttonS.setFont(QFont('SansSerif', 14))
        buttonS.clicked.connect(self.buttonClicked)

        buttonD = QPushButton('d', self)
        buttonD.move(136.68, 355)
        buttonD.resize(40,25)
        buttonD.setFont(QFont('SansSerif', 14))
        buttonD.clicked.connect(self.buttonClicked)

        buttonF = QPushButton('f', self)
        buttonF.move(183.34, 355)
        buttonF.resize(40,25)
        buttonF.setFont(QFont('SansSerif', 14))
        buttonF.clicked.connect(self.buttonClicked)

        buttonG = QPushButton('g', self)
        buttonG.move(230, 355)
        buttonG.resize(40,25)
        buttonG.setFont(QFont('SansSerif', 14))
        buttonG.clicked.connect(self.buttonClicked)

        buttonH = QPushButton('h', self)
        buttonH.move(276.66, 355)
        buttonH.resize(40,25)
        buttonH.setFont(QFont('SansSerif', 14))
        buttonH.clicked.connect(self.buttonClicked)

        buttonJ = QPushButton('j', self)
        buttonJ.move(323.32, 355)
        buttonJ.resize(40,25)
        buttonJ.setFont(QFont('SansSerif', 14))
        buttonJ.clicked.connect(self.buttonClicked)

        buttonK = QPushButton('k', self)
        buttonK.move(369.98, 355)
        buttonK.resize(40,25)
        buttonK.setFont(QFont('SansSerif', 14))
        buttonK.clicked.connect(self.buttonClicked)

        buttonL = QPushButton('l', self)
        buttonL.move(416.64, 355)
        buttonL.resize(40,25)
        buttonL.setFont(QFont('SansSerif', 14))
        buttonL.clicked.connect(self.buttonClicked)

        buttonZ = QPushButton('z', self)
        buttonZ.move(90.02, 385)
        buttonZ.resize(40,25)
        buttonZ.setFont(QFont('SansSerif', 14))
        buttonZ.clicked.connect(self.buttonClicked)

        buttonX = QPushButton('x', self)
        buttonX.move(136.68, 385)
        buttonX.resize(40,25)
        buttonX.setFont(QFont('SansSerif', 14))
        buttonX.clicked.connect(self.buttonClicked)

        buttonC = QPushButton('c', self)
        buttonC.move(183.34, 385)
        buttonC.resize(40,25)
        buttonC.setFont(QFont('SansSerif', 14))
        buttonC.clicked.connect(self.buttonClicked)

        buttonV = QPushButton('v', self)
        buttonV.move(230, 385)
        buttonV.resize(40,25)
        buttonV.setFont(QFont('SansSerif', 14))
        buttonV.clicked.connect(self.buttonClicked)

        buttonB = QPushButton('b', self)
        buttonB.move(276.66, 385)
        buttonB.resize(40,25)
        buttonB.setFont(QFont('SansSerif', 14))
        buttonB.clicked.connect(self.buttonClicked)

        buttonN = QPushButton('n', self)
        buttonN.move(323.32, 385)
        buttonN.resize(40,25)
        buttonN.setFont(QFont('SansSerif', 14))
        buttonN.clicked.connect(self.buttonClicked)

        buttonM = QPushButton('m', self)
        buttonM.move(369.98, 385)
        buttonM.resize(40,25)
        buttonM.setFont(QFont('SansSerif', 14))
        buttonM.clicked.connect(self.buttonClicked)


        
    def buttonClicked(self):
        sender = self.sender()
        self.led.setText(sender.text())
        
    
    def Check(self):
        self.guess = self.led.text()
        
        if self.guess in self.word:
            self.guessedLetters += self.guess
            self.cor.setVisible(True)
            QApplication.processEvents()
            sleep(1)
            self.cor.setVisible(False)
            QApplication.processEvents()
            
            
        else:
            self.num += 1
            self.img.setPixmap(QPixmap('hangman{}.png'.format(self.num)).scaled(*HANGMAN_PARMS))
            self.chances -= 1
            self.incor.setVisible(True)
            QApplication.processEvents()
            sleep(1)
            self.incor.setVisible(False)
            QApplication.processEvents()
            
        
        blank_word = ""
        for i in self.word:
            if i in self.guessedLetters:
                blank_word += i   

            else:
                blank_word += "_ "

        blank_word.rstrip()

        self.bwlabel.setText(blank_word)
        self.led.setText("")
        self.led.setFocus(True)

        if self.chances == 0:
            self.lose.setVisible(True)
            self.answer.setVisible(True)
            self.trylbl.setVisible(False)
            self.btn.setEnabled(False)
        if "_" not in blank_word:
            self.win.setVisible(True)
            self.trylbl.setVisible(False)
            self.btn.setEnabled(False)
        
        
        
 
app = QApplication(sys.argv)

window = MainWindow()
window.show()
window.resize(500, 450)

app.exec_()
