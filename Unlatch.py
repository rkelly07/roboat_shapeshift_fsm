# Unlatch State for Roboat Shapeshifting FSM
# Ryan Kelly January 2019

import rospy
import smach
import time

class Unlatch(smach.State):
    """
    Given the current configuration of the Roboats, perform an unlatch step.
    An unlatch step involves sending the correct messages to unlatch Roboats from eachother
    """
    def __init__(self):
        smach.State.__init__(self, 
                             outcomes=['step_complete', 'step_intermediate', 'failure'],
                             input_keys=['latch_instructions','intermediate', 'shapeshift_counter'],
                             output_keys=['intermediate', 'shapeshift_counter'])
        self.pub = rospy.Publisher('latches', String, queue_size=10)
        self.rate = rospy.Rate(5)

    def execute(self, userdata):
        counter = userdata.shapeshift_counter
        latch_instructions = userdata.latch_instructions[counter]
        userdata.shapeshift_counter = counter + 1

        if not rospy.is_shutdown():
            for instruction in latch_instructions:
                self.pub.publish(instruction)
                self.rate.sleep()
        # Wait for the the latches to all finish unlatching before returning
        time.sleep(10)

        if userdata.intermediate:
            userdata.intermediate = False
            return 'step_intermediate'
        else:
            userdata.intermediate = True
            return 'step_complete'