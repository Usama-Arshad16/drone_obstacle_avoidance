#!/usr/bin/env python


import rospy 
import rospkg 
from gazebo_msgs.msg import ModelState 
from gazebo_msgs.srv import SetModelState

p = -1
def main():
    rospy.init_node('set_pose')
    global p

    state_msg = ModelState()
    state_msg.model_name = 'drone'
    state_msg.pose.position.x = 5
    state_msg.pose.position.y = p
    state_msg.pose.position.z = 0.85
    state_msg.pose.orientation.x = 0
    state_msg.pose.orientation.y = 0
    state_msg.pose.orientation.z = 0
    state_msg.pose.orientation.w = 0
    #print "chal ja"

    rospy.wait_for_service('/gazebo/set_model_state')
    try:
        set_state = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState)
        resp = set_state( state_msg )

    except rospy.ServiceException, e:
        print "Service call failed: %s" % e

while not rospy.is_shutdown():
    for i in range(620):
        #print i
        p = p +0.003
        main()
    for i in range(620):
        #print i
        p = p - 0.003
        main()
    main()
    rospy.sleep(0.01)