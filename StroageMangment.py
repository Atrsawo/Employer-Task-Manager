#version 15/05/2022 22:33

import ast
import json
from datetime import datetime
from socket import socket

from matplotlib.font_manager import json_dump
from employe_class import employer 
from task import Task
from aelosemTime_class import aelosemTime
from resorce import Resource
###online 
import socket
import ast
import hashlib
##cinstant 
file_employers_name = 'employes.json'
file_Resources_name = 'resources.json'
file_login_name = 'login.json'
##
class StrogeUntily:
    print("version2.0.0")
    def Myisoformat(mytime:datetime)->str:
        if type(mytime)==datetime:
            mytime=mytime.isoformat()
        return mytime
     
    def Myfromisoformat(mytime:str)->datetime:
        try :
            mytime=datetime.fromisoformat(mytime)
            return mytime
        except:
            return None
            
            
           
    
    ### cast obj to dict 
    def EmployesObjtoDict(self,Employer:employer)->dict:
        return( {"Fname": Employer.fname,"Lname":Employer.lname, "rule_in_company":Employer.rule_in_company,
                "tasks":[StrogeUntily.TaskObjtoDict(task) for task in Employer.tasks],
                "unavailable":[self.aelosemTimesObjtoDict(unvaibal) for  unvaibal in Employer.unavability],
                "historyTasks":[self.TaskObjtoDict(task) for task in Employer.historyTaskCheck],
                "messeges":Employer.messeges
                })
    #resourcesNames
     #resourcesName          
    def TaskObjtoDict(Task:Task)->dict:
        return( {"StartTime":StrogeUntily.Myisoformat(Task.startTime),"endTime":StrogeUntily.Myisoformat(Task.deadline),
                "taskDescription":Task.taskDescription,"resources":Task.resourcesName,"done":Task.done}    )
    def aelosemTimesObjtoDict(self,aelosemTimes:aelosemTime)->dict:
        return {"title":aelosemTimes.title,"startTime":StrogeUntily.Myisoformat(aelosemTimes.startTime) ,"endTime":StrogeUntily.Myisoformat(aelosemTimes.endTime) }
    def ResourceObjtoDict(self,resources:Resource)->dict:
        return {"name": resources.name ,"unAvailableTime":[self.aelosemTimesObjtoDict(ilutz) for ilutz in resources.unAvailablityTime]}
    ###unAvailableTime
    #save obj from json file
    def SaveListEmployer(self,list:list):
        #try:
        dictList=[self.EmployesObjtoDict(employer) for employer in list ]
        file = open(file_employers_name, "w")
        json.dump(dictList, file,  indent=2 )
        file.close()
        #except:
            #print("EROR in try saveListEmployer")
            
    def SaveEmployer(self,employer:employer):
        '''add a new employer'''
        try:
            #open file
            file = open(file_employers_name, "r")
            dictList= json.load(file)
            #add employer 
            dictList.append(self.EmployesObjtoDict(employer))
            file.close()
            ##reopen file as write file
            file= open(file_employers_name, "w")
            json.dump(dictList, file,  indent=2)
        except:
             print("EROR in try saveEmployer")
        
        file.close()   
    def SaveResources(self,resources:list):
        
        ResourceList=[self.ResourceObjtoDict(resource) for resource in resources]
        file= open(file_Resources_name,"w")
        json.dump(ResourceList, file,  indent=2)
        #except: 
            #print("EROR in try saveResource")
        file.close()
    #get obj from  json file
    def GetListEmployer(self)->list:
        file = open(file_employers_name,"r")
        ListEmployer= json.load(file)
        file.close()
        print(type(ListEmployer))
        print(type(ListEmployer[0]))
        return (
                [
                employer(Employer["Fname"],Employer["Lname"],Employer["rule_in_company"],
                #bulid task list for ech employer
                [
                Task(StrogeUntily.Myfromisoformat(task["StartTime"]),
                StrogeUntily.Myfromisoformat(task["endTime"]),
                task["taskDescription"],task["resources"], task["done"]
                )for task in Employer["tasks"]
                ],
                #bulid aelosemTime for ech employer
                [
                    aelosemTime(StrogeUntily.Myfromisoformat(aelos["StartTime"]),
                    StrogeUntily.Myfromisoformat(aelos["endTime"]),aelos["title"]
                    )for aelos in Employer["unavailable"]
                    
                ],
                #bulid historyTasks for ehc employer
                [
                Task(StrogeUntily.Myfromisoformat(task["startTime"]),
                StrogeUntily.Myfromisoformat(task["endTime"]),
                task["taskDescription"],task["resources"], task["done"]
                )for task in Employer["historyTasks"]
                ],Employer["messeges"]
                )for Employer in ListEmployer
                ])
    
            
    def GetEmployer(self,EmployerName:str)->employer:
        file = open(file_employers_name,"r")
        ListEmployer= json.load(file)
        file.close()
        #find the employer
        Employer= list(filter(lambda x:x["Fname"]==EmployerName,ListEmployer))[0]
        return (employer
            (
                Employer["Fname"],Employer["Lname"],Employer["rule_in_company"],
                #bulid task list for ech employer
                  [
                   Task(StrogeUntily.Myfromisoformat(task["StartTime"]),
                   StrogeUntily.Myfromisoformat(task["endTime"]),
                   task["taskDescription"],task["resources"], task["done"]
                   )for task in Employer["tasks"]
                  ],
                #bulid aelosemTime for ech employer
                  [
                    aelosemTime(StrogeUntily.Myfromisoformat(aelos["StartTime"]),
                    StrogeUntily.Myfromisoformat(aelos["endTime"]),aelos["title"]
                    )for aelos in Employer["unavailable"]
                      
                  ],
                #bulid historyTasks for ehc employer
                  [
                   Task(StrogeUntily.Myfromisoformat(task["startTime"]),
                   StrogeUntily.Myfromisoformat(task["deadline"]),
                   task["taskDescription"],task["resource"], task["done"]
                   )for task in Employer["historyTasks"]
                  ],Employer["messeges"]
             ))
        
    def GetResources(self)->list:
        file = open(file_Resources_name,"r")
        resources= json.load(file)
        file.close()
        ###craet Resource
        CreatIlutz=lambda x: aelosemTime(x["title"],StrogeUntily.Myfromisoformat(x["startTime"]),StrogeUntily.Myfromisoformat(x["endTime"]))
        ListOfUnAvailableTime=[resource["unAvailableTime"] for resource in resources ]
        b=[list(map(CreatIlutz,ilutzs)) for ilutzs in ListOfUnAvailableTime]
        return [Resource(resources[i]["name"],b[i] ) for i in range(len(b))]
        
        
    #update obj from json file
    def updateEmployer(EmployerName:str,UpdateType:str,UpdateValue:str):
        file = open(file_employers_name,"r")
        ListEmployer= json.load(file)
        file.close()
        #find the employer
        Employer= list(filter(lambda x:x["Fname"]==EmployerName,ListEmployer))[0] # [UpdateType]=UpdateValue
        #update
        Employer[UpdateType]=UpdateValue
        #update the employer 
        file= open(file_employers_name,"w")
        json.dump(ListEmployer, file,  indent=2)
        file.close()
    def updateResource(resourceName:str,UpdateType:str,UpdateValue:str):
        file = open(file_Resources_name,"r")
        resources = json.load(file)
        file.close()
        resource= list(filter(lambda x:x["name"]==resourceName,resources))[0]
        resource[UpdateType]=UpdateValue
        file= open(file_Resources_name,"w")
        json.dump(resources, file,  indent=2)
        file.close()
    def udpateEmployerTask(EmployerName:str,taskDescription:str,TaskUpdateType:str,TaskUpdateValue:str):
        file = open(file_employers_name,"r")
        ListEmployer=json.load(file)
        file.close()
        Employer=list(filter(lambda x:x["Fname"]==EmployerName,ListEmployer))[0]
        task=list(filter(lambda x:x["taskDescription"]==taskDescription,Employer["tasks"]))[0]   
        task[TaskUpdateType]=TaskUpdateValue
        file= open(file_employers_name,"w")
        json.dump(ListEmployer, file, )
        file.close()
        ##update resource
        
    
    ###online 
    def sendData(data:dict,mesagePost)->str: 
        '''#mesagePost =b"save@sample_file.json@"'''
        try:
            HOST = "127.0.0.1"  # The server's hostname or IP address
            PORT = 65432  # The port used by the server
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                s.send(mesagePost)
                sendfile= json.dumps(data).encode('utf-8')    
                sendfileSplit= [sendfile[i:i+1000] for i in range(0,len(sendfile),1000)]
                #update
                #send files
                for mesage in sendfileSplit:         
                    s.sendall(mesage)
                return s.recv(1024) # ok code ==200 false have 401
        except:
            return b"401"
    def reciveData(mesagePost)->dict: 
        '''#mesagePost ="get@save@sample_file.json'''
        try:
            HOST = "127.0.0.1"  # The server's hostname or IP address
            PORT = 65432  # The port used by the server
            tempdata=[]
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                s.send(mesagePost)
                while True:
                    data = s.recv(1024)
                    if data:
                        tempdata.append(data)
                    if len(data)<1024:
                        break
                return ((b''.join(tempdata)).decode('utf-8'))
        except:
            return b"401"
            
    def SaveListEmployerOnline(self,data:list):
        mesagePost=b"save@"+file_employers_name.encode("utf-8")+b"@"
        dictList=[self.EmployesObjtoDict(employer) for employer in data ]
        count=0
        code= StrogeUntily.sendData(dictList ,mesagePost)
        while code == b"401":
            code=StrogeUntily.sendData(dictList ,mesagePost)
            count+=1
            if count>50:
                break
        return code
            
    def SaveResourcesOnline(self,resources:list)->None:
        mesagePost=b"save@"+file_Resources_name.encode("utf-8")+b"@"
        dictList=[self.ResourceObjtoDict(resource) for resource in resources]
        count=0
        code=StrogeUntily.sendData(dictList ,mesagePost)
        while code == b"401":
            code=StrogeUntily.sendData(dictList ,mesagePost)
            count+=1
            if count>50:
                break
        return code
        
    
    def GetListEmployerOnline(self)->list:
        #try:
            mesagePost=b"get@"+file_employers_name.encode("utf-8")
            count=0
            flag =False   
            employerList=b"401" 
            while employerList==b"401" or not flag:
                employerList=StrogeUntily.reciveData(mesagePost)
                count+=1
                if count>50:
                    return None
                try:
                    employerdict=json.loads(employerList)
                    flag=True
                except:
                    print('eror in data get list employer online')
                
                
            return(
                    [
                    employer(Employer["Fname"],Employer["Lname"],Employer["rule_in_company"],
                    #bulid task list for ech employer
                    [
                    Task(StrogeUntily.Myfromisoformat(task["StartTime"]),
                    StrogeUntily.Myfromisoformat(task["endTime"]),
                    task["taskDescription"],task["resources"], task["done"]
                    )for task in Employer["tasks"]
                    ],
                    #bulid aelosemTime for ech employer
                    [
                        aelosemTime(StrogeUntily.Myfromisoformat(aelos["startTime"]),
                        StrogeUntily.Myfromisoformat(aelos["endTime"]),aelos["title"]
                        )for aelos in Employer["unavailable"]
                        
                    ],
                    #bulid historyTasks for ehc employer
                    [
                    Task(StrogeUntily.Myfromisoformat(task["StartTime"]),
                    StrogeUntily.Myfromisoformat(task["endTime"]),
                    task["taskDescription"],task["resources"], task["done"]
                    )for task in Employer["historyTasks"]
                    ],Employer["messeges"]
                    )for Employer in  employerdict
                    ])
        # except: 
        #     return None
     
    def GetResourcesOnline(self)->list:
        try:
            mesagePost=b"get@"+file_Resources_name.encode("utf-8")
            count=0
            
            ResorcesList=StrogeUntily.reciveData(mesagePost)
            while ResorcesList == b"401":
                ResorcesList=StrogeUntily.reciveData(mesagePost)
                count+=1
                if count>50:
                    return b"401"
            Resourcesdict=json.loads(ResorcesList)
            ###craet Resource
            CreatIlutz=lambda x: aelosemTime(x["title"],StrogeUntily.Myfromisoformat(x["startTime"]),StrogeUntily.Myfromisoformat(x["endTime"]))
            ListOfUnAvailableTime=[resource["unAvailableTime"] for resource in Resourcesdict ]
            b=[list(map(CreatIlutz,ilutzs)) for ilutzs in ListOfUnAvailableTime]
            return [Resource(Resourcesdict[i]["name"],b[i] ) for i in range(len(b))]
        except:
            return b"401"

           
        
        
    def chek_login(username:str, password:str)->bool:
        #online
        try:
            mesagePost= b"login@"+file_login_name.encode("utf-8")+b"@"
            hash_username= hashlib.sha256(username.encode()).hexdigest()
            hash_password= hashlib.sha256(password.encode()).hexdigest()
            data={hash_username:hash_password}
            code= StrogeUntily.sendData(data,mesagePost)
            #employe login
            if code == b"202":
                return 202
            #manger login
            elif code == b"203":
                return 203
            elif code ==b"402":
                print("password is incorrect")
                return 402 
            elif code ==b"403":
                print("username is incorrect")
                return 403
            elif code == b"404":
                print("user is login another computer")
                return 404
        except:
            return b"401"
    def chek_login_offline(self,username:str, password:str)->bool:
        
        hash_username= hashlib.sha256(username.encode()).hexdigest()
        hash_password= hashlib.sha256(password.encode()).hexdigest()
        try:
            file =open(file_login_name,"r")
            loginDict= json.load(file)
        except:
            return False
        if hash_username in loginDict.keys():
            if loginDict[hash_username]==hash_password:
                return True
        return False
    def add_login(username:str, password:str,userType:str)->int:
        '''return b"200" ok b"401 false'''
        #online
        try:
            mesagePost= b"addUser@"+file_login_name.encode("utf-8")+b"@"
            hash_username= hashlib.sha256(username.encode()).hexdigest()
            hash_password= hashlib.sha256(password.encode()).hexdigest()
            data={hash_username:[hash_password,userType,False]}
            return StrogeUntily.sendData(data,mesagePost)
        except:
            return b"401"
    def add_login_offline(username:str, password:str)->None:
        hash_username= hashlib.sha256(username.encode()).hexdigest()
        hash_password= hashlib.sha256(password.encode()).hexdigest()
        try:
            file= open(file_login_name,"r")
            data= json.load(file)
        except:
            print("no file we open new one")
            data= {}
            
        
        data[hash_username]=hash_password
        file =open(file_login_name,"w")
        json.dump(data, file)
        file.close()
    def qxitlogin(username:str):
        try:
            mesagePost= b"exitlogin@"+file_login_name.encode("utf-8")+b"@"
            hash_username= hashlib.sha256(username.encode()).hexdigest()
            data=hash_username
            code= StrogeUntily.sendData(data,mesagePost)
            if code == b"200":
                return 200
        except:
            return b"401"
        
 
   
        
        
    
        
          
        
        
        