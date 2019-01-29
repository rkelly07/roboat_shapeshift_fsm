
def get_boat_configuration(x):
    rospy.wait_for_service('configuration')
    try:
        configuration = rospy.ServiceProxy('configuration', Configuration)
        resp1 = add_two_ints(x)
        return resp1.latches
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def load_obj(self, name):
    with open('trajectories/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

def verify_configuration(hc, current_configuration):
    if len(hc) != len(current_configuration):
        return False
    for latch in hc:
        test = (latch.boat1_id, latch.boat2_id, latch.boat1_latch, latch.boat2_latch)
        if test not in current_configuration:
            return False
    return True