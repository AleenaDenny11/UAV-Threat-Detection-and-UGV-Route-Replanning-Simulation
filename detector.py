import random
import time
GRID_SIZE=20
#false negative rate
FN_RATE=0.2
#false positive rate
FP_RATE=0.2
#threat generation
def generate_threats(num_threat=3):
    threats=[]
    for i in range(num_threat):
        #false negative, missed detection, there was a threat but the UAV didn't detect it
        if random.random() < FN_RATE:
            continue
        threat={"threat_id":i,
                "class":random.choice(["vehicle","person"]),
                "confidence":round(random.uniform(0.6, 0.99),2),
                "location":(random.randint(0,GRID_SIZE-1),random.randint(0,GRID_SIZE-1)),
                "timestamp":time.time()}
        threats.append(threat)
    # Add fake threat, false positive, UAV detects a FAKE threat
    if random.random() < FP_RATE:

        fake_threat = {
            "threat_id": 999,

            "class": "vehicle",

            "confidence": 0.40,

            "location": (
                random.randint(0, GRID_SIZE - 1),
                random.randint(0, GRID_SIZE - 1)
            ),

            "timestamp": time.time()
        }
        threats.append(fake_threat)

        
    
    
    return threats
