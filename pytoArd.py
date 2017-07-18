import serial # import Serial Library
import serial.tools.list_ports as list_ports
import sys
import timeprint "Getting all of the available ports"
ports = list(list_ports.comports())
for (port,name,PID) in ports:
   print "Testing %s which is port: %s"%(name,port)
   sys.stdout.flush()
   if "Arduino" in name:
       print "found the ardunio. opening comms"
       sys.stdout.flush()
       arduinoData = serial.Serial(port, 115200) #Creating our serial object named arduinoDataif arduinoData is None:
   print 'Failed to create arduinoData object. Exiting'
   sys.exit(-1)
   
while True:                                             # While loop that loops forever
   if (arduinoData.in_waiting==0):                     #Wait here until there is data
       time.sleep(0.001)                               #do something to pass the time, can be anything
   else:
       arduinoString = arduinoData.readline()          #read the line (returns a string)
       if 'V:' in arduinoString:
           try:
               arduinoString = arduinoString.replace('V:','')  #remove the V: from the string
               press = float( arduinoString)           #turn the string into a float
               print press                             #so something with press
           except Exception as e:
               print 'caught an exception when sifting through the data sent from the arduino'
       else:
           print 'ARDUINO ->' + arduinoString
