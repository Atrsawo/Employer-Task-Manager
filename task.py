
from datetime import datetime
from importlib.resources import Resource

#from manager_class import manager
from PyQt5.QtWidgets import *
from matplotlib.pyplot import text
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QSize

class Task():
    def __init__(self, startTime, deadline, taskDescription, resourcesNames, done = False, cancel = False ):
        self.app = QApplication([])
        self.startTime = startTime #datetime.strptime(startTime,"%Y-%m-%d %H:%M") #startTime
        
        self.deadline = deadline #datetime.strptime(deadline,"%Y-%m-%d %H:%M") #deadline
        
        self.taskDescription = taskDescription
       
        self.resourcesName = resourcesNames #[{"name": "computer1", "unAvailableTime": []}, {"name": "coumpter2", "unAvailableTime": []}] #resources
        
        self.done = done
        
        self.cancel = cancel
        
        self.taskDoneMassage = QWidget()
        
        self.grid_layoutD = QGridLayout()
        
        self.adddNewTask = QWidget() 
        
    def cancel_task_clicked(self):
        print('task cancled')
        self.cancel = True
        print(self.cancel)
                
    def changeStatusToDone(self):
        print('checked')
        self.done = True
        height = 200
        width = 400
        self.taskDoneMassage.setWindowTitle('Mission status')
        self.taskDoneMassage.setLayout(self.grid_layoutD)
        self.taskDoneMassage.setFixedHeight(height)
        self.taskDoneMassage.setFixedWidth(width)
        
        self.missiondMassageL =  QLabel('Mission done seccecfully')
        self.grid_layoutD.addWidget(self.missiondMassageL,0,0,0,0)
        self.taskDoneMassage.show()
      
