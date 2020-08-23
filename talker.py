#!/usr/bin/env python

from __future__ import print_function

import rospy

from geometry_msgs.msg import Twist


def talker(linear, angular):
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=1)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1)
    
    while not rospy.is_shutdown():
        cmd_vel = Twist()
        cmd_vel.linear.x, cmd_vel.linear.y, cmd_vel.linear.z= linear
        cmd_vel.angular.x, cmd_vel.angular.y, cmd_vel.angular.z = angular
        rospy.loginfo(cmd_vel)
        pub.publish(cmd_vel)
        rate.sleep()


if __name__ == '__main__':
    linear = [1.0, 0.0, 0.0]
    angular = [0.0, 0.0, 1.0]

    try:
        talker(linear, angular)
    except rospy.ROSInterruptException:
        pass
        
