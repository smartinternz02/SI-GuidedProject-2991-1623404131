import time
import sys
import ibmiotf.application
import ibmiotf.device
import random
import json

#Provide your IBM Watson Device Credentials
organization = "6ds44h"
deviceType = "IOT"
deviceId = "1729"
authMethod = "token"
authToken = "17291729"


# Initialize the device client.
T=0
w=0

def myCommandCallback(cmd):
        print("Command received: %s" % cmd.data['command'])


        if cmd.data['command']=='motoron':
                print("MOTOR ON IS RECEIVED")
                
                
        elif cmd.data['command']=='lightoff':
                print("MOTOR OFF IS RECEIVED")
        
        if cmd.command == "setInterval":
                if 'interval' not in cmd.data:
                        print("Error - command is missing required information: 'interval'")
                else:
                        interval = cmd.data['interval']
        elif cmd.command == "print":
                if 'message' not in cmd.data:
                        print("Error - command is missing required information: 'message'")
                else:
                        print(cmd.data['message'])

try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()

while True:
        T=23
        w=15
        #Send Temperature,waterlevel,Humidity to IBM Watson
        data = {"d":{ 'temperature' : T, 'waterlevel' : w}}
        print(data)
        def myOnPublishCallback():
            print ("Published Temperature = %s C" % T, "waterlevel = %s %%" % w, "to IBM Watson")

        success = deviceCli.publishEvent("Data", "json", data, qos=0, on_publish=myOnPublishCallback)
        if not success:
            print("Not connected to IoTF")
        time.sleep(1)
        
        deviceCli.commandCallback = myCommandCallback

# Disconnect the device and application from the cloud
deviceCli.disconnect()
