# Configuration Verifier State for Roboat Shapeshifting FSM
# Ryan Kelly January 2019

import rospy
import smach

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
        current_configuration = userdata.configuration_list[counter]
        current_latch_instructions = userdata.latching_list[counter]
        userdata.config_counter = counter + 1

        # TODO
        # Read in boat hardware configuration and compare to current configuration
        # if they are equal then exit otherwise pass current latch instructions to output
        hardware_configuration = 0
        if hardware_configuration == current_configuration:
            return 'completed'
        else:
            return 'shapeshift'