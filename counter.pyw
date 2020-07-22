from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Counter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__centWid=QWidget(self)
        self.setCentralWidget(self.__centWid)
        
        self.__max100=1
        self.__grade=100
        
        self.__ui()
    
    def __ui(self):
        def callback(a):
            self.__grade+=a
            self.__labDis.setText(str(self.__grade))
        def max100():
            self.__max100^=1
            self.__grade=50+self.__max100*50
            self.__btnMax.setText('Max: %d' %self.__grade)
            self.__labDis.setText(str(self.__grade))
        
        self.setWindowTitle('Counter')
        grid1=QGridLayout(self.__centWid)
        
        self.__labDis=QLabel(self.__centWid)
        self.__labDis.setText('100')
        self.__labDis.setAlignment(Qt.AlignCenter)
        grid1.addWidget(self.__labDis,0,0,1,1)
        
        self.__btnMax=QPushButton(self.__centWid)
        self.__btnMax.setText('Max: 100')
        self.__btnMax.clicked.connect(max100)
        grid1.addWidget(self.__btnMax,0,1,1,1)
        
        self.__btn2A=QPushButton(self.__centWid)
        self.__btn2A.setText('+2')
        self.__btn2A.clicked.connect(lambda: callback(2))
        grid1.addWidget(self.__btn2A,1,0,1,1)
        
        self.__btn2B=QPushButton(self.__centWid)
        self.__btn2B.setText('-2')
        self.__btn2B.clicked.connect(lambda: callback(-2))
        grid1.addWidget(self.__btn2B,1,1,1,1)
        
        self.__btn3A=QPushButton(self.__centWid)
        self.__btn3A.setText('+3')
        self.__btn3A.clicked.connect(lambda: callback(3))
        grid1.addWidget(self.__btn3A,2,0,1,1)
        
        self.__btn3B=QPushButton(self.__centWid)
        self.__btn3B.setText('-3')
        self.__btn3B.clicked.connect(lambda: callback(-3))
        grid1.addWidget(self.__btn3B,2,1,1,1)
        
        self.__btn4A=QPushButton(self.__centWid)
        self.__btn4A.setText('+4')
        self.__btn4A.clicked.connect(lambda: callback(4))
        grid1.addWidget(self.__btn4A,3,0,1,1)
        
        self.__btn4B=QPushButton(self.__centWid)
        self.__btn4B.setText('-4')
        self.__btn4B.clicked.connect(lambda: callback(-4))
        grid1.addWidget(self.__btn4B,3,1,1,1)


if __name__=='__main__':
    app=QApplication()
    
    count=Counter()
    count.show()
    
    app.exec_()