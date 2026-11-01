import json


# UAV sends threat message
def send_detection(threat):

    message = json.dumps(threat)

    return message


# UGV receives threat message
def receive_detection(message):

    threat = json.loads(message)

    return threat