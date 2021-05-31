#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import time
import os
import socket
############
#This script will subscribe to a MQTT topic "commands/clients" and listen to various commands that are published ther.



host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
clientID = host_ip

#connect to the topic
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("/testbranch")
    client.publish("/testbranch", "O:{}".format(clientID))

#Check for any messages that are published
def on_message(client, userdata, message):
    messageOUT = str(message.payload.decode("utf-8"))
    print(messageOUT)


########################################
broker_address="eyf-server"
print("creating new instance")
client = mqtt.Client(clientID)
client.on_message=on_message
client.on_connect=on_connect
print("connecting to broker")
client.connect(broker_address)
client.loop_start()
client.loop_forever()
