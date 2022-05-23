
from asyncio import tasks
from datetime import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow,)

#from StroageMangment import StrogeUntily

class Gui(QMainWindow):
    
    def __init__(self, mng,storge):
        super().__init__()
        self.storge=storge
        self.mng = mng
        self.app = QApplication([])
        self.pswd = QWidget()
        self.pswd.setWindowTitle('WELCOME')
        self.pswd.setFixedWidth(520)
        
        width, height = 800,800
        self.window = QWidget()
        self.task = QWidget()
        
        self.missionFaildMassage = QWidget() #reson massage window when employer cana't do a task
        self.taskDoneMassage  = QWidget() 
        self.addTaskWin = QWidget()

        
        self.grid_layoutT = QGridLayout()
        self.grid_layoutF = QGridLayout()
        self.grid_layoutD = QGridLayout()
        
        self.window.setWindowTitle('Employers tasks manager App')
        self.window.setFixedHeight(height)
        self.window.setFixedWidth(width) 
    
        self.nameLabel = QLabel('User Name',self.pswd)
        self.nameLabelEdit = QLineEdit(self.pswd)
        self.nameLabel.setBuddy(self.nameLabelEdit)
        
        self.passwordLabel = QLabel('Password',self.pswd)
        self.passwordLineEdit = QLineEdit(self.pswd)
        self.passwordLabel.setBuddy(self.passwordLineEdit)

        self.btnOK = QPushButton('OK')
        self.btnCancel = QPushButton('Cancel')
        self.btnOK.clicked.connect(self.btnOK_clicked)
        self.btnCancel.clicked.connect(self.btnCancel_clicked)
        
        
        mainLayout = QGridLayout(self.pswd)
        mainLayout.addWidget(self.nameLabel,0,0)
        mainLayout.addWidget(self.nameLabelEdit,0,1,1,2)
        
        mainLayout.addWidget(self.passwordLabel,1,0)
        mainLayout.addWidget(self.passwordLineEdit,1,1,1,2)

        mainLayout.addWidget(self.btnOK,2,1)
        mainLayout.addWidget(self.btnCancel,2,2)
        self.pswd.show()
        
        welcome = QLabel('Right',self.window)
        welcome.setText("Welcome to your employers manager App")
        welcome.move(260, 6)

        credit = QLabel('Right',self.window)
        credit.setText("@Developed by Maheir, Shiraz, Ziv, Port and Gil ")
        credit.move(250, 780)

        photo = QLabel('Left',self.window)
        pngPhoto = QPixmap('image.png')
        photo.setPixmap(pngPhoto)
        photo.resize(800,800)
        

        get_started = QPushButton("Get Started",self.window)
        get_started.move(245,100)#setGeometry(350,600, 100, 100)
        get_started.setStyleSheet("background-color: transparent;""border: 3px solid gray;"
                                "border-radius: 15px;""color: lightblack; ""font-size: 50px;")
        get_started.clicked.connect(self.get_started_clicked)
        ###online
        get_started_online = QPushButton("online",self.window)
        #get_started_online.move(0,0)#setGeometry(350,600, 100, 100)
        # get_started.setStyleSheet("background-color: transparent;""border: 3px solid gray;"
        #                         "border-radius: 15px;""color: lightblack; ""font-size: 50px;")
        get_started_online.clicked.connect(self.get_started_clicked_online)
        ###
        self.app.exec()
        
        
            
    def btnOK_clicked(self,psw):
        psw = self.passwordLineEdit.text()
        userName = self.nameLabelEdit.text()
        
        if  self.storge.chek_login_offline(userName,psw):
            self.window.show()
            self.pswd.close()
        else:     
            self.nameLabel.setText('EROOR: incorrrect password or user name, try again')
            
        
        
    def btnCancel_clicked(self):
            self.pswd.close()
            exit(0)
    
    def get_started_clicked_online(self):
        pass
    def get_started_clicked(self):
        self.emp = QWidget()
        self.scroll = QScrollArea() 
        self.grid_layoutE = QGridLayout()
        self.emp.setLayout(self.grid_layoutE)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.emp)

        self.setCentralWidget(self.scroll)
        self.setGeometry(600, 100, 1000, 900)
        self.setWindowTitle('List of employers')
        
        addTask = QPushButton('add task')
        addTask.clicked.connect(self.add_task_clicked)
        
        self.saveData = QPushButton('Save updated Data')
        self.saveData.clicked.connect(self.saveData_cliked)
        self.findTask = QPushButton('Shearch for  Task')
        self.findTask.clicked.connect(self.findTask_clicked)
        self.findTask.setStyleSheet("background-color:white")
        self.btnOK.clicked.connect(self.btnOK_clicked)
        
        self.emp.show()
        
        size = 0
        for i in range(len(self.mng.list_of_employers )):
            if self.mng.list_of_employers[i].fname != 0:
                size += 1
                
                
        size = len(self.mng.list_of_employers)
        print("size= ", size)
        
        self.detailLst = []
        self.removeEmpL = []
        
        fnameL =  QLabel('Left',self.emp)
        fnameL.setText('First name')
        
        lnameL = QLabel('Left',self.emp)
        lnameL.setText('Last name') 
        
        rullL = QLabel('Left',self.emp)
        rullL.setText('Rul')
                    
        for i in range(len(self.mng.list_of_employers)):
            if self.mng.list_of_employers[i].fname != 0:
                btn = QPushButton(" ")
                btn.setText("show employer task detail of "+ self.mng.list_of_employers[i].fname +" "+ self.mng.list_of_employers[i].lname)
                btn.clicked.connect(self.mng.list_of_employers[i].show_task_clicked)
                self.detailLst.append(btn)
        
        
        addEmpB = QPushButton("Add new employer")
        addEmpB.clicked.connect(self.add_employer_clicked)

        for i in range(len(self.mng.list_of_employers)):
            if self.mng.list_of_employers[i].fname != 0:
                rembtn = QPushButton("")
                rembtn.setText("Remove employer")
                rembtn.clicked.connect(self.mng.list_of_employers[i].emp_remove_clicked)
                self.removeEmpL.append(rembtn)
        
        for i in range( 0,1):
            for j in range(7):
                if i == 0 :
                    if j == 0:
                        self.grid_layoutE.addWidget(fnameL, i, j)
                    elif j == 1:
                         self.grid_layoutE.addWidget(lnameL, i, j)
                    elif j == 2:
                         self.grid_layoutE.addWidget(rullL, i, j)
                    elif j == 3:
                         self.grid_layoutE.addWidget(addEmpB, i, j)
                    elif j==4:
                        self.grid_layoutE.addWidget(addTask, i, j)
                    elif j==5:
                        self.grid_layoutE.addWidget(self.findTask, i, j) 
                    else:
                        self.grid_layoutE.addWidget(self.saveData, i, j)  
                        
        row = 1
        
        for i in range(len(self.mng.list_of_employers)):
                if self.mng.list_of_employers[i].fname != 0:
                    
                    tmpL = QLabel("")
                    print(self.mng.list_of_employers[i].fname)
                    tmpL.setText(self.mng.list_of_employers[i].fname)
                    self.grid_layoutE.addWidget(tmpL, row , 0)#adding employer first name
                    
                    tmpL1 = QLabel("")
                    tmpL1.setText(self.mng.list_of_employers[i].lname)
                    self.grid_layoutE.addWidget(tmpL1, row,1)#adding employer last name
                    
                    tmpL2 = QLabel("")
                    tmpL2.setText(self.mng.list_of_employers[i].rule_in_company)
                    self.grid_layoutE.addWidget(tmpL2, row,2)#adding employer rull in compeny
                    row +=1
                    
        for i in range(1,len(self.detailLst)+1):
                self.grid_layoutE.addWidget(self.detailLst[i-1],i,3)
                self.grid_layoutE.addWidget(self.removeEmpL[i-1],i,4)  
        self.show()
    
    def saveData_cliked(self):  #save updated data
        self.storge.SaveListEmployer(self.mng.list_of_employers)
        self.storge.SaveResources(self.mng.myResources)
        print('data saved')
        
    def findTask_clicked(self):
        self.findTaskWin = QWidget()
        self.findTaskWin.setWindowTitle("Task shearching window")
        self.findTaskWin.setFixedHeight(400)
        self.findTaskWin.setFixedWidth(800)
        self.grid_layoutS = QGridLayout()
        self.findTaskWin.setLayout(self.grid_layoutS)
       
        disToSearchL = QLabel('Discription')
        self.disToSearchlLEdit = QLineEdit()
        disToSearchL.setBuddy(self.disToSearchlLEdit)
        
        searchDisBtn = QPushButton("sreach")
        searchDisBtn.clicked.connect(self.searchDisBtn_clicked)
        self.grid_layoutS.addWidget(searchDisBtn,0,3)
        
        searchDisBtnD = QPushButton("sreach")
        searchDisBtnD.clicked.connect(self.serachByDate_clicked)
        self.grid_layoutS.addWidget(searchDisBtnD,1,4)
        
        self.grid_layoutS.addWidget(disToSearchL,0,0)
        self.grid_layoutS.addWidget(self.disToSearchlLEdit,0,1,1,1)
        self.grid_layoutS.addWidget(searchDisBtn, 0, 2)
        
        self.startTime = QLabel('Start Time',self.findTaskWin)
        self.startTimeEdit = QDateTimeEdit(self.findTaskWin)
        self.startTime.setBuddy(self.startTimeEdit)
        
        self.grid_layoutS.addWidget(self.startTime, 1,0)
        self.grid_layoutS.addWidget(self.startTimeEdit,1,1)
        self.startTimeEdit.setFixedWidth(200)
        self.endTime = QLabel('End Time',self.findTaskWin)
        self.endTimeEdit = QDateTimeEdit(self.findTaskWin)
        self.endTime.setBuddy(self.endTimeEdit)
        self.grid_layoutS.addWidget(self.endTime, 1,2)
        self.grid_layoutS.addWidget(self.endTimeEdit,1,3)
        
        self.findTaskWin.show()
        
    def searchDisBtn_clicked(self):
        text = self.disToSearchlLEdit.text()
        dict = self.mng.find_tasks_by_title(text)
        dict2 = {}
        for key,val in dict.items():
            if len(val) > 0:
                dict2[key]=val
                

        self.showFindTaskWin = QWidget()
        self.scroll1 = QScrollArea() 
        self.showFindTaskWin.setWindowTitle("Tasks by discription")
        self.grid_layoutFS = QGridLayout()
        self.showFindTaskWin.setLayout(self.grid_layoutFS) 
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.showFindTaskWin)
        self.setCentralWidget(self.scroll)
        self.setGeometry(600, 100, 1000, 900)
        self.showFindTaskWin.show()
        
        row = 0 
        for key,val in  dict2.items():
            
            for task in val:
                str0 = key.fname+" "+key.lname +":"
                str1 = str(task.startTime) + " "+ str(task.deadline) + " "+task.taskDescription
                l = QLabel("")
                l.setText(str0+" "+str1)
                self.grid_layoutFS.addWidget(l,row,0)
                row +=1
            
        self.show()
    
    def serachByDate_clicked(self):
        self.showFindTaskDateWin = QWidget()
        self.scroll1 = QScrollArea() 
        self.showFindTaskDateWin.setWindowTitle("Tasks search by date")
        self.grid_layoutFSD = QGridLayout()
        self.showFindTaskDateWin.setLayout(self.grid_layoutFSD) 
        self.scroll1.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll1.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll1.setWidgetResizable(True)
        self.scroll1.setWidget(self.showFindTaskDateWin)
        self.setCentralWidget(self.scroll1)
        self.setGeometry(600, 100, 1000, 900)
        
       
        self.showFindTaskDateWin.show()
        startDate = self.startTimeEdit.text()
        endTime = self.endTimeEdit.text()
        dict=self.mng.print_tasks_by_dates([startDate,endTime])
        dict2 = {}
        
        for key,val in dict.items():
            if len(val) > 0:
                dict2[key]=val
        row = 0 
        for key,val in  dict2.items():
            
            for task in val:
                str0 = key.fname+" "+key.lname +":"
                str1 = str(task.startTime) + " "+ str(task.deadline) + " "+task.taskDescription
                l = QLabel("")
                l.setText(str0+" "+str1)
                self.grid_layoutFSD.addWidget(l,row,0)
                row +=1
        self.show()
        
    def add_task_clicked(self):
        print('adding task')
        self.addTaskWin = QWidget()
        grid_layoutTmp = QGridLayout()
        
        self.addTaskWin.setWindowTitle('Create Mission')
        self.addTaskWin.setLayout(grid_layoutTmp)
        self.addTaskWin.setFixedHeight(600)
        self.addTaskWin.setFixedWidth(600)
        
        self.fnameL = QLabel("First Name")
        self.fnameLedit = QLineEdit(self.addTaskWin)
        self.fnameL.setBuddy(self.nameLabelEdit)
        grid_layoutTmp.addWidget(self.fnameL, 0,0)
        grid_layoutTmp.addWidget(self.fnameLedit,0,1,1,2)
        
        self.lnameL = QLabel("Last Name")
        self.lnameLedit = QLineEdit(self.addTaskWin)
        self.lnameL.setBuddy(self.nameLabelEdit)
        grid_layoutTmp.addWidget(self.lnameL, 1,0)
        grid_layoutTmp.addWidget(self.lnameLedit,1,1,1,2)
        
        self.discription = QLabel('Discription',self.addTaskWin)
        self.discriptionEdit = QLineEdit(self.addTaskWin)
        self.discription.setBuddy(self.discriptionEdit)
        grid_layoutTmp.addWidget(self.discription, 2,0)
        grid_layoutTmp.addWidget(self.discriptionEdit,2,1,1,2)
        
        self.startTime = QLabel('Start Time',self.addTaskWin)
        self.startTimeEdit = QDateTimeEdit(self.addTaskWin)
        self.startTime.setBuddy(self.startTimeEdit)
        grid_layoutTmp.addWidget(self.startTime, 3,0)
        grid_layoutTmp.addWidget(self.startTimeEdit,3,1,1,2)
        
        self.endTime = QLabel('End Time',self.addTaskWin)
        self.endTimeEdit = QDateTimeEdit(self.addTaskWin)
        self.endTime.setBuddy(self.endTimeEdit)
        grid_layoutTmp.addWidget(self.endTime, 4,0)
        grid_layoutTmp.addWidget(self.endTimeEdit,4,1,1,2)
        
        self.resurce = QLabel('Resource',self.addTaskWin)
        self.resurceEdit = QComboBox(self.addTaskWin)
        names = [res.name for res in self.mng.myResources]
        self.resurceEdit.addItems(names)
        self.resurce.setBuddy(self.resurceEdit)
        grid_layoutTmp.addWidget(self.resurce, 5,0)
        grid_layoutTmp.addWidget(self.resurceEdit,5,1,1,2)
        
        self.btnCreateTask = QPushButton('Create task')
        self.btnCreateTask.clicked.connect(self.btnCreateTask_clicked)
        
        self.btnCencelCreatingTask = QPushButton('Cancel')
        self.btnCencelCreatingTask.clicked.connect(self.cancel_creating_clicked)
        grid_layoutTmp.addWidget(self.btnCreateTask, 6,0)
        grid_layoutTmp.addWidget(self.btnCencelCreatingTask, 6,1)
        
        self.addTaskWin.show()
        
    def btnCreateTask_clicked(self):  #Task create
        print('creating task')
        fname = self.fnameLedit.text()
        lname = self.lnameLedit.text()
        t = []
        t.append(self.startTimeEdit.text())
        t.append(self.endTimeEdit.text())
        t.append(self.discriptionEdit.text())
        t.append(self.resurceEdit.currentText().split(","))
        t.append(None)
        t.append(None)
        
        if  not self.mng.new_task(fname,lname,t):

            self.addTaskWinMass = QWidget()
            grid_layoutTmp = QGridLayout()
            
            self.addTaskWinMass.setWindowTitle('Create Mission Massage')
            self.addTaskWinMass.setLayout(grid_layoutTmp)
            self.addTaskWinMass.setFixedHeight(200)
            self.addTaskWinMass.setFixedWidth(400)
            msgL = QLabel("Warring: Task could not create")
            rscl = QLabel(self.resurceEdit.currentText()+ " is missing")
            self.grid_layoutTmp.addWidget(msgL,0,0)
            self.grid_layoutTmp.addWidget(rscl,0,0)
            self.addTaskWinMass.show()
            
        self.fnameLedit.clear()
        self.lnameLedit.clear()
        self.endTimeEdit.clear()
        
    def cancel_creating_clicked(self):
        self.addTaskWin.close()
        self.addEmployer = QWidget()
        grid_layoutA = QGridLayout()
        self.addEmployer.setWindowTitle('Add new Emloyer')
        self.addEmployer.setLayout(grid_layoutA)
        self.addEmployer.setFixedWidth(400)
        self.addEmployer.setFixedHeight(300)
        
    def add_employer_clicked(self):
        self.addEmployer = QWidget()
        grid_layoutA = QGridLayout()
        self.addEmployer.setWindowTitle('Add new Emloyer')
        self.addEmployer.setLayout(grid_layoutA)
        self.addEmployer.setFixedWidth(400)
        self.addEmployer.setFixedHeight(300)
        
        self.fnameL =  QLabel('First Name',self.addEmployer)
        self.fnameLEdit = QLineEdit(self.addEmployer)
        self.fnameL.setBuddy(self.fnameLEdit)
        grid_layoutA.addWidget(self.fnameL, 0,0)
        grid_layoutA.addWidget(self.fnameLEdit,0,1,1,2)
        
        self.lnameL = QLabel('Last Name',self.addEmployer)
        self.lnameLEdit = QLineEdit(self.addEmployer)
        self.lnameL.setBuddy(self.lnameLEdit)
        grid_layoutA.addWidget(self.lnameL, 1,0)
        grid_layoutA.addWidget(self.lnameLEdit,1,1,1,2)
        
        self.rullL = QLabel('Rull',self.addEmployer)
        self.rullLEdit = QLineEdit(self.addEmployer)
        self.rullL.setBuddy(self.rullLEdit)
        grid_layoutA.addWidget(self.rullL, 2,0)
        grid_layoutA.addWidget(self.rullLEdit,2,1,1,2)
        
        addOK = QPushButton('OK')
        bCancel = QPushButton('Cencel')
        
        grid_layoutA.addWidget(addOK,4,1)
        grid_layoutA.addWidget(bCancel,4,2)
        addOK.clicked.connect(self.addOK_clicked) 
        bCancel.clicked.connect(self.bCancel_clicked)
        
        
        self.addEmployer.show()
    
    def addOK_clicked(self):
    
        self.mng.add_employe(self.fnameLEdit.text(), self.lnameLEdit.text(), self.rullLEdit.text())
        self.fnameLEdit.clear()
        self.lnameLEdit.clear()
        self.rullLEdit.clear()

    
    def bCancel_clicked(self):
        
        self.addEmployer.close()
        
        
    

