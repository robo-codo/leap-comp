import os, sys, inspect, thread, time

import Leap

def main():
        #create a sample listener and controller
        controller = Leap.Controller()
        listener = SampleListener()

        #Have the listener receive events from the controller
        controller.add_listener(listener)

        time.sleep(10)



class SampleListener(Leap.Listener):
        def on_init(self, controller):
                print "Initialized"
        
        def on_connect(self, controller):
                print "Connected"

                # Enable gestures
                controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
                controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
                controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
                controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

        def on_frame(self, controller):
                frame = controller.frame()
                print "Frame id: %d, timestampe: %d, hands: %d, fingers: %d" % (
                        frame.id, frame.timestamp, len(frame.hands), len(frame.fingers))


if __name__ == "__main__":
    main()
