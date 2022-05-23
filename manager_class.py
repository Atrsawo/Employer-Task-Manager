from datetime import datetime
from resorce import Resource
from aelosemTime_class import aelosemTime
from employe_class import employer
# IMPORT RESOURCE CLASS
from task import Task

class manager:
    def __init__(self,list_of_employers,resources):
        self.list_of_employers = list_of_employers
        self.myResources = resources
    def add_employe(self,fname,lname,rule_in_company)->None:
        messeges=["welcome to your new job"]
        historyTask = []
        unavability = []
        tasks = []
        self.list_of_employers.append(employer(fname,lname,rule_in_company
                                    ,tasks,unavability,historyTask ,messeges) )
    def get_employe(self,temp_fname,temp_lname)->employer:
        for employe in self.list_of_employers:
            if employe.fname == temp_fname and employe.lname == temp_lname:
                return employe
            
    def remove_employe(self,employe:employer)->None:
        print(employe.fname )
        self.list_of_employers.remove(employe)  
       
        
    def new_messege(self,employe:employer,messege)->None:
        employe.messeges.append(messege)
        
   
    def find_tasks_by_title(self,title1:str)->list:
        temp_dict = {}
        for employe in self.list_of_employers:
            temp_list = []
            for task in employe.tasks:
                if title1 in task.taskDescription:
                    temp_list.append(task) 
            temp_dict[employe]=temp_list 
        return(temp_dict) 
       
    def new_task(self,fname, lname, itask:list): 
        '''1992-04-23T12:06:34''' 
        startTime = itask[0]
        
        startTime = datetime.strptime(itask[0], '%d/%m/%Y %H:%M')
        endTime = itask[1]
        endTime = datetime.strptime(itask[1], '%d/%m/%Y %H:%M')
        taskDiscription = itask[2]
        resourcesNames = itask[3]
        for resource in resourcesNames:
            resourceType=list(filter(lambda x:x.name==resource,self.myResources))
            flag=False
            for myresource in resourceType:
                if (myresource.checkAvailable(startTime,endTime)):
                    myresource.addBusy(aelosemTime(taskDiscription,startTime,endTime))
                    flag=True
                    break          
            if not(flag):
                print("not availabel resource")
                return False
        self.get_employe(fname, lname).tasks.append(Task(startTime,endTime,taskDiscription,resourcesNames,False))   
        print()
    def cancel_task(self,employe:employer,task:Task)->None:
        employe.tasks.remove(task)
        
    def add_resources(self,name:Resource)->None:
        counter = 0
        for resource in self.myResources:
            if name in resource.name:
                if resource.name.split(name)[1].isdigit():
                    counter +=1
        name = name+str(counter + 1)      
        unAvailableTime = []
        self.myResources.append(Resource(name,unAvailableTime))
        
    def del_resource(self,resource):
        self.myResources.remove(resource)
        
    def print_tasks_by_dates(self,itask:list)-> list:
        '''1992-04-23T12:06:34''' 
        startTime = itask[0]
        startTime = datetime.strptime(itask[0], '%d/%m/%Y %H:%M')
        endTime = itask[1]
        endTime = datetime.strptime(itask[1], '%d/%m/%Y %H:%M')
        temp_dict = {}
        for employe in self.list_of_employers:
            temp_list_of_tasks =[]
            for task in employe.tasks:
                if  not (task.startTime > endTime or task.deadline < startTime):
                    temp_list_of_tasks.append(task)
            temp_dict[employe]=temp_list_of_tasks 
        return temp_dict   
    def get_all_task_history(self)->list:
        tepm_list = []
        for employe in self.list_of_employers:
            temp_list += employe.historyTaskCheck
        return temp_list
        
    def get_employe_history_task(self,employe):
        return employe.historyTaskCheck
    
    def check_done_task(self,employe,task):
        employe.historyTaskCheck.append(task)
        print('task is done')
            
                    
                 
               
            
        
    
        
    
                
                 
        