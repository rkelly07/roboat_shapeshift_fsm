#!/usr/bin/env python

import rospy
import smach
from Configuration_Verifier import *
from Latch import *
from Navigate import *
from Unlatch import *

Configuration_Sequence = []
Latching_Sequence = []
Trajectory_Sequence = []

def main():
    rospy.init_node('shapeshift_fsm')

    # Create State Machine to execute entire shapeshifting sequence
    sm_main = smach.StateMachine(outcomes=['sequence_completed','failure'])
    
    sm_main.userdata.configuration_list = Configuration_Sequence
    sm_main.userdata.latching_list = Latching_Sequence
    sm_main.userdata.trajectory_list = Trajectory_Sequence
    sm_main.userdata.config_counter = 0
    sm_main.userdata.shapeshift_counter = 0
    sm_main.intermediate = True
    
    with sm_main:
        smach.StateMachine.add('CONFIGURATION_VERIFIER', Configuration_Verifier(),
                               transitions={'shapeshift':'NAVIGATE',
                                             'completed':'sequence_completed'})

       

        smach.StateMachine.add('NAVIGATE', Navigate(),
                                   transitions={'success':'UNLATCH',
                                                'failure':'failure'})

        # Not sure if we are going to need this latch state
        # smach.StateMachine.add('LATCH', Latch(),
        #                        transitions={'success':'UNLATCH',
        #                                     'failure':'failure'})

        smach.StateMachine.add('UNLATCH', Unlatch(),
                               transitions={'step_complete':'CONFIGURATION_VERIFIER',
                                            'step_intermediate':'NAVIGATE',
                                            'failure':'failure'})

        # # Create Sub State Machine to execute singular shapeshifting step
        # sm_shapeshift = smach.StateMachine(outcomes=['step_complete', 'failure'])

        # sm_shapeshift.userdata.intermediate = True
        # with sm_shapeshift:

        #     smach.StateMachine.add('NAVIGATE', Navigate(),
        #                            transitions={'success':'UNLATCH',
        #                                         'failure':'failure'})

        #     # smach.StateMachine.add('LATCH', Latch(),
        #     #                        transitions={'success':'UNLATCH',
        #     #                                     'failure':'failure'})

        #     smach.StateMachine.add('UNLATCH', Unlatch(),
        #                            transitions={'step_complete':'step_complete',
        #                                         'step_intermediate':'NAVIGATE',
        #                                         'failure':'failure'})

        # smach.StateMachine.add('SHAPESHIFT', sm_shapeshift,
        #                        transitions={'step_complete':'CONFIGURATION_VERIFIER',
        #                                     'failure':'failure'})

        outcome = sm_main.execute()

if __name__ == '__main__':
    rospy.loginfo('Shapeshit Initialized')
    main()
    rospy.loginfo('Shapeshift Complete')