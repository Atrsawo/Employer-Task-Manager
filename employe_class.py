
from datetime import datetime
import aelosemTime_class
from gui import Gui
from task import Task
from resorce import Resource
from PyQt5.QtWidgets import *
from matplotlib.pyplot import text
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow)
from PyQt5.QtCore import Qt, QSize


class employer(QMainWindow):
    
    def __init__(self,fname,lname,rule_in_company,task,unavability,historyTaskCheck,mssg):
        
        self.app = QApplication([])
        super().__init__()
        self.fname = fname
        self.lname = lname
        self.rule_in_company = rule_in_company
        self.tasks = task
        self.unavability = unavability
        self.historyTaskCheck = historyTaskCheck
        self.messeges = mssg
        self.window = QWidget()
        
    def add_unavability(self, ilutz:aelosemTime_class)->None:
        self.unavability.append(ilutz)
    def remove_unavability(self,ilutz:aelosemTime_class)->None:
        self.unavability.remove(ilutz)
    # def taskIsDone(self,this_task:Task)->None:
    #     pass
    def read_messeges(self)->list:
        temp = (self.messeges)
        self.messeges = []
        return temp
    
    def show_task_clicked(self):
        self.window = QWidget()
        self.grid_layoutW = QGridLayout()
        self.window.setLayout(self.grid_layoutW)
        self.scroll = QScrollArea() 
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.window)
        self.setCentralWidget(self.scroll)
        self.setGeometry(600, 100, 1000, 900)
        self.setWindowTitle('Task of '+self.fname+" "+ self.lname)
        self.window.show()
    
        delTaskL = []
        doTaskL = []
       
        sTime = QLabel("")
        sTime.setText('Start time')
        
        showHistory = QPushButton('show history tasks')
        showHistory.clicked.connect(self.show_History_clicked) 
        
        dedline = QLabel("",)
        dedline.setText('End time')
        
        disc = QLabel("",)
        disc.setText('Task discreption')
        
        for i in range(len(self.tasks)):
            if len(self.tasks) >0:
                delTaskL.append(QPushButton())
                delTaskL[i].setText("cancel task")
                delTaskL[i].clicked.connect(self.tasks[i].cancel_task_clicked) 
        
        # for i in range(len(self.tasks)):
        #     if len(self.tasks) > 0 and self.tasks[i].cancel == False and self.tasks[i].done == False:
        #         doTaskBtnL.append(QPushButton())
        #         doTaskBtnL[i].setText("Do Task")
        #         doTaskBtnL[i].clicked.connect(self.tasks[i].do_task_clicked)
                
                
        for i in range(len(self.tasks)):
            if len(self.tasks) > 0 and self.tasks[i].cancel == False:
                if self.tasks[i].done == False:
                    doTaskL.append(QPushButton())
                    doTaskL[i].setText("check")
                    doTaskL[i].clicked.connect(self.tasks[i].changeStatusToDone)
          
        for i in range(1):
            for j in range(4):
                if j == 0:
                    self.grid_layoutW.addWidget(disc, i,j)
                elif j == 1:
                    self.grid_layoutW.addWidget(sTime, i,j)
                elif j == 2:
                    self.grid_layoutW.addWidget(dedline, i,j)
                elif j == 3:
                    self.grid_layoutW.addWidget(showHistory, i,j)
    
        row = 1               
        for i in range(len(self.tasks)):
            print(self.tasks[i].cancel)
            print(i)
            if self.tasks[i].cancel == False and self.tasks[i].done == False:
                for j in range(5):
                        if j == 0:
                            tmp = QLabel("")
                            tmp.setText(self.tasks[i].taskDescription)
                            self.grid_layoutW.addWidget(tmp, row,j)
                        elif j ==1:
                            tmp = QLabel("")
                            tmp.setText(str(self.tasks[i].startTime))
                            self.grid_layoutW.addWidget(tmp, row,j)
                        elif j==2:
                            tmp = QLabel("")
                            tmp.setText(str(self.tasks[i].deadline))
                            self.grid_layoutW.addWidget(tmp, row,j)
                        elif j==3:
                            self.grid_layoutW.addWidget(doTaskL[i], row,j)
                        else:
                            self.grid_layoutW.addWidget(delTaskL[i], row,j)
                row += 1
                    
               
        self.show()
    

    def show_History_clicked(self):
        self.histWin = QWidget()
        self.scroll = QScrollArea() 
        self.grid_layoutH = QGridLayout()
        self.histWin.setLayout(self.grid_layoutH)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.histWin)

        self.setCentralWidget(self.scroll)
        self.setGeometry(600, 100, 1000, 900)
        self.setWindowTitle('History tasks of '+ self.fname+' '+self.lname)
        self.show()
        
        row = 0
        
        for i in range(len(self.tasks)):
            if self.tasks[i].done == True:
                histL = QLabel("")
                histL.setText(self.tasks[i].taskDescription)
                self.grid_layoutH.addWidget(histL, row, 0)
                histL1 = QLabel("")
                histL1.setText(str(self.tasks[i].startTime))
                self.grid_layoutH.addWidget(histL1, row, 1)
                histL2 = QLabel("")
                histL2.setText(str(self.tasks[i].deadline))
                self.grid_layoutH.addWidget(histL2, row, 2)
                row +=1
        self.histWin.show()
        
    def emp_remove_clicked(self):
        self.fname = 0
        height = 200
        width = 400
        self.taskDoneMassage =QWidget()
        self.grid_layout = QGridLayout()
        self.taskDoneMassage.setWindowTitle('Mission status')
        self.taskDoneMassage.setLayout(self.grid_layout)
        self.taskDoneMassage.setFixedHeight(height)
        self.taskDoneMassage.setFixedWidth(width)
        self.missiondMassageL =  QLabel('employer removed seccesfully')
        self.missiondMassageL.setFont(QFont('Times', 10))
        self.grid_layout.addWidget(self.missiondMassageL,0,0,0,0)
        self.taskDoneMassage.show()
    
  
        