from timer.models import Activity
from random import randint


def returnRandomActivity():
    activity_title = " "
    with open("list_of_activities.txt", "r") as ins:
        array = []
        for line in ins:
            array.append(line)   
            
        activity_title = array[randint(0, (len(array) - 1))]
    
    
            
    
    
    
