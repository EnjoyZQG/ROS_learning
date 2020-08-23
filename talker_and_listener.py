#!/usr/bin/env python

from __future__ import print_function

import rospy

from geometry_msgs.msg import Twist
from turtlesim.msg import Pose



class TalkerAndListener():
    def __init__(self, linear, angular):
        cmd_vel = Twist()
        cmd_vel.linear.x, cmd_vel.linear.y, cmd_vel.linear.z= linear
        cmd_vel.angular.x, cmd_vel.angular.y, cmd_vel.angular.z = angular

        self.node = rospy.init_node('talker_and_listener', anonymous=True)        
        self.pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=1)
 
        self.beginn = rospy.get_rostime().secs

        self.listener()
        
    def poseInfoCallback(self, msg):
        right_now = rospy.get_rostime().secs
        if (right_now - self.beginn) > 5:
            print(1)
            self.beginn = right_now
        #           pub.publish(cmd_vel)
        
        # rospy.loginfo("Position [x, y] is: [{}, {}]".format(msg.x, msg.y))
    
    def listener(self):
        rospy.Subscriber("turtle1/pose", Pose, self.poseInfoCallback,
                    queue_size=1, buff_size=10) 

        rospy.spin()


if __name__ == '__main__':
    linear = [1.0, 0.0, 0.0]
    angular = [0.0, 0.0, 1.0]

    try:
        TalkerAndListener(linear, angular)
    except rospy.ROSInterruptException:
        pass
        
