#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from rospy.topics import Publisher 
from std_msgs.msg import String

class Processor:
    def __init__(self):
        rospy.init_node("Processor",anonymous= True); # Initialize node 
        rospy.Subscriber('/serial/drive',String,self.drive); # Subscribe drive topic and send data to self.drive function 
        rospy.Subscriber('/serial/robotic_arm',String,self.robotic_arm); # Subscribe robotic_arm topic and send data to self.robotic_arm function
        
        self.pub_drive = rospy.Publisher("/position/drive",String,queue_size=10) # Assign drive Publisher

        self.pub_robotic_arm = rospy.Publisher("/position/robotic_arm",String,queue_size=10) # Assign robotic_arm Publisher

        rospy.spin() # keep continue until node stop 

    def drive(self,data): # process data coming from serial/drive topic
        if data.data[0] == "A" and data.data[len(data.data)-1] == "B": # check if data starts with A and end with B
            str_return = ""
            i = 1
            while i < len(data.data)-1:
                if(data.data[i] == "1"):
                    str_return += "-"
                i += 1
                val = int(data.data[i:i+3])
                if val > 255 :
                    val = 255
                i+=3
                str_return += (str (val) + " ")
            str_return = str_return[0:len(str_return)-1]
            self.pub_drive.publish(str_return)


    def robotic_arm(self,data):
        if data.data[0] == "A" and data.data[len(data.data)-1] == "B": # check if data starts with A and end with B
            str_return = ""
            i = 1
            while i < len(data.data)-1:
                if(data.data[i] == "1"):
                    str_return += "-"
                i += 1
                val = int(data.data[i:i+3])
                if val > 255 :
                    val = 255
                i+=3
                str_return += (str (val) + " ")
                    
            str_return = str_return[0:len(str_return)-1]
            self.pub_robotic_arm.publish(str_return)
    

	    
if __name__ == "__main__":
    p = Processor()