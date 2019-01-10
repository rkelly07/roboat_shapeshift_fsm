# Latch State for Roboat Shapeshifting FSM
# Ryan Kelly January 2019

import rospy
import smach

class Latch(smach.State):
    """
    Given the current configuration of the Roboats, perform a latch step.
    A latch step involves the final movement to successfully latch the roboats together
    """
    def __init__(self, outcomes=['success', 'failure'],
                       input_keys=[],
                       output_keys=[]):
        # State initialization
        pass

    def execute(self, userdata):
        pass