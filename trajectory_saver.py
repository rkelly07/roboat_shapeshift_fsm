import pickle
import numpy as np

def load_obj(name):
    with open('trajectories/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

def main():
    file_name = '9_shinkyu1'
    trajs = load_obj(file_name)
    S = trajs['S']
    U = trajs['U']
    lines = []
    S = S[0]
    U = U[0]
    for i in xrange(S.shape[0]):
        x, y, theta, xdot, ydot, thetadot = S[i]
        xdotdot, ydotdot, thetadotdot = U[i]
        line = [x, y, theta, xdot, ydot, thetadot, xdotdot, ydotdot, thetadotdot]
        line = [str(item) for item in line]
        str_line = ','.join(line)
        lines.append(str_line)
    with open(file_name +'.txt', 'w') as f:
        for line in lines:
            f.write("%s\n" % line)
    print("Success")


if __name__ == '__main__':
    main()