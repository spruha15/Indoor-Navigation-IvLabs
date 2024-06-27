#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist 
import random

if __name__ == '__main__':
    rospy.init_node('Random_Motion')
    rospy.loginfo('Random motion has been started')
    pub = rospy.Publisher('/cmd_vel',Twist,queue_size=10)
    rate = rospy.Rate(5)



    #l = [0.3,0.6,0.9,1,2,2.3,2.6,2.9,3] #linear velocity
    #l1 = [0.2,0.4,0.6,0.8,1,1.2,1.4,1.6]#angular velocity

    #v = random.choice(l)
    #w = random.choice(l1)

    while not rospy.is_shutdown():
        l = [0.3,0.6,0.9,1,1.3,1.5,2] #linear velocity
        l1 = [1.57,-1.57,0.5,0.3]#angular velocity
        l2 = [0.3,0.6,0.9,1,2,2.3,2.6,2.9,3]#y axis linear velocity
        

        v = random.choice(l)
        u = random.random()
        w = random.choice(l1)
        
        print(v,u,w)
        msg = Twist()
        msg.linear.x = v  
        msg.linear.y = u
        msg.angular.z = w

        pub.publish(msg)
        rate.sleep()

