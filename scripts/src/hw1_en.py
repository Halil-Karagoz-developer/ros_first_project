#!/usr/bin/env python 

#My generator code
import rospy
from std_msgs.msg import String
from random import randint,choice
import string

class Encoder:
    def __init__(self):
        rospy.init_node("encoder")
        self.pub_16 = rospy.Publisher("/serial/drive",String,queue_size= 10)
        self.pub_24 = rospy.Publisher("/serial/robotic_arm",String,queue_size= 10)
        self.continue_forever()

    def random_number(self,how_many):
        str_r = ""
        for i in range(how_many):
            val = randint(0,300)
            sign = randint(0,1)
            # can be done also using mod operation !
            new_str = "{}{:03}".format(str(sign),val)
            str_r += new_str
        return str_r

    def random_16(self):
        str_f = "A"
        str_f += self.random_number(4)
        str_f += "B"
        return str_f

    def random_24(self):
        str_f = "A"
        str_f += self.random_number(6)
        str_f += "B"
        return str_f

    def random_wrong16(self):
        str_f = ""
        str_f +=choice(string.ascii_letters)
        str_f += self.random_number(4)
        str_f +=choice(string.ascii_letters)
        return str_f

    def random_wrong24(self):
        str_f = ""
        str_f +=choice(string.ascii_letters)
        str_f += self.random_number(6)
        str_f +=choice(string.ascii_letters)
        return str_f
    
            
    def continue_forever(self):
        rate = rospy.Rate(2) # 2hz
        while not rospy.is_shutdown():
            if (randint(0,1)):
                if (randint(0,1)):
                    self.pub_16.publish(self.random_16())
                else:
                    self.pub_16.publish(self.random_wrong16())

            else :
                if (randint(0,1)):
                    self.pub_24.publish(self.random_24())
                else:
                    self.pub_24.publish(self.random_wrong24())
        
            rate.sleep()


if __name__ == '__main__':
    e = Encoder();