#!/usr/bin/env python

"""
This is a variation of the Unicorn script
where I learned to pass mqtt message data to functions.
Here I want to control the IR cut-filter with mqtt messages
that can be generated, for instance from RPi Cam Web Int.

There are a bunch of hard-coded bad bits in here than need 
a strategy
"""
# the mqtt is from from digi.com

import argparse
import paho.mqtt.client as mqtt
import json
import logging
import os
from socket import gethostname


DEFAULT_MQTT_BROKER_IP = "ansipi.local"
DEFAULT_MQTT_BROKER_PORT = 1883
DEFAULT_MQTT_TOPIC = "test"
DEFAULT_MQTT_ACTION = "toggle"


logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


def on_connect(client, userdata, flags, rc):
    logging.info("OnConnect:  Connected with result code {0}".format(str(rc)))
    client.subscribe(DEFAULT_MQTT_TOPIC)


def on_message(client, userdata, msg):
    logging.info("OnMessage:  Message received-> " + msg.topic + " " + str(msg.payload))
    values =  json.loads(msg.payload)
    logging.debug("OnMessage:  The converted dictionary is : " + str(values))
    logging.debug("OnMessage:  The type is: " + str(type(values)))
    action = (values["action"])
    desktop_control(action)

def desktop_control(action):
    logging.debug("Desktop control: Action received = " + str(action))
    if action == 'soft':
        # do something here
        os.system("~/kill_switch_soft.sh")
    elif action == 'off':
        # do something here 
        os.system("~/kill_switch.sh")
    elif action == 'toggle':
        # do something here
        pass
    else:
        logging.warning("IR filter control: action out of bounds")

parser = argparse.ArgumentParser(
    description = "Receive commands for Desktop."
    )
parser.add_argument(
    "--broker",
    default=DEFAULT_MQTT_BROKER_IP,
    type=str,
    help="mqtt broker port",
    )
parser.add_argument(
        "--port",
        default=DEFAULT_MQTT_BROKER_PORT,
        type=int,
        help="mqtt broker port",
    )
parser.add_argument(
        "--topic",
        default=DEFAULT_MQTT_TOPIC,
        type=str,
        help="mqtt topic"
    )
args = parser.parse_args()


client = mqtt.Client(gethostname())
client.on_connect = on_connect
client.on_message = on_message
client.connect(DEFAULT_MQTT_BROKER_IP, DEFAULT_MQTT_BROKER_PORT)
client.loop_forever()
