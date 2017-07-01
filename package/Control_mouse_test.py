#Simple test of finding finger endpoints via polling

import Leap, sys, thread, time, os

from pymouse import PyMouse
from pykeyboard import PyKeyboard

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

    #initialize controller, mouse, and keyboard
    controller = Leap.Controller()
    m = PyMouse()
    x_dim, y_dim = m.screen_size()
    k = PyKeyboard()
    
    
    
    
    #print positions every half second
    looping = True
    while looping:
        #update hand positions
        R_pos = update(controller,0);
        L_pos = update(controller,1);

        #Track mouse to right index finger
        #press if z is negative
        pressed = False
        mouseX = int(R_pos[1][0] * x_dim / 200.0 + x_dim / 2)
        if mouseX < 0:
            mouseX = 0
        elif mouseX > x_dim:
            mouseX = x_dim - 1

        mouseY = int(y_dim - ((R_pos[1][1] - 200) * y_dim / 100.0))
        if mouseY < 0:
            mouseY = 0
        if mouseY > y_dim - 1:
            mouseY = y_dim - 1

        mouseZ = R_pos[1][2]

        if mouseZ > 10:
            if pressed:
                m.release(mouseX,mouseY,1)
                pressed = False
            else:
                m.move(mouseX,mouseY)
        if mouseZ < -10:
            if not pressed:
                m.press(mouseX,mouseY,1)
                pressed = True
            else:
                #m.move(mouseX,mouseY)
                pass
                
        
        #End if either index finger is above the controller
        for positions in [L_pos, R_pos]:
            if (positions[1][0] < 50 and positions[1][0] > -50) and \
                (positions[1][1] < 50 and positions[1][1] > 0) and \
                (positions[1][2] < 50 and positions[1][2] > -50):
                looping = False
        
        

if __name__ == "__main__":
    main()
