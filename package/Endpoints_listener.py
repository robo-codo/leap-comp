################################################################################
# Copyright (C) 2012-2013 Leap Motion, Inc. All rights reserved.               #
# Leap Motion proprietary and confidential. Not for distribution.              #
# Use subject to the terms of the Leap Motion SDK Agreement available at       #
# https://developer.leapmotion.com/sdk_agreement, or another agreement         #
# between Leap Motion and you, your company or other organization.             #
################################################################################
from __future__ import print_function

import Leap, sys, thread, time
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

positions = [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)]

class SampleListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']

    def on_init(self, controller):
        print ("Initialized")

    def on_connect(self, controller):
        print ("Connected")

        # Enable gestures
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print ("Disconnected")

    def on_exit(self, controller):
        print ("Exited")

    def on_frame(self, controller):
        global positions
        # Get the most recent frame and report some basic information
        frame = controller.frame()

        #If nothing in frame, set values to zero
        if (len(frame.hands) < 1):
            positions = [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)]
        
        # Get hands
        for hand in frame.hands:
            if (not hand.is_left):
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

def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)
    
    #print positions every half second
    #break upon keyboard interrupt
    while True:
        time.sleep(.5)
        print (positions)
    
    # Remove the sample listener when done
    controller.remove_listener(listener)


if __name__ == "__main__":
    main()
