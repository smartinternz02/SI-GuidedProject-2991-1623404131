import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "6ds44h",
        "typeId": "IOT",
        "deviceId":"1729"
    },
    "auth": {
        "token": "17291729"
    }
}
def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    temp=random.randint(-20,100)
    water=random.randint(0,100)
    Ph=random.randint(0,14)
    Flouride=random.randint(0,1)
    ISE=random.randint(0,10)
    myData={'temperature':temp, 'waterlevel':water, 'Ph':Ph, 'flouride':Flouride, 'ISE':ISE}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()
