# Configuration Verifier State for Roboat Shapeshifting FSM
# Ryan Kelly January 2019

import rospy
import smach
from utils import *

class Configuration_Verifier(smach.State):
    """
    Analyze the current configuration of the Roboats, if they are in the goal configuration
    then the shapeshifting is complete.
    """
    def __init__(self):
        smach.State.__init__(self, 
                            outcomes=['completed', 'shapeshift'],
                            input_keys=['configuration_list', 'latching_list', 'config_step'],
                            output_keys=['config_counter'])

    def execute(self, userdata):
        counter = userdata.config_counter
        current_configuration = set(userdata.configuration_list[counter])
        current_latch_instructions = userdata.latching_list[counter]
        userdata.config_counter = counter + 1

        hc = get_boat_configuration(1)
        if verify_configuration(hc, current_configuration):
            return 'completed'
        return 'shapeshift'
