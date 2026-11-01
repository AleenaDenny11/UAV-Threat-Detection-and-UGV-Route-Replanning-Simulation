from detector import generate_threats
from messaging import (
    send_detection,
    receive_detection
)

# Generate one threat
threats = generate_threats(1)

threat = threats[0]

print("\nORIGINAL THREAT:\n")
print(threat)

# Send message
message = send_detection(threat)

print("\nJSON MESSAGE:\n")
print(message)

# Receive message
decoded = receive_detection(message)

print("\nDECODED MESSAGE:\n")
print(decoded)