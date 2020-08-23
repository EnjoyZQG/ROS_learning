#!/usr/bin/env python

from __future__ import print_function

import rospy
from turtlesim.msg import Pose

def poseInfoCallback(msg):
    # print(rospy.get_rostime().secs)
    rospy.loginfo("Position [x, y] is: [{}, {}]".format(msg.x, msg.y))

def pose_subscriber1():
    # continually get the pose message until node shut down
    # this function creates a direct contact between turtulesim node and  
    # this node, conecttion is the turtleX/pose topic
    
    rospy.init_node('pose_subscriber', anonymous=True)
    sub = rospy.Subscriber("turtle1/pose", Pose, poseInfoCallback,
                    queue_size=1, buff_size=10) 

    rospy.spin()

def pose_subscriber2():
    # just a node to get the pose message, no direct connection from
    # turtlesim node 

    rospy.init_node('pose_subscriber', anonymous=True)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        msg = rospy.wait_for_message('turtle1/pose', Pose, timeout=None)
        rospy.loginfo("Position [x, y] is: [{}, {}]".format(msg.x, msg.y))
        rate.sleep()

def pose_subscriber3():
    rospy.init_node('pose_subscriber', anonymous=True)
    msg = rospy.wait_for_message('turtle1/pose', Pose, timeout=None)
    # rospy.loginfo("Position [x, y] is: [{}, {}]".format(msg.x, msg.y))
    
    return msg


if __name__ == '__main__':
    pose_subscriber1()
    # try:
    #     pose_subscriber2()
        # pose_subscriber3()
    # except rospy.ROSInterruptException:
    #     pass

     
