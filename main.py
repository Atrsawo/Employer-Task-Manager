
from datetime import datetime
from resorce import Resource
import sys
from gui import Gui
from StroageMangment import StrogeUntily
from manager_class import manager
from employe_class import employer
from task import Task
# from resorce import Resource

def main():
    storage = StrogeUntily()
    resoList = ["hammer","computer","hammer","computer","airhammer"]
    mngr =  manager(storage.GetListEmployer(),storage.GetResources() )
    storage.SaveListEmployer(mngr.list_of_employers)
    for resname in resoList:
        mngr.add_resources(resname)
    g = Gui(mngr,storage)
 

if __name__== '__main__':  
    main() 
    exit(0)
    
       
 
    
    