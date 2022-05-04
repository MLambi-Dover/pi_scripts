# This is a very simple Python mqtt client
# Everything is hardcoded, not a good practice but
# easier to learn from and cleaner to read.
# Pay particular attention to the single function.
# You can define other functions and from on_message
# parse out and act on particular pieces of data.


import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("received message: " ,str(message.payload.decode("utf-8")))

mqttBroker ="10.0.0.5"

client = mqtt.Client("Smartphone")
client.connect(mqttBroker) 

client.loop_forever()

# an example of subscribing to 2 topics; see the paho mqtt docs
# client.subscribe([("IamAlive",1),("enviro",2)])
client.subscribe("IamAlive")
client.on_message=on_message 

# time.sleep(30)
# client.loop_stop()
