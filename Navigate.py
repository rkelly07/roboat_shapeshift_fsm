# Navigate State for Roboat Shapeshifting FSM
# Ryan Kelly January 2019

import rospy
import smach
import time
from utils import *

class Navigate(smach.State):
    """
    Given the current configuration of the Roboats, perform a navigation step.
    A navigation step involves generating and following a trajectory to rearrange the Roboats.
    """
    def __init__(self):
        smach.State.__init__(self, 
                             outcomes=['success', 'failure'],
                             input_keys=['trajectory_list', 'shapeshift_counter'],
                             output_keys=[])
        self.pub = rospy.Publisher('trajectory', String, queue_size=10)
        self.rate = rospy.Rate(5)

    def execute(self, userdata):
        # Load the current trajectory
        counter = userdata.shapeshift_counter
        current_trajectory = userdata.trajectory_list[counter]
        current_goal_configuration = set(userdata.configuration_list[counter])
        current_s = current_trajectory['S'] # x,y,theta,xdot,ydot,thetadot
        current_u = current_trajectory['U'] # xdotdot,ydotdot,thetadotdot

        # Publish all of the points in the trajectory so that the tracker node has access
        if not rospy.is_shutdown():
            for point in current_trajectory:
                self.pub.publish(point)
                self.rate.sleep()

        # Wait for the trajectory to finish tracking before returning
        hc = get_boat_configuration(1)
        while not verify_configuration(hc, current_configuration):
            time.sleep(0.5)
            hc = get_boat_configuration(1)

        return 'success'

