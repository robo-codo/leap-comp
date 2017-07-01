#Simple test of finding finger endpoints via polling

import Leap, sys, thread, time, os

import msvcrt

def update(controller, i):
    # Get the most recent frame and report some basic information
    frame = controller.frame()
    #If hand is not in frame, set values to zero
    #If target hand is not in frame, all zeroes will be returned
    positions = [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)]
        
    # Get hands
    for hand in frame.hands:
        if (hand.is_left and i == 0) or (not hand.is_left and i == 1):
            continue
        for i in range(4,-1,-1):
            positions[i] = (hand.fingers[i].bone(3).next_joint.x,
                            hand.fingers[i].bone(3).next_joint.y,
                            hand.fingers[i].bone(3).next_joint.z)
        #Reduce positions to ints
        for i in range(5):
            positions[i] = (int(positions[i][0]),
                            int(positions[i][1]),
                            int(positions[i][2]))
    return positions

def main():
    #Initialize positions
    L_pos = [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)]
    R_pos = [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)]
    print "Mapping both hands, printing out left hand positional data"
    print "Place either index finger immediately above the leap controller to end"    # Create a sample listener and controller
    print ""
    print "X is right, Y is up, Z is out. Measurements are in mm"
    print "Fingers are ordered starting from the thumb"
    controller = Leap.Controller()
    
    #print positions every half second
    looping = True
    while looping:
        time.sleep(0.5)
        R_pos = update(controller,0);
        L_pos = update(controller,1);
        print L_pos
        #End if either index finger is above the controller
        for positions in [L_pos, R_pos]:
            if (positions[1][0] < 50 and positions[1][0] > -50) and \
                (positions[1][1] < 50 and positions[1][1] > 0) and \
                (positions[1][2] < 50 and positions[1][2] > -50):
                looping = False
        
        

if __name__ == "__main__":
    main()
