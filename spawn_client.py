#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
from turtlesim.srv import Spawn

def spawn_client(x, y, name):
    rospy.init_node('spawn_client')
    rospy.wait_for_service('spawn')

    try:
        spawner = rospy.ServiceProxy('spawn', Spawn)
        response = spawner(x, y, 0, name)

        return response.name
    except rospy.ServiceException, e:
        print("Service call failed: ", e)

if __name__ == "__main__":
    x = 1.0
    y = 2.0
    name = 'turtle2'
    print("Response : [{}]".format(spawn_client(float(x), float(y), name)))

