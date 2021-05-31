#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import time
import os
import argparse
############

#parser = argparse.ArgumentParser(description='Process some integers.')
#parser.add_argument('-cmd', '-cmd', help='helpcmd', required=False)
#parser.add_argument('-service', '-srv', help='service', required=False)
#parser.print_help()

#args = parser.parse_args()

node = "node1"


broker_address="192.168.1.162"
print("creating new instance")
client = mqtt.Client(node)
print("connecting to broker")
client.connect(broker_address)
#client.publish("commands/client2", "this is server")
#arg_command = args.cmd
#arg_service = args.service

text = "{} = {}".format(node, 'online')

#mqtt_command = "{} {}".format(arg_command,arg_service)
client.publish("/testbranch", text)
print("message send")

